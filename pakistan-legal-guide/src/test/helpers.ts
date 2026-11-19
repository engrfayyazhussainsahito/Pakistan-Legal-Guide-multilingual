import { readFileSync } from 'node:fs'
import { resolve } from 'node:path'
import type { LegalData } from '../services/data'
import type { GlossaryFile, LawsFile, TopicsFile } from '../types'

const read = <T>(f: string): T => JSON.parse(readFileSync(resolve(__dirname, '../../public/data', f), 'utf8')) as T

export function loadFixture(): LegalData {
  const laws = read<LawsFile>('laws.json')
  const gl = read<GlossaryFile>('glossary.json')
  const tp = read<TopicsFile>('topics.json')
  return { libraryVersion: laws.libraryVersion, lastReviewed: laws.lastReviewed, laws: laws.laws, glossary: gl.entries, topics: tp.topics, faqs: tp.faqs, rights: tp.rights }
}
