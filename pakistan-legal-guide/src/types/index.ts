export type Lang = 'en' | 'ur' | 'sd'

export type JurisdictionId =
  | 'sindh'
  | 'punjab'
  | 'kpk'
  | 'balochistan'
  | 'ict'
  | 'gb'
  | 'ajk'
  | 'federal'

/** '' means "not selected" (show everything, labelled) */
export type JurisdictionChoice = JurisdictionId | ''

export type CategoryId =
  | 'constitutional'
  | 'criminal'
  | 'civil'
  | 'family'
  | 'property'
  | 'labour'
  | 'consumer'
  | 'administrative'
  | 'cyber'
  | 'police'
  | 'traffic'
  | 'humanrights'
  | 'legalaid'
  | 'government'

/** Text that may exist in some languages only. Missing = translation not available. */
export type LocalizedText = Partial<Record<Lang, string>>

/**
 * How trustworthy is a piece of content?
 * - verified: checked against the official source on `lastVerified`
 * - source-linked: official source portal is linked but the entry's details were not yet checked line-by-line
 * - illustrative: demonstration content, NOT a verified legal document
 */
export type VerificationStatus = 'verified' | 'source-linked' | 'illustrative'

export type ReviewStatus = 'reviewed' | 'unreviewed'

export interface LawSection {
  id: string
  /** e.g. "Article 25", "Section 154" */
  number: string
  heading: string
  /** Verbatim statutory text if bundled. Never edited or paraphrased. */
  originalText?: string
  originalTextSource?: string
  /** Simple-language explanation written for this site (not official). */
  explanation: LocalizedText
  /** Difficult terms and what they mean in simple words */
  terms?: { term: string; meaning: LocalizedText }[]
  /** Important conditions and exceptions */
  conditions?: LocalizedText
  /** Related glossary term ids */
  glossary?: string[]
}

export interface Law {
  id: string
  title: string
  titleTranslations?: LocalizedText
  abbreviation?: string
  category: CategoryId
  jurisdiction: JurisdictionId
  /** Jurisdictions where this law is understood to apply (explicit, never assumed) */
  appliesTo: JurisdictionId[]
  applicabilityNote?: LocalizedText
  year?: number
  summary: LocalizedText
  keywords: string[]
  sections: LawSection[]
  sourceUrl: string
  sourceName: string
  sourceUrlVerified: boolean
  version?: string
  lastVerified?: string
  languages: Lang[]
  verification: VerificationStatus
  featured?: boolean
  relatedLaws?: string[]
}

export interface GlossaryEntry {
  id: string
  en: string
  sd: string
  ur: string
  definition: LocalizedText
  category: CategoryId
  example: LocalizedText
  relatedLaws: string[]
  review: ReviewStatus
}

export interface Faq {
  id: string
  question: LocalizedText
  answer: LocalizedText
  /** If true the answer depends materially on province/territory */
  jurisdictionSensitive?: boolean
  keywords: string[]
  relatedLaws: { lawId: string; sectionId?: string }[]
  review: ReviewStatus
}

export type PhaseId = 1 | 2 | 3 | 4

export interface Topic {
  id: string
  /** Chapter number, 1-based, shown as "01" */
  number: number
  phase: PhaseId
  category: CategoryId
  title: LocalizedText
  description: LocalizedText
  /** "In plain words" introduction */
  intro: LocalizedText
  /** Practical next steps */
  steps: LocalizedText[]
  faqIds: string[]
  /** Self-check: question + answer revealed on demand */
  check: { q: LocalizedText; a: LocalizedText }[]
  /** Glossary term ids used in this chapter */
  terms: string[]
  relatedLaws: { lawId: string; sectionId?: string }[]
  keywords: string[]
  /** Approximate reading time in minutes */
  minutes: number
}

export interface Right {
  id: string
  title: LocalizedText
  body: LocalizedText
  lawId: string
  sectionId?: string
}

export interface TopicsFile {
  topics: Topic[]
  faqs: Faq[]
  rights: Right[]
}

export interface GlossaryFile {
  entries: GlossaryEntry[]
}

export interface LawsFile {
  libraryVersion: string
  lastReviewed: string
  laws: Law[]
}

export interface Citation {
  title: string
  url: string
  section?: string
  jurisdiction?: string
}

export interface ChatMessage {
  id: string
  role: 'user' | 'assistant'
  text: string
  mode?: 'local' | 'ai'
  citations?: Citation[]
  /** Structured fields returned by the AI endpoint */
  structured?: AiAnswer
  /** Internal links to documents in the local library */
  localLinks?: { label: string; to: string; jurisdiction?: string }[]
  error?: boolean
  needsJurisdiction?: boolean
}

export interface AiRequest {
  question: string
  language: Lang
  jurisdiction: JurisdictionChoice
  /** Last few turns only — never the whole transcript */
  history: { role: 'user' | 'assistant'; text: string }[]
}

export interface AiAnswer {
  shortAnswer: string
  jurisdiction?: string
  relevantLaw?: string
  explanation?: string
  nextSteps?: string[]
  limitations?: string
  citations: Citation[]
  insufficientEvidence?: boolean
}

export interface SearchResult {
  kind: 'law' | 'section' | 'glossary' | 'faq' | 'topic'
  id: string
  title: string
  snippet: string
  to: string
  score: number
  category?: CategoryId
  jurisdictionLabel?: string
  jurisdictionId?: JurisdictionId
  verification?: VerificationStatus
  /** federal law shown for GB/AJK where applicability must be verified */
  verifyApplicability?: boolean
}
