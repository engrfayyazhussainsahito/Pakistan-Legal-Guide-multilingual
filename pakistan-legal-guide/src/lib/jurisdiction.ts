import type { JurisdictionChoice, JurisdictionId, Law } from '../types'

export const JURISDICTIONS: JurisdictionId[] = [
  'sindh',
  'punjab',
  'kpk',
  'balochistan',
  'ict',
  'gb',
  'ajk',
  'federal',
]

export type JurisdictionKind = 'federal' | 'provincial' | 'territory'

export function kindOf(j: JurisdictionId): JurisdictionKind {
  if (j === 'federal') return 'federal'
  if (j === 'ict' || j === 'gb' || j === 'ajk') return 'territory'
  return 'provincial'
}

export interface Visibility {
  visible: boolean
  /** Federal law shown for GB / AJK where applicability must be checked */
  verifyApplicability: boolean
  /** The law is made specifically for the selected jurisdiction */
  exact: boolean
}

/**
 * Decide whether a law should be shown for the chosen jurisdiction.
 * - No selection: everything is visible (and labelled).
 * - "Federal / nationwide": laws made at federal level.
 * - A province/territory: laws that explicitly list it in `appliesTo`.
 *   Laws from other provinces are hidden — we never assume Punjab law applies in Sindh.
 * - Gilgit-Baltistan / AJK: federal laws are shown with a caution flag.
 */
export function lawVisibility(law: Law, choice: JurisdictionChoice): Visibility {
  if (!choice) return { visible: true, verifyApplicability: false, exact: false }
  if (choice === 'federal') {
    return { visible: law.jurisdiction === 'federal', verifyApplicability: false, exact: law.jurisdiction === 'federal' }
  }
  if (law.appliesTo.includes(choice)) {
    return { visible: true, verifyApplicability: false, exact: law.jurisdiction === choice }
  }
  if ((choice === 'gb' || choice === 'ajk') && law.jurisdiction === 'federal') {
    return { visible: true, verifyApplicability: true, exact: false }
  }
  return { visible: false, verifyApplicability: false, exact: false }
}
