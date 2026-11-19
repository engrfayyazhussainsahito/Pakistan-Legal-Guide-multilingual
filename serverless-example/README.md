# Serverless AI proxy (optional)

The website works fully without this. Add it only if you want the optional AI mode.

- Keep your provider key **only** in the serverless platform's secret store.
- Set `ALLOWED_ORIGIN` to your GitHub Pages origin.
- Answer only from retrieved, verified passages (RAG) and return `insufficientEvidence: true` otherwise.
- Add rate limits; do not store questions.
- In GitHub: Settings → Secrets and variables → Actions → **Variables** → add `VITE_AI_ENDPOINT` (your https URL). Use a *variable*, not a secret: it is public by design.
