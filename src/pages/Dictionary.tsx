import { useMemo, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { FallbackNote, ReviewBadge } from '../components/Badges'
import { Highlight } from '../components/Highlight'
import { PageHeader } from '../components/PageHeader'
import { EmptyState, ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'
import { normalize } from '../lib/normalize'

export default function Dictionary() {
  const { termId } = useParams()
  const { t, tl, data, status, reload } = useApp()
  const [q, setQ] = useState('')

  const list = useMemo(() => {
    if (!data) return []
    const nq = normalize(q)
    const sorted = [...data.glossary].sort((a, b) => a.en.localeCompare(b.en))
    if (!nq) return sorted
    return sorted.filter((g) => {
      const hay = normalize([g.en, g.ur, g.sd, ...Object.values(g.definition)].join(' '))
      return nq.split(' ').every((w) => hay.includes(w))
    })
  }, [data, q])

  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />

  const selected = termId ? data.glossary.find((g) => g.id === termId) : undefined

  return (
    <div>
      <PageHeader eyebrow={t('nav.dictionary')} title={t('glossary.title')} sub={t('glossary.sub')} />
      <p className="mb-4 max-w-3xl rounded-md bg-amber-50 px-3 py-2 text-sm text-amber-900">{t('glossary.caveat')}</p>

      {termId && !selected && <EmptyState title={t('glossary.empty')} hint={t('glossary.emptyHint')} />}

      {selected && <TermDetail id={selected.id} />}

      <div role="search" className="mb-4 mt-6">
        <label className="block">
          <span className="sr-only">{t('common.search')}</span>
          <input type="search" value={q} maxLength={80} onChange={(e) => setQ(e.target.value)} placeholder={t('glossary.searchPlaceholder')} className="field w-full max-w-xl" />
        </label>
        <p className="mt-2 text-sm text-navy-600" aria-live="polite">
          {t('glossary.count', { count: list.length })}
        </p>
      </div>

      {list.length === 0 ? (
        <EmptyState title={t('glossary.empty')} hint={t('glossary.emptyHint')} />
      ) : (
        <ul className="grid gap-3 md:grid-cols-2">
          {list.map((g) => {
            const def = tl(g.definition)
            return (
              <li key={g.id}>
                <Link to={`/dictionary/${g.id}`} className={`card card-hover block h-full p-4 ${g.id === termId ? 'ring-2 ring-teal-500' : ''}`}>
                  <span className="heading-font block text-lg font-semibold">
                    <Highlight text={g.en} query={q} />
                  </span>
                  <span className="mt-0.5 flex flex-wrap gap-x-4 text-sm text-navy-700">
                    <span lang="ur">
                      <Highlight text={g.ur} query={q} />
                    </span>
                    <span lang="sd">
                      <Highlight text={g.sd} query={q} />
                    </span>
                  </span>
                  <span lang={def.lang} className="mt-2 block line-clamp-2 text-xs text-navy-500">
                    {def.text}
                  </span>
                </Link>
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )

  function TermDetail({ id }: { id: string }) {
    const g = data!.glossary.find((x) => x.id === id)!
    const def = tl(g.definition)
    const ex = tl(g.example)
    const laws = g.relatedLaws.map((l) => data!.laws.find((x) => x.id === l)).filter((l) => !!l)
    return (
      <section aria-labelledby="term-h" className="card border-teal-300 p-6">
        <div className="flex flex-wrap items-center gap-2">
          <ReviewBadge status={g.review} />
          <span className="chip">{t(`cat.${g.category}`)}</span>
        </div>
        <h2 id="term-h" className="heading-font mt-2 text-2xl font-bold">
          {g.en}
        </h2>
        <dl className="mt-3 grid gap-3 text-sm sm:grid-cols-3">
          <div>
            <dt className="text-xs font-semibold text-navy-500">{t('glossary.english')}</dt>
            <dd lang="en">{g.en}</dd>
          </div>
          <div>
            <dt className="text-xs font-semibold text-navy-500">{t('glossary.urdu')}</dt>
            <dd lang="ur" className="text-lg">
              {g.ur}
            </dd>
          </div>
          <div>
            <dt className="text-xs font-semibold text-navy-500">{t('glossary.sindhi')}</dt>
            <dd lang="sd" className="text-lg">
              {g.sd}
            </dd>
          </div>
        </dl>
        <h3 className="mt-4 text-sm font-semibold">{t('glossary.definition')}</h3>
        <p lang={def.lang} className="prose-legal">
          {def.text}
        </p>
        <FallbackNote show={def.fallback} />
        {ex.text && (
          <>
            <h3 className="mt-4 text-sm font-semibold">{t('glossary.example')}</h3>
            <p lang={ex.lang} className="prose-legal">
              {ex.text}
            </p>
          </>
        )}
        {laws.length > 0 && (
          <>
            <h3 className="mt-4 text-sm font-semibold">{t('glossary.relatedLaws')}</h3>
            <ul className="mt-1 flex flex-wrap gap-3 text-sm">
              {laws.map((l) => (
                <li key={l!.id}>
                  <Link dir="ltr" to={`/laws/${l!.id}`} className="font-semibold text-teal-700 hover:underline">
                    {l!.abbreviation ?? l!.title}
                  </Link>
                </li>
              ))}
            </ul>
          </>
        )}
      </section>
    )
  }
}
