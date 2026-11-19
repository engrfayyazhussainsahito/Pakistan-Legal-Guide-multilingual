import { describe, expect, it } from 'vitest'
import { highlightSegments, normalize, stem, tokenize } from '../lib/normalize'

describe('normalize', () => {
  it('lowercases and strips punctuation', () => expect(normalize('  FIR, Bail!  ')).toBe('fir bail'))
  it('maps Arabic yeh/kaf variants to Urdu forms', () => expect(normalize('ك')).toBe(normalize('ک')))
  it('removes diacritics', () => expect(normalize('ضَمانت')).toBe(normalize('ضمانت')))
  it('maps Arabic-Indic digits', () => expect(normalize('دفعہ ١٥٤')).toContain('154'))
  it('stems simple English plurals', () => expect(stem('arrests')).toBe(stem('arrest')))
  it('tokenizes', () => expect(tokenize('Article 25')).toEqual(['article', '25']))
  it('highlight keeps original text intact', () => {
    const segs = highlightSegments('Bail after arrest', 'bail')
    expect(segs.map((s) => s.text).join('')).toBe('Bail after arrest')
    expect(segs.some((s) => s.match)).toBe(true)
  })
})
