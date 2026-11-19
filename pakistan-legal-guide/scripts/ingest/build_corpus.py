#!/usr/bin/env python3
"""Build serverless/corpus.json: the passages the AI endpoint is allowed to answer from.

Sources, in order:
 1. public/data (laws, sections, glossary, FAQs, chapters) bundled with the site
 2. corpus-input/*.md  - official law text YOU add (one file per law or part of a law)

Each corpus-input file starts with a header block, then the text:

    ---
    law: Code of Criminal Procedure, 1898
    jurisdiction: federal            # sindh | punjab | kpk | balochistan | ict | gb | ajk | federal
    year: 1898
    source_url: https://pakistancode.gov.pk/...   # exact official page you copied from
    section: Section 497              # optional
    verified_on: 2026-11-19           # date you compared it with the official source
    ---
    <verbatim text copied from the official source>

Only text you copied from an official source should go here. Run:  python3 scripts/ingest/build_corpus.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "serverless" / "corpus.json"
MAX_CHARS = 1400  # ~ one passage


def pick(v, lang="en"):
    if isinstance(v, dict):
        return v.get(lang) or v.get("en") or next(iter(v.values()), "")
    return v or ""


def chunk(text, size=MAX_CHARS):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    cur, out = "", []
    for p in paras:
        if len(cur) + len(p) > size and cur:
            out.append(cur.strip()); cur = ""
        while len(p) > size:
            out.append(p[:size]); p = p[size:]
        cur += p + "\n\n"
    if cur.strip():
        out.append(cur.strip())
    return out


def main():
    laws = json.loads((ROOT / "public/data/laws.json").read_text())["laws"]
    gloss = json.loads((ROOT / "public/data/glossary.json").read_text())["entries"]
    topics = json.loads((ROOT / "public/data/topics.json").read_text())
    docs = []

    def add(**d):
        docs.append(d)

    for l in laws:
        base = dict(law=l["title"], jurisdiction=l["jurisdiction"], appliesTo=l["appliesTo"], year=l.get("year"),
                    url=l["sourceUrl"], verified=l["verification"] == "verified")
        add(**base, kind="summary", section="", text=pick(l["summary"]), official=False)
        for s in l["sections"]:
            if s.get("originalText"):
                add(**base, kind="original", section=f'{s["number"]} {s["heading"]}', text=s["originalText"], official=True)
            add(**base, kind="explanation", section=f'{s["number"]} {s["heading"]}', text=pick(s["explanation"]), official=False)
    for g in gloss:
        add(law="Legal glossary", jurisdiction="federal", appliesTo=[], year=None, url="", verified=False, kind="glossary",
            section=g["en"], text=f'{g["en"]} / {g["ur"]} / {g["sd"]}: {pick(g["definition"])}', official=False)
    for f in topics["faqs"]:
        add(law="FAQ", jurisdiction="federal", appliesTo=[], year=None, url="", verified=False, kind="faq",
            section=pick(f["question"]), text=pick(f["question"]) + " " + pick(f["answer"]), official=False)

    extra = 0
    for p in sorted(q for q in (ROOT / "corpus-input").glob("*.md") if q.name.lower() != "readme.md"):
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", p.read_text(encoding="utf-8"), re.S)
        if not m:
            print(f"skip {p.name}: missing header block"); continue
        meta = {k.strip(): v.split("#")[0].strip() for k, v in (ln.split(":", 1) for ln in m.group(1).splitlines() if ":" in ln)}
        if not meta.get("source_url", "").startswith("https://") or not meta.get("law") or not meta.get("jurisdiction"):
            print(f"skip {p.name}: need law, jurisdiction, source_url (https)"); continue
        for c in chunk(m.group(2)):
            add(law=meta["law"], jurisdiction=meta["jurisdiction"], appliesTo=[meta["jurisdiction"]],
                year=int(meta["year"]) if meta.get("year", "").isdigit() else None, url=meta["source_url"],
                verified=bool(meta.get("verified_on")), kind="original", section=meta.get("section", ""), text=c, official=True)
            extra += 1

    for i, d in enumerate(docs):
        d["id"] = i
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(docs, ensure_ascii=False), encoding="utf-8")
    print(f"corpus: {len(docs)} passages ({extra} from corpus-input) -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
