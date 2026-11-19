import { useMemo } from 'react'
import { useApp } from '../context/AppContext'
import { lawVisibility } from './jurisdiction'
import type { Law } from '../types'

export interface VisibleLaw {
  law: Law
  verifyApplicability: boolean
  exact: boolean
}

/** Laws that apply for the currently selected jurisdiction (exact matches first). */
export function useVisibleLaws(): VisibleLaw[] {
  const { data, jurisdiction } = useApp()
  return useMemo(() => {
    if (!data) return []
    const out: VisibleLaw[] = []
    for (const law of data.laws) {
      const v = lawVisibility(law, jurisdiction)
      if (v.visible) out.push({ law, verifyApplicability: v.verifyApplicability, exact: v.exact })
    }
    return out.sort((a, b) => Number(b.exact) - Number(a.exact) || a.law.title.localeCompare(b.law.title))
  }, [data, jurisdiction])
}
