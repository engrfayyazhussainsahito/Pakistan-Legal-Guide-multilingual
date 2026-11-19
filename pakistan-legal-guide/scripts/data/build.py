"""Generates public/data/{laws,glossary,topics}.json from the Python sources and validates references.

Run:  python3 scripts/data/build.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))

from laws_a import LAWS as A
from laws_b import LAWS as B
from laws_c import LAWS as C
from topics_1 import CH as CH1, FAQS as F1
from topics_2 import CH as CH2, FAQS as F2
from topics_3 import CH as CH3, FAQS as F3
from glossary_rights import GLOSSARY, RIGHTS

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "public", "data")
os.makedirs(OUT, exist_ok=True)

LAW_VERSION = "2026.1"
LAST_REVIEWED = "2026-11-18"

laws = A + B + C
# small text fixes
for l in laws:
    for k, v in list(l["summary"].items()):
        l["summary"][k] = v.replace("(وفاقی ombudsman)", "(وفاقی محتسب)")

law_ids = {l["id"] for l in laws}
assert len(law_ids) == len(laws), "duplicate law ids"

# normalise glossary references in sections: "equality before law" -> "equality-before-law"
glossary_ids = {g["id"] for g in GLOSSARY}
section_ids = {}
for l in laws:
    section_ids[l["id"]] = {s["id"] for s in l["sections"]}
    for s in l["sections"]:
        if "glossary" in s:
            s["glossary"] = [x.replace(" ", "-") for x in s["glossary"]]
            for x in s["glossary"]:
                assert x in glossary_ids, f"unknown glossary id {x} in {s['id']}"

# related laws must exist
for l in laws:
    for r in l.get("relatedLaws", []):
        assert r in law_ids, f"{l['id']} relates to unknown law {r}"
    # every law must carry an explicit note when federal and applicable to provinces
    assert l["sourceUrl"].startswith("https://")

for g in GLOSSARY:
    for r in g["relatedLaws"]:
        assert r in law_ids, f"glossary {g['id']} unknown law {r}"

faqs = F1 + F2 + F3
faq_ids = {f["id"] for f in faqs}
assert len(faq_ids) == len(faqs), "duplicate faq ids"

chapters = CH1 + CH2 + CH3
chapters.sort(key=lambda c: c["number"])
assert [c["number"] for c in chapters] == list(range(1, len(chapters) + 1))

def check_ref(ref, ctx):
    assert ref["lawId"] in law_ids, f"{ctx}: unknown law {ref['lawId']}"
    if "sectionId" in ref:
        assert ref["sectionId"] in section_ids[ref["lawId"]], f"{ctx}: unknown section {ref['sectionId']} in {ref['lawId']}"

for f in faqs:
    for r in f["relatedLaws"]:
        check_ref(r, f["id"])
used_faqs = set()
for c in chapters:
    for r in c["relatedLaws"]:
        check_ref(r, c["id"])
    for fid in c["faqIds"]:
        assert fid in faq_ids, f"{c['id']}: unknown faq {fid}"
        used_faqs.add(fid)
    for t in c["terms"]:
        assert t in glossary_ids, f"{c['id']}: unknown term {t}"
for fid in faq_ids - used_faqs:
    print("WARNING: unused faq", fid)

for r in RIGHTS:
    check_ref({"lawId": r["lawId"], "sectionId": r["sectionId"]}, r["id"])

# language completeness report
def langs(d):
    return {k for k, v in d.items() if v}
missing = []
for c in chapters:
    for fld in ("title", "description", "intro"):
        if langs(c[fld]) != {"en", "ur", "sd"}:
            missing.append((c["id"], fld))
    for i, s in enumerate(c["steps"]):
        if langs(s) != {"en", "ur", "sd"}:
            missing.append((c["id"], f"step{i}"))
for m in missing:
    print("WARNING missing translation:", m)

def dump(name, obj):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)

dump("laws.json", {"libraryVersion": LAW_VERSION, "lastReviewed": LAST_REVIEWED, "laws": laws})
dump("glossary.json", {"entries": GLOSSARY})
dump("topics.json", {"topics": chapters, "faqs": faqs, "rights": RIGHTS})

n_sections = sum(len(l["sections"]) for l in laws)
n_orig = sum(1 for l in laws for s in l["sections"] if s.get("originalText"))
print(f"laws={len(laws)} sections={n_sections} with-original-text={n_orig} glossary={len(GLOSSARY)} chapters={len(chapters)} faqs={len(faqs)} rights={len(RIGHTS)}")
