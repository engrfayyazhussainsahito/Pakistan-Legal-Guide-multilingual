import json, os
base = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

NEW = {
 "en": {
  "guide": {
   "phase": "Phase {n}", "phases": "Learning path",
   "p1": "Foundations", "p2": "Criminal justice", "p3": "Family & civil law", "p4": "Everyday life & getting help",
   "p1d": "Your constitutional rights and how the legal system and statutes work.",
   "p2d": "From reporting a crime to arrest, remand and bail.",
   "p3d": "Marriage, divorce, children, inheritance and civil disputes.",
   "p4d": "Renting, property, work, consumer, online safety, information and legal aid.",
   "chapter": "Chapter {n}", "minutes": "{min} min read", "markRead": "Mark chapter as read", "isRead": "Read — click to undo",
   "progress": "{done} of {total} chapters read", "reset": "Reset progress",
   "resetConfirm": "Reset your reading progress? This only affects this browser.",
   "saved": "Progress is saved only in this browser.",
   "inPlainWords": "In plain words", "steps": "What to do, step by step", "check": "Check yourself",
   "showAnswer": "Show answer", "hideAnswer": "Hide answer", "keyTerms": "Key terms in this chapter",
   "next": "Next chapter", "prev": "Previous chapter", "all": "All chapters", "onPage": "On this page",
   "lawsHere": "Laws and sections behind this chapter", "start": "Start with Chapter 1", "syllabus": "View the syllabus",
   "askAbout": "Ask the assistant about this chapter", "faqAnchor": "Common questions"
  },
  "home": {
   "eyebrow": "Free legal information · English · اردو · سنڌي",
   "statsChapters": "Guide chapters", "statsFaqs": "Questions answered",
   "f1t": "Plain language first", "f1b": "Each chapter starts with the idea in everyday words, then shows the section it comes from.",
   "f2t": "Original wording kept intact", "f2b": "Where bundled, statutory text is shown exactly as published, never rewritten — explanations are labelled as ours.",
   "f3t": "Province-aware", "f3b": "Choose Sindh, Punjab, Khyber Pakhtunkhwa and more; laws from other provinces are never assumed to apply.",
   "f4t": "Three languages", "f4b": "Switch between English, Urdu and Sindhi at any time without losing your place.",
   "pathTitle": "Learning path", "pathSub": "Four phases, eighteen chapters. Read in order, or jump to what you need.",
   "chaptersTitle": "All chapters", "chaptersSub": "Every chapter has an introduction, practical steps, common questions and a self-check.",
   "studyTitle": "How to use this guide",
   "study1t": "Read for the idea first", "study1b": "Start with “In plain words”, then open the exact section it points to.",
   "study2t": "Pick your province", "study2b": "Use the selector in the header so the right laws come first.",
   "study3t": "Follow the steps", "study3b": "Each chapter ends in practical next steps you can act on today.",
   "study4t": "Test yourself", "study4b": "Use “Check yourself” questions; answers stay hidden until you open them.",
   "study5t": "Confirm at the source", "study5b": "Laws change. Always check the official source before you rely on anything.",
   "prereqTitle": "Before you start", "prereqBody": "No legal background is needed. This site gives general legal information — it is not legal advice and cannot replace a qualified lawyer.",
   "tipsTitle": "Good to know", "tipsBody": "Your language, province and reading progress are stored only in your browser. Press “/” anywhere to jump to search."
  },
  "search": {"hint": "Press / to search", "typeAll": "All types"},
  "sidebar": {"title": "Guide chapters", "about": "About & sources", "open": "Open chapters menu"},
  "laws": {"viewBy": "Library"}
 },
 "ur": {
  "guide": {
   "phase": "مرحلہ {n}", "phases": "سیکھنے کا راستہ",
   "p1": "بنیادیں", "p2": "فوجداری انصاف", "p3": "خاندانی اور دیوانی قانون", "p4": "روزمرہ زندگی اور مدد کا حصول",
   "p1d": "آپ کے آئینی حقوق اور قانونی نظام اور قوانین کیسے کام کرتے ہیں۔",
   "p2d": "جرم کی اطلاع سے لے کر گرفتاری، ریمانڈ اور ضمانت تک۔",
   "p3d": "نکاح، طلاق، بچے، وراثت اور دیوانی تنازعات۔",
   "p4d": "کرایہ داری، جائیداد، ملازمت، صارفین، آن لائن تحفظ، معلومات اور قانونی امداد۔",
   "chapter": "باب {n}", "minutes": "{min} منٹ کا مطالعہ", "markRead": "باب کو پڑھا ہوا نشان زد کریں", "isRead": "پڑھ لیا — واپس کرنے کے لیے کلک کریں",
   "progress": "{total} میں سے {done} ابواب پڑھے گئے", "reset": "پیش رفت صاف کریں",
   "resetConfirm": "کیا آپ مطالعے کی پیش رفت صاف کرنا چاہتے ہیں؟ اس کا اثر صرف اسی براؤزر پر ہو گا۔",
   "saved": "پیش رفت صرف اسی براؤزر میں محفوظ ہوتی ہے۔",
   "inPlainWords": "آسان الفاظ میں", "steps": "کیا کریں، قدم بہ قدم", "check": "خود کو جانچیں",
   "showAnswer": "جواب دکھائیں", "hideAnswer": "جواب چھپائیں", "keyTerms": "اس باب کی اہم اصطلاحات",
   "next": "اگلا باب", "prev": "پچھلا باب", "all": "تمام ابواب", "onPage": "اس صفحے پر",
   "lawsHere": "اس باب کے پیچھے قوانین اور دفعات", "start": "باب 1 سے آغاز کریں", "syllabus": "نصاب دیکھیں",
   "askAbout": "اس باب کے بارے میں معاون سے پوچھیں", "faqAnchor": "عام سوالات"
  },
  "home": {
   "eyebrow": "مفت قانونی معلومات · English · اردو · سنڌي",
   "statsChapters": "رہنما ابواب", "statsFaqs": "جوابات والے سوالات",
   "f1t": "پہلے آسان زبان", "f1b": "ہر باب بات کو روزمرہ الفاظ میں بتاتا ہے، پھر وہ دفعہ دکھاتا ہے جہاں سے وہ لی گئی ہے۔",
   "f2t": "اصل الفاظ جوں کے توں", "f2b": "جہاں شامل ہو، قانونی متن بالکل ویسا ہی دکھایا جاتا ہے جیسے شائع ہوا، کبھی دوبارہ نہیں لکھا جاتا — وضاحتوں پر ہماری طرف سے ہونے کا نشان ہوتا ہے۔",
   "f3t": "صوبے کے مطابق", "f3b": "سندھ، پنجاب، خیبر پختونخوا وغیرہ منتخب کریں؛ دوسرے صوبوں کے قوانین کو کبھی لاگو فرض نہیں کیا جاتا۔",
   "f4t": "تین زبانیں", "f4b": "اپنی جگہ کھوئے بغیر کسی بھی وقت انگریزی، اردو اور سندھی کے درمیان تبدیل کریں۔",
   "pathTitle": "سیکھنے کا راستہ", "pathSub": "چار مراحل، اٹھارہ ابواب۔ ترتیب سے پڑھیں یا اپنی ضرورت کے باب پر جائیں۔",
   "chaptersTitle": "تمام ابواب", "chaptersSub": "ہر باب میں تعارف، عملی اقدامات، عام سوالات اور خود جانچ ہے۔",
   "studyTitle": "اس رہنما کو کیسے استعمال کریں",
   "study1t": "پہلے بات سمجھیں", "study1b": "“آسان الفاظ میں” سے آغاز کریں، پھر وہ عین دفعہ کھولیں جس کی طرف اشارہ ہے۔",
   "study2t": "اپنا صوبہ منتخب کریں", "study2b": "ہیڈر میں سلیکٹر استعمال کریں تاکہ درست قوانین پہلے آئیں۔",
   "study3t": "اقدامات پر عمل کریں", "study3b": "ہر باب عملی اگلے اقدامات پر ختم ہوتا ہے جو آپ آج ہی کر سکتے ہیں۔",
   "study4t": "خود کو آزمائیں", "study4b": "“خود کو جانچیں” کے سوالات استعمال کریں؛ جواب آپ کے کھولنے تک چھپے رہتے ہیں۔",
   "study5t": "ماخذ پر تصدیق کریں", "study5b": "قوانین بدلتے ہیں۔ کسی بھی چیز پر بھروسا کرنے سے پہلے ہمیشہ سرکاری ماخذ دیکھیں۔",
   "prereqTitle": "شروع کرنے سے پہلے", "prereqBody": "کسی قانونی پس منظر کی ضرورت نہیں۔ یہ سائٹ عمومی قانونی معلومات دیتی ہے — یہ قانونی مشورہ نہیں اور کسی مستند وکیل کا متبادل نہیں۔",
   "tipsTitle": "جاننا اچھا ہے", "tipsBody": "آپ کی زبان، صوبہ اور مطالعے کی پیش رفت صرف آپ کے براؤزر میں محفوظ ہوتی ہے۔ کہیں سے بھی تلاش پر جانے کے لیے “/” دبائیں۔"
  },
  "search": {"hint": "تلاش کے لیے / دبائیں", "typeAll": "تمام اقسام"},
  "sidebar": {"title": "رہنما ابواب", "about": "تعارف اور ماخذ", "open": "ابواب کا مینو کھولیں"},
  "laws": {"viewBy": "لائبریری"}
 },
 "sd": {
  "guide": {
   "phase": "مرحلو {n}", "phases": "سکڻ جو رستو",
   "p1": "بنيادون", "p2": "فوجداري انصاف", "p3": "خانداني ۽ ديواني قانون", "p4": "روزمره جي زندگي ۽ مدد جو حصول",
   "p1d": "توهان جا آئيني حق ۽ قانوني نظام ۽ قانون ڪيئن ڪم ڪن ٿا.",
   "p2d": "ڏوهه جي اطلاع کان وٺي گرفتاري، ريمانڊ ۽ ضمانت تائين.",
   "p3d": "نڪاح، طلاق، ٻار، وراثت ۽ ديواني تڪرار.",
   "p4d": "ڪرائي داري، ملڪيت، نوڪري، صارف، آن لائن حفاظت، ڄاڻ ۽ قانوني مدد.",
   "chapter": "باب {n}", "minutes": "{min} منٽ جو مطالعو", "markRead": "باب کي پڙهيل نشان ڪريو", "isRead": "پڙهيو ويو — واپس ڪرڻ لاءِ ڪلڪ ڪريو",
   "progress": "{total} مان {done} باب پڙهيا ويا", "reset": "پيش رفت صاف ڪريو",
   "resetConfirm": "ڇا توهان مطالعي جي پيش رفت صاف ڪرڻ چاهيو ٿا؟ ان جو اثر رڳو هن براؤزر تي ٿيندو.",
   "saved": "پيش رفت رڳو هن براؤزر ۾ محفوظ ٿئي ٿي.",
   "inPlainWords": "سادن لفظن ۾", "steps": "ڇا ڪجي، قدم بہ قدم", "check": "پاڻ کي جاچيو",
   "showAnswer": "جواب ڏيکاريو", "hideAnswer": "جواب لڪايو", "keyTerms": "هن باب جا اهم اصطلاح",
   "next": "ايندڙ باب", "prev": "پويون باب", "all": "سڀ باب", "onPage": "هن صفحي تي",
   "lawsHere": "هن باب جي پويان قانون ۽ دفعا", "start": "باب 1 کان شروع ڪريو", "syllabus": "نصاب ڏسو",
   "askAbout": "هن باب بابت مددگار کان پڇو", "faqAnchor": "عام سوال"
  },
  "home": {
   "eyebrow": "مفت قانوني ڄاڻ · English · اردو · سنڌي",
   "statsChapters": "رهنما باب", "statsFaqs": "جواب سان سوال",
   "f1t": "پهرين سادي ٻولي", "f1b": "هر باب ڳالهه روزمره جي لفظن ۾ ٻڌائي ٿو، پوءِ اهو دفعو ڏيکاري ٿو جتان اها ورتل آهي.",
   "f2t": "اصل لفظ جيئن جو تيئن", "f2b": "جتي شامل هجي، قانوني متن بلڪل ائين ڏيکاريو وڃي ٿو جيئن ڇپيل آهي، ڪڏهن ٻيهر نٿو لکجي — وضاحتن تي اسان طرفان هجڻ جو نشان هوندو آهي.",
   "f3t": "صوبي مطابق", "f3b": "سنڌ، پنجاب، خيبر پختونخوا وغيره چونڊيو؛ ٻين صوبن جا قانون ڪڏهن به لاڳو فرض نٿا ڪيا وڃن.",
   "f4t": "ٽي ٻوليون", "f4b": "پنهنجي جڳهه وڃائڻ کانسواءِ ڪنهن به وقت انگريزي، اردو ۽ سنڌي وچ ۾ بدلايو.",
   "pathTitle": "سکڻ جو رستو", "pathSub": "چار مرحلا، ارڙهه باب. ترتيب سان پڙهو يا پنهنجي ضرورت واري باب ڏانهن وڃو.",
   "chaptersTitle": "سڀ باب", "chaptersSub": "هر باب ۾ تعارف، عملي قدم، عام سوال ۽ پاڻ جاچ آهي.",
   "studyTitle": "هي رهنما ڪيئن استعمال ڪجي",
   "study1t": "پهرين ڳالهه سمجهو", "study1b": "“سادن لفظن ۾” کان شروع ڪريو، پوءِ اهو صحيح دفعو کوليو جنهن ڏانهن اشارو آهي.",
   "study2t": "پنهنجو صوبو چونڊيو", "study2b": "هيڊر ۾ سليڪٽر استعمال ڪريو ته صحيح قانون پهرين اچن.",
   "study3t": "قدمن تي عمل ڪريو", "study3b": "هر باب عملي ايندڙ قدمن تي ختم ٿئي ٿو جيڪي توهان اڄ ئي ڪري سگهو ٿا.",
   "study4t": "پاڻ کي آزمايو", "study4b": "“پاڻ کي جاچيو” جا سوال استعمال ڪريو؛ جواب توهان جي کولڻ تائين لڪيل رهن ٿا.",
   "study5t": "ماخذ تي تصديق ڪريو", "study5b": "قانون بدلبا رهن ٿا. ڪنهن به شيءِ تي ڀروسو ڪرڻ کان اڳ هميشه سرڪاري ماخذ ڏسو.",
   "prereqTitle": "شروع ڪرڻ کان اڳ", "prereqBody": "ڪنهن قانوني پس منظر جي ضرورت ناهي. هيءَ سائيٽ عام قانوني ڄاڻ ڏئي ٿي — هي قانوني صلاح ناهي ۽ ڪنهن مستند وڪيل جو متبادل ناهي.",
   "tipsTitle": "ڄاڻڻ سٺو آهي", "tipsBody": "توهان جي ٻولي، صوبو ۽ مطالعي جي پيش رفت رڳو توهان جي براؤزر ۾ محفوظ ٿين ٿا. ڪٿان به ڳولا ڏانهن وڃڻ لاءِ “/” دٻايو."
  },
  "search": {"hint": "ڳولا لاءِ / دٻايو", "typeAll": "سڀ قسم"},
  "sidebar": {"title": "رهنما باب", "about": "تعارف ۽ ماخذ", "open": "بابن جو مينيو کوليو"},
  "laws": {"viewBy": "لائبريري"}
 }
}

def merge(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            merge(a[k], v)
        else:
            a[k] = v

for lang, add in NEW.items():
    p = os.path.join(base, f'{lang}.json')
    d = json.load(open(p, encoding='utf-8'))
    merge(d, add)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(lang, 'ok')
