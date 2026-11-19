from common import L

def _norm(laws):
    return [(l,) if isinstance(l, str) else l for l in (laws or [])]

def faq(id, q, a, kw, laws=None, sens=False):
    laws = _norm(laws)
    d = {"id": id, "question": q, "answer": a, "keywords": kw,
         "relatedLaws": [{"lawId": l[0], **({"sectionId": l[1]} if len(l) > 1 else {})} for l in (laws or [])],
         "review": "unreviewed"}
    if sens:
        d["jurisdictionSensitive"] = True
    return d

def ch(number, id, phase, cat, title, desc, intro, steps, faqs, check, terms, laws, kw, mins=6):
    laws = _norm(laws)
    return {
        "id": id, "number": number, "phase": phase, "category": cat,
        "title": title, "description": desc, "intro": intro, "steps": steps,
        "faqIds": faqs, "check": [{"q": q, "a": a} for q, a in check], "terms": terms,
        "relatedLaws": [{"lawId": l[0], **({"sectionId": l[1]} if len(l) > 1 else {})} for l in laws],
        "keywords": kw, "minutes": mins,
    }
