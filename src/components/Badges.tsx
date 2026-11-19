import { BadgeCheck, FileWarning, Link2, Languages, Landmark, Building2, MapPin } from 'lucide-react'
import { useApp } from '../context/AppContext'
import { kindOf } from '../lib/jurisdiction'
import { cn } from '../lib/utils'
import type { JurisdictionId, ReviewStatus, VerificationStatus } from '../types'

export function VerificationBadge({ status, className }: { status: VerificationStatus; className?: string }) {
  const { t } = useApp()
  const map = {
    verified: { Icon: BadgeCheck, label: t('status.verified'), desc: t('status.verifiedDesc'), cls: 'border-teal-300 bg-teal-50 text-teal-800' },
    'source-linked': { Icon: Link2, label: t('status.sourceLinked'), desc: t('status.sourceLinkedDesc'), cls: 'border-amber-300 bg-amber-50 text-amber-900' },
    illustrative: { Icon: FileWarning, label: t('status.illustrative'), desc: t('status.illustrativeDesc'), cls: 'border-rose-300 bg-rose-50 text-rose-900' },
  }[status]
  return (
    <span
      title={map.desc}
      className={cn('inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-xs font-semibold', map.cls, className)}
    >
      <map.Icon className="h-3.5 w-3.5 shrink-0" aria-hidden />
      {map.label}
    </span>
  )
}

export function JurisdictionTag({ id, className }: { id: JurisdictionId; className?: string }) {
  const { t, jurName } = useApp()
  const kind = kindOf(id)
  const Icon = kind === 'federal' ? Landmark : kind === 'provincial' ? Building2 : MapPin
  const kindLabel = t(kind === 'federal' ? 'jur.federalTag' : kind === 'provincial' ? 'jur.provincialTag' : 'jur.territoryTag')
  return (
    <span
      title={kindLabel}
      className={cn('inline-flex items-center gap-1 rounded-full border border-navy-200 bg-navy-50 px-2.5 py-0.5 text-xs font-medium text-navy-700', className)}
    >
      <Icon className="h-3.5 w-3.5 shrink-0" aria-hidden />
      {jurName(id)}
    </span>
  )
}

export function ReviewBadge({ status }: { status: ReviewStatus }) {
  const { t } = useApp()
  return status === 'reviewed' ? (
    <span className="chip border-teal-300 bg-teal-50 text-teal-800">{t('status.reviewed')}</span>
  ) : (
    <span className="chip">{t('status.unreviewed')}</span>
  )
}

/** Shown when content is not available in the chosen language so English is displayed instead. */
export function FallbackNote({ show }: { show: boolean }) {
  const { t, lang } = useApp()
  if (!show) return null
  return (
    <p className="mt-1 inline-flex items-center gap-1 text-xs text-amber-800">
      <Languages className="h-3.5 w-3.5" aria-hidden />
      {t('common.notAvailableInLang', { lang: t(`lang.${lang}`) })}
    </p>
  )
}

/** Marks Sindhi / Urdu text written for this site as unofficial. */
export function UnofficialNote({ show }: { show: boolean }) {
  const { t } = useApp()
  if (!show) return null
  return (
    <p className="mt-1 inline-flex items-start gap-1 text-xs text-sand-700">
      <Languages className="mt-0.5 h-3.5 w-3.5 shrink-0" aria-hidden />
      <span>{t('common.unofficialTranslation')}</span>
    </p>
  )
}
