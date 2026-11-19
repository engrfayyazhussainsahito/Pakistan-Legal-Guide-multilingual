import { MapPin } from 'lucide-react'
import { useId } from 'react'
import { useApp } from '../context/AppContext'
import { JURISDICTIONS } from '../lib/jurisdiction'
import { cn } from '../lib/utils'
import type { JurisdictionChoice } from '../types'

export function JurisdictionSelector({ className, compact = false }: { className?: string; compact?: boolean }) {
  const { jurisdiction, setJurisdiction, t, jurName } = useApp()
  const id = useId()
  return (
    <div className={cn('flex items-center gap-1.5', className)}>
      <label htmlFor={id} className="sr-only">
        {t('jur.label')}
      </label>
      <MapPin className="h-4 w-4 shrink-0 text-navy-400" aria-hidden />
      <select
        id={id}
        value={jurisdiction}
        onChange={(e) => setJurisdiction(e.target.value as JurisdictionChoice)}
        className={cn(
          'rounded-lg border border-navy-200 bg-white py-1.5 ps-2 pe-7 text-sm text-navy-800 focus:border-teal-600',
          compact ? 'max-w-[11rem]' : 'max-w-full',
        )}
      >
        <option value="">{t('jur.none')}</option>
        {JURISDICTIONS.map((j) => (
          <option key={j} value={j}>
            {jurName(j)}
          </option>
        ))}
      </select>
    </div>
  )
}

/** Card-style jurisdiction picker used on the homepage. */
export function JurisdictionGrid() {
  const { jurisdiction, setJurisdiction, t, jurName } = useApp()
  const all: JurisdictionChoice[] = ['', ...JURISDICTIONS]
  return (
    <div role="radiogroup" aria-label={t('jur.label')} className="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-5">
      {all.map((j) => {
        const active = jurisdiction === j
        return (
          <button
            key={j || 'all'}
            role="radio"
            aria-checked={active}
            onClick={() => setJurisdiction(j)}
            className={cn(
              'rounded-lg border px-3 py-2.5 text-start text-sm font-medium transition',
              active ? 'border-teal-600 bg-teal-50 text-teal-900 shadow-card' : 'border-sand-200 bg-white text-navy-700 hover:border-teal-300',
            )}
          >
            {j ? jurName(j) : t('jur.none')}
          </button>
        )
      })}
    </div>
  )
}
