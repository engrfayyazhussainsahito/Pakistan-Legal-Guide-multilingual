import { Bot, Menu, Scale, Search, X } from 'lucide-react'
import { useEffect } from 'react'
import { Link, NavLink, useLocation } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { cn } from '../lib/utils'
import { JurisdictionSelector } from './JurisdictionSelector'
import { LanguageSelector } from './LanguageSelector'

const NAV: { to: string; key: string; end?: boolean }[] = [
  { to: '/', key: 'nav.home', end: true },
  { to: '/laws', key: 'nav.laws' },
  { to: '/topics', key: 'nav.topics' },
  { to: '/rights', key: 'nav.rights' },
  { to: '/dictionary', key: 'nav.dictionary' },
  { to: '/assistant', key: 'nav.assistant' },
]

export function Brand({ onClick }: { onClick?: () => void }) {
  const { t } = useApp()
  return (
    <Link to="/" onClick={onClick} className="flex items-center gap-2.5 rounded-lg">
      <span className="grid h-9 w-9 place-items-center rounded-lg bg-navy-900 text-teal-300 shadow-card">
        <Scale className="h-5 w-5" aria-hidden />
      </span>
      <span className="leading-tight">
        <span className="heading-font block text-[17px] font-bold text-navy-900">{t('app.name')}</span>
        <span className="hidden text-[11px] font-medium text-teal-700 sm:block">{t('app.tagline')}</span>
      </span>
    </Link>
  )
}

export function Header() {
  const { t, menuOpen, setMenuOpen } = useApp()
  const loc = useLocation()

  // Close the mobile menu whenever the route changes
  useEffect(() => setMenuOpen(false), [loc.pathname, setMenuOpen])

  useEffect(() => {
    if (!menuOpen) return
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && setMenuOpen(false)
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [menuOpen, setMenuOpen])

  const linkCls = ({ isActive }: { isActive: boolean }) =>
    cn(
      'rounded-md px-2.5 py-1.5 text-sm font-medium transition',
      isActive ? 'bg-navy-900 text-white' : 'text-navy-700 hover:bg-navy-50',
    )

  return (
    <header className="sticky top-0 z-40 border-b border-sand-200 bg-[#faf7f2]/95 backdrop-blur">
      <a
        href="#main"
        onClick={(e) => {
          e.preventDefault()
          document.getElementById('main')?.focus()
        }}
        className="sr-only focus:not-sr-only focus:absolute focus:start-3 focus:top-3 focus:z-50 focus:rounded-lg focus:bg-navy-900 focus:px-4 focus:py-2 focus:text-white"
      >
        {t('nav.skip')}
      </a>
      <div className="container-page flex h-16 items-center gap-3">
        <Brand />
        <nav aria-label={t('nav.primary')} className="ms-4 hidden items-center gap-0.5 whitespace-nowrap 2xl:flex">
          {NAV.map((n) => (
            <NavLink key={n.to} to={n.to} end={n.end} className={linkCls}>
              {n.to === '/assistant' && <Bot className="me-1 inline h-3.5 w-3.5 align-[-2px]" aria-hidden />}
              {t(n.key)}
            </NavLink>
          ))}
        </nav>
        <div className="ms-auto flex items-center gap-2">
          <NavLink
            to="/search"
            aria-label={`${t('nav.search')} (/)`}
            title={t('search.hint')}
            className={({ isActive }) =>
              cn(
                'inline-flex items-center gap-1.5 rounded-lg border border-navy-200 bg-white px-2.5 py-1.5 text-sm text-navy-700 transition hover:border-navy-400',
                isActive && 'border-teal-600',
              )
            }
          >
            <Search className="h-4 w-4" aria-hidden />
            <span className="hidden sm:inline">{t('nav.search')}</span>
            <kbd className="hidden rounded border border-sand-300 bg-sand-50 px-1.5 text-[11px] text-sand-700 md:inline">/</kbd>
          </NavLink>
          <JurisdictionSelector compact className="hidden md:flex" />
          <LanguageSelector className="hidden sm:inline-flex" />
          <button
            type="button"
            className="btn-secondary px-2.5 2xl:hidden"
            aria-expanded={menuOpen}
            aria-controls="mobile-menu"
            aria-label={menuOpen ? t('nav.closeMenu') : t('nav.openMenu')}
            onClick={() => setMenuOpen(!menuOpen)}
          >
            {menuOpen ? <X className="h-5 w-5" aria-hidden /> : <Menu className="h-5 w-5" aria-hidden />}
          </button>
        </div>
      </div>

      {menuOpen && (
        <div id="mobile-menu" className="border-t border-sand-200 bg-[#faf7f2] 2xl:hidden">
          <nav aria-label={t('nav.primary')} className="container-page flex flex-col gap-1 py-3">
            {NAV.map((n) => (
              <NavLink
                key={n.to}
                to={n.to}
                end={n.end}
                className={({ isActive }) =>
                  cn('rounded-lg px-3 py-2.5 text-base font-medium', isActive ? 'bg-navy-900 text-white' : 'text-navy-800 hover:bg-navy-50')
                }
              >
                {t(n.key)}
              </NavLink>
            ))}
            <NavLink to="/about" className="rounded-lg px-3 py-2.5 text-base font-medium text-navy-800 hover:bg-navy-50">
              {t('nav.about')}
            </NavLink>
            <div className="mt-2 flex flex-col gap-3 border-t border-sand-200 pt-3 sm:hidden">
              <LanguageSelector className="self-start" />
            </div>
            <div className="mt-2 md:hidden">
              <JurisdictionSelector />
            </div>
          </nav>
        </div>
      )}
    </header>
  )
}
