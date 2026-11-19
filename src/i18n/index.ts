import en from './en.json'
import ur from './ur.json'
import sd from './sd.json'
import type { Lang, LocalizedText } from '../types'

export const LANGS: Lang[] = ['en', 'ur', 'sd']
export const RTL_LANGS: Lang[] = ['ur', 'sd']
export const LANG_LABEL: Record<Lang, string> = { en: 'English', ur: 'اردو', sd: 'سنڌي' }
/** BCP-47 tags used for the `lang` attribute. Sindhi in Arabic script. */
export const LANG_TAG: Record<Lang, string> = { en: 'en', ur: 'ur', sd: 'sd' }

type Dict = Record<string, unknown>
const dictionaries: Record<Lang, Dict> = { en, ur, sd } as Record<Lang, Dict>

export function dirOf(lang: Lang): 'ltr' | 'rtl' {
  return RTL_LANGS.includes(lang) ? 'rtl' : 'ltr'
}

function lookup(dict: Dict, key: string): unknown {
  let cur: unknown = dict
  for (const part of key.split('.')) {
    if (cur && typeof cur === 'object' && part in (cur as Dict)) cur = (cur as Dict)[part]
    else return undefined
  }
  return cur
}

export function interpolate(str: string, vars?: Record<string, string | number>): string {
  if (!vars) return str
  return str.replace(/\{(\w+)\}/g, (_, k) => (k in vars ? String(vars[k]) : `{${k}}`))
}

/** Translate a UI key. Falls back to English, then to the key itself. */
export function translate(lang: Lang, key: string, vars?: Record<string, string | number>): string {
  const v = lookup(dictionaries[lang], key) ?? lookup(dictionaries.en, key)
  return typeof v === 'string' ? interpolate(v, vars) : key
}

export function translateList(lang: Lang, key: string): string[] {
  const v = lookup(dictionaries[lang], key) ?? lookup(dictionaries.en, key)
  return Array.isArray(v) ? (v as string[]) : []
}

export interface Localized {
  text: string
  /** language actually used */
  lang: Lang
  /** true if the requested language was not available and English was used */
  fallback: boolean
}

/** Pick the requested language from content, falling back to English. Never invents a translation. */
export function pickText(value: LocalizedText | undefined, lang: Lang): Localized {
  const wanted = value?.[lang]
  if (wanted) return { text: wanted, lang, fallback: false }
  const en = value?.en
  if (en) return { text: en, lang: 'en', fallback: lang !== 'en' }
  return { text: '', lang, fallback: false }
}

export function uiLanguageName(lang: Lang): string {
  return LANG_LABEL[lang]
}
