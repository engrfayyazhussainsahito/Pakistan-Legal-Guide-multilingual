# Pakistan Legal Guide

*Understand Your Rights. Know Your Law.*

A static, multilingual (English, اردو, سنڌي) legal-information website. It runs entirely in the browser, deploys to GitHub Pages, and needs no backend, database or API key.

> **Important:** this is general legal information, not legal advice. Every law is currently marked **source-linked**: the official portal is linked, but entries, URLs and plain-language explanations have **not** been verified line by line. Only seven short constitutional extracts carry verbatim text, and they are labelled "confirm against the official text". Urdu and Sindhi UI text and explanations are **unreviewed**. Statute titles and section headings stay in English; no official translation is invented. Have a lawyer review the content, and check every official URL, before you rely on this site publicly.

## What is inside
- 14 legal categories, 38 laws, 49 sections, 30 glossary terms (en/ur/sd), 31 FAQs, 8 rights, 18 study chapters in 4 phases.
- Two reading modes for each law: **Original law** and **Understand this law** (side by side on desktop, tabs on mobile).
- Province-aware filtering: laws of another province are never shown as if they applied to you.
- Local search with suggestions, filters and Urdu/Sindhi normalisation (press `/` to search).
- Assistant: a **local search assistant** (not generative AI, works offline, no key), plus an **optional** AI mode through your own serverless endpoint.
- The static site is **not** RAG. A RAG design is only possible through the optional endpoint (see `serverless/`).

## Run it locally (beginner steps)
1. Install [Node.js](https://nodejs.org) 20 or newer.
2. In a terminal inside this folder: `npm ci`
3. Start the site: `npm run dev` and open the address it prints.
4. Check everything: `npm run lint`, `npm run typecheck`, `npm test`, `npm run build`.

## Publish on GitHub Pages
1. Create a GitHub repository and push this folder to the `main` branch.
2. In the repository: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main` (or run the workflow from the **Actions** tab). `.github/workflows/deploy.yml` installs from the lockfile, lints, type-checks, tests, builds and deploys.
4. Your site appears at `https://USER.github.io/REPO/`.

**Sub-path safe:** the build uses relative asset paths (`base: './'`) and hash routing (`#/laws`), so it works at `/REPO/` and needs no server rewrites. To force an absolute path set `VITE_BASE_PATH=/REPO/`.

## Editing the legal library
Data is generated from Python files in `scripts/data/` into `public/data/*.json`:
```
python3 scripts/data/build.py
```
The script checks that every cross-reference exists and reports missing translations. Rules: never paste statutory text you have not copied from the official source; set `originalText` only for verbatim text; keep `verification` honest; set `sourceUrlVerified` and `lastVerified` only after you have opened the official page.

## Chatbot that answers from the laws (RAG)
`serverless/` holds a ready-to-deploy endpoint that retrieves passages from `serverless/corpus.json` and has an AI model answer **only** from them, with citations the model cannot invent. It is not "trained" on all Pakistani law: coverage equals the official text you add to `corpus-input/` (then run `python3 scripts/ingest/build_corpus.py`). Step-by-step deployment is in `serverless/README.md`. Retrieval is keyword-based over mostly English text, so Urdu/Sindhi questions match mainly through the glossary; add Urdu/Sindhi official texts or an embeddings step for better coverage.

## Optional AI mode
Copy `.env.example` to `.env.local` and set `VITE_AI_ENDPOINT` to an **https** URL you control. For GitHub Pages add it as a repository **variable** (not a secret). **Never put an API key in the frontend**: keep it in your serverless platform. Users see a privacy notice and must agree before any question leaves their browser. If the endpoint is missing, slow, rate-limited or returns something malformed, the chat shows a clear message and falls back to the local assistant.

## Privacy
No accounts, no analytics, no cookies. Browser storage holds only: language, chosen province, and chapters marked read (and the AI consent choice). Chat history stays in memory.

## Troubleshooting
- *Blank page on GitHub Pages:* check Settings → Pages uses GitHub Actions and the workflow succeeded.
- *Data failed to load:* run `python3 scripts/data/build.py` and confirm `public/data/*.json` exist.
- *Urdu/Sindhi looks wrong:* fonts are bundled (Noto Naskh Arabic, Noto Nastaliq Urdu); make sure `lang="ur"`/`lang="sd"` is kept on translated text.

## Licence and sources
Official sources: Pakistan Code, National Assembly, Ministry of Law and Justice, Supreme Court, and provincial law portals (see the About page). Plain-language text on this site is unofficial.
