from common import *

LAWS = []

# ------------------------------------------------------------------ CIVIL
LAWS.append(law(
    "cpc-1908", "Code of Civil Procedure, 1908", "civil", "federal",
    L("The procedural law for civil cases (disputes about money, property, contracts and rights): how to file a suit, serve notice, get temporary orders such as injunctions, and enforce a decree. Provinces have made some local amendments.",
      "دیوانی مقدمات (رقم، جائیداد، معاہدوں اور حقوق کے تنازعات) کا طریقۂ کار: دعویٰ دائر کرنا، نوٹس کی تعمیل، حکمِ امتناعی جیسے عارضی احکامات حاصل کرنا، اور ڈگری پر عمل درآمد۔ صوبوں نے کچھ مقامی ترامیم کی ہیں۔",
      "ديواني ڪيسن (رقم، ملڪيت، معاهدن ۽ حقن جا تڪرار) جو طريقو: دعويٰ داخل ڪرڻ، نوٽيس جي تعميل، حڪمِ امتناعي جهڙا عارضي حڪم ڪرائڻ، ۽ ڊگريءَ تي عمل. صوبن ڪجهه مقامي ترميمون ڪيون آهن."),
    ["cpc", "civil procedure", "suit", "plaint", "injunction", "decree", "money recovery", "summary suit", "notice", "execution"],
    abbr="CPC", year=1908, featured=True, applies=NATIONWIDE, note=FED_NOTE,
    version="Amended many times, including provincial amendments. Check the official consolidated text for your province.",
    related=["contract-act-1872", "specific-relief-act-1877", "limitation-act-1908"],
    sections=[
        sec("cpc-9", "Section 9", "Courts to try all civil suits unless barred",
            "Civil courts can hear every civil dispute unless the law expressly or by clear implication takes it away from them. If you have a civil right and nobody else has been given the power to decide, the civil court is usually the place to go.",
            "دیوانی عدالتیں ہر دیوانی تنازع سن سکتی ہیں جب تک قانون صراحتاً یا واضح مفہوم کے ذریعے اسے ان سے الگ نہ کر دے۔ اگر آپ کا کوئی دیوانی حق ہے اور فیصلے کا اختیار کسی دوسرے ادارے کو نہیں دیا گیا تو عموماً دیوانی عدالت ہی جانے کی جگہ ہے۔",
            "ديواني عدالتون هر ديواني تڪرار ٻڌي سگهن ٿيون جيستائين قانون صاف صاف يا واضح مفهوم سان ان کي انهن کان ڌار نه ڪري. جيڪڏهن توهان جو ڪو ديواني حق آهي ۽ فيصلي جو اختيار ٻئي ڪنهن کي ڏنل ناهي ته عام طور ديواني عدالت ئي وڃڻ جي جڳهه آهي."),
        sec("cpc-80", "Section 80", "Notice before suing the Government or a public officer",
            "Before suing the Government or a public officer for something done in an official capacity, a written notice generally has to be given and a waiting period must pass, with limited exceptions. Check the current text for the waiting period and exceptions.",
            "حکومت یا کسی سرکاری افسر کے خلاف اس کے سرکاری حیثیت میں کیے گئے کام پر دعویٰ کرنے سے پہلے عموماً تحریری نوٹس دینا اور انتظار کی مدت گزارنا ضروری ہے، محدود استثنا کے ساتھ۔ انتظار کی مدت اور استثنا کے لیے موجودہ متن دیکھیں۔",
            "حڪومت يا ڪنهن سرڪاري آفيسر خلاف سندس سرڪاري حيثيت ۾ ڪيل ڪم تي دعويٰ ڪرڻ کان اڳ عام طور لکت وارو نوٽيس ڏيڻ ۽ انتظار جي مدت گذارڻ ضروري آهي، محدود استثنائن سان. انتظار جي مدت ۽ استثنائن لاءِ موجوده متن ڏسو.",
            terms=[("notice", ("A written warning telling the other side what you claim and that you may sue.", "تحریری اطلاع جو دوسرے فریق کو بتاتا ہے کہ آپ کیا دعویٰ کر رہے ہیں اور مقدمہ کر سکتے ہیں۔", "لکت وارو اطلاع جيڪو ٻئي ڌر کي ٻڌائي ٿو ته توهان ڇا دعويٰ ڪري رهيا آهيو ۽ ڪيس ڪري سگهو ٿا."))]),
        sec("cpc-o37", "Order XXXVII", "Summary procedure on negotiable instruments",
            "A faster “summary suit” route for recovering money based on certain documents such as cheques, bills of exchange and promissory notes. The defendant needs the court's permission to defend. Check the current text and your province's amendments.",
            "چیک، بل آف ایکسچینج اور پرامسری نوٹ جیسی بعض دستاویزات کی بنیاد پر رقم کی وصولی کا تیز تر “سمری سوٹ” راستہ۔ مدعا علیہ کو دفاع کے لیے عدالت کی اجازت درکار ہوتی ہے۔ موجودہ متن اور اپنے صوبے کی ترامیم دیکھیں۔",
            "چيڪ، بل آف ايڪسچينج ۽ پرامسري نوٽ جهڙين ڪجهه دستاويزن جي بنياد تي رقم جي وصوليءَ جو تڪڙو “سمري سوٽ” رستو. مدعا عليه کي دفاع لاءِ عدالت جي اجازت گهرجي. موجوده متن ۽ پنهنجي صوبي جون ترميمون ڏسو.",
            terms=[("summary suit", ("A shortened court process for clear money claims on specified documents.", "مخصوص دستاویزات پر واضح رقم کے دعووں کے لیے مختصر عدالتی عمل۔", "مخصوص دستاويزن تي واضح رقم جي دعوائن لاءِ مختصر عدالتي عمل."))],
            gl=["summons"]),
        sec("cpc-o39", "Order XXXIX, Rules 1 and 2", "Temporary injunctions",
            "Lets a court order someone to stop (or sometimes do) something while the main case is pending — for example, to stop a person from selling or building on disputed property. The applicant usually has to show a prima facie case, that harm would be hard to undo, and that the balance of convenience favours them.",
            "مقدمہ زیرِ سماعت ہونے کے دوران عدالت کسی کو کوئی کام روکنے (یا بعض اوقات کرنے) کا حکم دے سکتی ہے — مثلاً متنازع جائیداد بیچنے یا اس پر تعمیر سے روکنا۔ درخواست گزار کو عموماً ظاہری طور پر مضبوط مقدمہ، ناقابلِ تلافی نقصان کا خدشہ اور سہولت کا توازن اپنے حق میں ثابت کرنا ہوتا ہے۔",
            "ڪيس هلندي عدالت ڪنهن کي ڪو ڪم روڪڻ (يا ڪڏهن ڪرڻ) جو حڪم ڏئي سگهي ٿي — مثال طور تڪراري ملڪيت وڪڻڻ يا ان تي اڏاوت ڪرڻ کان روڪڻ. درخواست ڏيندڙ کي عام طور ظاهري طور مضبوط ڪيس، ناقابلِ تلافي نقصان جو انديشو ۽ سهوليت جو توازن پنهنجي حق ۾ ثابت ڪرڻو پوي ٿو.",
            terms=[("injunction", ("A court order to do or not do something.", "کوئی کام کرنے یا نہ کرنے کا عدالتی حکم۔", "ڪو ڪم ڪرڻ يا نه ڪرڻ جو عدالتي حڪم.")),
                   ("prima facie", ("“At first sight”: enough evidence to support the claim unless disproved.", "“پہلی نظر میں”: دعوے کی حمایت کے لیے کافی شواہد جب تک رد نہ ہوں۔", "“پهرين نظر ۾”: دعوائي جي حمايت لاءِ ڪافي ثبوت جيستائين رد نه ٿين."))],
            gl=["injunction"]),
    ]))

LAWS.append(law(
    "contract-act-1872", "Contract Act, 1872", "civil", "federal",
    L("Explains when a promise or agreement becomes a legally enforceable contract, what makes it valid or void, and what remedies (such as compensation) are available for breach.",
      "بتاتا ہے کہ وعدہ یا معاہدہ کب قانونی طور پر قابلِ نفاذ معاہدہ بنتا ہے، کیا چیز اسے درست یا کالعدم بناتی ہے، اور خلاف ورزی پر کون سے علاج (جیسے ہرجانہ) دستیاب ہیں۔",
      "وضاحت ڪري ٿو ته واعدو يا معاهدو ڪڏهن قانوني طور لاڳو ٿيڻ جوڳو معاهدو بڻجي ٿو، ڪهڙي شيءِ ان کي صحيح يا باطل بڻائي ٿي، ۽ ڀڃڪڙيءَ تي ڪهڙا علاج (جهڙوڪ معاوضو) دستياب آهن."),
    ["contract", "agreement", "breach", "compensation", "consideration", "offer", "acceptance", "damages"],
    year=1872, applies=NATIONWIDE, note=FED_NOTE, related=["cpc-1908", "specific-relief-act-1877"],
    sections=[
        sec("ca-10", "Section 10", "What agreements are contracts",
            "Agreements are contracts when the parties are competent to contract, freely consent, have a lawful object and lawful consideration (something of value exchanged), and are not expressly declared void. Some contracts must also be in writing or registered.",
            "معاہدے اس وقت قانونی معاہدے بنتے ہیں جب فریقین معاہدہ کرنے کے اہل ہوں، آزادانہ رضامندی دیں، مقصد اور عوض (تبادلے میں دی گئی قیمتی چیز) قانونی ہو، اور اسے صراحتاً کالعدم قرار نہ دیا گیا ہو۔ بعض معاہدوں کا تحریری یا رجسٹرڈ ہونا بھی ضروری ہے۔",
            "معاهدا تڏهن قانوني معاهدا بڻجن ٿا جڏهن ڌريون معاهدو ڪرڻ جوڳيون هجن، آزاديءَ سان رضامندي ڏين، مقصد ۽ عوض (بدلي ۾ ڏنل قيمتي شيءِ) قانوني هجي، ۽ ان کي صاف طور باطل قرار نه ڏنو ويو هجي. ڪجهه معاهدن جو لکت ۾ يا رجسٽرڊ هجڻ به ضروري آهي.",
            terms=[("consideration", ("Something of value each side gives or promises, such as money, goods or a promise to act.", "ہر فریق کی طرف سے دی گئی یا وعدہ کی گئی قیمتی چیز، جیسے رقم، سامان یا کام کا وعدہ۔", "هر ڌر طرفان ڏنل يا واعدو ڪيل قيمتي شيءِ، جهڙوڪ رقم، سامان يا ڪم جو واعدو."))],
            gl=["contract"]),
        sec("ca-73", "Section 73", "Compensation for loss or damage caused by breach of contract",
            "If one party breaks a contract, the other can claim compensation for the loss that naturally arose from the breach (or that both sides knew was likely). It does not cover remote or indirect losses.",
            "اگر ایک فریق معاہدہ توڑے تو دوسرا اس نقصان کے ہرجانے کا دعویٰ کر سکتا ہے جو خلاف ورزی سے فطری طور پر پیدا ہوا (یا جس کا دونوں کو امکان معلوم تھا)۔ دور کے یا بالواسطہ نقصانات اس میں شامل نہیں۔",
            "جيڪڏهن هڪ ڌر معاهدو ڀڃي ته ٻي ڌر ان نقصان جي معاوضي جو دعويٰ ڪري سگهي ٿي جيڪو ڀڃڪڙيءَ مان فطري طور پيدا ٿيو (يا جنهن جو ٻنهي کي امڪان معلوم هو). پري جا يا اڻسڌا نقصان ان ۾ شامل ناهن.",
            gl=["contract"]),
    ]))

LAWS.append(law(
    "specific-relief-act-1877", "Specific Relief Act, 1877", "civil", "federal",
    L("Allows courts to declare rights and to order a person to do (specific performance) or stop doing (injunction) something, instead of only awarding money. Used in many property and contract disputes.",
      "عدالتوں کو حقوق کا اعلان کرنے اور کسی کو کوئی کام کرنے (مخصوص عمل درآمد) یا روکنے (حکمِ امتناعی) کا حکم دینے کی اجازت دیتا ہے، محض رقم دلوانے کے بجائے۔ جائیداد اور معاہدوں کے کئی تنازعات میں استعمال ہوتا ہے۔",
      "عدالتن کي حقن جو اعلان ڪرڻ ۽ ڪنهن کي ڪو ڪم ڪرڻ (مخصوص عمل درآمد) يا روڪڻ (حڪمِ امتناعي) جو حڪم ڏيڻ جي اجازت ڏئي ٿو، رڳو پئسا ڏياريندڙ ٿيڻ بدران. ملڪيت ۽ معاهدن جي ڪيترن تڪرارن ۾ استعمال ٿئي ٿو."),
    ["specific performance", "injunction", "declaration", "declaratory suit", "decree", "property dispute"],
    year=1877, applies=NATIONWIDE, note=FED_NOTE, related=["cpc-1908", "contract-act-1872"],
    sections=[
        sec("sra-42", "Section 42", "Discretion of court as to declaration of status or right",
            "A person with a legal right or character who is denied it can ask the court for a declaration (a formal statement) of that right — for example, a declaration of ownership. The court has discretion and will not grant it if a further relief could have been asked but wasn't.",
            "جس شخص کا کوئی قانونی حق یا حیثیت ہو اور اس سے انکار کیا جائے تو وہ عدالت سے اس حق کا اعلان (رسمی بیان) مانگ سکتا ہے — مثلاً ملکیت کا اعلان۔ عدالت کو صوابدید حاصل ہے اور اگر مزید ریلیف مانگا جا سکتا تھا مگر نہیں مانگا گیا تو وہ اعلان نہیں دے گی۔",
            "جنهن شخص جو ڪو قانوني حق يا حيثيت هجي ۽ ان کان انڪار ڪيو وڃي ته هو عدالت کان ان حق جو اعلان (رسمي بيان) گهري سگهي ٿو — مثال طور ملڪيت جو اعلان. عدالت کي صوابديد آهي ۽ جيڪڏهن وڌيڪ رليف گهري سگهجي ٿي پر نه گهري وئي هجي ته اها اعلان نه ڏيندي."),
        sec("sra-54", "Section 54", "Perpetual injunctions when granted",
            "After a full hearing, a court can permanently forbid someone from violating your legal right (for example from interfering with your possession of property). It differs from a temporary injunction, which lasts only while the case is pending.",
            "مکمل سماعت کے بعد عدالت کسی کو آپ کے قانونی حق کی خلاف ورزی (مثلاً جائیداد پر آپ کے قبضے میں مداخلت) سے ہمیشہ کے لیے روک سکتی ہے۔ یہ عارضی حکمِ امتناعی سے مختلف ہے جو صرف مقدمے کے دوران رہتا ہے۔",
            "مڪمل ٻڌڻيءَ کانپوءِ عدالت ڪنهن کي توهان جي قانوني حق جي ڀڃڪڙي (مثال طور ملڪيت تي توهان جي قبضي ۾ مداخلت) کان هميشه لاءِ روڪي سگهي ٿي. هي عارضي حڪمِ امتناعي کان مختلف آهي جيڪو رڳو ڪيس هلڻ دوران رهي ٿو.",
            gl=["injunction"]),
    ]))

LAWS.append(law(
    "limitation-act-1908", "Limitation Act, 1908", "civil", "federal",
    L("Sets the time limits within which a suit, appeal or application must be filed. Missing a deadline can end a claim, so check the limit that applies to your type of case as early as possible.",
      "دعویٰ، اپیل یا درخواست دائر کرنے کی مقررہ مدتیں طے کرتا ہے۔ مدت گزر جانے سے دعویٰ ختم ہو سکتا ہے، اس لیے اپنی نوعیت کے مقدمے کی مدت جلد از جلد معلوم کریں۔",
      "دعويٰ، اپيل يا درخواست داخل ڪرڻ جون مقرر مدتون طئه ڪري ٿو. مدت گذري وڃڻ سان دعويٰ ختم ٿي سگهي ٿو، تنهن ڪري پنهنجي قسم جي ڪيس جي مدت جلد کان جلد معلوم ڪريو."),
    ["limitation", "time limit", "deadline", "time barred", "appeal period"],
    year=1908, applies=NATIONWIDE, note=FED_NOTE, related=["cpc-1908"]))

# ------------------------------------------------------------------ PROPERTY
LAWS.append(law(
    "tpa-1882", "Transfer of Property Act, 1882", "property", "federal",
    L("Governs how immovable property (land, houses) is transferred: sale, mortgage, lease, gift and exchange. It defines these transactions and says when documents must be written and registered.",
      "غیر منقولہ جائیداد (زمین، مکان) کی منتقلی کا طریقہ: فروخت، رہن، پٹہ، ہبہ اور تبادلہ۔ یہ ان معاملات کی تعریف کرتا ہے اور بتاتا ہے کہ دستاویز کب تحریری اور رجسٹرڈ ہونا ضروری ہے۔",
      "غير منقول ملڪيت (زمين، گهر) جي منتقليءَ جو طريقو: وڪرو، رهن، ليز، تحفو ۽ بدلو. هي انهن معاملن جي وصف ڪري ٿو ۽ ٻڌائي ٿو ته دستاويز ڪڏهن لکت ۾ ۽ رجسٽرڊ هجڻ ضروري آهي."),
    ["property", "sale", "lease", "mortgage", "gift", "transfer", "immovable", "land", "house", "title"],
    abbr="TPA", year=1882, applies=NATIONWIDE, note=FED_NOTE,
    related=["registration-act-1908", "sindh-rented-premises-1979", "punjab-rented-premises-2009"],
    sections=[
        sec("tpa-54", "Section 54", "“Sale” defined",
            "A sale transfers ownership of property for a price. For property of higher value, the transfer is made only by a registered instrument; for very low-value property, delivery of possession may be enough. Check the current monetary limits and your province's registration rules.",
            "فروخت قیمت کے عوض جائیداد کی ملکیت کی منتقلی ہے۔ زیادہ مالیت کی جائیداد کی منتقلی صرف رجسٹرڈ دستاویز کے ذریعے ہوتی ہے؛ بہت کم مالیت میں قبضہ دینا کافی ہو سکتا ہے۔ موجودہ مالی حدود اور اپنے صوبے کے رجسٹریشن قواعد دیکھیں۔",
            "وڪرو قيمت جي عوض ملڪيت جي مالڪيءَ جي منتقلي آهي. وڌيڪ قيمت واري ملڪيت جي منتقلي رڳو رجسٽرڊ دستاويز ذريعي ٿئي ٿي؛ تمام گهٽ قيمت ۾ قبضو ڏيڻ ڪافي ٿي سگهي ٿو. موجوده مالي حدون ۽ پنهنجي صوبي جا رجسٽريشن قاعدا ڏسو.",
            terms=[("registered instrument", ("A written document officially recorded with the Sub-Registrar.", "تحریری دستاویز جو سب رجسٹرار کے پاس سرکاری طور پر درج ہو۔", "لکت وارو دستاويز جيڪو سب رجسٽرار وٽ سرڪاري طور درج ٿيل هجي."))]),
        sec("tpa-105", "Section 105", "Lease defined",
            "A lease transfers the right to enjoy property for a time in return for rent or another price. The giver is the lessor (landlord) and the taker is the lessee (tenant). Rented-premises laws of each province add specific tenant and landlord rules.",
            "پٹہ کسی مدت کے لیے کرائے یا کسی اور قیمت کے عوض جائیداد سے فائدہ اٹھانے کا حق منتقل کرتا ہے۔ دینے والا لیسر (مالک مکان) اور لینے والا لیسی (کرایہ دار) ہے۔ ہر صوبے کے کرایہ دارانہ قوانین مخصوص قواعد شامل کرتے ہیں۔",
            "ليز ڪنهن مدت لاءِ ڪرائي يا ٻي قيمت جي عوض ملڪيت مان فائدو وٺڻ جو حق منتقل ڪري ٿي. ڏيندڙ ليسر (مالڪ مڪان) ۽ وٺندڙ ليسي (ڪرائيدار) آهي. هر صوبي جا ڪرائي دارن جا قانون مخصوص قاعدا شامل ڪن ٿا.",
            terms=[("lessor", ("The owner/landlord who gives the lease.", "پٹہ دینے والا مالک/مالک مکان۔", "ليز ڏيندڙ مالڪ/مالڪ مڪان.")), ("lessee", ("The tenant who takes the lease.", "پٹہ لینے والا کرایہ دار۔", "ليز وٺندڙ ڪرائيدار."))]),
        sec("tpa-107", "Section 107", "Leases how made",
            "A lease of immovable property for more than one year must be made by a registered instrument; shorter leases can be made by a registered instrument or by delivery of possession. A written, registered tenancy agreement is safer for both sides.",
            "ایک سال سے زیادہ مدت کا غیر منقولہ جائیداد کا پٹہ رجسٹرڈ دستاویز سے ہونا ضروری ہے؛ کم مدت کے پٹے رجسٹرڈ دستاویز یا قبضہ دینے سے ہو سکتے ہیں۔ تحریری اور رجسٹرڈ کرایہ نامہ دونوں فریقوں کے لیے زیادہ محفوظ ہے۔",
            "هڪ سال کان وڌيڪ مدت جي غير منقول ملڪيت جي ليز رجسٽرڊ دستاويز سان ٿيڻ ضروري آهي؛ گهٽ مدت جون ليزون رجسٽرڊ دستاويز يا قبضو ڏيڻ سان ٿي سگهن ٿيون. لکت ۾ ۽ رجسٽرڊ ڪرائي نامو ٻنهي ڌرين لاءِ وڌيڪ محفوظ آهي.",
            gl=["tenant"]),
    ]))

LAWS.append(law(
    "registration-act-1908", "Registration Act, 1908", "property", "federal",
    L("Explains which documents must be registered (such as many sale deeds and long leases), where and when to register them, and why registration protects your title.",
      "بتاتا ہے کہ کون سی دستاویزات کا رجسٹرڈ ہونا لازم ہے (جیسے بہت سے بیع نامے اور طویل پٹے)، رجسٹریشن کہاں اور کب کرانی ہے، اور رجسٹریشن آپ کے حق کو کیسے تحفظ دیتی ہے۔",
      "ٻڌائي ٿو ته ڪهڙن دستاويزن جو رجسٽرڊ ٿيڻ ضروري آهي (جهڙوڪ ڪيترائي وڪري نامي ۽ ڊگهيون ليزون)، رجسٽريشن ڪٿي ۽ ڪڏهن ڪرائڻي آهي، ۽ رجسٽريشن توهان جي حق کي ڪيئن تحفظ ڏئي ٿي."),
    ["registration", "sub-registrar", "sale deed", "title", "stamp duty", "registered document"],
    year=1908, applies=NATIONWIDE, note=FED_NOTE, related=["tpa-1882"],
    sections=[
        sec("ra-17", "Section 17", "Documents of which registration is compulsory",
            "Lists documents that must be registered to be effective — for example, instruments that create or transfer rights in immovable property above a stated value, and leases for more than one year. An unregistered document of this kind may not be accepted as proof of the transaction.",
            "ان دستاویزات کی فہرست دیتی ہے جن کا مؤثر ہونے کے لیے رجسٹرڈ ہونا لازم ہے — مثلاً مقررہ مالیت سے زیادہ غیر منقولہ جائیداد میں حقوق پیدا یا منتقل کرنے والی دستاویزات، اور ایک سال سے زائد پٹے۔ اس نوعیت کی غیر رجسٹرڈ دستاویز لین دین کے ثبوت کے طور پر قبول نہیں ہو سکتی۔",
            "انهن دستاويزن جي لسٽ ڏئي ٿو جن جو اثرائتو ٿيڻ لاءِ رجسٽرڊ ٿيڻ ضروري آهي — مثال طور مقرر قيمت کان وڌيڪ غير منقول ملڪيت ۾ حق پيدا يا منتقل ڪندڙ دستاويز، ۽ هڪ سال کان وڌيڪ ليزون. هن قسم جو غير رجسٽرڊ دستاويز ٻٽاڪي جي ثبوت طور قبول نه ٿي سگهي.")]))

LAWS.append(law(
    "sindh-rented-premises-1979", "Sindh Rented Premises Ordinance, 1979", "property", "sindh",
    L("The main tenancy law in Sindh: fair rent, tenant and landlord duties, the grounds on which a landlord can seek eviction, and the Rent Controller who decides such disputes.",
      "سندھ میں کرایہ داری کا بنیادی قانون: مناسب کرایہ، کرایہ دار اور مالک مکان کے فرائض، بے دخلی کے وہ جواز جن پر مالک مکان درخواست دے سکتا ہے، اور رینٹ کنٹرولر جو ایسے تنازعات کا فیصلہ کرتا ہے۔",
      "سنڌ ۾ ڪرائي داريءَ جو بنيادي قانون: مناسب ڪرايو، ڪرائيدار ۽ مالڪ مڪان جا فرض، بي دخلي جا اهي سبب جن تي مالڪ مڪان درخواست ڏئي سگهي ٿو، ۽ رينٽ ڪنٽرولر جيڪو اهڙن تڪرارن جو فيصلو ڪري ٿو."),
    ["tenant", "landlord", "rent", "eviction", "rent controller", "sindh", "ejectment", "fair rent", "tenancy"],
    abbr="SRPO", year=1979, featured=True,
    note=L("Applies to rented premises in Sindh as understood here; confirm the current text and any amendments.", "یہاں سندھ میں کرائے کی عمارتوں پر لاگو سمجھا گیا ہے؛ موجودہ متن اور ترامیم کی تصدیق کریں۔", "هتي سنڌ ۾ ڪرائي تي ڏنل عمارتن تي لاڳو سمجهيو ويو آهي؛ موجوده متن ۽ ترميمن جي تصديق ڪريو."),
    related=["tpa-1882", "registration-act-1908"]))

LAWS.append(law(
    "punjab-rented-premises-2009", "Punjab Rented Premises Act, 2009", "property", "punjab",
    L("The tenancy law in Punjab. It covers tenancy agreements, rent, eviction and the Rent Tribunal. Check the current text for registration of tenancy agreements and eviction procedure.",
      "پنجاب میں کرایہ داری کا قانون۔ اس میں کرایہ نامے، کرایہ، بے دخلی اور رینٹ ٹربیونل شامل ہیں۔ کرایہ ناموں کی رجسٹریشن اور بے دخلی کے طریقۂ کار کے لیے موجودہ متن دیکھیں۔",
      "پنجاب ۾ ڪرائي داريءَ جو قانون. ان ۾ ڪرائي نامو، ڪرايو، بي دخلي ۽ رينٽ ٽربيونل شامل آهن. ڪرائي نامن جي رجسٽريشن ۽ بي دخليءَ جي طريقي لاءِ موجوده متن ڏسو."),
    ["tenant", "landlord", "rent", "eviction", "punjab", "tribunal", "tenancy agreement"],
    year=2009, related=["tpa-1882"]))

LAWS.append(law(
    "ict-rent-restriction-2001", "Islamabad Rent Restriction Ordinance, 2001", "property", "ict",
    L("The tenancy law for Islamabad Capital Territory covering rent, eviction and the Rent Controller.",
      "اسلام آباد وفاقی دارالحکومت کے لیے کرایہ داری کا قانون جس میں کرایہ، بے دخلی اور رینٹ کنٹرولر شامل ہیں۔",
      "اسلام آباد وفاقي دارالحڪومت لاءِ ڪرائي داريءَ جو قانون جنهن ۾ ڪرايو، بي دخلي ۽ رينٽ ڪنٽرولر شامل آهن."),
    ["tenant", "landlord", "rent", "eviction", "islamabad", "ict", "rent controller"],
    year=2001, related=["tpa-1882"]))

# ------------------------------------------------------------------ FAMILY
LAWS.append(law(
    "mflo-1961", "Muslim Family Laws Ordinance, 1961", "family", "federal",
    L("Regulates several matters for Muslims: registration of marriage, notice and procedure for talaq, restrictions on a second marriage, maintenance, and the share of grandchildren whose parent died before the grandparent. It applies to Muslim citizens; other communities have their own personal laws.",
      "مسلمانوں کے کئی معاملات کو منضبط کرتا ہے: نکاح کا اندراج، طلاق کا نوٹس اور طریقہ، دوسری شادی پر پابندیاں، نان نفقہ، اور ان پوتے/نواسوں کا حصہ جن کے والدین دادا/نانا سے پہلے فوت ہو گئے ہوں۔ یہ مسلمان شہریوں پر لاگو ہے؛ دیگر برادریوں کے اپنے شخصی قوانین ہیں۔",
      "مسلمانن جي ڪيترن معاملن کي منظم ڪري ٿو: نڪاح جو اندراج، طلاق جو نوٽيس ۽ طريقو، ٻي شاديءَ تي پابنديون، نان نفقو، ۽ انهن پوٽن/ڏوهٽن جو حصو جن جا والدين ڏاڏي/ناني کان اڳ گذاري ويا هجن. هي مسلمان شهرين تي لاڳو آهي؛ ٻين برادرين جا پنهنجا ذاتي قانون آهن."),
    ["marriage", "nikah", "registration", "talaq", "divorce", "polygamy", "maintenance", "inheritance", "succession", "arbitration council", "union council", "muslim"],
    abbr="MFLO", year=1961, featured=True, applies=NATIONWIDE,
    note=L("Applies to Muslims. Federal law understood to apply in the provinces and Islamabad; confirm applicability in Gilgit-Baltistan and Azad Jammu & Kashmir.",
           "مسلمانوں پر لاگو۔ وفاقی قانون جو صوبوں اور اسلام آباد میں لاگو سمجھا جاتا ہے؛ گلگت بلتستان اور آزاد جموں و کشمیر میں اطلاق کی تصدیق کریں۔",
           "مسلمانن تي لاڳو. وفاقي قانون جيڪو صوبن ۽ اسلام آباد ۾ لاڳو سمجهيو وڃي ٿو؛ گلگت-بلتستان ۽ آزاد جمون ۽ ڪشمير ۾ لاڳو ٿيڻ جي تصديق ڪريو."),
    related=["dissolution-muslim-marriages-1939", "family-courts-act-1964", "guardians-wards-1890", "dowry-bridal-gifts-1976"],
    sections=[
        sec("mflo-4", "Section 4", "Succession",
            "If a son or daughter dies before their parent, that person's children (the grandchildren) are treated as inheriting the share their parent would have received from the grandparent. Read the full section for the conditions.",
            "اگر بیٹا یا بیٹی اپنے والد/والدہ سے پہلے فوت ہو جائے تو اس کی اولاد (پوتے/نواسے) کو وہ حصہ ملتا ہے جو اس کے والد/والدہ کو دادا/نانا کی جائیداد سے ملتا۔ شرائط کے لیے پوری دفعہ پڑھیں۔",
            "جيڪڏهن پٽ يا ڌيءَ پنهنجي والد/والدہ کان اڳ گذاري وڃي ته ان جي اولاد (پوٽن/ڏوهٽن) کي اهو حصو ملي ٿو جيڪو سندن والد/والدہ کي ڏاڏي/ناني جي ملڪيت مان ملي ها. شرطن لاءِ پورو دفعو پڙهو.",
            gl=["inheritance"]),
        sec("mflo-5", "Section 5", "Registration of marriages",
            "A Muslim marriage should be registered with the Union Council (or the relevant local authority). The Nikah Registrar who solemnises the marriage must record it in the prescribed form and give a copy to the parties. A registered nikahnama is key proof of marriage, dower and conditions.",
            "مسلمان نکاح یونین کونسل (یا متعلقہ مقامی ادارے) میں رجسٹرڈ ہونا چاہیے۔ نکاح پڑھانے والے نکاح رجسٹرار کو مقررہ فارم میں اندراج کرنا اور فریقین کو نقل دینا ہوتی ہے۔ رجسٹرڈ نکاح نامہ نکاح، حق مہر اور شرائط کا بنیادی ثبوت ہے۔",
            "مسلمان نڪاح يونين ڪائونسل (يا لاڳاپيل مقامي اداري) ۾ رجسٽرڊ ٿيڻ گهرجي. نڪاح پڙهائيندڙ نڪاح رجسٽرار کي مقرر فارم ۾ اندراج ڪرڻو ۽ ڌرين کي ڪاپي ڏيڻي پوي ٿي. رجسٽرڊ نڪاح نامو نڪاح، حق مهر ۽ شرطن جو بنيادي ثبوت آهي.",
            terms=[("nikahnama", ("The marriage contract/certificate recording the nikah, dower and any conditions.", "نکاح، حق مہر اور شرائط کو درج کرنے والا نکاح نامہ/سرٹیفکیٹ۔", "نڪاح، حق مهر ۽ شرطن کي درج ڪندڙ نڪاح نامو/سرٽيفڪيٽ."))],
            gl=["dower", "nikah"]),
        sec("mflo-6", "Section 6", "Polygamy",
            "A man who already has a wife must not contract another marriage without first applying for written permission from the Arbitration Council and the application must state whether the existing wife's consent has been obtained. Marrying without permission has legal consequences. Check the current text.",
            "جس مرد کی پہلے سے بیوی ہو وہ آربٹریشن کونسل سے تحریری اجازت کے لیے درخواست دیے بغیر دوسری شادی نہیں کر سکتا، اور درخواست میں بتانا ہوتا ہے کہ موجودہ بیوی کی رضامندی لی گئی ہے یا نہیں۔ اجازت کے بغیر شادی کے قانونی نتائج ہیں۔ موجودہ متن دیکھیں۔",
            "جنهن مرد جي اڳ ۾ زال هجي اهو آربيٽريشن ڪائونسل کان لکت وارين اجازت لاءِ درخواست ڏيڻ کانسواءِ ٻي شادي نٿو ڪري سگهي، ۽ درخواست ۾ ٻڌائڻو پوي ٿو ته موجوده زال جي رضامندي ورتل آهي يا نه. اجازت کانسواءِ شاديءَ جا قانوني نتيجا آهن. موجوده متن ڏسو."),
        sec("mflo-7", "Section 7", "Talaq",
            "A man who pronounces talaq must give written notice to the Chairman of the Union Council and supply a copy to his wife. The Council then tries reconciliation, and under this section the talaq generally takes effect after a waiting period (ninety days from the notice, unless the wife is pregnant, in which case the rules differ). Read the exact text.",
            "جو مرد طلاق دے اسے یونین کونسل کے چیئرمین کو تحریری نوٹس دینا اور اس کی نقل بیوی کو دینا ہوتی ہے۔ کونسل مصالحت کی کوشش کرتی ہے اور اس دفعہ کے تحت طلاق عموماً انتظار کی مدت (نوٹس سے نوے دن، سوائے حمل کی صورت کے جہاں قواعد مختلف ہیں) کے بعد مؤثر ہوتی ہے۔ عین الفاظ پڑھیں۔",
            "جيڪو مرد طلاق ڏئي ان کي يونين ڪائونسل جي چيئرمين کي لکت وارو نوٽيس ڏيڻو ۽ ان جي ڪاپي زال کي ڏيڻي پوي ٿي. ڪائونسل صلح جي ڪوشش ڪري ٿي ۽ هن دفعي تحت طلاق عام طور انتظار جي مدت (نوٽيس کان نوي ڏينهن، سواءِ حمل جي حالت جي جتي قاعدا مختلف آهن) کانپوءِ اثرائتي ٿئي ٿي. صحيح لفظ پڙهو.",
            terms=[("Arbitration Council", ("A local body led by the Union Council chairman that tries to reconcile a couple.", "مقامی ادارہ جس کی سربراہی یونین کونسل کا چیئرمین کرتا ہے اور جو جوڑے میں صلح کی کوشش کرتا ہے۔", "مقامي اداره جنهن جي سربراهي يونين ڪائونسل جو چيئرمين ڪري ٿو ۽ جيڪو جوڙي ۾ صلح جي ڪوشش ڪري ٿو."))],
            cond=("Failure to give notice can be an offence. A woman seeking to end a marriage has other routes (see the Dissolution of Muslim Marriages Act, 1939 and the Family Courts Act, 1964).", "نوٹس نہ دینا جرم ہو سکتا ہے۔ جو عورت نکاح ختم کرانا چاہے اس کے پاس دیگر راستے ہیں (دیکھیں تنسیخِ نکاحِ مسلمانان ایکٹ 1939 اور فیملی کورٹس ایکٹ 1964)۔", "نوٽيس نه ڏيڻ ڏوهه ٿي سگهي ٿو. جيڪا عورت نڪاح ختم ڪرائڻ چاهي ان وٽ ٻيا رستا آهن (ڏسو ڊزولوشن آف مسلم ميريجز ايڪٽ 1939 ۽ فئملي ڪورٽس ايڪٽ 1964)."),
            gl=["divorce"]),
        sec("mflo-9", "Section 9", "Maintenance",
            "If a husband fails to maintain his wife (or fails to treat co-wives equitably), the wife can apply to the Chairman of the Union Council, which can decide on maintenance. Many maintenance claims are also brought in the Family Court. Read the current text.",
            "اگر شوہر اپنی بیوی کا نان نفقہ ادا نہ کرے (یا ایک سے زیادہ بیویوں میں انصاف نہ کرے) تو بیوی یونین کونسل کے چیئرمین کو درخواست دے سکتی ہے جو نان نفقہ پر فیصلہ کر سکتا ہے۔ نان نفقہ کے کئی دعوے فیملی کورٹ میں بھی کیے جاتے ہیں۔ موجودہ متن دیکھیں۔",
            "جيڪڏهن مڙس پنهنجي زال جو نان نفقو نه ڏئي (يا هڪ کان وڌيڪ زالن ۾ انصاف نه ڪري) ته زال يونين ڪائونسل جي چيئرمين کي درخواست ڏئي سگهي ٿي جيڪو نان نفقي تي فيصلو ڪري سگهي ٿو. نان نفقي جا ڪيترائي دعوائون فئملي ڪورٽ ۾ به ڪيون وڃن ٿيون. موجوده متن ڏسو.",
            gl=["maintenance"]),
    ]))

LAWS.append(law(
    "dissolution-muslim-marriages-1939", "Dissolution of Muslim Marriages Act, 1939", "family", "federal",
    L("Lists the grounds on which a Muslim woman can ask a court to dissolve her marriage (for example, if the husband's whereabouts are unknown, he fails to maintain her, or treats her with cruelty). It works alongside the right to khula and the Family Courts Act, 1964.",
      "ان بنیادوں کی فہرست دیتا ہے جن پر مسلمان عورت عدالت سے نکاح ختم کرنے کی درخواست کر سکتی ہے (مثلاً شوہر کا پتہ نہ ہونا، نان نفقہ نہ دینا یا ظلم کرنا)۔ یہ خلع کے حق اور فیملی کورٹس ایکٹ 1964 کے ساتھ مل کر کام کرتا ہے۔",
      "انهن بنيادن جي لسٽ ڏئي ٿو جن تي مسلمان عورت عدالت کان نڪاح ختم ڪرڻ جي درخواست ڪري سگهي ٿي (مثال طور مڙس جو پتو نه هئڻ، نان نفقو نه ڏيڻ يا ظلم ڪرڻ). هي خلع جي حق ۽ فئملي ڪورٽس ايڪٽ 1964 سان گڏجي ڪم ڪري ٿو."),
    ["divorce", "dissolution", "khula", "cruelty", "maintenance", "tanseekh", "muslim woman", "marriage"],
    year=1939, applies=NATIONWIDE, note=FED_NOTE, related=["mflo-1961", "family-courts-act-1964"],
    sections=[
        sec("dmma-2", "Section 2", "Grounds for decree for dissolution of marriage",
            "A woman married under Muslim law can seek a decree dissolving her marriage on specific grounds, such as the husband being missing for a period, failing to provide maintenance, imprisonment for a long term, failing to perform marital obligations, cruelty, and certain other grounds listed in the section. Read the exact list and time periods in the official text.",
            "مسلمان قانون کے تحت نکاح کرنے والی عورت مخصوص بنیادوں پر نکاح کی تنسیخ کی ڈگری مانگ سکتی ہے، مثلاً شوہر کا ایک مدت تک لاپتہ ہونا، نان نفقہ ادا نہ کرنا، طویل قید، ازدواجی ذمہ داریاں ادا نہ کرنا، ظلم، اور دفعہ میں درج دیگر بنیادیں۔ درست فہرست اور مدتیں سرکاری متن میں پڑھیں۔",
            "مسلمان قانون تحت نڪاح ڪندڙ عورت مخصوص بنيادن تي نڪاح جي تنسيخ جي ڊگري گهري سگهي ٿي، مثال طور مڙس جو هڪ مدت تائين لاپتا هئڻ، نان نفقو نه ڏيڻ، ڊگهي قيد، ازدواجي ذميواريون ادا نه ڪرڻ، ظلم، ۽ دفعي ۾ ڏنل ٻيا بنياد. صحيح لسٽ ۽ مدتون سرڪاري متن ۾ پڙهو.",
            terms=[("dissolution of marriage", ("A court decree ending a marriage.", "عدالتی ڈگری جو نکاح ختم کرتی ہے۔", "عدالتي ڊگري جيڪا نڪاح ختم ڪري ٿي."))],
            gl=["divorce", "khula"])]))

LAWS.append(law(
    "family-courts-act-1964", "West Pakistan Family Courts Act, 1964", "family", "federal",
    L("Creates Family Courts that hear marriage, dissolution (including khula), dower, maintenance, custody of children and related disputes. It requires the court to attempt reconciliation and aims at quicker, simpler procedure than ordinary civil courts.",
      "فیملی کورٹس قائم کرتا ہے جو نکاح، تنسیخ (بشمول خلع)، حق مہر، نان نفقہ، بچوں کی تحویل اور متعلقہ تنازعات سنتی ہیں۔ عدالت پر مصالحت کی کوشش لازم ہے اور عام دیوانی عدالتوں کے مقابلے میں تیز اور سادہ طریقۂ کار کا ہدف ہے۔",
      "فئملي ڪورٽون قائم ڪري ٿو جيڪي نڪاح، تنسيخ (بشمول خلع)، حق مهر، نان نفقي، ٻارن جي سنڀال ۽ لاڳاپيل تڪرارن کي ٻڌن ٿيون. عدالت تي صلح جي ڪوشش لازمي آهي ۽ عام ديواني عدالتن جي ڀيٽ ۾ تڪڙي ۽ سادي طريقي جو مقصد آهي."),
    ["family court", "khula", "dower", "mehr", "maintenance", "custody", "guardianship", "reconciliation", "divorce", "dissolution"],
    year=1964, featured=True, applies=NATIONWIDE, note=FED_NOTE,
    related=["mflo-1961", "dissolution-muslim-marriages-1939", "guardians-wards-1890", "dowry-bridal-gifts-1976"],
    sections=[
        sec("fca-5", "Section 5 and the Schedule", "Jurisdiction",
            "Family Courts have exclusive jurisdiction over the matters listed in the Schedule to the Act, such as dissolution of marriage (including khula), dower, maintenance, restitution of conjugal rights, custody and guardianship of children, and the return of dowry or bridal gifts. Check the current Schedule.",
            "فیملی کورٹس کو ایکٹ کے شیڈول میں درج معاملات پر خصوصی اختیارِ سماعت حاصل ہے، جیسے تنسیخِ نکاح (بشمول خلع)، حق مہر، نان نفقہ، رجوعِ ازدواجی حقوق، بچوں کی تحویل و سرپرستی، اور جہیز یا تحائف کی واپسی۔ موجودہ شیڈول دیکھیں۔",
            "فئملي ڪورٽن کي ايڪٽ جي شيڊول ۾ درج معاملن تي خاص ٻڌڻيءَ جو اختيار آهي، جهڙوڪ نڪاح جي تنسيخ (بشمول خلع)، حق مهر، نان نفقو، ازدواجي حقن جي بحالي، ٻارن جي سنڀال ۽ سرپرستي، ۽ جهيز يا تحفن جي واپسي. موجوده شيڊول ڏسو.",
            gl=["khula", "dower", "maintenance", "custody"]),
        sec("fca-10", "Section 10", "Pre-trial reconciliation",
            "Before and during a family case the court is required to try to bring the parties to a compromise. In suits for dissolution of marriage the court has particular duties to attempt reconciliation, and in a khula case the court's powers and the effect on dower are set out in this section. Read the exact text.",
            "خاندانی مقدمے سے پہلے اور اس کے دوران عدالت پر فریقین میں صلح کرانے کی کوشش لازم ہے۔ تنسیخِ نکاح کے دعووں میں مصالحت کی خصوصی ذمہ داریاں ہیں، اور خلع کے مقدمے میں عدالت کے اختیارات اور حق مہر پر اثر اس دفعہ میں بیان ہیں۔ عین الفاظ پڑھیں۔",
            "خانداني ڪيس کان اڳ ۽ ان دوران عدالت تي ڌرين ۾ صلح ڪرائڻ جي ڪوشش لازمي آهي. نڪاح جي تنسيخ جي دعوائن ۾ صلح جون خاص ذميواريون آهن، ۽ خلع جي ڪيس ۾ عدالت جا اختيار ۽ حق مهر تي اثر هن دفعي ۾ ڏنل آهن. صحيح لفظ پڙهو.",
            gl=["khula"])]))

LAWS.append(law(
    "guardians-wards-1890", "Guardians and Wards Act, 1890", "family", "federal",
    L("Governs the appointment of guardians for minors and decisions about their custody. Courts treat the welfare of the child as the leading consideration.",
      "نابالغ بچوں کے سرپرست مقرر کرنے اور ان کی تحویل کے فیصلوں کو منضبط کرتا ہے۔ عدالتیں بچے کی فلاح کو سب سے اہم پہلو سمجھتی ہیں۔",
      "نابالغ ٻارن لاءِ سرپرست مقرر ڪرڻ ۽ سندن سنڀال بابت فيصلن کي منظم ڪري ٿو. عدالتون ٻار جي ڀلائيءَ کي سڀ کان اهم پاسو سمجهن ٿيون."),
    ["guardian", "ward", "custody", "minor", "welfare of the child", "guardianship", "hizanat"],
    year=1890, applies=NATIONWIDE, note=FED_NOTE, related=["family-courts-act-1964", "mflo-1961"],
    sections=[
        sec("gwa-17", "Section 17", "Matters to be considered by the court in appointing guardian",
            "In appointing a guardian the court considers what is for the welfare of the minor, taking into account the minor's age, sex and religion, the character and capacity of the proposed guardian, existing relationships, and the minor's own preference if old enough to form one.",
            "سرپرست مقرر کرتے وقت عدالت دیکھتی ہے کہ نابالغ کی فلاح کس میں ہے، اور نابالغ کی عمر، جنس اور مذہب، مجوزہ سرپرست کے کردار و اہلیت، موجودہ رشتے، اور اگر نابالغ اتنا بڑا ہو تو اس کی اپنی ترجیح کو مدِنظر رکھتی ہے۔",
            "سرپرست مقرر ڪرڻ وقت عدالت ڏسي ٿي ته نابالغ جي ڀلائي ڪنهن ۾ آهي، ۽ نابالغ جي عمر، جنس ۽ مذهب، تجويز ڪيل سرپرست جي ڪردار ۽ اهليت، موجوده رشتن، ۽ جيڪڏهن نابالغ ايترو وڏو هجي ته سندس پنهنجي ترجيح کي ڌيان ۾ رکي ٿي.",
            gl=["custody"]),
        sec("gwa-25", "Section 25", "Title of guardian to custody of ward",
            "If a ward leaves or is removed from the custody of the guardian, the court can order the ward to be returned if it is for the ward's welfare. Welfare of the child, not the parents' preference, is the central test.",
            "اگر نابالغ سرپرست کی تحویل سے نکل جائے یا نکال دیا جائے تو عدالت بچے کی فلاح کے مطابق ہو تو اسے واپس لوٹانے کا حکم دے سکتی ہے۔ بنیادی کسوٹی بچے کی فلاح ہے، والدین کی ترجیح نہیں۔",
            "جيڪڏهن نابالغ سرپرست جي سنڀال مان نڪري وڃي يا ڪڍيو وڃي ته عدالت ٻار جي ڀلائيءَ مطابق هجي ته کيس واپس ڪرڻ جو حڪم ڏئي سگهي ٿي. بنيادي ڪسوٽي ٻار جي ڀلائي آهي، والدين جي ترجيح نه.",
            gl=["custody"])]))

LAWS.append(law(
    "dowry-bridal-gifts-1976", "Dowry and Bridal Gifts (Restriction) Act, 1976", "family", "federal",
    L("Limits dowry and bridal gifts and requires that gifts given to the bride be treated as her property. Disputes about return of dowry and gifts commonly go to the Family Court.",
      "جہیز اور دلہن کے تحائف کو محدود کرتا ہے اور لازم کرتا ہے کہ دلہن کو دیے گئے تحائف اس کی ملکیت سمجھے جائیں۔ جہیز اور تحائف کی واپسی کے تنازعات عموماً فیملی کورٹ میں جاتے ہیں۔",
      "جهيز ۽ ڪنوار جي تحفن کي محدود ڪري ٿو ۽ لازمي ڪري ٿو ته ڪنوار کي ڏنل تحفا سندس ملڪيت سمجهيا وڃن. جهيز ۽ تحفن جي واپسيءَ جا تڪرار عام طور فئملي ڪورٽ ۾ وڃن ٿا."),
    ["dowry", "jahez", "bridal gifts", "marriage", "property of the bride"],
    year=1976, applies=NATIONWIDE, note=FED_NOTE, related=["family-courts-act-1964", "mflo-1961"]))

LAWS.append(law(
    "succession-act-1925", "Succession Act, 1925", "family", "federal",
    L("Provides rules on inheritance by will and on intestate succession for people to whom it applies, primarily non-Muslims. Muslim inheritance follows Islamic personal law as applied in Pakistan (see MFLO 1961, Section 4).",
      "ان لوگوں کے لیے وصیت اور بلا وصیت وراثت کے قواعد دیتا ہے جن پر یہ لاگو ہے، بنیادی طور پر غیر مسلم۔ مسلمانوں کی وراثت پاکستان میں رائج اسلامی شخصی قانون کے مطابق ہوتی ہے (دیکھیں عائلی قوانین آرڈیننس 1961، دفعہ 4)۔",
      "انهن ماڻهن لاءِ وصيت ۽ بي وصيت وراثت جا قاعدا ڏئي ٿو جن تي هي لاڳو آهي، بنيادي طور غير مسلمن. مسلمانن جي وراثت پاڪستان ۾ رائج اسلامي ذاتي قانون مطابق ٿئي ٿي (ڏسو عائلي قانون آرڊيننس 1961، دفعو 4)."),
    ["inheritance", "will", "succession", "intestate", "non-muslim", "heirs", "probate", "succession certificate"],
    year=1925, applies=NATIONWIDE, note=FED_NOTE, related=["mflo-1961"]))

LAWS.append(law(
    "sindh-child-marriage-2013", "Sindh Child Marriage Restraint Act, 2013", "family", "sindh",
    L("Provincial law in Sindh that restrains child marriage and sets the minimum marriage age at 18 for both boys and girls, with penalties. Rules differ in other provinces, so check the law for your own province.",
      "سندھ کا صوبائی قانون جو کم عمری کی شادی کو روکتا ہے اور لڑکوں اور لڑکیوں دونوں کے لیے شادی کی کم از کم عمر 18 سال مقرر کرتا ہے، سزاؤں کے ساتھ۔ دوسرے صوبوں میں قواعد مختلف ہیں، اس لیے اپنے صوبے کا قانون دیکھیں۔",
      "سنڌ جو صوبائي قانون جيڪو ننڍي عمر جي شاديءَ کي روڪي ٿو ۽ ڇوڪرن ۽ ڇوڪرين ٻنهي لاءِ شاديءَ جي گهٽ ۾ گهٽ عمر 18 سال مقرر ڪري ٿو، سزائن سان. ٻين صوبن ۾ قاعدا مختلف آهن، تنهن ڪري پنهنجي صوبي جو قانون ڏسو."),
    ["child marriage", "minimum age", "underage marriage", "sindh", "marriage age", "18"],
    year=2013, note=L("Sindh only. Other provinces and territories have different laws and ages; verify before relying on this.", "صرف سندھ۔ دیگر صوبوں اور علاقوں کے قوانین اور عمریں مختلف ہیں؛ بھروسا کرنے سے پہلے تصدیق کریں۔", "رڳو سنڌ. ٻين صوبن ۽ علائقن جا قانون ۽ عمرون مختلف آهن؛ ڀروسو ڪرڻ کان اڳ تصديق ڪريو."),
    related=["mflo-1961"]))
