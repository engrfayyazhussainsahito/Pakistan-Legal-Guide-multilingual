import { describe, expect, it } from 'vitest'
import { lawVisibility } from '../lib/jurisdiction'
import { loadFixture } from './helpers'

const { laws } = loadFixture()
const get = (id: string) => laws.find((l) => l.id === id)!

describe('lawVisibility', () => {
  it('shows everything when nothing is selected', () => {
    expect(laws.every((l) => lawVisibility(l, '').visible)).toBe(true)
  })
  it('never shows a Punjab-only law for Sindh', () => {
    const punjab = laws.filter((l) => l.jurisdiction === 'punjab')
    expect(punjab.length).toBeGreaterThan(0)
    for (const l of punjab) if (!l.appliesTo.includes('sindh')) expect(lawVisibility(l, 'sindh').visible).toBe(false)
  })
  it('shows Sindh laws for Sindh as exact matches', () => {
    const s = laws.find((l) => l.jurisdiction === 'sindh')!
    expect(lawVisibility(s, 'sindh')).toMatchObject({ visible: true, exact: true })
  })
  it('federal selection shows only federal laws', () => {
    for (const l of laws) expect(lawVisibility(l, 'federal').visible).toBe(l.jurisdiction === 'federal')
  })
  it('flags federal laws for GB as needing applicability check', () => {
    const f = laws.find((l) => l.jurisdiction === 'federal' && !l.appliesTo.includes('gb'))
    if (f) expect(lawVisibility(f, 'gb')).toMatchObject({ visible: true, verifyApplicability: true })
  })
  it('constitution exists', () => expect(get('constitution-1973')).toBeTruthy())
})
