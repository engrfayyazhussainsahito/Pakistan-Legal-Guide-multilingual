import { useEffect } from 'react'
import { Route, Routes, useLocation, useNavigate } from 'react-router-dom'
import { Footer } from './components/Footer'
import { FloatingChat } from './components/FloatingChat'
import { Header } from './components/Header'
import { Sidebar } from './components/Sidebar'
import { ChatProvider } from './context/ChatContext'
import About from './pages/About'
import Assistant from './pages/Assistant'
import Dictionary from './pages/Dictionary'
import Home from './pages/Home'
import LawDetail from './pages/LawDetail'
import Laws from './pages/Laws'
import NotFound from './pages/NotFound'
import Rights from './pages/Rights'
import SearchPage from './pages/SearchPage'
import TopicDetail from './pages/TopicDetail'
import Topics from './pages/Topics'

/** Scroll to top on navigation, but leave in-page anchors (#faq-...) to their own handlers. */
function ScrollManager() {
  const { pathname, hash } = useLocation()
  useEffect(() => {
    if (!hash) window.scrollTo({ top: 0 })
  }, [pathname, hash])
  return null
}

/** Press "/" anywhere (outside form fields) to open search. */
function SearchShortcut() {
  const nav = useNavigate()
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return
      const el = e.target as HTMLElement | null
      const tag = el?.tagName
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || el?.isContentEditable) return
      e.preventDefault()
      nav('/search')
    }
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [nav])
  return null
}

export default function App() {
  return (
    <ChatProvider>
      <ScrollManager />
      <SearchShortcut />
      <div className="flex min-h-dvh flex-col">
        <Header />
        <div className="container-page flex flex-1 gap-10 lg:pt-6">
          <aside className="no-print sticky top-24 hidden h-[calc(100dvh-7rem)] w-64 shrink-0 overflow-y-auto pb-6 pe-2 xl:block">
            <Sidebar />
          </aside>
          <main id="main" tabIndex={-1} className="min-w-0 flex-1 pb-8 outline-none">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/laws" element={<Laws />} />
              <Route path="/laws/:id" element={<LawDetail />} />
              <Route path="/laws/:id/:sectionId" element={<LawDetail />} />
              <Route path="/topics" element={<Topics />} />
              <Route path="/topics/:id" element={<TopicDetail />} />
              <Route path="/rights" element={<Rights />} />
              <Route path="/dictionary" element={<Dictionary />} />
              <Route path="/dictionary/:termId" element={<Dictionary />} />
              <Route path="/search" element={<SearchPage />} />
              <Route path="/assistant" element={<Assistant />} />
              <Route path="/about" element={<About />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </main>
        </div>
        <Footer />
      </div>
      <FloatingChat />
    </ChatProvider>
  )
}
