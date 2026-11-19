import { ChevronDown } from 'lucide-react'
import { useEffect, useId, useRef, useState, type ReactNode } from 'react'
import { cn } from '../lib/utils'

/** Accessible disclosure (button + region). `defaultOpen` and `openSignal` allow deep-linking. */
export function Collapsible({
  id,
  title,
  children,
  defaultOpen = false,
  className,
  titleLang,
}: {
  id?: string
  title: ReactNode
  children: ReactNode
  defaultOpen?: boolean
  className?: string
  titleLang?: string
}) {
  const [open, setOpen] = useState(defaultOpen)
  const uid = useId()
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (defaultOpen) {
      setOpen(true)
      ref.current?.scrollIntoView({ block: 'center', behavior: 'smooth' })
    }
  }, [defaultOpen])

  return (
    <div id={id} ref={ref} className={cn('card scroll-mt-28 overflow-hidden', className)}>
      <h3>
        <button
          type="button"
          aria-expanded={open}
          aria-controls={`${uid}-panel`}
          onClick={() => setOpen((o) => !o)}
          className="flex w-full items-center justify-between gap-3 px-5 py-3.5 text-start font-semibold text-navy-900 hover:bg-sand-50"
        >
          <span lang={titleLang}>{title}</span>
          <ChevronDown className={cn('h-5 w-5 shrink-0 text-navy-400 transition', open && 'rotate-180')} aria-hidden />
        </button>
      </h3>
      <div id={`${uid}-panel`} role="region" hidden={!open} className="border-t border-sand-200 px-5 py-4">
        {children}
      </div>
    </div>
  )
}
