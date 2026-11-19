# Add official law text here

Create one `.md` file per law (or per part). See the header format in `scripts/ingest/build_corpus.py`.
Copy text only from the official portals (Pakistan Code, provincial law sites). Then run
`python3 scripts/ingest/build_corpus.py` and redeploy the worker. The more official text you add,
the more the assistant can answer; without it, it will say it has no evidence.
