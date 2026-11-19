import { ExternalLink } from 'lucide-react'
import { PageHeader } from '../components/PageHeader'
import { useApp } from '../context/AppContext'
import { OFFICIAL_SOURCES } from '../services/data'

export default function About() {
  const { t, data } = useApp()
  const blocks: [string, string][] = [
    ['missionTitle', 'mission'],
    ['verifyTitle', 'verifyBody'],
    ['translationTitle', 'translationBody'],
    ['privacyTitle', 'privacyBody'],
    ['limitsTitle', 'limitsBody'],
    ['ragTitle', 'ragBody'],
  ]
  return (
    <div className="max-w-3xl">
      <PageHeader eyebrow={t('nav.about')} title={t('about.title')} />
      <div className="space-y-8">
        {blocks.map(([h, b]) => (
          <section key={h}>
            <h2 className="heading-font text-xl font-semibold">{t(`about.${h}`)}</h2>
            <p className="prose-legal mt-2">{t(`about.${b}`)}</p>
          </section>
        ))}
        <section>
          <h2 className="heading-font text-xl font-semibold">{t('about.sourcesTitle')}</h2>
          <ul className="mt-3 space-y-2">
            {OFFICIAL_SOURCES.map((s) => (
              <li key={s.url}>
                <a href={s.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm font-semibold text-teal-700 hover:underline">
                  {t(`sources.${s.key}`)}
                  <ExternalLink className="h-3.5 w-3.5" aria-hidden />
                  <span className="sr-only">{t('common.opensNewTab')}</span>
                </a>
              </li>
            ))}
          </ul>
        </section>
        {data && (
          <p className="text-xs text-navy-500">
            {t('law.version')}: {data.libraryVersion} · {t('law.lastVerified')}: {data.lastReviewed}
          </p>
        )}
      </div>
    </div>
  )
}
