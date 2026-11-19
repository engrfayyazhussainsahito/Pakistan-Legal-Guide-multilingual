import { AlertTriangle, Bot, ExternalLink, Info, Loader2, SendHorizontal, ShieldCheck, Trash2, User } from 'lucide-react'
import { useEffect, useId, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { useChat } from '../context/ChatContext'
import { LANGS, LANG_LABEL, LANG_TAG, dirOf, translate, translateList } from '../i18n'
import { cn } from '../lib/utils'
import { AI_PROVIDER_NAME, MAX_QUESTION } from '../services/aiClient'
import type { ChatMessage, Citation } from '../types'

function Paragraphs({ text }: { text: string }) {
  return (
    <>
      {text.split(/\n{2,}/).map((p, i) => (
        <p key={i} className={i ? 'mt-2' : ''}>
          {p}
        </p>
      ))}
    </>
  )
}

function Citations({ items, label }: { items: Citation[]; label: string }) {
  if (!items.length) return null
  return (
    <div className="mt-3 border-t border-sand-200 pt-2">
      <p className="text-xs font-semibold uppercase tracking-wide text-navy-500">{label}</p>
      <ul className="mt-1 space-y-1">
        {items.map((c, i) => (
          <li key={`${c.url}-${i}`} className="text-xs">
            <a href={c.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-start gap-1 text-teal-700 underline-offset-2 hover:underline">
              <ExternalLink className="mt-0.5 h-3 w-3 shrink-0" aria-hidden />
              <span dir="ltr" className="text-start">
                {c.title}
                {c.section ? ` — ${c.section}` : ''}
                {c.jurisdiction ? ` (${c.jurisdiction})` : ''}
              </span>
            </a>
          </li>
        ))}
      </ul>
    </div>
  )
}

function AssistantBody({ m }: { m: ChatMessage }) {
  const { chatLang } = useChat()
  const tr = (k: string) => translate(chatLang, k)
  const s = m.structured
  return (
    <div>
      <p className="mb-1 text-[11px] font-semibold uppercase tracking-wide text-teal-700">
        {m.mode === 'ai' ? tr('chat.aiLabel') : m.mode === 'local' ? tr('chat.localLabel') : tr('chat.assistant')}
      </p>
      {s ? (
        <div className="space-y-3">
          {s.insufficientEvidence && (
            <p className="rounded-lg border border-amber-300 bg-amber-50 p-2.5 text-sm text-amber-900">{tr('chat.insufficient')}</p>
          )}
          {s.shortAnswer && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.shortAnswer')}</h3>
              <p className="font-medium">{s.shortAnswer}</p>
            </section>
          )}
          {s.jurisdiction && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.applicableJurisdiction')}</h3>
              <p>{s.jurisdiction}</p>
            </section>
          )}
          {s.relevantLaw && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.relevantLaw')}</h3>
              <p>{s.relevantLaw}</p>
            </section>
          )}
          {s.explanation && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.explanation')}</h3>
              <Paragraphs text={s.explanation} />
            </section>
          )}
          {s.nextSteps && s.nextSteps.length > 0 && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.nextSteps')}</h3>
              <ol className="ms-5 list-decimal space-y-1">
                {s.nextSteps.map((n, i) => (
                  <li key={i}>{n}</li>
                ))}
              </ol>
            </section>
          )}
          {s.limitations && (
            <section>
              <h3 className="text-xs font-semibold text-navy-500">{tr('chat.limitationsTitle')}</h3>
              <p className="text-sm text-navy-700">{s.limitations}</p>
            </section>
          )}
        </div>
      ) : (
        <Paragraphs text={m.text} />
      )}

      {m.localLinks && m.localLinks.length > 0 && (
        <ul className="mt-3 flex flex-wrap gap-2">
          {m.localLinks.map((l) => (
            <li key={l.to}>
              <Link to={l.to} className="inline-flex items-center gap-1.5 rounded-lg border border-teal-300 bg-teal-50 px-2.5 py-1 text-xs font-medium text-teal-900 hover:bg-teal-100">
                {l.label}
                {l.jurisdiction && <span className="text-teal-700/80">· {l.jurisdiction}</span>}
              </Link>
            </li>
          ))}
        </ul>
      )}
      {m.needsJurisdiction && (
        <p className="mt-3 flex items-start gap-1.5 rounded-lg bg-amber-50 p-2 text-xs text-amber-900">
          <Info className="mt-0.5 h-3.5 w-3.5 shrink-0" aria-hidden />
          {tr('chat.needJurisdiction')}
        </p>
      )}
      <Citations items={m.citations ?? []} label={tr('chat.sources')} />
    </div>
  )
}

export function ChatPanel({ compact = false }: { compact?: boolean }) {
  const { t, jurisdiction, jurName } = useApp()
  const chat = useChat()
  const [text, setText] = useState('')
  const endRef = useRef<HTMLDivElement>(null)
  const inputId = useId()
  const tr = (k: string, v?: Record<string, string | number>) => translate(chat.chatLang, k, v)
  const dir = dirOf(chat.chatLang)

  useEffect(() => {
    endRef.current?.scrollIntoView({ block: 'end', behavior: 'smooth' })
  }, [chat.messages.length, chat.loading])

  const submit = () => {
    const v = text
    if (!v.trim() || chat.loading) return
    setText('')
    void chat.send(v)
  }

  const suggestions = translateList(chat.chatLang, 'chat.suggestedList')

  return (
    <div className={cn('flex flex-col', compact ? 'h-full' : 'min-h-[32rem]')}>
      {/* Mode banner — always honest about what this is */}
      {chat.aiOn ? (
        <div className="m-3 mb-0 flex gap-2 rounded-lg border border-teal-300 bg-teal-50 p-3 text-xs text-teal-900">
          <ShieldCheck className="mt-0.5 h-4 w-4 shrink-0" aria-hidden />
          <div>
            <p className="font-semibold">{t('chat.aiBannerTitle')}</p>
            <p>{t('chat.aiBanner')}</p>
          </div>
        </div>
      ) : (
        <div className="m-3 mb-0 flex gap-2 rounded-lg border border-amber-300 bg-amber-50 p-3 text-xs text-amber-900">
          <Info className="mt-0.5 h-4 w-4 shrink-0" aria-hidden />
          <div>
            <p className="font-semibold">{t('chat.localBannerTitle')}</p>
            <p>{t('chat.localBanner')}</p>
            {!chat.aiConfigured && <p className="mt-1">{t('chat.aiUnavailable')}</p>}
          </div>
        </div>
      )}

      {/* Controls */}
      <div className="flex flex-wrap items-center gap-x-4 gap-y-2 px-3 pt-3 text-xs">
        <label className="flex items-center gap-1.5 text-navy-700">
          <span>{t('chat.language')}</span>
          <select
            value={chat.chatLang}
            onChange={(e) => chat.setChatLang(e.target.value as (typeof LANGS)[number])}
            className="rounded-md border border-navy-200 bg-white py-1 ps-2 pe-6 text-xs"
          >
            {LANGS.map((l) => (
              <option key={l} value={l} lang={LANG_TAG[l]}>
                {LANG_LABEL[l]}
              </option>
            ))}
          </select>
        </label>
        <span className="text-navy-600">
          {jurisdiction ? t('chat.jurisdictionNow', { name: jurName(jurisdiction) }) : t('jur.none')}
        </span>
        <label className={cn('ms-auto flex items-center gap-1.5', !chat.aiConfigured && 'opacity-60')} title={!chat.aiConfigured ? t('chat.aiUnavailable') : undefined}>
          <input
            type="checkbox"
            checked={chat.aiOn}
            disabled={!chat.aiConfigured}
            onChange={(e) => (e.target.checked ? chat.requestAi() : chat.disableAi())}
            className="h-4 w-4 accent-teal-600"
          />
          <span>{t('chat.aiToggle')}</span>
        </label>
      </div>

      {/* Messages */}
      <div role="log" aria-live="polite" aria-relevant="additions" aria-label={t('chat.title')} className={cn('flex-1 space-y-3 overflow-y-auto px-3 py-3', compact ? 'min-h-0' : 'max-h-[32rem]')}>
        {chat.messages.length === 0 && (
          <div>
            <p className="text-sm text-navy-700" dir={dir} lang={LANG_TAG[chat.chatLang]}>
              {tr('chat.sub')}
            </p>
            <p className="mb-2 mt-4 text-xs font-semibold uppercase tracking-wide text-navy-500">{t('chat.suggested')}</p>
            <ul className="flex flex-col gap-2" dir={dir} lang={LANG_TAG[chat.chatLang]}>
              {suggestions.map((q) => (
                <li key={q}>
                  <button
                    type="button"
                    onClick={() => void chat.send(q)}
                    className="w-full rounded-lg border border-sand-300 bg-white px-3 py-2 text-start text-sm text-navy-800 transition hover:border-teal-400 hover:bg-teal-50"
                  >
                    {q}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}
        {chat.messages.map((m) => (
          <div key={m.id} className={cn('flex gap-2', m.role === 'user' && 'flex-row-reverse')}>
            <span className={cn('mt-0.5 grid h-7 w-7 shrink-0 place-items-center rounded-full', m.role === 'user' ? 'bg-navy-800 text-white' : 'bg-teal-100 text-teal-800')} aria-hidden>
              {m.role === 'user' ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
            </span>
            <div
              dir={dir}
              lang={LANG_TAG[chat.chatLang]}
              className={cn(
                'max-w-[88%] rounded-2xl px-3.5 py-2.5 text-sm leading-relaxed',
                m.role === 'user' ? 'bg-navy-800 text-white' : m.error ? 'border border-amber-300 bg-amber-50 text-amber-950' : 'border border-sand-200 bg-white text-navy-900',
              )}
            >
              <span className="sr-only">{m.role === 'user' ? t('chat.you') : t('chat.assistant')}: </span>
              {m.role === 'user' ? (
                <p className="whitespace-pre-wrap break-words">{m.text}</p>
              ) : m.error ? (
                <p className="flex items-start gap-1.5">
                  <AlertTriangle className="mt-1 h-4 w-4 shrink-0" aria-hidden />
                  {m.text}
                </p>
              ) : (
                <AssistantBody m={m} />
              )}
            </div>
          </div>
        ))}
        {chat.loading && (
          <div role="status" className="flex items-center gap-2 text-sm text-navy-600" dir={dir}>
            <Loader2 className="h-4 w-4 animate-spin" aria-hidden />
            {chat.aiOn ? tr('chat.thinkingAi') : tr('chat.thinking')}
          </div>
        )}
        <div ref={endRef} />
      </div>

      {/* Composer */}
      <form
        onSubmit={(e) => {
          e.preventDefault()
          submit()
        }}
        className="border-t border-sand-200 bg-white/70 p-3"
      >
        <label htmlFor={inputId} className="sr-only">
          {tr('chat.placeholder')}
        </label>
        <div className="flex items-end gap-2">
          <textarea
            id={inputId}
            value={text}
            rows={2}
            maxLength={MAX_QUESTION}
            dir={dir}
            lang={LANG_TAG[chat.chatLang]}
            placeholder={tr('chat.placeholder')}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault()
                submit()
              }
            }}
            className="field resize-none"
          />
          <button type="submit" disabled={chat.loading || text.trim().length < 3} className="btn-primary h-[42px] shrink-0 px-3" aria-label={t('chat.send')}>
            <SendHorizontal className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
          </button>
        </div>
        <div className="mt-2 flex items-center justify-between text-[11px] text-navy-500">
          <span>
            {t('chat.footerNote')} · {t('chat.sessionNote')}
          </span>
          {chat.messages.length > 0 && (
            <button type="button" onClick={chat.clear} className="inline-flex items-center gap-1 text-navy-600 hover:text-navy-900">
              <Trash2 className="h-3 w-3" aria-hidden />
              {t('chat.clear')}
            </button>
          )}
        </div>
      </form>

      {chat.consentOpen && <ConsentDialog />}
    </div>
  )
}

function ConsentDialog() {
  const { t } = useApp()
  const chat = useChat()
  const ref = useRef<HTMLButtonElement>(null)
  useEffect(() => ref.current?.focus(), [])
  return (
    <div className="fixed inset-0 z-[60] grid place-items-center bg-navy-950/60 p-4" role="presentation">
      <div role="alertdialog" aria-modal="true" aria-labelledby="consent-title" aria-describedby="consent-body" className="card max-w-md p-6">
        <h2 id="consent-title" className="heading-font text-lg font-semibold">
          {t('chat.privacyTitle')}
        </h2>
        <p id="consent-body" className="mt-2 text-sm leading-relaxed text-navy-700">
          {t('chat.privacyBody')}
        </p>
        <p className="mt-2 text-xs text-navy-500">{AI_PROVIDER_NAME}</p>
        <div className="mt-5 flex flex-wrap gap-2">
          <button ref={ref} className="btn-primary" onClick={chat.acceptConsent}>
            {t('chat.privacyAccept')}
          </button>
          <button className="btn-secondary" onClick={chat.declineConsent}>
            {t('chat.privacyDecline')}
          </button>
        </div>
      </div>
    </div>
  )
}
