import { Bot, Maximize2, X } from 'lucide-react'
import { useEffect, useRef, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useApp } from '../context/AppContext'
import { ChatPanel } from './ChatPanel'

/** Floating chatbot button + popover. Hidden on the dedicated assistant page. */
export function FloatingChat() {
  const { t } = useApp()
  const [open, setOpen] = useState(false)
  const loc = useLocation()
  const btnRef = useRef<HTMLButtonElement>(null)

  useEffect(() => setOpen(false), [loc.pathname])
  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setOpen(false)
        btnRef.current?.focus()
      }
    }
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [open])

  if (loc.pathname === '/assistant') return null

  return (
    <div className="no-print fixed bottom-4 end-4 z-50 flex flex-col items-end gap-3">
      {open && (
        <section
          role="dialog"
          aria-label={t('chat.title')}
          className="flex h-[min(34rem,calc(100dvh-7rem))] w-[min(24rem,calc(100vw-2rem))] flex-col overflow-hidden rounded-2xl border border-sand-300 bg-[#faf7f2] shadow-lift"
        >
          <div className="flex items-center gap-2 bg-navy-900 px-4 py-2.5 text-white">
            <Bot className="h-5 w-5 text-teal-300" aria-hidden />
            <h2 className="flex-1 text-sm font-semibold !text-white">{t('chat.title')}</h2>
            <Link to="/assistant" className="rounded-md p-1.5 hover:bg-white/10" aria-label={t('chat.openFull')} title={t('chat.openFull')}>
              <Maximize2 className="h-4 w-4" aria-hidden />
            </Link>
            <button type="button" onClick={() => setOpen(false)} className="rounded-md p-1.5 hover:bg-white/10" aria-label={t('common.close')}>
              <X className="h-4 w-4" aria-hidden />
            </button>
          </div>
          <div className="min-h-0 flex-1">
            <ChatPanel compact />
          </div>
        </section>
      )}
      <button
        ref={btnRef}
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        aria-label={t('chat.open')}
        className="inline-flex items-center gap-2 rounded-full bg-teal-600 px-4 py-3 text-sm font-semibold text-white shadow-lift transition hover:bg-teal-700"
      >
        <Bot className="h-5 w-5" aria-hidden />
        <span className="hidden sm:inline">{t('nav.assistant')}</span>
      </button>
    </div>
  )
}
