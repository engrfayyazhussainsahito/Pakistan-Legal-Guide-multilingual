import { Link } from 'react-router-dom'
import { FallbackNote } from '../components/Badges'
import { PageHeader } from '../components/PageHeader'
import { ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'

export default function Rights() {
  const { t, tl, data, status, reload } = useApp()
  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />
  return (
    <div>
      <PageHeader eyebrow={t('nav.rights')} title={t('rights.title')} sub={t('rights.sub')} />
      <p className="mb-6 max-w-3xl text-sm text-navy-600">{t('rights.intro')}</p>
      <ul className="grid gap-4 md:grid-cols-2">
        {data.rights.map((r) => {
          const title = tl(r.title)
          const body = tl(r.body)
          const law = data.laws.find((l) => l.id === r.lawId)
          const sec = law?.sections.find((s) => s.id === r.sectionId)
          return (
            <li key={r.id} className="card p-5">
              <h2 lang={title.lang} className="heading-font text-lg font-semibold">
                {title.text}
              </h2>
              <p lang={body.lang} className="mt-2 text-sm leading-relaxed text-navy-700">
                {body.text}
              </p>
              <FallbackNote show={body.fallback} />
              {law && (
                <Link dir="ltr" to={`/laws/${law.id}${sec ? `/${sec.id}` : ''}`} className="mt-3 inline-block text-start text-sm font-semibold text-teal-700 hover:underline">
                  {t('rights.readLaw')}: {law.abbreviation ?? law.title}
                  {sec ? ` · ${sec.number}` : ''}
                </Link>
              )}
            </li>
          )
        })}
      </ul>
    </div>
  )
}
