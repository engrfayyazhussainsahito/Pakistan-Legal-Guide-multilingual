import { describe, expect, it } from 'vitest'
import { localAnswer } from '../services/localAssistant'
import { buildIndex } from '../services/localSearch'
import { loadFixture } from './helpers'

const data = loadFixture()
const engine = buildIndex(data)
const labels = { foundDocs: 'Found', foundAnswer: 'Answer', noMatch: 'No match', unofficial: 'Unofficial', jurisdictionName: (j: string) => j }

describe('localAnswer', () => {
  it('answers without any API key and links to documents', () => {
    const m = localAnswer('What is bail?', { data, engine, lang: 'en', jurisdiction: '', labels })
    expect(m.role).toBe('assistant')
    expect(m.mode).toBe('local')
    expect((m.localLinks?.length ?? 0) + (m.citations?.length ?? 0)).toBeGreaterThan(0)
  })
  it('gives an honest no-match message', () => {
    const m = localAnswer('zzqqxxyy', { data, engine, lang: 'en', jurisdiction: '', labels })
    expect(m.text).toContain('No match')
  })
  it('citations only use http(s) urls', () => {
    const m = localAnswer('FIR police', { data, engine, lang: 'en', jurisdiction: '', labels })
    for (const c of m.citations ?? []) expect(c.url.startsWith('http')).toBe(true)
  })
})
