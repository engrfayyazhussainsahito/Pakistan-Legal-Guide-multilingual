/**
 * Lightweight local search (no server, no semantic model).
 *
 * This is a plain keyword index with Unicode normalisation for English, Urdu and Sindhi.
 * It is NOT semantic search and NOT retrieval-augmented generation (RAG).
 * The `SearchEngine` interface is deliberately small so a stronger engine
 * (for example MiniSearch/Lunr or a remote hybrid retriever) can be swapped in later.
 */
import { meaningfulTokens, normalize, stem } from '../lib/normalize'
import { lawVisibility } from '../lib/jurisdiction'
import { pickText } from '../i18n'
import type { CategoryId, JurisdictionChoice, Lang, SearchResult } from '../types'
import type { LegalData } from './data'

type Kind = SearchResult['kind']

interface Field {
  norm: string
  words: string[]
  weight: number
}

interface Doc {
  kind: Kind
  id: string
  to: string
  category?: CategoryId
  lawId?: string
  fields: Field[]
  title: (lang: Lang) => string
  snippet: (lang: Lang) => string
}

export interface SearchOptions {
  lang: Lang
  jurisdiction: JurisdictionChoice
  categories?: CategoryId[]
  kinds?: Kind[]
  limit?: number
}

export interface SearchEngine {
  search(query: string, opts: SearchOptions): SearchResult[]
  suggest(query: string, opts: SearchOptions): string[]
}

function field(text: string | undefined, weight: number): Field | null {
  if (!text) return null
  const norm = normalize(text)
  if (!norm) return null
  return { norm, words: norm.split(' ').map(stem), weight }
}

function fields(...list: (Field | null)[]): Field[] {
  return list.filter((f): f is Field => f !== null)
}

function allLangs(v: Partial<Record<Lang, string>> | undefined): string {
  return v ? Object.values(v).filter(Boolean).join(' ') : ''
}

function clip(text: string, max = 170): string {
  const t = text.replace(/\s+/g, ' ').trim()
  return t.length <= max ? t : t.slice(0, max - 1).trimEnd() + '…'
}

export function buildIndex(data: LegalData): SearchEngine {
  const lawsById = new Map(data.laws.map((l) => [l.id, l]))
  const faqToChapter = new Map<string, string>()
  data.topics.forEach((t) => t.faqIds.forEach((f) => faqToChapter.set(f, t.id)))
  const docs: Doc[] = []

  for (const law of data.laws) {
    docs.push({
      kind: 'law',
      id: law.id,
      to: `/laws/${law.id}`,
      category: law.category,
      lawId: law.id,
      fields: fields(
        field(law.title, 10),
        field(law.abbreviation, 10),
        field(law.keywords.join(' '), 6),
        field(String(law.year ?? ''), 4),
        field(allLangs(law.summary), 3),
      ),
      title: () => law.title,
      snippet: (lang) => clip(pickText(law.summary, lang).text),
    })
    for (const s of law.sections) {
      docs.push({
        kind: 'section',
        id: `${law.id}/${s.id}`,
        to: `/laws/${law.id}/${s.id}`,
        category: law.category,
        lawId: law.id,
        fields: fields(
          field(s.number, 12),
          field(s.heading, 9),
          field(law.abbreviation, 3),
          field(law.title, 2),
          field(allLangs(s.explanation), 2),
          field(s.originalText, 2),
        ),
        title: () => `${law.abbreviation ?? law.title} — ${s.number}: ${s.heading}`,
        snippet: (lang) => clip(pickText(s.explanation, lang).text),
      })
    }
  }

  for (const g of data.glossary) {
    docs.push({
      kind: 'glossary',
      id: g.id,
      to: `/dictionary/${g.id}`,
      category: g.category,
      fields: fields(field(g.en, 11), field(g.ur, 11), field(g.sd, 11), field(allLangs(g.definition), 3)),
      title: (lang) => (lang === 'en' ? g.en : `${g[lang]} · ${g.en}`),
      snippet: (lang) => clip(pickText(g.definition, lang).text),
    })
  }

  for (const f of data.faqs) {
    const chapterId = faqToChapter.get(f.id)
    docs.push({
      kind: 'faq',
      id: f.id,
      to: chapterId ? `/topics/${chapterId}#${f.id}` : '/topics',
      fields: fields(field(allLangs(f.question), 8), field(f.keywords.join(' '), 6), field(allLangs(f.answer), 2)),
      title: (lang) => pickText(f.question, lang).text,
      snippet: (lang) => clip(pickText(f.answer, lang).text),
    })
  }

  for (const t of data.topics) {
    docs.push({
      kind: 'topic',
      id: t.id,
      to: `/topics/${t.id}`,
      category: t.category,
      fields: fields(
        field(allLangs(t.title), 10),
        field(t.keywords.join(' '), 6),
        field(allLangs(t.description), 3),
        field(allLangs(t.intro), 1),
      ),
      title: (lang) => pickText(t.title, lang).text,
      snippet: (lang) => clip(pickText(t.description, lang).text),
    })
  }

  function score(doc: Doc, tokens: string[]): number {
    let matched = 0
    let total = 0
    for (const tok of tokens) {
      let best = 0
      for (const f of doc.fields) {
        let m = 0
        if (f.words.includes(tok)) m = f.weight * 1.25
        else if (tok.length > 2 && f.words.some((w) => w.startsWith(tok))) m = f.weight
        else if (tok.length > 3 && f.norm.includes(tok)) m = f.weight * 0.6
        if (m > best) best = m
      }
      if (best > 0) matched++
      total += best
    }
    const required = tokens.length <= 2 ? tokens.length : Math.ceil(tokens.length * 0.6)
    return matched >= required ? total * (matched / tokens.length) : 0
  }

  function search(query: string, opts: SearchOptions): SearchResult[] {
    const tokens = meaningfulTokens(query).map(stem)
    if (!tokens.length) return []
    const out: SearchResult[] = []
    for (const doc of docs) {
      if (opts.kinds && !opts.kinds.includes(doc.kind)) continue
      if (opts.categories?.length && doc.category && !opts.categories.includes(doc.category)) continue
      if (opts.categories?.length && !doc.category) continue
      let boost = 0
      let jurLabelId: SearchResult['jurisdictionId']
      let verifyApplicability = false
      let verification: SearchResult['verification']
      if (doc.lawId) {
        const law = lawsById.get(doc.lawId)!
        const vis = lawVisibility(law, opts.jurisdiction)
        if (!vis.visible) continue
        verifyApplicability = vis.verifyApplicability
        if (vis.exact) boost += 3
        jurLabelId = law.jurisdiction
        verification = law.verification
      }
      const s = score(doc, tokens)
      if (s <= 0) continue
      out.push({
        kind: doc.kind,
        id: doc.id,
        title: doc.title(opts.lang),
        snippet: doc.snippet(opts.lang),
        to: doc.to,
        score: s + boost + (doc.kind === 'law' ? 1 : 0),
        category: doc.category,
        jurisdictionId: jurLabelId,
        verification,
        verifyApplicability,
      })
    }
    out.sort((a, b) => b.score - a.score || a.title.localeCompare(b.title))
    return out.slice(0, opts.limit ?? 40)
  }

  function suggest(query: string, opts: SearchOptions): string[] {
    const n = normalize(query)
    if (n.length < 2) return []
    const hits = search(query, { ...opts, limit: 8, kinds: ['law', 'glossary', 'topic', 'faq'] })
    const seen = new Set<string>()
    const titles: string[] = []
    for (const h of hits) {
      if (!seen.has(h.title)) {
        seen.add(h.title)
        titles.push(h.title)
      }
      if (titles.length >= 6) break
    }
    return titles
  }

  return { search, suggest }
}
