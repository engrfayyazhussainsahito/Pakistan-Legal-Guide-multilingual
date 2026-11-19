import { Languages } from 'lucide-react'
import { useApp } from '../context/AppContext'
import { LANGS, LANG_LABEL, LANG_TAG } from '../i18n'
import { cn } from '../lib/utils'

/** Three-way language switch. Changing language never changes the current route. */
export function LanguageSelector({ className }: { className?: string }) {
  const { lang, setLang, t } = useApp()
  return (
    <div role="group" aria-label={t('lang.label')} className={cn('inline-flex items-center rounded-lg border border-navy-200 bg-white p-0.5', className)}>
      <Languages className="mx-1.5 h-4 w-4 text-navy-400" aria-hidden />
      {LANGS.map((l) => (
        <button
          key={l}
          type="button"
          lang={LANG_TAG[l]}
          onClick={() => setLang(l)}
          aria-pressed={lang === l}
          className={cn(
            'rounded-md px-2.5 py-1 text-sm font-medium leading-normal transition',
            lang === l ? 'bg-navy-800 text-white' : 'text-navy-700 hover:bg-navy-50',
          )}
        >
          {LANG_LABEL[l]}
        </button>
      ))}
    </div>
  )
}
