import type { ReactNode } from 'react'
import { AlertTriangle, Loader2, SearchX } from 'lucide-react'
import { useApp } from '../context/AppContext'

export function Loading({ label }: { label?: string }) {
  const { t } = useApp()
  return (
    <div role="status" aria-live="polite" className="flex items-center justify-center gap-3 py-20 text-navy-600">
      <Loader2 className="h-5 w-5 animate-spin" aria-hidden />
      <span className="text-sm">{label ?? t('common.loading')}</span>
    </div>
  )
}

export function ErrorState({ message, onRetry }: { message?: string; onRetry?: () => void }) {
  const { t } = useApp()
  return (
    <div role="alert" className="card mx-auto my-10 max-w-lg p-8 text-center">
      <AlertTriangle className="mx-auto h-8 w-8 text-amber-600" aria-hidden />
      <h2 className="heading-font mt-3 text-xl font-semibold">{t('common.error')}</h2>
      <p className="mt-2 text-sm text-navy-600">{message ?? t('common.dataLoadError')}</p>
      {onRetry && (
        <button onClick={onRetry} className="btn-primary mt-5">
          {t('common.retry')}
        </button>
      )}
    </div>
  )
}

export function EmptyState({ title, hint, action }: { title: string; hint?: string; action?: ReactNode }) {
  return (
    <div className="card mx-auto my-6 max-w-xl p-8 text-center">
      <SearchX className="mx-auto h-8 w-8 text-sand-500" aria-hidden />
      <h2 className="heading-font mt-3 text-lg font-semibold">{title}</h2>
      {hint && <p className="mt-2 text-sm text-navy-600">{hint}</p>}
      {action && <div className="mt-5 flex flex-wrap justify-center gap-2">{action}</div>}
    </div>
  )
}
