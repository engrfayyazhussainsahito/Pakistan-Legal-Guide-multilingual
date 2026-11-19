/**
 * Mode A — the offline "local legal search assistant".
 *
 * It is NOT a generative AI model. It searches the bundled legal library, returns the
 * reviewed FAQ explanation when there is a close match, and links to relevant documents.
 */
import { pickText } from '../i18n'
import { lawVisibility } from '../lib/jurisdiction'
import type { ChatMessage, Citation, JurisdictionChoice, Lang } from '../types'
import type { LegalData } from './data'
import type { SearchEngine } from './localSearch'

export interface LocalAnswerContext {
  data: LegalData
  engine: SearchEngine
  lang: Lang
  jurisdiction: JurisdictionChoice
  /** Localised helpers supplied by the UI so this module stays free of React */
  labels: {
    foundDocs: string
    foundAnswer: string
    noMatch: string
    unofficial: string
    jurisdictionName: (j: string) => string
  }
}

const FAQ_THRESHOLD = 9

let counter = 0
export const newId = () => `m${Date.now().toString(36)}${(counter++).toString(36)}`

export function localAnswer(question: string, ctx: LocalAnswerContext): ChatMessage {
  const { data, engine, lang, jurisdiction, labels } = ctx
  const lawsById = new Map(data.laws.map((l) => [l.id, l]))
  const results = engine.search(question, { lang, jurisdiction, limit: 12 })

  const localLinks: NonNullable<ChatMessage['localLinks']> = []
  const citations: Citation[] = []
  const seenCite = new Set<string>()
  const addCitation = (lawId: string, sectionNumber?: string) => {
    const law = lawsById.get(lawId)
    if (!law) return
    const key = `${lawId}|${sectionNumber ?? ''}`
    if (seenCite.has(key)) return
    seenCite.add(key)
    citations.push({
      title: law.title,
      url: law.sourceUrl,
      section: sectionNumber,
      jurisdiction: labels.jurisdictionName(law.jurisdiction),
    })
  }
  const addLink = (label: string, to: string, jur?: string) => {
    if (!localLinks.some((l) => l.to === to)) localLinks.push({ label, to, jurisdiction: jur })
  }

  const topFaq = results.find((r) => r.kind === 'faq' && r.score >= FAQ_THRESHOLD)
  let text = ''
  let needsJurisdiction = false

  if (topFaq) {
    const faq = data.faqs.find((f) => f.id === topFaq.id)!
    const a = pickText(faq.answer, lang)
    text = `${labels.foundAnswer}\n\n${a.text}`
    if (a.fallback) text += `\n\n(${labels.unofficial})`
    needsJurisdiction = !!faq.jurisdictionSensitive && !jurisdiction
    for (const ref of faq.relatedLaws) {
      const law = lawsById.get(ref.lawId)
      if (!law) continue
      const vis = lawVisibility(law, jurisdiction)
      if (!vis.visible) continue
      const section = ref.sectionId ? law.sections.find((s) => s.id === ref.sectionId) : undefined
      addLink(
        section ? `${law.abbreviation ?? law.title} — ${section.number}` : law.title,
        section ? `/laws/${law.id}/${section.id}` : `/laws/${law.id}`,
        labels.jurisdictionName(law.jurisdiction),
      )
      addCitation(law.id, section?.number)
    }
    if (topFaq.to.startsWith('/topics/')) addLink(topFaq.title, topFaq.to.split('#')[0])
  }

  const docs = results.filter((r) => ['law', 'section', 'topic', 'glossary'].includes(r.kind)).slice(0, 5)
  if (!topFaq && docs.length) text = labels.foundDocs
  for (const d of docs) {
    const lawId = d.kind === 'law' ? d.id : d.kind === 'section' ? d.id.split('/')[0] : undefined
    addLink(d.title, d.to, d.jurisdictionId ? labels.jurisdictionName(d.jurisdictionId) : undefined)
    if (lawId) addCitation(lawId, d.kind === 'section' ? d.title.split('—')[1]?.split(':')[0]?.trim() : undefined)
    if (!jurisdiction && d.jurisdictionId && d.jurisdictionId !== 'federal' && d.kind !== 'glossary') needsJurisdiction = true
  }

  if (!text) text = labels.noMatch

  return {
    id: newId(),
    role: 'assistant',
    mode: 'local',
    text,
    citations: citations.slice(0, 6),
    localLinks: localLinks.slice(0, 8),
    needsJurisdiction,
  }
}
