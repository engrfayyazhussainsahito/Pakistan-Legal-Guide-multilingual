import { Check } from 'lucide-react'
import { Link } from 'react-router-dom'
import { PageHeader } from '../components/PageHeader'
import { PHASES } from '../components/Sidebar'
import { ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'

export default function Topics() {
  const { t, tl, data, status, reload, read } = useApp()
  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />

  return (
    <div>
      <PageHeader eyebrow={t('guide.syllabus')} title={t('topics.title')} sub={t('topics.sub')}>
        <p className="mt-3 text-sm font-medium text-teal-800">
          {t('guide.progress', { done: read.filter((id) => data.topics.some((c) => c.id === id)).length, total: data.topics.length })}
        </p>
      </PageHeader>
      <div className="space-y-10">
        {PHASES.map((p) => (
          <section key={p} aria-labelledby={`phase-${p}`}>
            <p className="eyebrow">{t('guide.phase', { n: p })}</p>
            <h2 id={`phase-${p}`} className="heading-font mt-1 text-2xl font-bold">
              {t(`guide.p${p}`)}
            </h2>
            <p className="mb-4 mt-1 text-sm text-navy-600">{t(`guide.p${p}d`)}</p>
            <ol className="grid gap-3 md:grid-cols-2">
              {data.topics
                .filter((c) => c.phase === p)
                .map((c) => {
                  const title = tl(c.title)
                  const desc = tl(c.description)
                  const done = read.includes(c.id)
                  return (
                    <li key={c.id}>
                      <Link to={`/topics/${c.id}`} className="card card-hover flex h-full gap-4 p-4">
                        <span className="heading-font text-2xl font-bold tabular-nums text-teal-700">{String(c.number).padStart(2, '0')}</span>
                        <span className="min-w-0 flex-1">
                          <span lang={title.lang} className="block font-semibold text-navy-900">
                            {title.text}
                          </span>
                          <span lang={desc.lang} className="mt-1 block text-sm text-navy-600">
                            {desc.text}
                          </span>
                          <span className="mt-2 flex items-center gap-3 text-xs text-navy-500">
                            <span>{t('guide.minutes', { min: c.minutes })}</span>
                            {done && (
                              <span className="inline-flex items-center gap-1 font-semibold text-teal-700">
                                <Check className="h-3.5 w-3.5" aria-hidden />
                                {t('guide.isRead')}
                              </span>
                            )}
                          </span>
                        </span>
                      </Link>
                    </li>
                  )
                })}
            </ol>
          </section>
        ))}
      </div>
    </div>
  )
}
