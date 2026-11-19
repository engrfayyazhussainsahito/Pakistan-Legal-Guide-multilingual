/**
 * Optional client for an EXTERNAL AI / RAG endpoint (Mode B).
 *
 * - The endpoint URL is public configuration (VITE_AI_ENDPOINT). It is NOT a secret.
 * - No API key is ever read or sent from the browser. Model credentials live only
 *   in the separately deployed serverless backend (see serverless/ and README).
 * - If no endpoint is configured the site simply uses the local search assistant.
 *
 * Expected request  (POST, JSON):
 *   { question, language: "en"|"ur"|"sd", jurisdiction: "sindh"|...|"", history: [{role,text}] }
 * Expected response (JSON):
 *   { answer: { shortAnswer, jurisdiction?, relevantLaw?, explanation?, nextSteps?: string[],
 *               limitations?, citations: [{title,url,section?,jurisdiction?}], insufficientEvidence? } }
 */
import type { AiAnswer, AiRequest, Citation } from '../types'

export const AI_ENDPOINT: string = (import.meta.env.VITE_AI_ENDPOINT as string | undefined)?.trim() ?? ''
export const AI_PROVIDER_NAME: string = (import.meta.env.VITE_AI_PROVIDER_NAME as string | undefined)?.trim() || 'an external AI service'

export const MIN_QUESTION = 3
export const MAX_QUESTION = 1000
const TIMEOUT_MS = 30000
const MAX_HISTORY = 4

export type AiErrorKind = 'config' | 'network' | 'rate' | 'timeout' | 'bad' | 'input'

export class AiError extends Error {
  kind: AiErrorKind
  constructor(kind: AiErrorKind, message?: string) {
    super(message ?? kind)
    this.kind = kind
  }
}

export function isAiConfigured(): boolean {
  if (!AI_ENDPOINT) return false
  try {
    const u = new URL(AI_ENDPOINT)
    return u.protocol === 'https:' || u.hostname === 'localhost'
  } catch {
    return false
  }
}

/** Remove control characters and collapse whitespace. */
export function sanitizeQuestion(input: string): string {
  // eslint-disable-next-line no-control-regex
  return input.replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, '').replace(/\s+/g, ' ').trim()
}

export function validateQuestion(input: string): string {
  const q = sanitizeQuestion(input)
  if (q.length < MIN_QUESTION || q.length > MAX_QUESTION) throw new AiError('input')
  return q
}

/** Only http(s) links may be rendered as citations. */
function safeUrl(u: unknown): string | null {
  if (typeof u !== 'string') return null
  try {
    const url = new URL(u)
    return url.protocol === 'https:' || url.protocol === 'http:' ? url.href : null
  } catch {
    return null
  }
}

const str = (v: unknown, max = 4000): string | undefined =>
  typeof v === 'string' && v.trim() ? v.slice(0, max) : undefined

/** Validate the untrusted response from the endpoint. Citations without a valid URL are dropped. */
export function parseAiResponse(json: unknown): AiAnswer {
  const root = (json && typeof json === 'object' ? (json as Record<string, unknown>) : {}) as Record<string, unknown>
  const a = (root.answer && typeof root.answer === 'object' ? root.answer : root) as Record<string, unknown>
  const shortAnswer = str(a.shortAnswer)
  const insufficient = a.insufficientEvidence === true
  if (!shortAnswer && !insufficient) throw new AiError('bad')
  const citations: Citation[] = []
  if (Array.isArray(a.citations)) {
    for (const c of a.citations.slice(0, 12)) {
      if (!c || typeof c !== 'object') continue
      const o = c as Record<string, unknown>
      const url = safeUrl(o.url)
      const title = str(o.title, 300)
      if (url && title) citations.push({ title, url, section: str(o.section, 100), jurisdiction: str(o.jurisdiction, 100) })
    }
  }
  return {
    shortAnswer: shortAnswer ?? '',
    jurisdiction: str(a.jurisdiction, 200),
    relevantLaw: str(a.relevantLaw),
    explanation: str(a.explanation),
    nextSteps: Array.isArray(a.nextSteps)
      ? a.nextSteps.map((s) => str(s, 600)).filter((s): s is string => !!s).slice(0, 8)
      : undefined,
    limitations: str(a.limitations),
    citations,
    insufficientEvidence: insufficient,
  }
}

export async function askAi(req: AiRequest, signal?: AbortSignal): Promise<AiAnswer> {
  if (!isAiConfigured()) throw new AiError('config')
  const question = validateQuestion(req.question)
  const body = JSON.stringify({
    question,
    language: req.language,
    jurisdiction: req.jurisdiction,
    history: req.history.slice(-MAX_HISTORY).map((h) => ({ role: h.role, text: h.text.slice(0, 1500) })),
  })

  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort('timeout'), TIMEOUT_MS)
  const onAbort = () => controller.abort('user')
  signal?.addEventListener('abort', onAbort)
  try {
    const res = await fetch(AI_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body,
      signal: controller.signal,
      credentials: 'omit', // never send cookies
      referrerPolicy: 'no-referrer',
    })
    if (res.status === 429) throw new AiError('rate')
    if (res.status === 401 || res.status === 403 || res.status === 404) throw new AiError('config')
    if (!res.ok) throw new AiError('bad', `HTTP ${res.status}`)
    let json: unknown
    try {
      json = await res.json()
    } catch {
      throw new AiError('bad')
    }
    return parseAiResponse(json)
  } catch (e) {
    if (e instanceof AiError) throw e
    if (controller.signal.aborted) {
      throw new AiError(controller.signal.reason === 'timeout' ? 'timeout' : 'network', 'aborted')
    }
    throw new AiError('network')
  } finally {
    clearTimeout(timer)
    signal?.removeEventListener('abort', onAbort)
  }
}
