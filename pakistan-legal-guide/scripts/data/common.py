# Helpers used by the data generators (build-time only, not shipped).
PC = "https://pakistancode.gov.pk/"
SINDH = "https://www.sindhlaws.gov.pk/"
PUNJAB = "https://punjablaws.gov.pk/"
KP = "https://www.pakp.gov.pk/all-acts/"
SRC = {
    "federal": ("Pakistan Code (Government of Pakistan)", PC),
    "ict": ("Pakistan Code (Government of Pakistan)", PC),
    "sindh": ("Sindh Laws portal (Government of Sindh)", SINDH),
    "punjab": ("Punjab Laws portal (Government of Punjab)", PUNJAB),
    "kpk": ("Provincial Assembly of Khyber Pakhtunkhwa – Acts", KP),
}
NATIONWIDE = ["federal", "sindh", "punjab", "kpk", "balochistan", "ict"]

def L(en, ur=None, sd=None):
    d = {"en": en}
    if ur: d["ur"] = ur
    if sd: d["sd"] = sd
    return d

def sec(id, number, heading, en, ur=None, sd=None, original=None, osrc=None,
        terms=None, cond=None, gl=None):
    s = {"id": id, "number": number, "heading": heading, "explanation": L(en, ur, sd)}
    if original:
        s["originalText"] = original
        s["originalTextSource"] = osrc
    if terms:
        s["terms"] = [{"term": t, "meaning": L(*m) if isinstance(m, tuple) else L(m)} for t, m in terms]
    if cond:
        s["conditions"] = L(*cond) if isinstance(cond, tuple) else L(cond)
    if gl:
        s["glossary"] = gl
    return s

def law(id, title, category, jurisdiction, summary, keywords, sections=None, abbr=None,
        year=None, applies=None, note=None, title_tr=None, featured=False, related=None,
        version=None, src=None, verification="source-linked"):
    sname, surl = SRC[jurisdiction] if src is None else src
    langs = [k for k in ("en", "ur", "sd") if k in summary]
    d = {
        "id": id, "title": title, "category": category, "jurisdiction": jurisdiction,
        "appliesTo": applies if applies is not None else [jurisdiction],
        "summary": summary, "keywords": keywords, "sections": sections or [],
        "sourceUrl": surl, "sourceName": sname, "sourceUrlVerified": False,
        "languages": langs, "verification": verification,
    }
    if abbr: d["abbreviation"] = abbr
    if year: d["year"] = year
    if note: d["applicabilityNote"] = note
    if title_tr: d["titleTranslations"] = title_tr
    if featured: d["featured"] = True
    if related: d["relatedLaws"] = related
    if version: d["version"] = version
    return d

FED_NOTE = L(
    "Federal law. It is understood to apply across the provinces and Islamabad; whether and how it applies in Gilgit-Baltistan and Azad Jammu & Kashmir must be checked separately.",
    "وفاقی قانون۔ اسے صوبوں اور اسلام آباد میں لاگو سمجھا جاتا ہے؛ گلگت بلتستان اور آزاد جموں و کشمیر میں اس کا اطلاق اور طریقۂ اطلاق الگ سے دیکھنا ضروری ہے۔",
    "وفاقي قانون. اهو صوبن ۽ اسلام آباد ۾ لاڳو سمجهيو وڃي ٿو؛ گلگت-بلتستان ۽ آزاد جمون ۽ ڪشمير ۾ ان جو لاڳو ٿيڻ ۽ طريقو الڳ چيڪ ڪرڻ گهرجي.")
