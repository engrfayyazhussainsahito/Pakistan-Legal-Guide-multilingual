import { Search, X } from 'lucide-react'
import { forwardRef, useEffect, useId, useMemo, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { cn } from '../lib/utils'

interface Props {
  initial?: string
  className?: string
  autoFocus?: boolean
  size?: 'md' | 'lg'
  placeholder?: string
  /** Called on submit instead of navigating to /search */
  onSubmit?: (q: string) => void
  /** Called as the user types (for live filtering on the search page) */
  onChange?: (q: string) => void
}

/** Search input with instant suggestions (ARIA combobox). Submitting opens the search page. */
export const LegalSearch = forwardRef<HTMLInputElement, Props>(function LegalSearch(
  { initial = '', className, autoFocus, size = 'md', placeholder, onSubmit, onChange },
  ref,
) {
  const { t, lang, jurisdiction, engine } = useApp()
  const nav = useNavigate()
  const [q, setQ] = useState(initial)
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState(-1)
  const listId = useId()
  const wrapRef = useRef<HTMLDivElement>(null)

  useEffect(() => setQ(initial), [initial])

  const suggestions = useMemo(
    () => (engine && q.trim().length >= 2 ? engine.suggest(q, { lang, jurisdiction }) : []),
    [engine, q, lang, jurisdiction],
  )

  useEffect(() => {
    const onDoc = (e: MouseEvent) => {
      if (!wrapRef.current?.contains(e.target as Node)) setOpen(false)
    }
    document.addEventListener('mousedown', onDoc)
    return () => document.removeEventListener('mousedown', onDoc)
  }, [])

  const go = (value: string) => {
    const v = value.trim()
    if (!v) return
    setOpen(false)
    if (onSubmit) onSubmit(v)
    else nav(`/search?q=${encodeURIComponent(v)}`)
  }

  return (
    <div ref={wrapRef} className={cn('relative', className)}>
      <form
        role="search"
        onSubmit={(e) => {
          e.preventDefault()
          go(active >= 0 && suggestions[active] ? suggestions[active] : q)
        }}
        className="relative"
      >
        <label htmlFor={`${listId}-input`} className="sr-only">
          {t('search.placeholder')}
        </label>
        <Search className="pointer-events-none absolute start-3.5 top-1/2 h-5 w-5 -translate-y-1/2 text-navy-400" aria-hidden />
        <input
          ref={ref}
          id={`${listId}-input`}
          type="search"
          value={q}
          autoFocus={autoFocus}
          autoComplete="off"
          maxLength={200}
          role="combobox"
          aria-expanded={open && suggestions.length > 0}
          aria-controls={listId}
          aria-autocomplete="list"
          aria-activedescendant={active >= 0 ? `${listId}-${active}` : undefined}
          placeholder={placeholder ?? t('search.placeholder')}
          onChange={(e) => {
            setQ(e.target.value)
            setOpen(true)
            setActive(-1)
            onChange?.(e.target.value)
          }}
          onFocus={() => setOpen(true)}
          onKeyDown={(e) => {
            if (e.key === 'ArrowDown') {
              e.preventDefault()
              setOpen(true)
              setActive((a) => Math.min(a + 1, suggestions.length - 1))
            } else if (e.key === 'ArrowUp') {
              e.preventDefault()
              setActive((a) => Math.max(a - 1, -1))
            } else if (e.key === 'Escape') {
              setOpen(false)
              setActive(-1)
            }
          }}
          className={cn(
            'w-full rounded-xl border border-sand-300 bg-white ps-11 pe-24 text-navy-900 shadow-card placeholder:text-navy-300 focus:border-teal-600',
            size === 'lg' ? 'py-4 text-base' : 'py-2.5 text-sm',
          )}
        />
        {q && (
          <button
            type="button"
            aria-label={t('common.clear')}
            onClick={() => {
              setQ('')
              onChange?.('')
              setActive(-1)
            }}
            className="absolute end-[4.6rem] top-1/2 -translate-y-1/2 rounded-md p-1.5 text-navy-400 hover:bg-navy-50 hover:text-navy-700"
          >
            <X className="h-4 w-4" aria-hidden />
          </button>
        )}
        <button type="submit" className={cn('btn-primary absolute end-1.5 top-1/2 -translate-y-1/2', size === 'lg' ? 'px-4 py-2.5' : 'px-3 py-1.5')}>
          {t('common.search')}
        </button>
      </form>
      {open && suggestions.length > 0 && (
        <ul
          id={listId}
          role="listbox"
          aria-label={t('search.ariaSuggestions')}
          className="absolute z-30 mt-2 w-full overflow-hidden rounded-xl border border-sand-200 bg-white py-1 shadow-lift"
        >
          {suggestions.map((s, i) => (
            <li
              key={s}
              id={`${listId}-${i}`}
              role="option"
              aria-selected={i === active}
              onMouseDown={(e) => {
                e.preventDefault()
                setQ(s)
                go(s)
              }}
              onMouseEnter={() => setActive(i)}
              className={cn('flex cursor-pointer items-center gap-2 px-4 py-2 text-sm', i === active ? 'bg-teal-50 text-teal-900' : 'text-navy-800')}
            >
              <Search className="h-4 w-4 shrink-0 text-navy-300" aria-hidden />
              <span className="truncate">{s}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
})
