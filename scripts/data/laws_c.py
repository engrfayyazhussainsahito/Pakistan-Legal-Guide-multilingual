from common import *

LAWS = []

# ------------------------------------------------------------------ LABOUR
LAWS.append(law(
    "payment-of-wages-1936", "Payment of Wages Act, 1936", "labour", "federal",
    L("Requires employers to pay wages on time and limits deductions from wages. A worker whose wages are delayed or wrongly deducted can claim before the authority appointed under the Act. Provinces have their own versions or amendments.",
      "آجروں پر وقت پر اجرت ادا کرنا لازم کرتا ہے اور اجرت سے کٹوتیوں کو محدود کرتا ہے۔ جس کارکن کی اجرت میں تاخیر ہو یا غلط کٹوتی ہو وہ ایکٹ کے تحت مقرر اتھارٹی کے سامنے دعویٰ کر سکتا ہے۔ صوبوں کے اپنے ورژن یا ترامیم ہیں۔",
      "ملازمن تي وقت تي اجرت ڏيڻ لازمي ڪري ٿو ۽ اجرت مان ڪٽوتين کي محدود ڪري ٿو. جنهن ڪم ڪندڙ جي اجرت ۾ دير ٿئي يا غلط ڪٽوتي ٿئي اهو ايڪٽ تحت مقرر اٿارٽيءَ آڏو دعويٰ ڪري سگهي ٿو. صوبن جا پنهنجا ورزن يا ترميمون آهن."),
    ["wages", "salary", "deduction", "delay", "labour", "worker", "employer", "payment"],
    year=1936, applies=NATIONWIDE, note=FED_NOTE, related=["ira-2012", "sindh-standing-orders-2015"]))

LAWS.append(law(
    "ira-2012", "Industrial Relations Act, 2012", "labour", "federal",
    L("Covers trade unions, collective bargaining, industrial disputes and unfair labour practices in establishments to which it applies (mainly in Islamabad and inter-provincial establishments). Provinces have their own industrial relations laws for provincial matters.",
      "اس کے لاگو اداروں (بنیادی طور پر اسلام آباد اور بین الصوبائی اداروں) میں ٹریڈ یونینوں، اجتماعی سودے بازی، صنعتی تنازعات اور غیر منصفانہ مزدور طریقوں کا احاطہ کرتا ہے۔ صوبائی معاملات کے لیے صوبوں کے اپنے قوانین ہیں۔",
      "ان جي لاڳو ادارن (بنيادي طور اسلام آباد ۽ بين الصوبائي ادارن) ۾ ٽريڊ يونين، اجتماعي سودابازي، صنعتي تڪرارن ۽ غير منصفانه مزدور طريقن کي ڍڪي ٿو. صوبائي معاملن لاءِ صوبن جا پنهنجا قانون آهن."),
    ["trade union", "collective bargaining", "strike", "industrial dispute", "labour", "nirc", "unfair labour practice"],
    abbr="IRA", year=2012, applies=["ict", "federal"],
    note=L("Mainly for Islamabad and trans-provincial establishments. Provincial establishments are covered by provincial industrial relations laws.", "بنیادی طور پر اسلام آباد اور بین الصوبائی اداروں کے لیے۔ صوبائی اداروں پر صوبائی صنعتی تعلقات کے قوانین لاگو ہیں۔", "بنيادي طور اسلام آباد ۽ بين الصوبائي ادارن لاءِ. صوبائي ادارن تي صوبائي صنعتي لاڳاپن جا قانون لاڳو آهن."),
    related=["payment-of-wages-1936"]))

LAWS.append(law(
    "sindh-standing-orders-2015", "Sindh Terms of Employment (Standing Orders) Act, 2015", "labour", "sindh",
    L("Sets basic terms of employment in covered Sindh establishments: appointment letters, working conditions, leave, misconduct procedures and termination. Check the current text for who is covered.",
      "سندھ کے احاطہ شدہ اداروں میں ملازمت کی بنیادی شرائط طے کرتا ہے: تقرری نامے، کام کے حالات، رخصت، بدعنوانی/بدانتظامی کے طریقۂ کار اور برخاستگی۔ کون شامل ہے اس کے لیے موجودہ متن دیکھیں۔",
      "سنڌ جي ڍڪيل ادارن ۾ نوڪريءَ جون بنيادي شرطون طئه ڪري ٿو: تقرري جا خط، ڪم جا حالتون، موڪل، بدانتظامي جا طريقا ۽ برطرفي. ڪير ڍڪيل آهي ان لاءِ موجوده متن ڏسو."),
    ["employment", "standing orders", "termination", "appointment letter", "leave", "dismissal", "sindh", "worker", "labour"],
    year=2015, related=["payment-of-wages-1936"]))

# ------------------------------------------------------------------ CONSUMER
LAWS.append(law(
    "sindh-consumer-protection-2014", "Sindh Consumer Protection Act, 2014", "consumer", "sindh",
    L("Protects consumers in Sindh against defective goods, deficient services and unfair practices, and provides for Consumer Courts where a consumer can file a complaint. Check the current text for the procedure and time limits.",
      "سندھ میں صارفین کو ناقص اشیا، ناکافی خدمات اور غیر منصفانہ طرزِ عمل سے تحفظ دیتا ہے اور کنزیومر کورٹس فراہم کرتا ہے جہاں صارف شکایت دائر کر سکتا ہے۔ طریقۂ کار اور مدتوں کے لیے موجودہ متن دیکھیں۔",
      "سنڌ ۾ صارفن کي خراب شين، ناقص خدمتن ۽ غير منصفانه طريقن کان تحفظ ڏئي ٿو ۽ ڪنزيومر ڪورٽون مهيا ڪري ٿو جتي صارف شڪايت داخل ڪري سگهي ٿو. طريقي ۽ مدتن لاءِ موجوده متن ڏسو."),
    ["consumer", "defective goods", "refund", "warranty", "consumer court", "complaint", "sindh", "unfair practice", "service"],
    year=2014, featured=True, related=["contract-act-1872"]))

LAWS.append(law(
    "punjab-consumer-protection-2005", "Punjab Consumer Protection Act, 2005", "consumer", "punjab",
    L("Protects consumers in Punjab and provides for Consumer Courts. It covers defective products, misleading advertisements and poor service. Check the current text for time limits.",
      "پنجاب میں صارفین کو تحفظ دیتا ہے اور کنزیومر کورٹس فراہم کرتا ہے۔ ناقص مصنوعات، گمراہ کن اشتہارات اور ناقص خدمات اس میں شامل ہیں۔ مدتوں کے لیے موجودہ متن دیکھیں۔",
      "پنجاب ۾ صارفن کي تحفظ ڏئي ٿو ۽ ڪنزيومر ڪورٽون مهيا ڪري ٿو. خراب پراڊڪٽس، گمراهه ڪندڙ اشتهار ۽ خراب خدمتون ان ۾ شامل آهن. مدتن لاءِ موجوده متن ڏسو."),
    ["consumer", "defective product", "refund", "misleading advertisement", "consumer court", "punjab"],
    year=2005))

LAWS.append(law(
    "ict-consumer-protection-1995", "Islamabad Capital Territory Consumer Protection Act, 1995", "consumer", "ict",
    L("Consumer protection law for Islamabad Capital Territory, covering defective goods and unfair practices and providing a complaint process.",
      "اسلام آباد وفاقی دارالحکومت کے لیے صارفین کے تحفظ کا قانون جو ناقص اشیا اور غیر منصفانہ طرزِ عمل کا احاطہ کرتا اور شکایت کا طریقہ فراہم کرتا ہے۔",
      "اسلام آباد وفاقي دارالحڪومت لاءِ صارفن جي تحفظ جو قانون جيڪو خراب شين ۽ غير منصفانه طريقن کي ڍڪي ٿو ۽ شڪايت جو طريقو مهيا ڪري ٿو."),
    ["consumer", "islamabad", "defective goods", "complaint"],
    year=1995))

# ------------------------------------------------------------------ ADMINISTRATIVE
LAWS.append(law(
    "wafaqi-mohtasib-1983", "Establishment of the Office of Wafaqi Mohtasib (Ombudsman) Order, 1983", "administrative", "federal",
    L("Creates the Federal Ombudsman (Wafaqi Mohtasib), an office where anyone can complain free of charge about maladministration by federal government agencies — for example delay, neglect, or unfair treatment. Provinces have their own Ombudsman offices for provincial departments.",
      "وفاقی محتسب (وفاقی ombudsman) کا دفتر قائم کرتا ہے جہاں کوئی بھی شخص وفاقی سرکاری اداروں کی بدانتظامی — مثلاً تاخیر، غفلت یا ناانصافی — کے خلاف مفت شکایت کر سکتا ہے۔ صوبائی محکموں کے لیے صوبوں کے اپنے محتسب دفاتر ہیں۔",
      "وفاقي محتسب جو آفيس قائم ڪري ٿو جتي ڪو به شخص وفاقي سرڪاري ادارن جي بدانتظاميءَ — مثال طور دير، غفلت يا ناانصافي — خلاف مفت شڪايت ڪري سگهي ٿو. صوبائي کاتن لاءِ صوبن جا پنهنجا محتسب آفيس آهن."),
    ["ombudsman", "mohtasib", "maladministration", "complaint", "government office", "delay", "federal"],
    year=1983, featured=True, applies=NATIONWIDE, note=FED_NOTE, related=["constitution-1973", "rti-federal-2017"]))

# ------------------------------------------------------------------ CYBER
LAWS.append(law(
    "peca-2016", "Prevention of Electronic Crimes Act, 2016", "cyber", "federal",
    L("Defines cyber offences such as unauthorised access to systems and data, identity misuse, offences against the dignity and modesty of a person, and cyber stalking, and sets out investigation powers and procedure. It was amended in 2025; always check the current consolidated text.",
      "سائبر جرائم کی تعریف کرتا ہے جیسے نظام اور ڈیٹا تک غیر مجاز رسائی، شناخت کا غلط استعمال، کسی شخص کے وقار اور حیا کے خلاف جرائم، اور سائبر اسٹاکنگ، اور تفتیشی اختیارات اور طریقۂ کار طے کرتا ہے۔ 2025 میں اس میں ترمیم ہوئی؛ ہمیشہ موجودہ مرتب شدہ متن دیکھیں۔",
      "سائبر ڏوهن جي وصف ڪري ٿو جهڙوڪ نظام ۽ ڊيٽا تائين غير مجاز رسائي، شناخت جو غلط استعمال، ڪنهن شخص جي وقار ۽ حيا خلاف ڏوهه، ۽ سائبر اسٽاڪنگ، ۽ تفتيشي اختيار ۽ طريقو مقرر ڪري ٿو. 2025 ۾ ان ۾ ترميم ٿي؛ هميشه موجوده گڏيل متن ڏسو."),
    ["cybercrime", "peca", "online harassment", "hacking", "identity theft", "cyber stalking", "fia", "nr3c", "social media", "blackmail", "digital"],
    abbr="PECA", year=2016, featured=True, applies=NATIONWIDE, note=FED_NOTE,
    version="Amended in 2025 (reported). The exact amendments and current section numbering must be checked on the official source.",
    related=["ppc-1860", "qanun-e-shahadat-1984"],
    sections=[
        sec("peca-16", "Section 16", "Unauthorised use of identity information",
            "Using, obtaining or selling another person's identity information (for example, a CNIC number or photographs) without authority and for gain or harm can be an offence. Section numbering should be confirmed in the current text.",
            "کسی دوسرے شخص کی شناختی معلومات (مثلاً شناختی کارڈ نمبر یا تصاویر) کو اختیار کے بغیر فائدے یا نقصان کی نیت سے استعمال کرنا، حاصل کرنا یا بیچنا جرم ہو سکتا ہے۔ دفعہ کا نمبر موجودہ متن میں تصدیق کریں۔",
            "ڪنهن ٻئي شخص جي سڃاڻپ جي معلومات (مثال طور شناختي ڪارڊ نمبر يا تصويرون) اختيار کانسواءِ فائدي يا نقصان جي نيت سان استعمال ڪرڻ، حاصل ڪرڻ يا وڪڻڻ ڏوهه ٿي سگهي ٿو. دفعي جو نمبر موجوده متن ۾ تصديق ڪريو."),
        sec("peca-20", "Section 20", "Offences against dignity of a natural person",
            "Intentionally publishing or displaying false or intimidating information about a person that harms their reputation or privacy can be an offence. Check the current text and amendments.",
            "کسی شخص کے بارے میں جان بوجھ کر جھوٹی یا خوفزدہ کرنے والی معلومات شائع یا ظاہر کرنا جو اس کی ساکھ یا نجی زندگی کو نقصان پہنچائے جرم ہو سکتا ہے۔ موجودہ متن اور ترامیم دیکھیں۔",
            "ڪنهن شخص بابت ڄاڻي واڻي ڪوڙي يا ڊيڄاريندڙ معلومات شايع يا ڏيکارڻ جيڪا سندس ساک يا خانگي زندگيءَ کي نقصان پهچائي ڏوهه ٿي سگهي ٿي. موجوده متن ۽ ترميمون ڏسو."),
        sec("peca-21", "Section 21", "Offences against modesty of a natural person and minor",
            "Covers sharing or threatening to share sexually explicit or manipulated images of a person, including for blackmail. Victims can complain to the FIA's cybercrime wing. Check the current text.",
            "کسی شخص کی جنسی طور پر نازیبا یا تبدیل شدہ تصاویر شیئر کرنے یا شیئر کرنے کی دھمکی دینے، بشمول بلیک میلنگ، کا احاطہ کرتی ہے۔ متاثرین ایف آئی اے کے سائبر کرائم ونگ میں شکایت کر سکتے ہیں۔ موجودہ متن دیکھیں۔",
            "ڪنهن شخص جي جنسي طور نازيبا يا تبديل ٿيل تصويرن شيئر ڪرڻ يا شيئر ڪرڻ جي ڌمڪي ڏيڻ، بشمول بليڪ ميلنگ، کي ڍڪي ٿي. متاثر ايف آءِ اي جي سائبر ڪرائم ونگ ۾ شڪايت ڪري سگهن ٿا. موجوده متن ڏسو.",
            gl=["harassment"]),
        sec("peca-24", "Section 24", "Cyber stalking",
            "Repeatedly following, contacting, monitoring or harassing a person through the internet or other electronic means, causing fear or distress, can be cyber stalking. Check the current text.",
            "انٹرنیٹ یا دیگر برقی ذرائع سے کسی شخص کا بار بار پیچھا کرنا، رابطہ کرنا، نگرانی یا ہراساں کرنا جس سے خوف یا پریشانی پیدا ہو سائبر اسٹاکنگ ہو سکتا ہے۔ موجودہ متن دیکھیں۔",
            "انٽرنيٽ يا ٻين اليڪٽرانڪ ذريعن سان ڪنهن شخص جو بار بار پيڇو ڪرڻ، رابطو ڪرڻ، نگراني يا تنگ ڪرڻ جنهن سان خوف يا پريشاني پيدا ٿئي سائبر اسٽاڪنگ ٿي سگهي ٿو. موجوده متن ڏسو.",
            gl=["harassment"]),
    ]))

# ------------------------------------------------------------------ HUMAN RIGHTS
LAWS.append(law(
    "workplace-harassment-2010", "Protection against Harassment of Women at the Workplace Act, 2010", "humanrights", "federal",
    L("Requires organisations to adopt a code of conduct and set up an Inquiry Committee for harassment complaints, and allows complaints to the Ombudsman (federal or provincial). It protects the person complaining from retaliation. Check the current text and any later amendments on the official portal.",
      "اداروں پر ضابطۂ اخلاق اپنانے اور ہراسانی کی شکایات کے لیے انکوائری کمیٹی بنانے کی پابندی لگاتا ہے، اور محتسب (وفاقی یا صوبائی) کو شکایت کی اجازت دیتا ہے۔ شکایت کرنے والے کو انتقامی کارروائی سے تحفظ دیتا ہے۔ موجودہ متن اور ترامیم دیکھیں۔",
      "اداري تي ضابطه اخلاق اپنائڻ ۽ تنگ ڪرڻ جي شڪايتن لاءِ انڪوائري ڪميٽي ٺاهڻ جي پابندي رکي ٿو، ۽ محتسب (وفاقي يا صوبائي) کي شڪايت جي اجازت ڏئي ٿو. شڪايت ڪندڙ کي بدلي واري ڪارروائيءَ کان تحفظ ڏئي ٿو. موجوده متن ۽ ترميمون ڏسو."),
    ["harassment", "workplace", "women", "inquiry committee", "ombudsman", "complaint", "human rights", "labour"],
    year=2010, applies=NATIONWIDE, note=FED_NOTE, related=["ppc-1860", "peca-2016"]))

LAWS.append(law(
    "sindh-domestic-violence-2013", "Sindh Domestic Violence (Prevention and Protection) Act, 2013", "humanrights", "sindh",
    L("Provides protection against domestic violence in Sindh, including protection orders, residence and monetary relief, and a complaint mechanism. Check the current text and how it is implemented in your district.",
      "سندھ میں گھریلو تشدد سے تحفظ فراہم کرتا ہے، جس میں تحفظی احکامات، رہائش اور مالی ریلیف، اور شکایتی نظام شامل ہیں۔ موجودہ متن اور اپنے ضلع میں اس کا نفاذ دیکھیں۔",
      "سنڌ ۾ گهريلو تشدد کان تحفظ مهيا ڪري ٿو، جنهن ۾ تحفظي حڪم، رهائش ۽ مالي رليف، ۽ شڪايت جو نظام شامل آهن. موجوده متن ۽ پنهنجي ضلعي ۾ ان جو لاڳو ٿيڻ ڏسو."),
    ["domestic violence", "protection order", "abuse", "women", "sindh", "shelter", "human rights"],
    year=2013, featured=True, related=["ppc-1860", "family-courts-act-1964"]))

LAWS.append(law(
    "punjab-women-violence-2016", "Punjab Protection of Women against Violence Act, 2016", "humanrights", "punjab",
    L("Provides protection for women against violence in Punjab, including protection orders and a complaint process and shelters. Check the current text.",
      "پنجاب میں خواتین کو تشدد سے تحفظ دیتا ہے، جس میں تحفظی احکامات، شکایتی عمل اور پناہ گاہیں شامل ہیں۔ موجودہ متن دیکھیں۔",
      "پنجاب ۾ عورتن کي تشدد کان تحفظ ڏئي ٿو، جنهن ۾ تحفظي حڪم، شڪايت جو عمل ۽ پناهه گاهون شامل آهن. موجوده متن ڏسو."),
    ["violence against women", "protection order", "domestic violence", "punjab", "shelter"],
    year=2016))

# ------------------------------------------------------------------ LEGAL AID
LAWS.append(law(
    "legal-aid-justice-authority-2020", "Legal Aid and Justice Authority Act, 2020", "legalaid", "federal",
    L("Establishes a federal authority to provide legal aid to people who cannot afford a lawyer, particularly vulnerable groups. Check the current text and the authority's website for how to apply and which cases are covered.",
      "ایک وفاقی اتھارٹی قائم کرتا ہے جو ان لوگوں کو قانونی امداد فراہم کرے جو وکیل کا خرچ نہیں اٹھا سکتے، خصوصاً کمزور طبقات۔ درخواست کا طریقہ اور شامل مقدمات کے لیے موجودہ متن اور اتھارٹی کی ویب سائٹ دیکھیں۔",
      "هڪ وفاقي اٿارٽي قائم ڪري ٿو جيڪا انهن ماڻهن کي قانوني مدد ڏئي جيڪي وڪيل جو خرچ نٿا ڀري سگهن، خاص طور ڪمزور طبقن کي. درخواست جو طريقو ۽ شامل ڪيس ڏسڻ لاءِ موجوده متن ۽ اٿارٽيءَ جي ويب سائيٽ ڏسو."),
    ["legal aid", "free lawyer", "poor", "justice", "access to justice", "authority"],
    year=2020, featured=True, applies=NATIONWIDE, note=FED_NOTE, related=["constitution-1973", "crpc-1898"]))

# ------------------------------------------------------------------ GOVERNMENT SERVICES / RTI
LAWS.append(law(
    "rti-federal-2017", "Right of Access to Information Act, 2017", "government", "federal",
    L("Lets citizens request records held by federal public bodies. A public body must respond within a set time, and a refusal can be taken to the Information Commission. It does not cover provincial departments, which have their own right-to-information laws.",
      "شہریوں کو وفاقی عوامی اداروں کے ریکارڈ کی درخواست کا حق دیتا ہے۔ عوامی ادارے کو مقررہ وقت میں جواب دینا ہوتا ہے اور انکار کی صورت میں انفارمیشن کمیشن سے رجوع کیا جا سکتا ہے۔ صوبائی محکمے اس میں شامل نہیں؛ ان کے اپنے حقِ معلومات قوانین ہیں۔",
      "شهرين کي وفاقي عوامي ادارن وٽ رڪارڊ جي درخواست ڪرڻ جو حق ڏئي ٿو. عوامي ادارو مقرر وقت ۾ جواب ڏيڻو آهي ۽ انڪار جي صورت ۾ انفارميشن ڪميشن ڏانهن وڃي سگهجي ٿو. صوبائي کاتا ان ۾ شامل ناهن؛ سندن پنهنجا ڄاڻ جي حق وارا قانون آهن."),
    ["right to information", "rti", "records", "information commission", "public body", "request", "government"],
    year=2017, applies=NATIONWIDE, note=FED_NOTE, related=["constitution-1973", "rti-sindh-2016", "rti-punjab-2013"]))

LAWS.append(law(
    "rti-sindh-2016", "Sindh Transparency and Right to Information Act, 2016", "government", "sindh",
    L("The right-to-information law for Sindh public bodies: how to request records and how to complain to the Sindh Information Commission if refused.",
      "سندھ کے عوامی اداروں کے لیے حقِ معلومات کا قانون: ریکارڈ کیسے مانگا جائے اور انکار پر سندھ انفارمیشن کمیشن میں شکایت کیسے کی جائے۔",
      "سنڌ جي عوامي ادارن لاءِ ڄاڻ جي حق جو قانون: رڪارڊ ڪيئن گهرجي ۽ انڪار تي سنڌ انفارميشن ڪميشن ۾ شڪايت ڪيئن ڪجي."),
    ["right to information", "rti", "sindh", "transparency", "information commission"],
    year=2016, related=["rti-federal-2017"]))

LAWS.append(law(
    "rti-punjab-2013", "Punjab Transparency and Right to Information Act, 2013", "government", "punjab",
    L("The right-to-information law for Punjab public bodies, including how to request records and appeal to the Punjab Information Commission.",
      "پنجاب کے عوامی اداروں کے لیے حقِ معلومات کا قانون، بشمول ریکارڈ مانگنے اور پنجاب انفارمیشن کمیشن میں اپیل کا طریقہ۔",
      "پنجاب جي عوامي ادارن لاءِ ڄاڻ جي حق جو قانون، بشمول رڪارڊ گهرڻ ۽ پنجاب انفارميشن ڪميشن ۾ اپيل جو طريقو."),
    ["right to information", "rti", "punjab", "transparency", "information commission"],
    year=2013, related=["rti-federal-2017"]))

LAWS.append(law(
    "rti-kpk-2013", "Khyber Pakhtunkhwa Right to Information Act, 2013", "government", "kpk",
    L("The right-to-information law for Khyber Pakhtunkhwa public bodies, including how to request records and complain to the Information Commission.",
      "خیبر پختونخوا کے عوامی اداروں کے لیے حقِ معلومات کا قانون، بشمول ریکارڈ مانگنے اور انفارمیشن کمیشن میں شکایت کا طریقہ۔",
      "خيبر پختونخوا جي عوامي ادارن لاءِ ڄاڻ جي حق جو قانون، بشمول رڪارڊ گهرڻ ۽ انفارميشن ڪميشن ۾ شڪايت جو طريقو."),
    ["right to information", "rti", "khyber pakhtunkhwa", "kpk", "information commission"],
    year=2013, related=["rti-federal-2017"]))
