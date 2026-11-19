import { Check, Info, RotateCcw } from 'lucide-react'
import { NavLink } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { cn } from '../lib/utils'
import type { PhaseId } from '../types'

export const PHASES: PhaseId[] = [1, 2, 3, 4]

/** Persistent numbered table of contents grouped into four phases (desktop). */
export function Sidebar({ className }: { className?: string }) {
  const { t, tl, data, read, resetProgress, lang } = useApp()
  const topics = data?.topics ?? []
  const done = topics.filter((x) => read.includes(x.id)).length
  const pct = topics.length ? Math.round((done / topics.length) * 100) : 0

  return (
    <nav aria-label={t('sidebar.title')} className={cn('text-sm', className)}>
      <div className="mb-4 rounded-xl border border-sand-200 bg-white p-3.5 shadow-card">
        <div className="flex items-center justify-between text-xs font-semibold text-navy-700">
          <span>{t('guide.progress', { done, total: topics.length })}</span>
          <span className="tabular-nums text-teal-700">{pct}%</span>
        </div>
        <div
          role="progressbar"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={pct}
          aria-label={t('guide.progress', { done, total: topics.length })}
          className="mt-2 h-1.5 overflow-hidden rounded-full bg-sand-200"
        >
          <div className="h-full rounded-full bg-teal-600 transition-all" style={{ width: `${pct}%` }} />
        </div>
      </div>

      {PHASES.map((p) => {
        const items = topics.filter((x) => x.phase === p)
        if (!items.length) return null
        return (
          <div key={p} className="mb-5">
            <p className="eyebrow mb-1.5 px-2">
              {t('guide.phase', { n: p })} · {t(`guide.p${p}`)}
            </p>
            <ol className="space-y-0.5">
              {items.map((c) => {
                const isRead = read.includes(c.id)
                return (
                  <li key={c.id}>
                    <NavLink
                      to={`/topics/${c.id}`}
                      className={({ isActive }) =>
                        cn(
                          'flex items-start gap-2.5 rounded-lg px-2 py-1.5 leading-snug transition',
                          isActive ? 'bg-navy-900 text-white' : 'text-navy-700 hover:bg-navy-50',
                        )
                      }
                    >
                      <span
                        className={cn(
                          'mt-0.5 grid h-5 w-5 shrink-0 place-items-center rounded-full text-[10px] font-bold tabular-nums',
                          isRead ? 'bg-teal-600 text-white' : 'bg-sand-200 text-navy-700',
                        )}
                        aria-hidden
                      >
                        {isRead ? <Check className="h-3 w-3" /> : String(c.number).padStart(2, '0')}
                      </span>
                      <span lang={lang} className="min-w-0 flex-1">
                        {tl(c.title).text}
                        {isRead && <span className="sr-only"> ✓</span>}
                      </span>
                    </NavLink>
                  </li>
                )
              })}
            </ol>
          </div>
        )
      })}

      <div className="mt-2 space-y-1 border-t border-sand-200 pt-3">
        <NavLink to="/about" className="flex items-center gap-2 rounded-lg px-2 py-1.5 text-navy-700 hover:bg-navy-50">
          <Info className="h-4 w-4" aria-hidden />
          {t('sidebar.about')}
        </NavLink>
        <button
          type="button"
          onClick={() => {
            if (window.confirm(t('guide.resetConfirm'))) resetProgress()
          }}
          className="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-start text-navy-700 hover:bg-navy-50"
        >
          <RotateCcw className="h-4 w-4" aria-hidden />
          {t('guide.reset')}
        </button>
        <p className="px-2 pt-1 text-xs text-navy-400">{t('guide.saved')}</p>
      </div>
    </nav>
  )
}
