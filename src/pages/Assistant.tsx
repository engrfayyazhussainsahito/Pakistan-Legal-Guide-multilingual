import { ChatPanel } from '../components/ChatPanel'
import { PageHeader } from '../components/PageHeader'
import { useApp } from '../context/AppContext'

export default function Assistant() {
  const { t } = useApp()
  return (
    <div>
      <PageHeader eyebrow={t('nav.assistant')} title={t('chat.title')} sub={t('chat.sub')} />
      <ChatPanel />
    </div>
  )
}
