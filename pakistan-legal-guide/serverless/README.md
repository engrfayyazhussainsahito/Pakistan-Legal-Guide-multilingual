# AI assistant endpoint (retrieval-augmented)

This is the server half of the chatbot. The website sends a question; this worker finds the best
matching passages in `corpus.json`, asks the model to answer **only from those passages**, and
returns the structured answer the site already knows how to show (short answer, jurisdiction,
law and section, explanation, next steps, limitations, citations).

## Why not "train" a model?
Fine-tuning on statutes goes stale when laws are amended and can still invent sections.
Retrieval over official text can be updated by editing a file, always cites a source, and can say
"I don't have this".

## 1. Give it the laws
Copy official text into `../corpus-input/*.md` (header format in `../scripts/ingest/build_corpus.py`),
then run `python3 scripts/ingest/build_corpus.py`. **Coverage = what you add.** The assistant knows
only the bundled library (summaries, explanations, 7 constitutional extracts) until you do.

## 2. Deploy (Cloudflare Workers, free tier works)
```
cd serverless
npx wrangler login
# edit wrangler.toml: ALLOWED_ORIGIN = your GitHub Pages origin
npx wrangler secret put ANTHROPIC_API_KEY      # key stays here, never in the site
npx wrangler deploy
```
You get a URL like `https://pakistan-legal-guide-ai.YOURNAME.workers.dev`.

## 3. Connect the site
GitHub repo -> Settings -> Secrets and variables -> Actions -> **Variables**:
`VITE_AI_ENDPOINT` = that URL, `VITE_AI_PROVIDER_NAME` = e.g. `Claude (Anthropic)`.
Push to `main`; the chat page then offers the "Use the AI service" toggle behind the privacy notice.

## Safety built in
Origin allow-list, input limits, optional rate limit, province filtering, refusal when evidence is
missing, and citations rebuilt from your corpus (the model cannot invent a link). It is still
legal *information*: have a lawyer review the corpus and the answers before public launch.
## Cost note
Each question sends ~8 passages to the model, so you pay per request. Set a spend limit at your provider.
