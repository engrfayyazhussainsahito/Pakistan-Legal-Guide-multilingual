import { Bot } from 'lucide-react'
import { useMemo } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { VerificationBadge } from '../components/Badges'
import { Highlight } from '../components/Highlight'
import { LegalSearch } from '../components/LegalSearch'
import { PageHeader } from '../components/PageHeader'
import { EmptyState, ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'
import type { SearchResult } from '../types'

const KINDS: SearchResult['kind'][] = ['law', 'section', 'topic', 'faq', 'glossary']
const KIND_KEY: Record<SearchResult['kind'], string> = {
  law: 'kindLaw',
  section: 'kindSection',
  glossary: 'kindGlossary',
  faq: 'kindFaq',
  topic: 'kindTopic',
}

export default function SearchPage() {
  const { t, lang, jurisdiction, engine, status, reload, tList } = useApp()
  const [params, setParams] = useSearchParams()
  const q = (params.get('q') ?? '').slice(0, 200)
  const kindParam = params.get('type') ?? ''
  const kind = (KINDS as string[]).includes(kindParam) ? (kindParam as SearchResult['kind']) : ''

  const results = useMemo(
    () => (engine && q.trim() ? engine.search(q, { lang, jurisdiction, kinds: kind ? [kind] : undefined, limit: 60 }) : []),
    [engine, q, lang, jurisdiction, kind],
  )

  const update = (next: { q?: string; type?: string }) => {
    const p = new URLSearchParams(params)
    if (next.q !== undefined) {
      if (next.q) p.set('q', next.q)
      else p.delete('q')
    }
    if (next.type !== undefined) {
      if (next.type) p.set('type', next.type)
      else p.delete('type')
    }
    setParams(p, { replace: true })
  }

  if (status === 'loading') return <Loading />
  if (status === 'error') return <ErrorState onRetry={reload} />

  return (
    <div>
      <PageHeader eyebrow={t('nav.search')} title={t('search.title')} sub={t('search.hint')} />
      <LegalSearch size="lg" autoFocus initial={q} onSubmit={(v) => update({ q: v })} className="max-w-3xl" placeholder={t('search.placeholder')} />

      <div className="mt-4 flex flex-wrap gap-2" role="group" aria-label={t('search.filterType')}>
        {(['', ...KINDS] as const).map((k) => (
          <button key={k || 'all'} type="button" aria-pressed={kind === k} onClick={() => update({ type: k })} className={kind === k ? 'btn-primary !py-1.5 text-sm' : 'btn-secondary !py-1.5 text-sm'}>
            {k ? t(`search.${KIND_KEY[k]}`) : t('search.typeAll')}
          </button>
        ))}
      </div>

      {!q.trim() ? (
        <div className="mt-8">
          <p className="text-sm text-navy-600">{t('search.prompt')}</p>
          <ul className="mt-3 flex flex-wrap gap-2">
            {tList('search.examples').map((ex) => (
              <li key={ex}>
                <button type="button" onClick={() => update({ q: ex })} className="chip hover:bg-teal-50">
                  {ex}
                </button>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <section className="mt-6" aria-live="polite">
          <p className="mb-3 text-sm text-navy-600">
            {t('search.resultsFor', { query: q })} · {t('common.results', { count: results.length })}
          </p>
          {results.length === 0 ? (
            <EmptyState
              title={t('search.empty', { query: q })}
              hint={t('search.emptyHint')}
              action={
                <Link to="/assistant" className="btn-secondary">
                  <Bot className="h-4 w-4" aria-hidden />
                  {t('search.askAssistant')}
                </Link>
              }
            />
          ) : (
            <>
              <ul className="space-y-3">
                {results.map((r) => (
                  <li key={`${r.kind}-${r.id}`}>
                    <Link to={r.to} className="card card-hover block p-4">
                      <span className="flex flex-wrap items-center gap-2 text-xs">
                        <span className="chip">{t(`search.${KIND_KEY[r.kind]}`)}</span>
                        {r.jurisdictionLabel && <span className="chip">{r.jurisdictionLabel}</span>}
                        {r.verification && <VerificationBadge status={r.verification} />}
                      </span>
                      <span className="heading-font mt-2 block text-lg font-semibold text-navy-900">
                        <Highlight text={r.title} query={q} />
                      </span>
                      <span className="mt-1 block text-sm text-navy-600">
                        <Highlight text={r.snippet} query={q} />
                      </span>
                      {r.verifyApplicability && <span className="mt-2 block text-xs text-amber-800">{t('jur.verifyApplicability')}</span>}
                    </Link>
                  </li>
                ))}
              </ul>
              <Link to="/assistant" className="btn-secondary mt-6 inline-flex">
                <Bot className="h-4 w-4" aria-hidden />
                {t('search.askAssistant')}
              </Link>
            </>
          )}
        </section>
      )}
    </div>
  )
}
