import { assetUrl } from '../lib/utils'
import type { GlossaryEntry, GlossaryFile, Law, LawsFile, TopicsFile } from '../types'

export interface LegalData {
  libraryVersion: string
  lastReviewed: string
  laws: Law[]
  glossary: GlossaryEntry[]
  topics: TopicsFile['topics']
  faqs: TopicsFile['faqs']
  rights: TopicsFile['rights']
}

async function getJson<T>(path: string): Promise<T> {
  const res = await fetch(assetUrl(path), { headers: { Accept: 'application/json' } })
  if (!res.ok) throw new Error(`Failed to load ${path} (${res.status})`)
  return (await res.json()) as T
}

function assertArray(v: unknown, name: string): void {
  if (!Array.isArray(v)) throw new Error(`Invalid data file: ${name} is not a list`)
}

/** Load the static legal library bundled with the site (public/data/*.json). */
export async function loadLegalData(): Promise<LegalData> {
  const [laws, glossary, topics] = await Promise.all([
    getJson<LawsFile>('data/laws.json'),
    getJson<GlossaryFile>('data/glossary.json'),
    getJson<TopicsFile>('data/topics.json'),
  ])
  assertArray(laws.laws, 'laws')
  assertArray(glossary.entries, 'glossary')
  assertArray(topics.topics, 'topics')
  assertArray(topics.faqs, 'faqs')
  assertArray(topics.rights, 'rights')
  return {
    libraryVersion: laws.libraryVersion,
    lastReviewed: laws.lastReviewed,
    laws: laws.laws,
    glossary: glossary.entries,
    topics: [...topics.topics].sort((a, b) => a.number - b.number),
    faqs: topics.faqs,
    rights: topics.rights,
  }
}

export const OFFICIAL_SOURCES: { key: string; url: string }[] = [
  { key: 'pakistanCode', url: 'https://pakistancode.gov.pk/' },
  { key: 'nationalAssembly', url: 'https://na.gov.pk/' },
  { key: 'lawJustice', url: 'https://molaw.gov.pk/' },
  { key: 'supremeCourt', url: 'https://www.supremecourt.gov.pk/' },
  { key: 'sindhLaws', url: 'https://www.sindhlaws.gov.pk/' },
  { key: 'punjabLaws', url: 'https://punjablaws.gov.pk/' },
  { key: 'kpCode', url: 'https://www.pakp.gov.pk/all-acts/' },
]
