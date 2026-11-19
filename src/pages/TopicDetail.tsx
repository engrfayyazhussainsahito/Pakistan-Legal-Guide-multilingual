import { ArrowLeft, ArrowRight, Check } from 'lucide-react'
import { useState } from 'react'
import { Link, useLocation, useParams } from 'react-router-dom'
import { ReviewBadge, FallbackNote } from '../components/Badges'
import { Collapsible } from '../components/Collapsible'
import { EmptyState, ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'

export default function TopicDetail() {
  const { id } = useParams()
  const { hash } = useLocation()
  const { t, tl, data, status, reload, read, toggleRead } = useApp()
  const [shown, setShown] = useState<Record<number, boolean>>({})

  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />
  const idx = data.topics.findIndex((c) => c.id === id)
  const topic = data.topics[idx]
  if (!topic) {
    return (
      <EmptyState
        title={t('topics.notFound')}
        action={
          <Link to="/topics" className="btn-primary">
            {t('topics.backToTopics')}
          </Link>
        }
      />
    )
  }
  const prev = data.topics[idx - 1]
  const next = data.topics[idx + 1]
  const title = tl(topic.title)
  const intro = tl(topic.intro)
  const faqs = topic.faqIds.map((f) => data.faqs.find((x) => x.id === f)).filter((f) => !!f)
  const terms = topic.terms.map((x) => data.glossary.find((g) => g.id === x)).filter((g) => !!g)
  const isRead = read.includes(topic.id)
  const anchor = hash.replace('#', '')

  return (
    <article>
      <Link to="/topics" className="mb-4 inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:underline">
        <ArrowLeft className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
        {t('topics.backToTopics')}
      </Link>
      <header className="border-b border-sand-200 pb-6">
        <p className="eyebrow">
          {t('guide.chapter', { n: String(topic.number).padStart(2, '0') })} · {t('guide.phase', { n: topic.phase })} · {t('guide.minutes', { min: topic.minutes })}
        </p>
        <h1 lang={title.lang} className="heading-font mt-1 text-3xl font-bold tracking-tight sm:text-4xl">
          {title.text}
        </h1>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <ReviewBadge status="unreviewed" />
          <FallbackNote show={title.fallback} />
        </div>
        <p className="mt-2 text-xs text-navy-500">{t('topics.reviewNote')}</p>
      </header>

      <section className="mt-8">
        <h2 className="heading-font text-xl font-semibold">{t('guide.inPlainWords')}</h2>
        <p lang={intro.lang} className="prose-legal mt-2 max-w-3xl">
          {intro.text}
        </p>
      </section>

      {topic.steps.length > 0 && (
        <section className="mt-8">
          <h2 className="heading-font text-xl font-semibold">{t('topics.steps')}</h2>
          <ol className="mt-3 space-y-3">
            {topic.steps.map((s, i) => {
              const st = tl(s)
              return (
                <li key={i} className="flex gap-3">
                  <span className="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-navy-900 text-xs font-bold text-white">{i + 1}</span>
                  <p lang={st.lang} className="pt-0.5 text-[15px] leading-relaxed">
                    {st.text}
                  </p>
                </li>
              )
            })}
          </ol>
        </section>
      )}

      {faqs.length > 0 && (
        <section className="mt-10">
          <h2 className="heading-font text-xl font-semibold">{t('topics.faqs')}</h2>
          <div className="mt-3 space-y-3">
            {faqs.map((f) => {
              const q = tl(f!.question)
              const a = tl(f!.answer)
              return (
                <Collapsible key={f!.id} id={`faq-${f!.id}`} title={q.text} titleLang={q.lang} defaultOpen={anchor === f!.id || anchor === `faq-${f!.id}`}>
                  <p lang={a.lang} className="prose-legal">
                    {a.text}
                  </p>
                  {f!.jurisdictionSensitive && <p className="mt-2 text-xs text-amber-800">{t('topics.jurisdictionSensitive')}</p>}
                  <FallbackNote show={a.fallback} />
                  <div className="mt-2 flex flex-wrap gap-3 text-sm">
                    {f!.relatedLaws.map((r) => {
                      const law = data.laws.find((l) => l.id === r.lawId)
                      if (!law) return null
                      return (
                        <Link key={r.lawId + (r.sectionId ?? '')} dir="ltr" to={`/laws/${r.lawId}${r.sectionId ? `/${r.sectionId}` : ''}`} className="font-semibold text-teal-700 hover:underline">
                          {law.abbreviation ?? law.title}
                          {r.sectionId ? ` · ${law.sections.find((s) => s.id === r.sectionId)?.number ?? ''}` : ''}
                        </Link>
                      )
                    })}
                  </div>
                </Collapsible>
              )
            })}
          </div>
        </section>
      )}

      {topic.check.length > 0 && (
        <section className="mt-10 rounded-xl bg-sand-100 p-5">
          <h2 className="heading-font text-xl font-semibold">{t('guide.check')}</h2>
          <ul className="mt-3 space-y-3">
            {topic.check.map((c, i) => {
              const q = tl(c.q)
              const a = tl(c.a)
              const open = !!shown[i]
              return (
                <li key={i} className="rounded-lg bg-white p-4">
                  <p lang={q.lang} className="font-medium">
                    {q.text}
                  </p>
                  <button type="button" aria-expanded={open} onClick={() => setShown((s) => ({ ...s, [i]: !s[i] }))} className="btn-secondary mt-2">
                    {open ? t('guide.hideAnswer') : t('guide.showAnswer')}
                  </button>
                  {open && (
                    <p lang={a.lang} className="mt-2 text-sm text-navy-700">
                      {a.text}
                    </p>
                  )}
                </li>
              )
            })}
          </ul>
        </section>
      )}

      {terms.length > 0 && (
        <section className="mt-10">
          <h2 className="heading-font text-xl font-semibold">{t('guide.keyTerms')}</h2>
          <ul className="mt-3 flex flex-wrap gap-2">
            {terms.map((g) => (
              <li key={g!.id}>
                <Link to={`/dictionary/${g!.id}`} className="chip hover:bg-teal-50">
                  {g!.en}
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}

      {topic.relatedLaws.length > 0 && (
        <section className="mt-10">
          <h2 className="heading-font text-xl font-semibold">{t('guide.lawsHere')}</h2>
          <ul className="mt-3 grid gap-2 sm:grid-cols-2">
            {topic.relatedLaws.map((r) => {
              const law = data.laws.find((l) => l.id === r.lawId)
              if (!law) return null
              const sec = r.sectionId ? law.sections.find((s) => s.id === r.sectionId) : undefined
              return (
                <li key={r.lawId + (r.sectionId ?? '')}>
                  <Link to={`/laws/${r.lawId}${sec ? `/${sec.id}` : ''}`} className="card card-hover block p-3 text-sm">
                    <span dir="ltr" className="block text-start font-semibold">
                      {law.title}
                    </span>
                    {sec && (
                      <span dir="ltr" className="block text-start text-xs text-teal-700">
                        {sec.number} — {sec.heading}
                      </span>
                    )}
                  </Link>
                </li>
              )
            })}
          </ul>
        </section>
      )}

      <div className="mt-10 flex flex-wrap items-center justify-between gap-3 border-t border-sand-200 pt-6">
        <button type="button" onClick={() => toggleRead(topic.id)} aria-pressed={isRead} className={isRead ? 'btn-teal' : 'btn-secondary'}>
          <Check className="h-4 w-4" aria-hidden />
          {isRead ? t('guide.isRead') : t('guide.markRead')}
        </button>
        <div className="flex gap-2">
          {prev && (
            <Link to={`/topics/${prev.id}`} className="btn-secondary">
              <ArrowLeft className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
              {t('guide.prev')}
            </Link>
          )}
          {next && (
            <Link to={`/topics/${next.id}`} className="btn-primary">
              {t('guide.next')}
              <ArrowRight className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
            </Link>
          )}
        </div>
      </div>
      <p className="mt-3 text-xs text-navy-500">{t('guide.saved')}</p>
    </article>
  )
}

