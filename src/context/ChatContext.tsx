import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState, type ReactNode } from 'react'
import { useApp } from './AppContext'
import { translate } from '../i18n'
import { AiError, askAi, isAiConfigured, validateQuestion } from '../services/aiClient'
import { localAnswer, newId } from '../services/localAssistant'
import type { ChatMessage, Lang } from '../types'

interface ChatState {
  messages: ChatMessage[]
  loading: boolean
  chatLang: Lang
  setChatLang: (l: Lang) => void
  aiConfigured: boolean
  aiOn: boolean
  /** Ask to switch AI on — the UI must show the privacy notice first. */
  requestAi: () => void
  disableAi: () => void
  consentOpen: boolean
  acceptConsent: () => void
  declineConsent: () => void
  send: (text: string) => Promise<void>
  clear: () => void
}

const Ctx = createContext<ChatState | null>(null)
const CONSENT_KEY = 'pk-legal.ai-consent'

function hasConsent(): boolean {
  try {
    return localStorage.getItem(CONSENT_KEY) === '1'
  } catch {
    return false
  }
}

export function ChatProvider({ children }: { children: ReactNode }) {
  const { lang, jurisdiction, data, engine } = useApp()
  const [messages, setMessages] = useState<ChatMessage[]>([]) // in-memory only; never persisted
  const [loading, setLoading] = useState(false)
  const [chatLang, setChatLang] = useState<Lang>(lang)
  const [aiOn, setAiOn] = useState(false)
  const [consentOpen, setConsentOpen] = useState(false)
  const abortRef = useRef<AbortController | null>(null)
  const aiConfigured = isAiConfigured()

  // Follow the site language when it changes
  useEffect(() => setChatLang(lang), [lang])

  const requestAi = useCallback(() => {
    if (!aiConfigured) return
    if (hasConsent()) setAiOn(true)
    else setConsentOpen(true)
  }, [aiConfigured])

  const acceptConsent = useCallback(() => {
    try {
      localStorage.setItem(CONSENT_KEY, '1')
    } catch {
      /* ignore */
    }
    setConsentOpen(false)
    setAiOn(true)
  }, [])

  const declineConsent = useCallback(() => {
    setConsentOpen(false)
    setAiOn(false)
  }, [])

  const disableAi = useCallback(() => setAiOn(false), [])

  const clear = useCallback(() => {
    abortRef.current?.abort()
    setMessages([])
    setLoading(false)
  }, [])

  const send = useCallback(
    async (raw: string) => {
      const tr = (k: string, v?: Record<string, string | number>) => translate(chatLang, k, v)
      let question: string
      try {
        question = validateQuestion(raw)
      } catch {
        setMessages((m) => [...m, { id: newId(), role: 'assistant', text: tr('chat.errInput'), error: true }])
        return
      }
      const history = messages
        .filter((m) => !m.error)
        .slice(-6)
        .map((m) => ({ role: m.role, text: m.text }))
      setMessages((m) => [...m, { id: newId(), role: 'user', text: question }])
      setLoading(true)

      const runLocal = (prefix?: ChatMessage) => {
        if (!data || !engine) {
          setMessages((m) => [...m, { id: newId(), role: 'assistant', text: tr('common.dataLoadError'), error: true }])
          return
        }
        const ans = localAnswer(question, {
          data,
          engine,
          lang: chatLang,
          jurisdiction,
          labels: {
            foundDocs: tr('chat.foundDocs'),
            foundAnswer: tr('chat.foundAnswer'),
            noMatch: tr('chat.noMatch'),
            unofficial: tr('common.unofficialTranslation'),
            jurisdictionName: (j) => tr(`jur.${j}`),
          },
        })
        setMessages((m) => (prefix ? [...m, prefix, ans] : [...m, ans]))
      }

      try {
        if (aiOn && aiConfigured && hasConsent()) {
          const controller = new AbortController()
          abortRef.current = controller
          try {
            const answer = await askAi({ question, language: chatLang, jurisdiction, history }, controller.signal)
            setMessages((m) => [
              ...m,
              { id: newId(), role: 'assistant', mode: 'ai', text: answer.shortAnswer, structured: answer, citations: answer.citations },
            ])
          } catch (e) {
            if (controller.signal.aborted && (e as AiError).message === 'aborted' && (e as AiError).kind === 'network') return
            const kind = e instanceof AiError ? e.kind : 'network'
            const key = { network: 'chat.errNetwork', rate: 'chat.errRate', config: 'chat.errConfig', timeout: 'chat.errTimeout', bad: 'chat.errBad', input: 'chat.errInput' }[kind]
            const errMsg: ChatMessage = { id: newId(), role: 'assistant', text: tr(key), error: true }
            if (kind === 'rate' || kind === 'input') setMessages((m) => [...m, errMsg])
            else runLocal(errMsg) // graceful fallback to the local library
          }
        } else {
          // tiny delay so the loading state is perceivable and screen readers announce it
          await new Promise((r) => setTimeout(r, 150))
          runLocal()
        }
      } finally {
        setLoading(false)
      }
    },
    [messages, chatLang, jurisdiction, data, engine, aiOn, aiConfigured],
  )

  const value = useMemo<ChatState>(
    () => ({ messages, loading, chatLang, setChatLang, aiConfigured, aiOn, requestAi, disableAi, consentOpen, acceptConsent, declineConsent, send, clear }),
    [messages, loading, chatLang, aiConfigured, aiOn, requestAi, disableAi, consentOpen, acceptConsent, declineConsent, send, clear],
  )
  return <Ctx.Provider value={value}>{children}</Ctx.Provider>
}

export function useChat(): ChatState {
  const v = useContext(Ctx)
  if (!v) throw new Error('useChat must be used inside ChatProvider')
  return v
}
