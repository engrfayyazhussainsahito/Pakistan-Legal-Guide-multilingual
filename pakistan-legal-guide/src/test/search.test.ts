import { describe, expect, it } from 'vitest'
import { buildIndex } from '../services/localSearch'
import { loadFixture } from './helpers'

const data = loadFixture()
const engine = buildIndex(data)
const base = { lang: 'en' as const, jurisdiction: '' as const }

describe('local search', () => {
  it('finds bail content', () => {
    const r = engine.search('bail', base)
    expect(r.length).toBeGreaterThan(0)
  })
  it('finds Article 25 by number', () => {
    const r = engine.search('Article 25', base)
    expect(r.some((x) => x.to.includes('constitution-1973'))).toBe(true)
  })
  it('returns nothing for gibberish', () => expect(engine.search('zzqqxxyy', base)).toEqual([]))
  it('finds glossary term via Urdu script', () => {
    const g = data.glossary.find((x) => x.id === 'bail')!
    const r = engine.search(g.ur, { ...base, lang: 'ur' })
    expect(r.some((x) => x.kind === 'glossary' && x.id === 'bail')).toBe(true)
  })
  it('finds glossary term via Sindhi script', () => {
    const g = data.glossary.find((x) => x.id === 'bail')!
    const r = engine.search(g.sd, { ...base, lang: 'sd' })
    expect(r.some((x) => x.kind === 'glossary' && x.id === 'bail')).toBe(true)
  })
  it('respects kind filter', () => {
    const r = engine.search('bail', { ...base, kinds: ['glossary'] })
    expect(r.every((x) => x.kind === 'glossary')).toBe(true)
  })
  it('hides laws of other provinces', () => {
    const r = engine.search('rented premises', { ...base, jurisdiction: 'sindh' })
    expect(r.some((x) => x.to.includes('punjab-rented'))).toBe(false)
  })
  it('suggest returns strings', () => expect(Array.isArray(engine.suggest('bai', base))).toBe(true))
})
