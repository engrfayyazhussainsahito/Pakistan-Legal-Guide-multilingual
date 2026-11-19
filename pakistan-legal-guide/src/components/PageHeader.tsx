import type { ReactNode } from 'react'

export function PageHeader({ eyebrow, title, sub, children }: { eyebrow?: string; title: string; sub?: string; children?: ReactNode }) {
  return (
    <header className="mb-8 border-b border-sand-200 pb-6">
      {eyebrow && <p className="eyebrow">{eyebrow}</p>}
      <h1 className="heading-font mt-1 text-3xl font-bold leading-tight tracking-tight text-navy-900 sm:text-4xl">{title}</h1>
      {sub && <p className="mt-3 max-w-3xl text-base leading-relaxed text-navy-600">{sub}</p>}
      {children}
    </header>
  )
}

export function SectionHeading({ eyebrow, title, sub, action }: { eyebrow?: string; title: string; sub?: string; action?: ReactNode }) {
  return (
    <div className="mb-6 flex flex-wrap items-end justify-between gap-3">
      <div>
        {eyebrow && <p className="eyebrow">{eyebrow}</p>}
        <h2 className="heading-font mt-1 text-2xl font-bold tracking-tight text-navy-900 sm:text-[28px]">{title}</h2>
        {sub && <p className="mt-2 max-w-2xl text-[15px] text-navy-600">{sub}</p>}
      </div>
      {action}
    </div>
  )
}
