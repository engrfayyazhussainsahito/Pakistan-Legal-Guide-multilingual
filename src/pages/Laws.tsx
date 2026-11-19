import { useMemo, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { JurisdictionSelector } from '../components/JurisdictionSelector'
import { LawCard } from '../components/LawCard'
import { PageHeader } from '../components/PageHeader'
import { EmptyState, ErrorState, Loading } from '../components/StateViews'
import { useApp } from '../context/AppContext'
import { CATEGORIES } from '../lib/categories'
import { normalize } from '../lib/normalize'
import { useVisibleLaws } from '../lib/useLaws'
import type { CategoryId, Lang } from '../types'

export default function Laws() {
  const { t, status, reload, jurisdiction, jurName, data } = useApp()
  const [params, setParams] = useSearchParams()
  const visible = useVisibleLaws()
  const [q, setQ] = useState('')
  const [lawLang, setLawLang] = useState<'' | Lang>('')

  const catParam = params.get('category') ?? ''
  const category = (CATEGORIES as string[]).includes(catParam) ? (catParam as CategoryId) : ''

  const setCategory = (c: string) => {
    const next = new URLSearchParams(params)
    if (c) next.set('category', c)
    else next.delete('category')
    setParams(next, { replace: true })
  }

  const list = useMemo(() => {
    const nq = normalize(q)
    return visible.filter(({ law }) => {
      if (category && law.category !== category) return false
      if (lawLang && !law.languages.includes(lawLang)) return false
      if (nq) {
        const hay = normalize([law.title, law.abbreviation ?? '', ...law.keywords, ...Object.values(law.summary)].join(' '))
        if (!nq.split(' ').every((w) => hay.includes(w))) return false
      }
      return true
    })
  }, [visible, q, category, lawLang])

  if (status === 'loading') return <Loading />
  if (status === 'error' || !data) return <ErrorState onRetry={reload} />

  const reset = () => {
    setQ('')
    setLawLang('')
    setCategory('')
  }

  return (
    <div>
      <PageHeader eyebrow={t('nav.laws')} title={t('laws.title')} sub={t('laws.sub')} />

      <form role="search" onSubmit={(e) => e.preventDefault()} className="card mb-6 grid gap-4 p-4 md:grid-cols-2 lg:grid-cols-4">
        <label className="block">
          <span className="mb-1 block text-xs font-semibold text-navy-600">{t('common.search')}</span>
          <input type="search" value={q} maxLength={120} onChange={(e) => setQ(e.target.value)} placeholder={t('laws.searchPlaceholder')} className="field w-full" />
        </label>
        <label className="block">
          <span className="mb-1 block text-xs font-semibold text-navy-600">{t('laws.category')}</span>
          <select value={category} onChange={(e) => setCategory(e.target.value)} className="field w-full">
            <option value="">{t('common.all')}</option>
            {CATEGORIES.map((c) => (
              <option key={c} value={c}>
                {t(`cat.${c}`)}
              </option>
            ))}
          </select>
        </label>
        <div>
          <span className="mb-1 block text-xs font-semibold text-navy-600">{t('laws.jurisdiction')}</span>
          <JurisdictionSelector />
        </div>
        <label className="block">
          <span className="mb-1 block text-xs font-semibold text-navy-600">{t('laws.language')}</span>
          <select value={lawLang} onChange={(e) => setLawLang(e.target.value as '' | Lang)} className="field w-full">
            <option value="">{t('common.all')}</option>
            {(['en', 'ur', 'sd'] as Lang[]).map((l) => (
              <option key={l} value={l}>
                {t(`lang.${l}`)}
              </option>
            ))}
          </select>
        </label>
      </form>

      <div className="mb-4 flex flex-wrap items-center justify-between gap-2 text-sm text-navy-600" aria-live="polite">
        <p>
          {t('laws.showing', { count: list.length, total: visible.length })}
          {jurisdiction ? ` · ${jurName(jurisdiction)}` : ''}
        </p>
        {(q || category || lawLang) && (
          <button type="button" onClick={reset} className="font-semibold text-teal-700 hover:underline">
            {t('common.reset')}
          </button>
        )}
      </div>
      {!jurisdiction && <p className="mb-4 rounded-md bg-amber-50 px-3 py-2 text-sm text-amber-900">{t('jur.notSelectedWarning')}</p>}

      {list.length === 0 ? (
        <EmptyState
          title={t('laws.empty')}
          hint={t('laws.emptyHint')}
          action={
            <button type="button" onClick={reset} className="btn-secondary">
              {t('common.reset')}
            </button>
          }
        />
      ) : (
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {list.map((v) => (
            <LawCard key={v.law.id} law={v.law} verifyApplicability={v.verifyApplicability} />
          ))}
        </div>
      )}
    </div>
  )
}
