import { ArrowRight, TriangleAlert } from 'lucide-react'
import { Link } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { cn } from '../lib/utils'
import type { Law } from '../types'
import { JurisdictionTag, VerificationBadge } from './Badges'

export function LawCard({ law, verifyApplicability = false, className }: { law: Law; verifyApplicability?: boolean; className?: string }) {
  const { t, tl, lang } = useApp()
  const summary = tl(law.summary)
  return (
    <Link to={`/laws/${law.id}`} className={cn('card card-hover group flex h-full flex-col p-5', className)}>
      <div className="flex flex-wrap items-center gap-1.5">
        <JurisdictionTag id={law.jurisdiction} />
        <span className="chip">{t(`cat.${law.category}`)}</span>
        {law.year && <span className="chip tabular-nums">{law.year}</span>}
      </div>
      <h3 dir="ltr" className="heading-font mt-3 text-start text-[17px] font-semibold leading-snug text-navy-900 group-hover:text-teal-800">
        {law.title}
        {law.abbreviation && <span className="ms-2 text-sm font-medium text-teal-700">({law.abbreviation})</span>}
      </h3>
      <p lang={summary.lang} className="mt-2 line-clamp-3 flex-1 text-sm leading-relaxed text-navy-600">
        {summary.text}
      </p>
      {summary.fallback && lang !== 'en' && <p className="mt-1 text-xs text-amber-800">{t('common.notAvailableInLang', { lang: t(`lang.${lang}`) })}</p>}
      {verifyApplicability && (
        <p className="mt-2 flex items-start gap-1.5 rounded-md bg-amber-50 px-2 py-1.5 text-xs text-amber-900">
          <TriangleAlert className="mt-0.5 h-3.5 w-3.5 shrink-0" aria-hidden />
          {t('jur.verifyApplicability')}
        </p>
      )}
      <div className="mt-4 flex items-center justify-between gap-2">
        <VerificationBadge status={law.verification} />
        <span className="inline-flex items-center gap-1 text-sm font-semibold text-teal-700">
          {t('common.viewDetails')}
          <ArrowRight className="h-4 w-4 transition group-hover:translate-x-0.5 rtl:-scale-x-100 rtl:group-hover:-translate-x-0.5" aria-hidden />
        </span>
      </div>
    </Link>
  )
}
