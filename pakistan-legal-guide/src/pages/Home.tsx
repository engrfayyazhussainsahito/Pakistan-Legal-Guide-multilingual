import { ArrowRight, Bot, ExternalLink, Languages, MapPinned, Quote, ScrollText, Sigma } from 'lucide-react'
import { Link, useNavigate } from 'react-router-dom'
import { Collapsible } from '../components/Collapsible'
import { JurisdictionGrid } from '../components/JurisdictionSelector'
import { LawCard } from '../components/LawCard'
import { LegalSearch } from '../components/LegalSearch'
import { SectionHeading } from '../components/PageHeader'
import { ErrorState, Loading } from '../components/StateViews'
import { PHASES } from '../components/Sidebar'
import { useApp } from '../context/AppContext'
import { CATEGORIES, CATEGORY_ICON } from '../lib/categories'
import { useVisibleLaws } from '../lib/useLaws'
import { OFFICIAL_SOURCES } from '../services/data'

export default function Home() {
  const { t, tl, lang, data, status, reload, read, jurisdiction, jurName, tList } = useApp()
  const nav = useNavigate()
  const visible = useVisibleLaws()

  const [first, ...rest] = t('home.heroTitle').split(/(?<=[.۔])\s+/)
  const featured = visible.filter((v) => v.law.featured).slice(0, 6)
  const chapters = data?.topics ?? []
  const firstUnread = chapters.find((c) => !read.includes(c.id)) ?? chapters[0]

  return (
    <div className="space-y-20">
      {/* ------------------------------------------------ Hero */}
      <section aria-labelledby="hero-title" className="pt-6 lg:pt-2">
        <p className="eyebrow">{t('home.eyebrow')}</p>
        <h1 id="hero-title" className="heading-font mt-3 max-w-4xl text-4xl font-bold leading-[1.1] tracking-tight text-navy-900 sm:text-5xl lg:text-[56px]">
          {first}
          {rest.length > 0 && (
            <>
              {' '}
              <span className="text-teal-700">{rest.join(' ')}</span>
            </>
          )}
        </h1>
        <p className="mt-5 max-w-2xl text-lg leading-relaxed text-navy-600">{t('home.heroSub')}</p>

        <LegalSearch size="lg" placeholder={t('home.searchPlaceholder')} className="mt-7 max-w-3xl" />
        <p className="mt-2 text-xs text-navy-500">
          {t('search.tryThese')}:{' '}
          {tList('search.examples').map((ex, i) => (
            <button key={ex} type="button" onClick={() => nav(`/search?q=${encodeURIComponent(ex)}`)} className="me-2 underline-offset-2 hover:text-teal-700 hover:underline">
              {ex}
              {i < tList('search.examples').length - 1 ? ',' : ''}
            </button>
          ))}
        </p>

        <div className="mt-7 flex flex-wrap gap-3">
          <Link to="/laws" className="btn-primary px-5 py-3 text-base">
            {t('home.exploreLaws')}
            <ArrowRight className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
          </Link>
          <Link to="/assistant" className="btn-secondary px-5 py-3 text-base">
            <Bot className="h-4 w-4" aria-hidden />
            {t('home.askAssistant')}
          </Link>
          {firstUnread && (
            <Link to={`/topics/${firstUnread.id}`} className="btn-ghost px-4 py-3 text-base">
              {read.length === 0 ? t('guide.start') : t('guide.next')}
            </Link>
          )}
        </div>

        {/* Stats strip */}
        {data && (
          <dl className="mt-10 grid grid-cols-2 divide-sand-200 overflow-hidden rounded-xl border border-sand-200 bg-white shadow-card sm:grid-cols-4 sm:divide-x rtl:sm:divide-x-reverse">
            {[
              [data.laws.length, t('home.statsLaws')],
              [data.topics.length, t('home.statsChapters')],
              [data.glossary.length, t('home.statsTerms')],
              [3, t('home.statsLangs')],
            ].map(([n, label]) => (
              <div key={String(label)} className="px-5 py-4">
                <dt className="order-2 text-xs font-medium text-navy-500">{label}</dt>
                <dd className="heading-font text-3xl font-bold tabular-nums text-navy-900">{n}</dd>
              </div>
            ))}
          </dl>
        )}
      </section>

      {/* ------------------------------------------------ Features */}
      <section aria-label={t('app.name')}>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {[
            { Icon: Sigma, k: 'f1' },
            { Icon: ScrollText, k: 'f2' },
            { Icon: MapPinned, k: 'f3' },
            { Icon: Languages, k: 'f4' },
          ].map(({ Icon, k }) => (
            <div key={k} className="card p-5">
              <span className="grid h-10 w-10 place-items-center rounded-lg bg-navy-900 text-teal-300">
                <Icon className="h-5 w-5" aria-hidden />
              </span>
              <h3 className="heading-font mt-4 text-lg font-semibold">{t(`home.${k}t`)}</h3>
              <p className="mt-1.5 text-sm leading-relaxed text-navy-600">{t(`home.${k}b`)}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ------------------------------------------------ Categories */}
      <section aria-labelledby="cats">
        <SectionHeading eyebrow={t('nav.laws')} title={t('home.categoriesTitle')} sub={t('home.categoriesSub')} />
        <div id="cats" className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {CATEGORIES.map((c) => {
            const Icon = CATEGORY_ICON[c]
            const count = visible.filter((v) => v.law.category === c).length
            return (
              <Link key={c} to={`/laws?category=${c}`} className="card card-hover group flex items-start gap-4 p-5">
                <span className="grid h-11 w-11 shrink-0 place-items-center rounded-lg bg-teal-50 text-teal-700 transition group-hover:bg-teal-600 group-hover:text-white">
                  <Icon className="h-5 w-5" aria-hidden />
                </span>
                <span className="min-w-0">
                  <span className="heading-font block text-base font-semibold text-navy-900">{t(`cat.${c}`)}</span>
                  <span className="mt-0.5 block text-sm leading-snug text-navy-600">{t(`catDesc.${c}`)}</span>
                  <span className="mt-2 block text-xs font-semibold text-teal-700">{t('common.results', { count })}</span>
                </span>
              </Link>
            )
          })}
        </div>
      </section>

      {/* ------------------------------------------------ Learning path */}
      <section aria-labelledby="path">
        <SectionHeading eyebrow={t('guide.phases')} title={t('home.pathTitle')} sub={t('home.pathSub')} />
        {status === 'loading' && <Loading />}
        {status === 'error' && <ErrorState onRetry={reload} />}
        {data && (
          <div id="path" className="grid gap-4 md:grid-cols-2">
            {PHASES.map((p) => {
              const items = data.topics.filter((c) => c.phase === p)
              return (
                <div key={p} className="card p-5">
                  <p className="eyebrow">
                    {t('guide.phase', { n: p })} · {items.length}
                  </p>
                  <h3 className="heading-font mt-1 text-xl font-semibold">{t(`guide.p${p}`)}</h3>
                  <p className="mt-1 text-sm text-navy-600">{t(`guide.p${p}d`)}</p>
                  <ol className="mt-4 space-y-1.5">
                    {items.map((c) => (
                      <li key={c.id}>
                        <Link to={`/topics/${c.id}`} className="group flex items-baseline gap-3 rounded-md px-1 py-1 text-sm hover:bg-sand-50">
                          <span className="tabular-nums text-xs font-bold text-teal-700">{String(c.number).padStart(2, '0')}</span>
                          <span lang={tl(c.title).lang} className="text-navy-800 group-hover:text-teal-800 group-hover:underline">
                            {tl(c.title).text}
                          </span>
                        </Link>
                      </li>
                    ))}
                  </ol>
                </div>
              )
            })}
          </div>
        )}
      </section>

      {/* ------------------------------------------------ Featured documents */}
      <section aria-labelledby="featured">
        <SectionHeading
          eyebrow={jurisdiction ? t('jur.selected', { name: jurName(jurisdiction) }) : undefined}
          title={t('home.featuredTitle')}
          sub={t('home.featuredSub')}
          action={
            <Link to="/laws" className="btn-secondary">
              {t('common.viewAll')}
            </Link>
          }
        />
        {status === 'loading' ? (
          <Loading />
        ) : featured.length ? (
          <div id="featured" className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {featured.map((v) => (
              <LawCard key={v.law.id} law={v.law} verifyApplicability={v.verifyApplicability} />
            ))}
          </div>
        ) : (
          <p className="card p-6 text-sm text-navy-700">{t('jur.noEntries')}</p>
        )}
      </section>

      {/* ------------------------------------------------ Common questions */}
      <section aria-labelledby="faq">
        <SectionHeading eyebrow={t('topics.faqs')} title={t('home.faqTitle')} sub={t('home.faqSub')} />
        {data && (
          <div id="faq" className="space-y-3">
            {data.faqs.slice(0, 7).map((f) => {
              const q = tl(f.question)
              const a = tl(f.answer)
              return (
                <Collapsible key={f.id} title={q.text} titleLang={q.lang}>
                  <p lang={a.lang} className="prose-legal">
                    {a.text}
                  </p>
                  {f.jurisdictionSensitive && <p className="mt-2 text-xs text-amber-800">{t('topics.jurisdictionSensitive')}</p>}
                  <Link to={`/search?q=${encodeURIComponent(q.text)}`} className="mt-3 inline-flex text-sm font-semibold text-teal-700 hover:underline">
                    {t('search.title')} →
                  </Link>
                </Collapsible>
              )
            })}
          </div>
        )}
      </section>

      {/* ------------------------------------------------ Law explained simply */}
      <section aria-labelledby="simple" className="rounded-2xl bg-navy-900 p-6 text-white sm:p-10">
        <p className="eyebrow !text-teal-300">{t('law.understand')}</p>
        <h2 id="simple" className="heading-font mt-1 text-2xl font-bold !text-white sm:text-3xl">
          {t('home.simpleTitle')}
        </h2>
        <p className="mt-2 max-w-2xl text-navy-100">{t('home.simpleSub')}</p>
        <div className="mt-6 grid gap-4 md:grid-cols-2">
          <div className="rounded-xl border border-navy-600 bg-navy-800/70 p-5">
            <Quote className="h-5 w-5 text-teal-300" aria-hidden />
            <h3 className="mt-2 text-lg font-semibold !text-white">{t('home.simpleOriginal')}</h3>
            <p className="mt-1 text-sm text-navy-100">{t('home.simpleOriginalBody')}</p>
            <blockquote dir="ltr" className="mt-3 border-s-2 border-teal-400 ps-3 text-start font-serif text-sm text-navy-50">
              “All citizens are equal before law and are entitled to equal protection of law.”
              <footer className="mt-1 text-xs text-navy-300">Constitution, Article 25(1)</footer>
            </blockquote>
          </div>
          <div className="rounded-xl border border-teal-500/60 bg-teal-900/40 p-5">
            <Languages className="h-5 w-5 text-teal-300" aria-hidden />
            <h3 className="mt-2 text-lg font-semibold !text-white">{t('home.simpleUnderstand')}</h3>
            <p className="mt-1 text-sm text-navy-100">{t('home.simpleUnderstandBody')}</p>
            <p lang={lang} className="mt-3 text-sm text-white">
              {data ? tl(data.laws.find((l) => l.id === 'constitution-1973')?.sections.find((s) => s.id === 'art-25')?.explanation).text : ''}
            </p>
          </div>
        </div>
        <Link to="/laws/constitution-1973/art-25" className="btn-teal mt-6">
          {t('home.simpleTry')}
          <ArrowRight className="h-4 w-4 rtl:-scale-x-100" aria-hidden />
        </Link>
      </section>

      {/* ------------------------------------------------ Glossary preview */}
      <section aria-labelledby="gloss">
        <SectionHeading
          eyebrow={t('nav.dictionary')}
          title={t('home.glossaryTitle')}
          sub={t('home.glossarySub')}
          action={
            <Link to="/dictionary" className="btn-secondary">
              {t('home.glossaryAll')}
            </Link>
          }
        />
        {data && (
          <div id="gloss" className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {['bail', 'fir', 'warrant', 'summons', 'injunction', 'dower'].map((id) => {
              const g = data.glossary.find((x) => x.id === id)
              if (!g) return null
              return (
                <Link key={id} to={`/dictionary/${id}`} className="card card-hover p-4">
                  <p className="heading-font text-lg font-semibold">{g.en}</p>
                  <p className="mt-1 flex flex-wrap gap-x-4 text-sm text-navy-700">
                    <span lang="ur">{g.ur}</span>
                    <span lang="sd">{g.sd}</span>
                  </p>
                  <p lang={tl(g.definition).lang} className="mt-2 line-clamp-2 text-xs text-navy-500">
                    {tl(g.definition).text}
                  </p>
                </Link>
              )
            })}
          </div>
        )}
      </section>

      {/* ------------------------------------------------ Jurisdiction */}
      <section aria-labelledby="jur">
        <SectionHeading eyebrow={t('jur.label')} title={t('home.jurisdictionTitle')} sub={t('home.jurisdictionSub')} />
        <div id="jur">
          <JurisdictionGrid />
          <p className="mt-3 text-sm text-navy-600">{t('jur.hint')}</p>
        </div>
      </section>

      {/* ------------------------------------------------ Study guidance */}
      <section aria-labelledby="study" className="grid gap-8 lg:grid-cols-[1.3fr_1fr]">
        <div>
          <SectionHeading title={t('home.studyTitle')} />
          <ol className="space-y-4">
            {[1, 2, 3, 4, 5].map((n) => (
              <li key={n} className="flex gap-4">
                <span className="heading-font grid h-9 w-9 shrink-0 place-items-center rounded-full bg-navy-900 text-sm font-bold text-white">{n}</span>
                <div>
                  <h3 className="font-semibold">{t(`home.study${n}t`)}</h3>
                  <p className="text-sm text-navy-600">{t(`home.study${n}b`)}</p>
                </div>
              </li>
            ))}
          </ol>
        </div>
        <div className="space-y-4">
          <div className="card p-5">
            <h3 className="heading-font text-lg font-semibold">{t('home.prereqTitle')}</h3>
            <p className="mt-1.5 text-sm text-navy-600">{t('home.prereqBody')}</p>
          </div>
          <div className="card p-5">
            <h3 className="heading-font text-lg font-semibold">{t('home.tipsTitle')}</h3>
            <p className="mt-1.5 text-sm text-navy-600">{t('home.tipsBody')}</p>
          </div>
        </div>
      </section>

      {/* ------------------------------------------------ Official sources */}
      <section aria-labelledby="src">
        <SectionHeading eyebrow={t('common.officialSource')} title={t('home.sourcesTitle')} sub={t('home.sourcesSub')} />
        <ul id="src" className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {OFFICIAL_SOURCES.map((s) => (
            <li key={s.url}>
              <a href={s.url} target="_blank" rel="noopener noreferrer" className="card card-hover flex items-center justify-between gap-3 p-4">
                <span>
                  <span className="block text-sm font-semibold">{t(`sources.${s.key}`)}</span>
                  <span dir="ltr" className="block text-start text-xs text-navy-500">
                    {new URL(s.url).host}
                  </span>
                </span>
                <ExternalLink className="h-4 w-4 shrink-0 text-teal-700" aria-hidden />
                <span className="sr-only">{t('common.opensNewTab')}</span>
              </a>
            </li>
          ))}
        </ul>
      </section>
    </div>
  )
}
