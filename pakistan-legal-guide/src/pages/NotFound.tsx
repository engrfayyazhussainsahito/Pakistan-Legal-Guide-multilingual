import { Link } from 'react-router-dom'
import { useApp } from '../context/AppContext'

export default function NotFound() {
  const { t } = useApp()
  return (
    <div className="py-20 text-center">
      <p className="eyebrow">404</p>
      <h1 className="heading-font mt-2 text-3xl font-bold">{t('notFound.title')}</h1>
      <p className="mx-auto mt-3 max-w-md text-navy-600">{t('notFound.body')}</p>
      <Link to="/" className="btn-primary mt-6 inline-flex">
        {t('notFound.home')}
      </Link>
    </div>
  )
}
