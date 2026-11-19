import { ExternalLink, ShieldAlert } from 'lucide-react'
import { Link } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { OFFICIAL_SOURCES } from '../services/data'
import { Brand } from './Header'

export function Footer() {
  const { t, data } = useApp()
  return (
    <footer className="mt-16 border-t border-sand-200 bg-navy-950 text-navy-100">
      <div className="container-page grid gap-10 py-12 md:grid-cols-[1.4fr_1fr_1fr]">
        <div>
          <div className="[&_*]:!text-white [&_.text-teal-700]:!text-teal-300">
            <Brand />
          </div>
          <div className="mt-5 flex gap-3 rounded-xl border border-navy-700 bg-navy-900/60 p-4 text-sm leading-relaxed text-navy-100">
            <ShieldAlert className="mt-0.5 h-5 w-5 shrink-0 text-teal-300" aria-hidden />
            <div>
              <p className="font-semibold text-white">{t('footer.disclaimerTitle')}</p>
              <p className="mt-1 text-navy-200">{t('footer.disclaimer')}</p>
            </div>
          </div>
        </div>
        <div>
          <h2 className="eyebrow !text-teal-300">{t('footer.explore')}</h2>
          <ul className="mt-3 space-y-2 text-sm">
            {[
              ['/laws', 'nav.laws'],
              ['/topics', 'nav.topics'],
              ['/rights', 'nav.rights'],
              ['/dictionary', 'nav.dictionary'],
              ['/assistant', 'nav.assistant'],
              ['/search', 'nav.search'],
              ['/about', 'footer.privacy'],
            ].map(([to, key]) => (
              <li key={to}>
                <Link to={to} className="text-navy-100 hover:text-white hover:underline">
                  {t(key)}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h2 className="eyebrow !text-teal-300">{t('footer.sources')}</h2>
          <ul className="mt-3 space-y-2 text-sm">
            {OFFICIAL_SOURCES.map((s) => (
              <li key={s.url}>
                <a href={s.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-navy-100 hover:text-white hover:underline">
                  {t(`sources.${s.key}`)}
                  <ExternalLink className="h-3 w-3 opacity-70" aria-hidden />
                  <span className="sr-only">{t('common.opensNewTab')}</span>
                </a>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <div className="border-t border-navy-800">
        <div className="container-page flex flex-col gap-1 py-4 text-xs text-navy-300 sm:flex-row sm:justify-between">
          <p>{t('footer.copyright')}</p>
          {data && <p>{t('footer.version', { version: data.libraryVersion })}</p>}
        </div>
      </div>
    </footer>
  )
}
