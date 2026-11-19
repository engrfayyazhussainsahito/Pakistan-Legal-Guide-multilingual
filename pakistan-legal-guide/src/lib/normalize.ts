/**
 * Search normalisation for English, Urdu and Sindhi.
 * Used ONLY for matching — displayed text is never altered.
 */

const DIGIT_MAP: Record<string, string> = {}
'٠١٢٣٤٥٦٧٨٩'.split('').forEach((d, i) => (DIGIT_MAP[d] = String(i)))
'۰۱۲۳۴۵۶۷۸۹'.split('').forEach((d, i) => (DIGIT_MAP[d] = String(i)))

// Letter variants that users type interchangeably
const CHAR_MAP: Record<string, string> = {
  'ي': 'ی', // Arabic yeh
  'ى': 'ی', // alef maksura
  'ې': 'ی',
  'ے': 'ی', // Urdu yeh barree
  'ك': 'ک', // Arabic kaf
  'ڪ': 'ک', // Sindhi kaf
  'ه': 'ہ', // Arabic heh
  'ھ': 'ہ', // heh doachashmee
  'ۃ': 'ہ',
  'ة': 'ہ',
  'ۀ': 'ہ',
  'أ': 'ا',
  'إ': 'ا',
  'آ': 'ا',
  'ٱ': 'ا',
  'ؤ': 'و',
  'ئ': 'ی',
  'ڻ': 'ن', // Sindhi retroflex nun
  'ٺ': 'ت', // Sindhi aspirated/retroflex te variants
  'ٽ': 'ٹ',
  'ٿ': 'ت',
  'ڙ': 'ڑ',
  'ڏ': 'د',
  'ڊ': 'د',
  'ڌ': 'د',
  'ڍ': 'د',
  'ڇ': 'چ',
  'ڄ': 'ج',
  'ڃ': 'ن',
  'ڳ': 'گ',
  'ڱ': 'گ',
  'ٻ': 'ب',
  'ڀ': 'ب',
  'ڦ': 'پ',
  'ں': 'ن',
}

// Arabic diacritics (harakat), tatweel, superscript alef
const MARKS = /[ؐ-ًؚ-ٰٟۖ-ۭـ]/g

export function normalize(input: string): string {
  if (!input) return ''
  let out = input.normalize('NFKC').toLowerCase()
  out = out.replace(MARKS, '')
  let mapped = ''
  for (const ch of out) {
    mapped += DIGIT_MAP[ch] ?? CHAR_MAP[ch] ?? ch
  }
  // Collapse punctuation (incl. Arabic comma, question mark, full stop) to spaces
  mapped = mapped.replace(/[،؛؟۔.,;:!?()[\]{}"'“”‘’\-_/\\]/g, ' ')
  return mapped.replace(/\s+/g, ' ').trim()
}

export function tokenize(input: string): string[] {
  const n = normalize(input)
  return n ? n.split(' ') : []
}

/** Very small stop-word list (English only) so everyday questions match better. */
const STOP = new Set([
  'a', 'an', 'the', 'is', 'are', 'am', 'was', 'be', 'to', 'of', 'in', 'on', 'for', 'and', 'or',
  'my', 'i', 'me', 'can', 'do', 'does', 'how', 'what', 'when', 'where', 'who', 'which', 'if',
  'should', 'would', 'could', 'it', 'this', 'that', 'with', 'by', 'at', 'from', 'as', 'about',
  'have', 'has', 'get', 'will', 'we', 'you', 'your',
])

/** Light English suffix stripping so "arrested", "arrests" and "arrest" match each other. */
export function stem(token: string): string {
  if (!/^[a-z0-9]+$/.test(token) || token.length < 5) return token
  for (const suf of ['ing', 'ed', 'es', 's']) {
    if (token.endsWith(suf) && token.length - suf.length >= 4) return token.slice(0, -suf.length)
  }
  return token
}

export function meaningfulTokens(input: string): string[] {
  return tokenize(input).filter((t) => t.length > 0 && !STOP.has(t))
}

/**
 * Split `text` into segments marking which parts match any query token.
 * Matching is done on a per-word basis using normalised forms, so the original
 * text is always preserved exactly.
 */
export function highlightSegments(
  text: string,
  query: string,
): { text: string; match: boolean }[] {
  const tokens = meaningfulTokens(query)
    .map(stem)
    .filter((t) => t.length > 1 || /\d/.test(t))
  if (!tokens.length || !text) return [{ text, match: false }]
  const parts = text.split(/(\s+)/)
  const segments: { text: string; match: boolean }[] = []
  for (const part of parts) {
    if (!part) continue
    const n = normalize(part)
    const match = n.length > 0 && tokens.some((t) => n.includes(t))
    const last = segments[segments.length - 1]
    if (last && last.match === match) last.text += part
    else segments.push({ text: part, match })
  }
  return segments
}
