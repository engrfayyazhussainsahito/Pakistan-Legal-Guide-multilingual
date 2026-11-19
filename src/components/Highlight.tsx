import { highlightSegments } from '../lib/normalize'

/** Renders text with matching query words wrapped in <mark>. Text is escaped by React; original text is never altered. */
export function Highlight({ text, query }: { text: string; query: string }) {
  if (!query.trim()) return <>{text}</>
  const segs = highlightSegments(text, query)
  return (
    <>
      {segs.map((s, i) =>
        s.match ? (
          <mark key={i} className="hl">
            {s.text}
          </mark>
        ) : (
          <span key={i}>{s.text}</span>
        ),
      )}
    </>
  )
}
