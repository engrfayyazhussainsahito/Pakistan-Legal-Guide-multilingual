import { afterEach, describe, expect, it, vi } from 'vitest'
// @ts-expect-error plain JS worker, no types
import worker from '../../serverless/worker.js'
import { parseAiResponse } from '../services/aiClient'

const ORIGIN = 'https://site.example'
const env = { ALLOWED_ORIGIN: ORIGIN, ANTHROPIC_API_KEY: 'test-key' }
const req = (body: unknown, origin = ORIGIN) =>
  new Request('https://w.example', { method: 'POST', headers: { Origin: origin, 'Content-Type': 'application/json' }, body: JSON.stringify(body) })

afterEach(() => vi.unstubAllGlobals())

describe('AI worker', () => {
  it('rejects unknown origins and bad input', async () => {
    expect((await worker.fetch(req({ question: 'what is bail' }, 'https://evil.example'), env)).status).toBe(403)
    expect((await worker.fetch(req({ question: 'hi' }), env)).status).toBe(400)
  })
  it('answers from retrieved passages, rebuilds citations, and passes the client parser', async () => {
    let sent: { system: string; messages: { content: string }[] } | undefined
    vi.stubGlobal('fetch', async (_u: string, init: { body: string }) => {
      sent = JSON.parse(init.body)
      return new Response(
        JSON.stringify({ content: [{ text: JSON.stringify({ shortAnswer: 'Bail is release pending trial.', citations: [{ idx: 0 }, { idx: 99 }], nextSteps: ['See a lawyer'] }) }] }),
        { status: 200 },
      )
    })
    const res = await worker.fetch(req({ question: 'How do I get bail after arrest?', language: 'en', jurisdiction: 'sindh', history: [] }), env)
    expect(res.status).toBe(200)
    const body = await res.json()
    const parsed = parseAiResponse(body)
    expect(parsed.shortAnswer).toContain('Bail')
    expect(parsed.citations.length).toBe(1)
    expect(parsed.citations[0].url.startsWith('https://')).toBe(true)
    expect(sent!.messages.at(-1)!.content).toContain('PASSAGES')
    expect(sent!.system).toContain('ONLY from the numbered passages')
  })
  it('never retrieves another province for a chosen province', async () => {
    let ctx = ''
    vi.stubGlobal('fetch', async (_u: string, init: { body: string }) => {
      ctx = JSON.parse(init.body).messages.at(-1).content
      return new Response(JSON.stringify({ content: [{ text: '{"shortAnswer":"x","citations":[]}' }] }))
    })
    await worker.fetch(req({ question: 'rented premises tenant eviction', jurisdiction: 'sindh' }), env)
    expect(ctx).not.toMatch(/Punjab Rented Premises/i)
  })
  it('returns insufficient evidence when nothing matches, without calling the model', async () => {
    const f = vi.fn()
    vi.stubGlobal('fetch', f)
    const res = await worker.fetch(req({ question: 'zzqqxx wwvvuu' }), env)
    expect((await res.json()).insufficientEvidence).toBe(true)
    expect(f).not.toHaveBeenCalled()
  })
  it('fails safely without a key or on upstream errors', async () => {
    expect((await worker.fetch(req({ question: 'what is bail' }), { ALLOWED_ORIGIN: ORIGIN })).status).toBe(503)
    vi.stubGlobal('fetch', async () => new Response('x', { status: 500 }))
    expect((await worker.fetch(req({ question: 'what is bail' }), env)).status).toBe(502)
  })
})
