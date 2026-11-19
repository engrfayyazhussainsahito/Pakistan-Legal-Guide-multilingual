import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from 'react'
import { LANGS, dirOf, pickText, translate, translateList, LANG_TAG, type Localized } from '../i18n'
import { JURISDICTIONS } from '../lib/jurisdiction'
import { buildIndex, type SearchEngine } from '../services/localSearch'
import { loadLegalData, type LegalData } from '../services/data'
import type { JurisdictionChoice, Lang, LocalizedText } from '../types'

type Status = 'loading' | 'ready' | 'error'

interface AppState {
  lang: Lang
  setLang: (l: Lang) => void
  dir: 'ltr' | 'rtl'
  jurisdiction: JurisdictionChoice
  setJurisdiction: (j: JurisdictionChoice) => void
  t: (key: string, vars?: Record<string, string | number>) => string
  tList: (key: string) => string[]
  /** Pick localized content, falling back to English (never inventing a translation) */
  tl: (v: LocalizedText | undefined) => Localized
  jurName: (j: string) => string
  status: Status
  data: LegalData | null
  engine: SearchEngine | null
  reload: () => void
  read: string[]
  toggleRead: (id: string) => void
  markRead: (id: string) => void
  resetProgress: () => void
  menuOpen: boolean
  setMenuOpen: (v: boolean) => void
}

const Ctx = createContext<AppState | null>(null)

const LS = { lang: 'pk-legal.lang', jur: 'pk-legal.jurisdiction', read: 'pk-legal.read' }

function safeGet(key: string): string | null {
  try {
    return localStorage.getItem(key)
  } catch {
    return null
  }
}
function safeSet(key: string, value: string) {
  try {
    localStorage.setItem(key, value)
  } catch {
    /* storage unavailable (private mode etc.) — the site still works */
  }
}
function safeRemove(key: string) {
  try {
    localStorage.removeItem(key)
  } catch {
    /* ignore */
  }
}

function initialLang(): Lang {
  const stored = safeGet(LS.lang)
  if (stored && (LANGS as string[]).includes(stored)) return stored as Lang
  return 'en'
}

function initialJurisdiction(): JurisdictionChoice {
  const stored = safeGet(LS.jur)
  if (stored && (JURISDICTIONS as string[]).includes(stored)) return stored as JurisdictionChoice
  return ''
}

function initialRead(): string[] {
  try {
    const raw = safeGet(LS.read)
    const arr = raw ? JSON.parse(raw) : []
    return Array.isArray(arr) ? arr.filter((x) => typeof x === 'string') : []
  } catch {
    return []
  }
}

export function AppProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>(initialLang)
  const [jurisdiction, setJurState] = useState<JurisdictionChoice>(initialJurisdiction)
  const [status, setStatus] = useState<Status>('loading')
  const [data, setData] = useState<LegalData | null>(null)
  const [engine, setEngine] = useState<SearchEngine | null>(null)
  const [read, setRead] = useState<string[]>(initialRead)
  const [menuOpen, setMenuOpen] = useState(false)
  const [loadKey, setLoadKey] = useState(0)

  const dir = dirOf(lang)

  // Keep <html lang/dir> and the page title in sync — without touching the current route
  useEffect(() => {
    document.documentElement.lang = LANG_TAG[lang]
    document.documentElement.dir = dir
    document.title = `${translate(lang, 'app.name')} — ${translate(lang, 'app.tagline')}`
  }, [lang, dir])

  useEffect(() => {
    let cancelled = false
    setStatus('loading')
    loadLegalData()
      .then((d) => {
        if (cancelled) return
        setData(d)
        setEngine(buildIndex(d))
        setStatus('ready')
      })
      .catch(() => {
        if (!cancelled) setStatus('error')
      })
    return () => {
      cancelled = true
    }
  }, [loadKey])

  const setLang = useCallback((l: Lang) => {
    setLangState(l)
    safeSet(LS.lang, l)
  }, [])

  const setJurisdiction = useCallback((j: JurisdictionChoice) => {
    setJurState(j)
    if (j) safeSet(LS.jur, j)
    else safeRemove(LS.jur)
  }, [])

  const persistRead = (next: string[]) => {
    setRead(next)
    safeSet(LS.read, JSON.stringify(next))
  }
  const toggleRead = useCallback(
    (id: string) => {
      persistRead(read.includes(id) ? read.filter((x) => x !== id) : [...read, id])
    },
    [read],
  )
  const markRead = useCallback(
    (id: string) => {
      if (!read.includes(id)) persistRead([...read, id])
    },
    [read],
  )
  const resetProgress = useCallback(() => {
    setRead([])
    safeRemove(LS.read)
  }, [])

  const value = useMemo<AppState>(
    () => ({
      lang,
      setLang,
      dir,
      jurisdiction,
      setJurisdiction,
      t: (key, vars) => translate(lang, key, vars),
      tList: (key) => translateList(lang, key),
      tl: (v) => pickText(v, lang),
      jurName: (j) => translate(lang, `jur.${j}`),
      status,
      data,
      engine,
      reload: () => setLoadKey((k) => k + 1),
      read,
      toggleRead,
      markRead,
      resetProgress,
      menuOpen,
      setMenuOpen,
    }),
    [lang, setLang, dir, jurisdiction, setJurisdiction, status, data, engine, read, toggleRead, markRead, resetProgress, menuOpen],
  )

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>
}

export function useApp(): AppState {
  const v = useContext(Ctx)
  if (!v) throw new Error('useApp must be used inside AppProvider')
  return v
}
