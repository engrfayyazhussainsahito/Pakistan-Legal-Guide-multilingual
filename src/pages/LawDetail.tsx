import { ArrowLeft, ExternalLink } from 'lucide-react'
import { Link, useParams } from 'react-router-dom'
import { JurisdictionTag, VerificationBadge } from '../components/Badges'
import { LawReader } from '../components/LawReader'
import { EmptyState, ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'
import { lawVisibility } from '../lib/jurisdiction'

export default function LawDetail() {
  const { id, sectionId } = useParams()
  const { t, tl, data, status, reload, jurisdiction, jurName } = useApp()
  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />
  const law = data.laws.find((l) => l.id === id)
  if (!law) {
    return (
      <EmptyState
        title={t('laws.notFound')}
        hint={t('laws.notFoundBody')}
        action={
          <Link to="/laws" className="btn-primary">
            {t('laws.backToLaws')}
          </Link>
        }
      />
    )
  }
  const vis = lawVisibility(law, jurisdiction)
  const note = tl(law.applicabilityNote)
  const summary = tl(law.summary)
  const related = (law.relatedLaws ?? []).map((r) => data.laws.find((l) => l.id === r)).filter((l) => !!l)
  const terms = Array.from(new Set(law.sections.flatMap((s) => s.glossary ?? []))).map((g) => data.glossary.find((x) => x.id === g)).filter((g) => !!g)
  const meta: [string, string][] = [
    [t('law.abbreviation'), law.abbreviation ?? '—'],
    [t('law.category'), t(`cat.${law.category}`)],
    [t('law.enacted'), law.year ? String(law.year) : t('law.yearUnknown')],
    [t('law.version'), law.version ?? t('law.versionUnknown')],
    [t('law.lastVerified'), law.lastVerified ?? t('law.neverVerified')],
    [t('law.languages'), law.languages.map((l) => t(`lang.${l}`)).join(', ')],
  ]

  return (
    <article>
      <Link to="/laws" className="mb-4 inline-flex items-center gap-1 text-sm font-semibold text-teal-700 hover:underline">
        <ArrowLeft className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
        {t('laws.backToLaws')}
      </Link>
      <header className="border-b border-sand-200 pb-6">
        <div className="flex flex-wrap items-center gap-2">
          <JurisdictionTag id={law.jurisdiction} />
          <VerificationBadge status={law.verification} />
        </div>
        <h1 dir="ltr" className="heading-font mt-3 text-start text-3xl font-bold leading-tight tracking-tight sm:text-4xl">
          {law.title}
        </h1>
        {law.titleTranslations && (
          <p className="mt-1 text-sm text-navy-500">
            {t('law.titleTranslation')}: {Object.values(law.titleTranslations).join(' / ')}
          </p>
        )}
        <p lang={summary.lang} className="mt-3 max-w-3xl text-base text-navy-700">
          {summary.text}
        </p>
        <dl className="mt-5 grid grid-cols-2 gap-x-6 gap-y-3 text-sm sm:grid-cols-3">
          {meta.map(([k, v]) => (
            <div key={k}>
              <dt className="text-xs font-semibold text-navy-500">{k}</dt>
              <dd className="font-medium">{v}</dd>
            </div>
          ))}
          <div>
            <dt className="text-xs font-semibold text-navy-500">{t('law.appliesTo')}</dt>
            <dd className="font-medium">{law.appliesTo.map((a) => jurName(a)).join(', ')}</dd>
          </div>
        </dl>
        {vis.verifyApplicability && <p className="mt-4 rounded-md bg-amber-50 px-3 py-2 text-sm text-amber-900">{t('jur.verifyApplicability')}</p>}
        {note.text && (
          <p lang={note.lang} className="mt-3 text-sm text-navy-600">
            {t('law.applicabilityNote')}: {note.text}
          </p>
        )}
        <a href={law.sourceUrl} target="_blank" rel="noopener noreferrer" className="btn-secondary mt-4 inline-flex">
          {t('law.viewOfficial')} · {law.sourceName}
          <ExternalLink className="h-4 w-4" aria-hidden />
          <span className="sr-only">{t('common.opensNewTab')}</span>
        </a>
        {!law.sourceUrlVerified && <p className="mt-2 text-xs text-navy-500">{t('status.sourceUrlUnverified')}</p>}
      </header>

      <div className="mt-8">
        <LawReader law={law} focusSection={sectionId} />
      </div>

      {(related.length > 0 || terms.length > 0) && (
        <div className="mt-12 grid gap-8 md:grid-cols-2">
          {related.length > 0 && (
            <section>
              <h2 className="heading-font text-xl font-semibold">{t('law.relatedLaws')}</h2>
              <ul className="mt-3 space-y-2 text-sm">
                {related.map((l) => (
                  <li key={l!.id}>
                    <Link dir="ltr" to={`/laws/${l!.id}`} className="font-semibold text-teal-700 hover:underline">
                      {l!.title}
                    </Link>
                  </li>
                ))}
              </ul>
            </section>
          )}
          {terms.length > 0 && (
            <section>
              <h2 className="heading-font text-xl font-semibold">{t('law.relatedTerms')}</h2>
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
        </div>
      )}
    </article>
  )
}
