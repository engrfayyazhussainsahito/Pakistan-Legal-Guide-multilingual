import { BookOpen, Check, ExternalLink, Link as LinkIcon, Lightbulb } from 'lucide-react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { cn } from '../lib/utils'
import type { Law, LawSection } from '../types'
import { FallbackNote, UnofficialNote } from './Badges'

type Mode = 'original' | 'understand'

/**
 * Two reading modes for every document:
 *  - Original law: statutory wording shown exactly as bundled (never edited) with its source.
 *  - Understand this law: plain-language explanation, terms, conditions — labelled as written for this site.
 * Desktop: side by side. Mobile: tabs.
 */
export function LawReader({ law, focusSection }: { law: Law; focusSection?: string }) {
  const { t } = useApp()
  const [mode, setMode] = useState<Mode>('understand')

  useEffect(() => {
    if (!focusSection) return
    const el = document.getElementById(`sec-${focusSection}`)
    if (el) {
      // wait a tick so layout has settled
      const id = window.setTimeout(() => {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' })
        el.focus({ preventScroll: true })
      }, 80)
      return () => window.clearTimeout(id)
    }
  }, [focusSection, law.id])

  if (!law.sections.length) {
    return (
      <div className="card p-6">
        <p className="text-sm text-navy-700">{t('law.noSections')}</p>
        <a href={law.sourceUrl} target="_blank" rel="noopener noreferrer" className="btn-primary mt-4 inline-flex">
          {t('law.viewOfficial')} <ExternalLink className="h-4 w-4" aria-hidden />
        </a>
      </div>
    )
  }

  return (
    <div>
      {/* Mobile tabs */}
      <div role="tablist" aria-label={t('law.sideBySide')} className="sticky top-16 z-20 -mx-4 mb-4 flex gap-1 border-b border-sand-200 bg-[#faf7f2]/95 px-4 py-2 backdrop-blur lg:hidden">
        {(['understand', 'original'] as Mode[]).map((m) => (
          <button
            key={m}
            role="tab"
            aria-selected={mode === m}
            onClick={() => setMode(m)}
            className={cn('flex-1 rounded-lg px-3 py-2 text-sm font-semibold', mode === m ? 'bg-navy-900 text-white' : 'bg-white text-navy-700 border border-sand-300')}
          >
            {m === 'original' ? t('law.originalLaw') : t('law.understand')}
          </button>
        ))}
      </div>

      {/* Desktop column headings */}
      <div className="mb-3 hidden grid-cols-2 gap-6 lg:grid">
        <h2 className="heading-font flex items-center gap-2 text-lg font-semibold">
          <BookOpen className="h-5 w-5 text-navy-500" aria-hidden />
          {t('law.originalLaw')}
        </h2>
        <h2 className="heading-font flex items-center gap-2 text-lg font-semibold">
          <Lightbulb className="h-5 w-5 text-teal-600" aria-hidden />
          {t('law.understand')}
        </h2>
      </div>

      <div className="space-y-6">
        {law.sections.map((s) => (
          <SectionRow key={s.id} law={law} s={s} mode={mode} focused={focusSection === s.id} />
        ))}
      </div>
    </div>
  )
}

function SectionRow({ law, s, mode, focused }: { law: Law; s: LawSection; mode: Mode; focused: boolean }) {
  const { t, tl, lang, data } = useApp()
  const [copied, setCopied] = useState(false)
  const explanation = tl(s.explanation)
  const conditions = s.conditions ? tl(s.conditions) : null

  const copyLink = async () => {
    const url = `${location.origin}${location.pathname}#/laws/${law.id}/${s.id}`
    try {
      await navigator.clipboard.writeText(url)
      setCopied(true)
      setTimeout(() => setCopied(false), 1800)
    } catch {
      /* clipboard unavailable — ignore */
    }
  }

  return (
    <article
      id={`sec-${s.id}`}
      tabIndex={-1}
      className={cn('card scroll-mt-32 overflow-hidden p-0 transition', focused && 'ring-2 ring-teal-500')}
    >
      <header className="flex flex-wrap items-center gap-3 border-b border-sand-200 bg-sand-50 px-5 py-3">
        <span dir="ltr" className="rounded-md bg-navy-900 px-2 py-0.5 text-sm font-semibold text-white">
          {s.number}
        </span>
        <h3 dir="ltr" className="heading-font flex-1 text-start text-base font-semibold">
          {s.heading}
        </h3>
        <button type="button" onClick={copyLink} className="btn-ghost px-2 py-1 text-xs" aria-label={t('law.copyLink')}>
          {copied ? <Check className="h-3.5 w-3.5 text-teal-700" aria-hidden /> : <LinkIcon className="h-3.5 w-3.5" aria-hidden />}
          <span aria-live="polite">{copied ? t('law.linkCopied') : t('law.copyLink')}</span>
        </button>
      </header>

      <div className="grid gap-0 lg:grid-cols-2 lg:divide-x lg:divide-sand-200 rtl:lg:divide-x-reverse">
        {/* Original */}
        <section className={cn('p-5', mode === 'original' ? 'block' : 'hidden', 'lg:block')} aria-label={t('law.originalLaw')}>
          <h4 className="eyebrow mb-2 lg:hidden">{t('law.originalLaw')}</h4>
          {s.originalText ? (
            <>
              {/* Statutory text is English and shown verbatim; kept LTR so numbering/punctuation never flips */}
              <blockquote dir="ltr" lang="en" className="whitespace-pre-line border-s-4 border-navy-200 ps-4 text-start font-serif text-[15.5px] leading-7 text-navy-900">
                {s.originalText}
              </blockquote>
              <p className="mt-3 text-xs text-navy-500">{t('law.originalLabel')}</p>
              <p dir="ltr" className="mt-1 text-start text-xs text-navy-500">
                {t('law.sourceLine', { source: s.originalTextSource ?? law.sourceName })}
              </p>
            </>
          ) : (
            <p className="rounded-lg border border-dashed border-sand-300 bg-sand-50 p-4 text-sm text-navy-700">{t('law.noOriginalText')}</p>
          )}
          <a href={law.sourceUrl} target="_blank" rel="noopener noreferrer" className="mt-3 inline-flex items-center gap-1.5 text-sm font-semibold text-teal-700 hover:underline">
            {t('law.viewOfficial')}
            <ExternalLink className="h-3.5 w-3.5" aria-hidden />
            <span className="sr-only">{t('common.opensNewTab')}</span>
          </a>
        </section>

        {/* Understand */}
        <section className={cn('bg-teal-50/40 p-5', mode === 'understand' ? 'block' : 'hidden', 'lg:block')} aria-label={t('law.understand')}>
          <h4 className="eyebrow mb-2 lg:hidden">{t('law.understand')}</h4>
          <div lang={explanation.lang} className="prose-legal">
            <p>{explanation.text}</p>
          </div>
          <FallbackNote show={explanation.fallback} />
          <p className="mt-2 text-xs text-navy-500">{t('law.explanationLabel')}</p>
          <UnofficialNote show={lang !== 'en' && !explanation.fallback} />

          {s.terms && s.terms.length > 0 && (
            <div className="mt-4">
              <h4 className="text-sm font-semibold text-navy-800">{t('law.terms')}</h4>
              <dl className="mt-1.5 space-y-1.5 text-sm">
                {s.terms.map((term) => {
                  const m = tl(term.meaning)
                  return (
                    <div key={term.term}>
                      <dt dir="ltr" className="inline text-start font-semibold text-teal-800">
                        {term.term}
                      </dt>
                      <dd lang={m.lang} className="inline text-navy-700">
                        {' — '}
                        {m.text}
                      </dd>
                    </div>
                  )
                })}
              </dl>
            </div>
          )}

          {conditions && (
            <div className="mt-4 rounded-lg border border-amber-200 bg-amber-50 p-3 text-sm text-amber-950">
              <h4 className="font-semibold">{t('law.conditions')}</h4>
              <p lang={conditions.lang} className="mt-1">
                {conditions.text}
              </p>
            </div>
          )}

          {s.glossary && s.glossary.length > 0 && data && (
            <div className="mt-4 flex flex-wrap items-center gap-1.5">
              <span className="text-xs font-semibold text-navy-500">{t('law.relatedTerms')}:</span>
              {s.glossary.map((gid) => {
                const g = data.glossary.find((x) => x.id === gid)
                return g ? (
                  <Link key={gid} to={`/dictionary/${gid}`} className="chip border-teal-300 bg-white text-teal-800 hover:bg-teal-50">
                    <span lang={lang === 'en' ? 'en' : lang}>{lang === 'en' ? g.en : g[lang]}</span>
                  </Link>
                ) : null
              })}
            </div>
          )}
        </section>
      </div>
    </article>
  )
}
