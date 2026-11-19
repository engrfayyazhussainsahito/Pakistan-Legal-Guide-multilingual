from common import L
from topics_common import faq, ch

FAQS = []
CH = []

# ============================================================ 11 Renting
FAQS += [
    faq("faq-eviction",
        L("Can a landlord throw out a tenant without a court order?", "کیا مالک مکان عدالتی حکم کے بغیر کرایہ دار کو نکال سکتا ہے؟", "ڇا مالڪ مڪان عدالتي حڪم کانسواءِ ڪرائيدار کي ڪڍي سگهي ٿو؟"),
        L("In general, no. Provincial rented-premises laws provide a legal process: the landlord applies to the Rent Controller or Rent Tribunal on one of the grounds allowed by law (for example non-payment of rent, subletting or genuine personal need), and the tenant is heard. Forcibly removing a tenant or cutting off essential services can itself create legal problems for the landlord. The exact grounds differ between Sindh, Punjab and Islamabad.",
          "عموماً نہیں۔ صوبائی کرایہ دارانہ قوانین قانونی عمل دیتے ہیں: مالک مکان قانون میں دی گئی بنیادوں (مثلاً کرایہ ادا نہ کرنا، آگے کرایہ پر دینا یا حقیقی ذاتی ضرورت) پر رینٹ کنٹرولر یا رینٹ ٹربیونل میں درخواست دیتا ہے اور کرایہ دار کو سنا جاتا ہے۔ زبردستی نکالنا یا لازمی خدمات منقطع کرنا مالک مکان کے لیے خود قانونی مسائل پیدا کر سکتا ہے۔ درست بنیادیں سندھ، پنجاب اور اسلام آباد میں مختلف ہیں۔",
          "عام طور نه. صوبائي ڪرائي دارن جا قانون قانوني عمل ڏين ٿا: مالڪ مڪان قانون ۾ ڏنل بنيادن (مثال طور ڪرايو ادا نه ڪرڻ، اڳتي ڪرائي تي ڏيڻ يا حقيقي ذاتي ضرورت) تي رينٽ ڪنٽرولر يا رينٽ ٽربيونل ۾ درخواست ڏئي ٿو ۽ ڪرائيدار کي ٻڌو وڃي ٿو. زوريءَ ڪڍڻ يا لازمي خدمتون ڪٽڻ مالڪ مڪان لاءِ پاڻ قانوني مسئلا پيدا ڪري سگهي ٿو. صحيح بنياد سنڌ، پنجاب ۽ اسلام آباد ۾ مختلف آهن."),
        ["eviction", "tenant", "landlord", "rent controller", "ejectment"],
        [("sindh-rented-premises-1979"), ("punjab-rented-premises-2009"), ("ict-rent-restriction-2001")], True),
    faq("faq-rent-agreement",
        L("Do I need a written tenancy agreement?", "کیا مجھے تحریری کرایہ نامہ درکار ہے؟", "ڇا مون کي لکت وارو ڪرائي نامو گهرجي؟"),
        L("A written agreement is strongly advisable. A lease of immovable property for more than one year must be by registered instrument (Transfer of Property Act, Section 107), and some provinces have specific tenancy-agreement or registration rules. A clear agreement stating rent, advance, duration, repairs and notice makes disputes much easier to resolve.",
          "تحریری معاہدہ انتہائی مناسب ہے۔ ایک سال سے زیادہ مدت کا غیر منقولہ جائیداد کا پٹہ رجسٹرڈ دستاویز سے ہونا لازم ہے (ٹرانسفر آف پراپرٹی ایکٹ، دفعہ 107) اور بعض صوبوں میں کرایہ نامے یا رجسٹریشن کے مخصوص قواعد ہیں۔ کرایہ، ایڈوانس، مدت، مرمت اور نوٹس کی واضح شقوں والا معاہدہ تنازعات کو بہت آسان بنا دیتا ہے۔",
          "لکت وارو معاهدو سخت مناسب آهي. هڪ سال کان وڌيڪ مدت جي غير منقول ملڪيت جي ليز رجسٽرڊ دستاويز سان ٿيڻ لازمي آهي (ٽرانسفر آف پراپرٽي ايڪٽ، دفعو 107) ۽ ڪجهه صوبن ۾ ڪرائي نامي يا رجسٽريشن جا مخصوص قاعدا آهن. ڪرايو، ايڊوانس، مدت، مرمت ۽ نوٽيس جي واضح شقن وارو معاهدو تڪرارن کي تمام آسان بڻائي ٿو."),
        ["tenancy agreement", "lease", "rent agreement", "registered", "advance"], [("tpa-1882", "tpa-107")], True),
]
CH.append(ch(
    11, "renting-tenant-landlord", 4, "property",
    L("Renting: tenant and landlord", "کرایہ داری: کرایہ دار اور مالک مکان", "ڪرائي داري: ڪرائيدار ۽ مالڪ مڪان"),
    L("Agreements, rent, deposits, eviction and where tenancy disputes are decided — by province.",
      "معاہدے، کرایہ، ایڈوانس، بے دخلی اور کرایہ داری کے تنازعات کہاں طے ہوتے ہیں — صوبہ وار۔",
      "معاهدا، ڪرايو، ايڊوانس، بي دخلي ۽ ڪرائي داريءَ جا تڪرار ڪٿي طئه ٿين ٿا — صوبي مطابق."),
    L("Tenancy is mainly governed by provincial law: the Sindh Rented Premises Ordinance, 1979, the Punjab Rented Premises Act, 2009, the Islamabad Rent Restriction Ordinance, 2001, and equivalent laws elsewhere. They usually provide for a Rent Controller or Rent Tribunal, set out grounds for eviction, and protect tenants from arbitrary removal. The general rules on leases are in the Transfer of Property Act, 1882. Choose your province on this site to see the right law first.",
      "کرایہ داری بنیادی طور پر صوبائی قانون سے منضبط ہے: سندھ رینٹڈ پریمائسز آرڈیننس 1979، پنجاب رینٹڈ پریمائسز ایکٹ 2009، اسلام آباد رینٹ ریسٹرکشن آرڈیننس 2001، اور دیگر جگہوں پر مساوی قوانین۔ ان میں عموماً رینٹ کنٹرولر یا رینٹ ٹربیونل ہوتا ہے، بے دخلی کی بنیادیں طے ہوتی ہیں اور کرایہ داروں کو من مانی بے دخلی سے تحفظ ملتا ہے۔ پٹوں کے عمومی قواعد ٹرانسفر آف پراپرٹی ایکٹ 1882 میں ہیں۔ درست قانون پہلے دیکھنے کے لیے اس سائٹ پر اپنا صوبہ منتخب کریں۔",
      "ڪرائي داري بنيادي طور صوبائي قانون هيٺ آهي: سنڌ رينٽڊ پريمسز آرڊيننس 1979، پنجاب رينٽڊ پريمسز ايڪٽ 2009، اسلام آباد رينٽ ريسٽرڪشن آرڊيننس 2001، ۽ ٻين هنڌن تي ساڳيا قانون. انهن ۾ عام طور رينٽ ڪنٽرولر يا رينٽ ٽربيونل هوندو آهي، بي دخليءَ جا بنياد مقرر هوندا آهن ۽ ڪرائيدارن کي خود مختيار بي دخليءَ کان تحفظ ملي ٿو. ليزن جا عام قاعدا ٽرانسفر آف پراپرٽي ايڪٽ 1882 ۾ آهن. صحيح قانون پهرين ڏسڻ لاءِ هن سائيٽ تي پنهنجو صوبو چونڊيو."),
    [L("Sign a written agreement stating rent, advance, duration, repairs and notice; have it registered where required.", "کرایہ، ایڈوانس، مدت، مرمت اور نوٹس کے ساتھ تحریری معاہدہ کریں؛ جہاں لازم ہو رجسٹر کرائیں۔", "ڪرايو، ايڊوانس، مدت، مرمت ۽ نوٽيس سان لکت وارو معاهدو ڪريو؛ جتي لازمي هجي رجسٽر ڪرايو."),
     L("Pay rent through a traceable method and keep receipts.", "کرایہ قابلِ سراغ طریقے سے ادا کریں اور رسیدیں رکھیں۔", "ڪرايو ڳولي سگهجڻ وارين طريقي سان ادا ڪريو ۽ رسيدون رکو."),
     L("If the landlord refuses to accept rent, ask a lawyer about depositing it with the Rent Controller where your province allows.", "اگر مالک مکان کرایہ لینے سے انکار کرے تو وکیل سے پوچھیں کہ آپ کے صوبے میں رینٹ کنٹرولر کے پاس جمع کرایا جا سکتا ہے یا نہیں۔", "جيڪڏهن مالڪ مڪان ڪرايو وٺڻ کان انڪار ڪري ته وڪيل کان پڇو ته توهان جي صوبي ۾ رينٽ ڪنٽرولر وٽ جمع ڪرائي سگهجي ٿو يا نه."),
     L("Landlords seeking eviction must apply to the Rent Controller or Tribunal on a lawful ground and follow the procedure.", "بے دخلی چاہنے والے مالکان کو قانونی بنیاد پر رینٹ کنٹرولر یا ٹربیونل میں درخواست دینا اور طریقۂ کار پر عمل کرنا ہوتا ہے۔", "بي دخلي چاهيندڙ مالڪن کي قانوني بنياد تي رينٽ ڪنٽرولر يا ٽربيونل ۾ درخواست ڏيڻي ۽ طريقي تي عمل ڪرڻو آهي."),
     L("Keep records of notices, receipts and condition photographs at move-in and move-out.", "نوٹسز، رسیدیں اور داخلے و روانگی کے وقت حالت کی تصاویر کا ریکارڈ رکھیں۔", "نوٽيس، رسيدن ۽ داخلا ۽ روانگيءَ وقت حالت جي تصويرن جو رڪارڊ رکو.")],
    ["faq-eviction", "faq-rent-agreement"],
    [(L("Which Act contains the general rules on leases?", "پٹوں کے عمومی قواعد کس ایکٹ میں ہیں؟", "ليزن جا عام قاعدا ڪهڙي ايڪٽ ۾ آهن؟"), L("The Transfer of Property Act, 1882 (Sections 105 and 107).", "ٹرانسفر آف پراپرٹی ایکٹ 1882 (دفعہ 105 اور 107)۔", "ٽرانسفر آف پراپرٽي ايڪٽ 1882 (دفعا 105 ۽ 107).")),
     (L("Who decides eviction applications?", "بے دخلی کی درخواستوں کا فیصلہ کون کرتا ہے؟", "بي دخليءَ جي درخواستن جو فيصلو ڪير ڪري ٿو؟"), L("Generally a Rent Controller or Rent Tribunal under the provincial law.", "عموماً صوبائی قانون کے تحت رینٹ کنٹرولر یا رینٹ ٹربیونل۔", "عام طور صوبائي قانون تحت رينٽ ڪنٽرولر يا رينٽ ٽربيونل."))],
    ["tenant"],
    [("sindh-rented-premises-1979"), ("punjab-rented-premises-2009"), ("ict-rent-restriction-2001"), ("tpa-1882", "tpa-105"), ("tpa-1882", "tpa-107")],
    ["rent", "tenant", "landlord", "eviction", "tenancy", "lease", "agreement"], 6))

# ============================================================ 12 Buying property
FAQS += [
    faq("faq-buy-property-checks",
        L("What should I check before buying property?", "جائیداد خریدنے سے پہلے مجھے کیا دیکھنا چاہیے؟", "ملڪيت خريد ڪرڻ کان اڳ مون کي ڇا ڏسڻ گهرجي؟"),
        L("Verify that the seller is the true owner (title documents and the official revenue or registry record), check for existing mortgages, disputes or court cases, confirm the property's description and boundaries, and make sure the sale is completed by a registered sale deed followed by mutation in the record. Pay by traceable bank instruments and keep every receipt. Use a lawyer for due diligence.",
          "تصدیق کریں کہ فروخت کنندہ حقیقی مالک ہے (ملکیتی دستاویزات اور سرکاری مالیہ یا رجسٹری ریکارڈ)، موجودہ رہن، تنازعات یا مقدمات دیکھیں، جائیداد کی تفصیل اور حدود کی تصدیق کریں، اور یقینی بنائیں کہ فروخت رجسٹرڈ بیع نامے اور پھر ریکارڈ میں انتقال سے مکمل ہو۔ قابلِ سراغ بینک ذرائع سے ادائیگی کریں اور ہر رسید رکھیں۔ جانچ پڑتال کے لیے وکیل سے مدد لیں۔",
          "تصديق ڪريو ته وڪرو ڪندڙ حقيقي مالڪ آهي (مالڪيءَ جا دستاويز ۽ سرڪاري مالياتي يا رجسٽري رڪارڊ)، موجوده رهن، تڪرار يا ڪيس ڏسو، ملڪيت جي وصف ۽ حدن جي تصديق ڪريو، ۽ پڪ ڪريو ته وڪرو رجسٽرڊ وڪري نامي ۽ پوءِ رڪارڊ ۾ انتقال سان مڪمل ٿئي. ڳولي سگهجڻ وارن بئنڪ ذريعن سان ادائيگي ڪريو ۽ هر رسيد رکو. جاچ لاءِ وڪيل جي مدد وٺو."),
        ["buy property", "due diligence", "title", "registry", "sale deed", "mutation"], [("tpa-1882", "tpa-54"), ("registration-act-1908", "ra-17")], True),
]
CH.append(ch(
    12, "buying-property-registration", 4, "property",
    L("Buying property and registration", "جائیداد کی خرید اور رجسٹریشن", "ملڪيت جي خريد ۽ رجسٽريشن"),
    L("Due diligence, the registered sale deed and why mutation matters.",
      "جانچ پڑتال، رجسٹرڈ بیع نامہ اور انتقال کیوں اہم ہے۔",
      "جاچ پڙتال، رجسٽرڊ وڪرو نامو ۽ انتقال ڇو اهم آهي."),
    L("A sale transfers ownership for a price (Transfer of Property Act, Section 54). For property above a stated value, the transfer must be by a registered instrument, and the Registration Act, 1908 lists documents that must be registered (Section 17). Registration and the later mutation in the revenue or municipal record are what protect your title against later claims. Most property disputes — double sales, forged documents, unpaid instalments — can be avoided by checking before paying.",
      "فروخت قیمت کے عوض ملکیت منتقل کرتی ہے (ٹرانسفر آف پراپرٹی ایکٹ، دفعہ 54)۔ مقررہ مالیت سے زیادہ جائیداد کی منتقلی رجسٹرڈ دستاویز سے ہونی چاہیے اور رجسٹریشن ایکٹ 1908 ان دستاویزات کی فہرست دیتا ہے جن کی رجسٹریشن لازم ہے (دفعہ 17)۔ رجسٹریشن اور بعد میں مالیہ یا بلدیاتی ریکارڈ میں انتقال ہی آپ کے حق کو بعد کے دعووں سے بچاتے ہیں۔ دوہری فروخت، جعلی دستاویزات، غیر ادا شدہ اقساط جیسے اکثر جائیداد تنازعات ادائیگی سے پہلے جانچ سے ٹل سکتے ہیں۔",
      "وڪرو قيمت جي عوض مالڪي منتقل ڪري ٿو (ٽرانسفر آف پراپرٽي ايڪٽ، دفعو 54). مقرر قيمت کان مٿي ملڪيت جي منتقلي رجسٽرڊ دستاويز سان ٿيڻ گهرجي ۽ رجسٽريشن ايڪٽ 1908 انهن دستاويزن جي لسٽ ڏئي ٿو جن جي رجسٽريشن لازمي آهي (دفعو 17). رجسٽريشن ۽ پوءِ مالياتي يا ميونسپل رڪارڊ ۾ انتقال ئي توهان جي حق کي پوءِ جي دعوائن کان بچائين ٿا. ٻٽو وڪرو، جعلي دستاويز، ادا نه ٿيل قسط جهڙا گهڻا ملڪيت جا تڪرار ادائيگي کان اڳ جاچ سان ٽري سگهن ٿا."),
    [L("Obtain certified copies of the title and revenue/registry record and verify them at the official office.", "ملکیت اور مالیہ/رجسٹری ریکارڈ کی مصدقہ نقول لیں اور سرکاری دفتر میں ان کی تصدیق کریں۔", "مالڪي ۽ مالياتي/رجسٽري رڪارڊ جون تصديق ٿيل ڪاپيون وٺو ۽ سرڪاري آفيس ۾ انهن جي تصديق ڪريو."),
     L("Search for mortgages, litigation, unpaid taxes and utility dues.", "رہن، مقدمات، غیر ادا شدہ ٹیکس اور یوٹیلٹی بقایا جات کی تلاش کریں۔", "رهن، ڪيس، ادا نه ٿيل ٽيڪس ۽ يوٽيلٽي بقايا جي ڳولا ڪريو."),
     L("Sign a written agreement to sell with clear payment schedule; pay by bank instruments only.", "ادائیگی کے واضح شیڈول کے ساتھ تحریری بیع کا معاہدہ کریں؛ صرف بینک ذرائع سے ادائیگی کریں۔", "ادائيگيءَ جي واضح شيڊول سان لکت وارو وڪري جو معاهدو ڪريو؛ رڳو بئنڪ ذريعن سان ادائيگي ڪريو."),
     L("Execute and register the sale deed before the Sub-Registrar and pay applicable duties.", "سب رجسٹرار کے سامنے بیع نامہ تحریر اور رجسٹر کرائیں اور لاگو محصولات ادا کریں۔", "سب رجسٽرار آڏو وڪرو نامو لکو ۽ رجسٽر ڪرايو ۽ لاڳو محصول ادا ڪريو."),
     L("Apply for mutation in the record and take possession; keep all documents safe.", "ریکارڈ میں انتقال کی درخواست دیں اور قبضہ لیں؛ تمام کاغذات محفوظ رکھیں۔", "رڪارڊ ۾ انتقال جي درخواست ڏيو ۽ قبضو وٺو؛ سڀ ڪاغذ محفوظ رکو.")],
    ["faq-buy-property-checks"],
    [(L("Which section of the Registration Act lists documents that must be registered?", "رجسٹریشن ایکٹ کی کون سی دفعہ لازمی رجسٹریشن والی دستاویزات کی فہرست دیتی ہے؟", "رجسٽريشن ايڪٽ جو ڪهڙو دفعو لازمي رجسٽريشن وارن دستاويزن جي لسٽ ڏئي ٿو؟"), L("Section 17.", "دفعہ 17۔", "دفعو 17.")),
     (L("Why is mutation important after registration?", "رجسٹریشن کے بعد انتقال کیوں اہم ہے؟", "رجسٽريشن کانپوءِ انتقال ڇو اهم آهي؟"), L("It updates the official record so that your name appears as owner.", "یہ سرکاری ریکارڈ اپڈیٹ کرتا ہے تاکہ آپ کا نام مالک کے طور پر آئے۔", "هي سرڪاري رڪارڊ اپڊيٽ ڪري ٿو ته توهان جو نالو مالڪ طور اچي."))],
    ["contract", "inheritance"],
    [("tpa-1882", "tpa-54"), ("registration-act-1908", "ra-17"), ("specific-relief-act-1877", "sra-42")],
    ["property", "sale deed", "registry", "mutation", "title", "stamp duty"], 6))

# ============================================================ 13 Work and wages
FAQS += [
    faq("faq-unpaid-wages",
        L("What can I do if my employer does not pay my wages?", "اگر آجر میری اجرت ادا نہ کرے تو میں کیا کر سکتا ہوں؟", "جيڪڏهن ملازم رکندڙ منهنجي اجرت ادا نه ڪري ته مان ڇا ڪري سگهان ٿو؟"),
        L("Ask for payment in writing and keep proof of your work and agreed pay (appointment letter, messages, attendance, payslips). If unpaid, complain to the labour department or the authority under the wages law that applies to your workplace — for example the Payment of Wages Act, 1936 as applied in your province — or a labour court. Time limits apply, so act soon.",
          "تحریری طور پر ادائیگی مانگیں اور اپنے کام اور طے شدہ تنخواہ کا ثبوت (تقرری نامہ، پیغامات، حاضری، پے سلپ) رکھیں۔ ادا نہ ہو تو اپنے کام کی جگہ پر لاگو اجرت کے قانون — مثلاً آپ کے صوبے میں لاگو پیمنٹ آف ویجز ایکٹ 1936 — کے تحت محکمۂ محنت یا مقررہ اتھارٹی یا لیبر کورٹ سے رجوع کریں۔ مدتیں مقرر ہیں، اس لیے جلد کارروائی کریں۔",
          "لکت ۾ ادائيگي گهرو ۽ پنهنجي ڪم ۽ طئه ٿيل پگهار جو ثبوت (تقرري نامو، پيغام، حاضري، پي سلپ) رکو. ادا نه ٿئي ته پنهنجي ڪم جي جڳهه تي لاڳو اجرت جي قانون — مثال طور توهان جي صوبي ۾ لاڳو پيمينٽ آف ويجز ايڪٽ 1936 — تحت محنت کاتي يا مقرر اٿارٽيءَ يا ليبر ڪورٽ ڏانهن وڃو. مدتون مقرر آهن، تنهن ڪري جلد ڪارروائي ڪريو."),
        ["wages", "salary", "unpaid", "employer", "labour court", "labour department"], [("payment-of-wages-1936"), ("sindh-standing-orders-2015")], True),
    faq("faq-termination",
        L("Can my employer terminate me without notice?", "کیا آجر مجھے بغیر نوٹس کے برطرف کر سکتا ہے؟", "ڇا ملازم رکندڙ مون کي نوٽيس کانسواءِ برطرف ڪري سگهي ٿو؟"),
        L("It depends on your contract and the labour law that applies (for example the Sindh Terms of Employment (Standing Orders) Act, 2015 for covered Sindh establishments). Covered workers are usually entitled to notice or pay in lieu and, for misconduct, to a fair procedure. Keep your appointment letter and speak to the labour department or a lawyer quickly.",
          "یہ آپ کے معاہدے اور لاگو لیبر قانون پر منحصر ہے (مثلاً سندھ کے احاطہ شدہ اداروں کے لیے سندھ ٹرمز آف ایمپلائمنٹ (اسٹینڈنگ آرڈرز) ایکٹ 2015)۔ احاطہ شدہ کارکن عموماً نوٹس یا اس کے بدلے تنخواہ اور بدعنوانی/بدانتظامی کی صورت میں منصفانہ طریقۂ کار کے حق دار ہوتے ہیں۔ تقرری نامہ رکھیں اور جلد محکمۂ محنت یا وکیل سے بات کریں۔",
          "هي توهان جي معاهدي ۽ لاڳو ليبر قانون تي منحصر آهي (مثال طور سنڌ جي ڍڪيل ادارن لاءِ سنڌ ٽرمز آف ايمپلائمينٽ (اسٽينڊنگ آرڊرز) ايڪٽ 2015). ڍڪيل ڪم ڪندڙ عام طور نوٽيس يا ان جي بدران پگهار ۽ بدانتظامي جي صورت ۾ منصفانه طريقي جا حقدار هوندا آهن. تقرري نامو رکو ۽ جلد محنت کاتي يا وڪيل سان ڳالهايو."),
        ["termination", "dismissal", "notice", "employment", "standing orders"], [("sindh-standing-orders-2015")], True),
]
CH.append(ch(
    13, "work-and-wages", 4, "labour",
    L("Work, wages and termination", "ملازمت، اجرت اور برطرفی", "نوڪري، اجرت ۽ برطرفي"),
    L("Appointment letters, timely wages, deductions, termination and where to complain.",
      "تقرری نامے، بروقت اجرت، کٹوتیاں، برطرفی اور شکایت کہاں کریں۔",
      "تقرري نامون، وقت تي اجرت، ڪٽوتيون، برطرفي ۽ شڪايت ڪٿي ڪجي."),
    L("Employment rights come from several laws: federal and provincial wages laws, standing orders on terms of employment, industrial-relations laws and minimum-wage notifications. Which applies depends on your province and on whether your workplace is covered. Basic protections usually include being paid on time, limits on deductions, written terms, and a fair process before dismissal for misconduct. Written proof — an appointment letter, payslips, messages — is your most valuable evidence.",
      "ملازمت کے حقوق کئی قوانین سے آتے ہیں: وفاقی اور صوبائی اجرت کے قوانین، ملازمت کی شرائط کے اسٹینڈنگ آرڈرز، صنعتی تعلقات کے قوانین اور کم از کم اجرت کے نوٹیفکیشن۔ کون سا لاگو ہوتا ہے یہ آپ کے صوبے اور کام کی جگہ کے احاطہ شدہ ہونے پر منحصر ہے۔ بنیادی تحفظات میں عموماً بروقت ادائیگی، کٹوتیوں پر حد، تحریری شرائط، اور بدانتظامی پر برطرفی سے پہلے منصفانہ عمل شامل ہیں۔ تحریری ثبوت — تقرری نامہ، پے سلپ، پیغامات — آپ کا سب سے قیمتی ثبوت ہے۔",
      "نوڪريءَ جا حق ڪيترن قانونن مان اچن ٿا: وفاقي ۽ صوبائي اجرت جا قانون، نوڪريءَ جي شرطن جا اسٽينڊنگ آرڊر، صنعتي لاڳاپن جا قانون ۽ گهٽ ۾ گهٽ اجرت جا نوٽيفڪيشن. ڪهڙو لاڳو ٿئي ٿو اهو توهان جي صوبي ۽ ڪم جي جڳهه جي ڍڪيل هئڻ تي منحصر آهي. بنيادي تحفظن ۾ عام طور وقت تي ادائيگي، ڪٽوتين تي حد، لکت وارا شرط، ۽ بدانتظاميءَ تي برطرفيءَ کان اڳ منصفانه عمل شامل آهن. لکت وارو ثبوت — تقرري نامو، پي سلپ، پيغام — توهان جو سڀ کان قيمتي ثبوت آهي."),
    [L("Ask for a written appointment letter stating pay, hours and duties.", "تنخواہ، اوقات اور فرائض والا تحریری تقرری نامہ مانگیں۔", "پگهار، ڪم جا ڪلاڪ ۽ فرض وارو لکت وارو تقرري نامو گهرو."),
     L("Keep records of attendance, payslips, bank statements and messages.", "حاضری، پے سلپ، بینک اسٹیٹمنٹ اور پیغامات کا ریکارڈ رکھیں۔", "حاضري، پي سلپ، بئنڪ اسٽيٽمينٽ ۽ پيغامن جو رڪارڊ رکو."),
     L("If unpaid or wrongly deducted, demand payment in writing, then complain to the labour department or authority under the applicable wages law.", "ادا نہ ہو یا غلط کٹوتی ہو تو تحریری مطالبہ کریں، پھر محکمۂ محنت یا لاگو اجرت قانون کے تحت اتھارٹی سے شکایت کریں۔", "ادا نه ٿئي يا غلط ڪٽوتي ٿئي ته لکت ۾ مطالبو ڪريو، پوءِ محنت کاتي يا لاڳو اجرت قانون تحت اٿارٽيءَ کي شڪايت ڪريو."),
     L("If dismissed, check your notice rights and file a grievance within the time allowed by your labour law.", "برطرفی کی صورت میں نوٹس کے حقوق دیکھیں اور اپنے لیبر قانون میں مقررہ مدت کے اندر شکایت دائر کریں۔", "برطرفي جي صورت ۾ نوٽيس جا حق ڏسو ۽ پنهنجي ليبر قانون ۾ مقرر مدت اندر شڪايت داخل ڪريو.")],
    ["faq-unpaid-wages", "faq-termination"],
    [(L("Which Act deals with timely payment of wages and deductions?", "وقت پر اجرت کی ادائیگی اور کٹوتیوں سے کون سا ایکٹ متعلق ہے؟", "وقت تي اجرت ۽ ڪٽوتين بابت ڪهڙو ايڪٽ آهي؟"), L("The Payment of Wages Act, 1936 (as applied in each province).", "پیمنٹ آف ویجز ایکٹ 1936 (ہر صوبے میں لاگو شکل میں)۔", "پيمينٽ آف ويجز ايڪٽ 1936 (هر صوبي ۾ لاڳو صورت ۾)."))],
    ["maintenance", "contract"],
    [("payment-of-wages-1936"), ("sindh-standing-orders-2015"), ("ira-2012"), ("workplace-harassment-2010")],
    ["wages", "salary", "employment", "termination", "labour", "worker", "harassment"], 6))

# ============================================================ 14 Consumer
FAQS += [
    faq("faq-consumer-complaint",
        L("How do I complain about a defective product or poor service?", "ناقص مصنوعات یا ناقص خدمات کی شکایت کیسے کروں؟", "خراب پراڊڪٽ يا ناقص خدمت جي شڪايت ڪيئن ڪريان؟"),
        L("Keep the receipt, warranty and any advertisement. Complain to the seller or provider in writing and give them a reasonable time to fix, replace or refund. If unresolved, you can approach the Consumer Court under your province's consumer protection law (for example the Sindh Consumer Protection Act, 2014 or the Punjab Consumer Protection Act, 2005). Check the time limit and the required notice.",
          "رسید، وارنٹی اور کوئی اشتہار رکھیں۔ فروخت کنندہ یا خدمت فراہم کنندہ کو تحریری شکایت دیں اور مرمت، تبدیلی یا رقم واپسی کے لیے معقول وقت دیں۔ حل نہ ہو تو اپنے صوبے کے صارفین کے تحفظ کے قانون (مثلاً سندھ کنزیومر پروٹیکشن ایکٹ 2014 یا پنجاب کنزیومر پروٹیکشن ایکٹ 2005) کے تحت کنزیومر کورٹ سے رجوع کر سکتے ہیں۔ مدت اور مطلوبہ نوٹس دیکھیں۔",
          "رسيد، وارنٽي ۽ ڪو اشتهار رکو. وڪرو ڪندڙ يا خدمت ڏيندڙ کي لکت ۾ شڪايت ڏيو ۽ مرمت، مٽاسٽا يا رقم واپسي لاءِ معقول وقت ڏيو. حل نه ٿئي ته پنهنجي صوبي جي صارفن جي تحفظ جي قانون (مثال طور سنڌ ڪنزيومر پروٽيڪشن ايڪٽ 2014 يا پنجاب ڪنزيومر پروٽيڪشن ايڪٽ 2005) تحت ڪنزيومر ڪورٽ ڏانهن وڃي سگهو ٿا. مدت ۽ گهربل نوٽيس ڏسو."),
        ["consumer", "complaint", "defective", "refund", "warranty", "consumer court"],
        [("sindh-consumer-protection-2014"), ("punjab-consumer-protection-2005"), ("ict-consumer-protection-1995")], True),
]
CH.append(ch(
    14, "consumer-complaints", 4, "consumer",
    L("Consumer complaints", "صارفین کی شکایات", "صارفن جون شڪايتون"),
    L("Defective goods, misleading ads and poor service: how to complain and where to go.",
      "ناقص اشیا، گمراہ کن اشتہارات اور ناقص خدمات: شکایت کیسے کریں اور کہاں جائیں۔",
      "خراب شيون، گمراهه ڪندڙ اشتهار ۽ ناقص خدمتون: شڪايت ڪيئن ڪجي ۽ ڪٿي وڃجي."),
    L("Consumer protection laws are mostly provincial. They protect people who buy goods or services from defects, misleading claims and unfair practices, and set up Consumer Courts that are simpler and cheaper than ordinary civil courts. Your strongest tools are paperwork: the receipt, the warranty card, the advertisement, and a dated written complaint. The Contract Act, 1872 also applies, because buying something is a contract.",
      "صارفین کے تحفظ کے قوانین زیادہ تر صوبائی ہیں۔ یہ مصنوعات یا خدمات خریدنے والوں کو نقائص، گمراہ کن دعووں اور غیر منصفانہ طرزِ عمل سے تحفظ دیتے ہیں اور ایسی کنزیومر کورٹس قائم کرتے ہیں جو عام دیوانی عدالتوں سے سادہ اور سستی ہیں۔ آپ کے سب سے مضبوط ہتھیار کاغذات ہیں: رسید، وارنٹی کارڈ، اشتہار اور تاریخ والی تحریری شکایت۔ کنٹریکٹ ایکٹ 1872 بھی لاگو ہوتا ہے کیونکہ خریداری ایک معاہدہ ہے۔",
      "صارفن جي تحفظ جا قانون گهڻو ڪري صوبائي آهن. هي شيون يا خدمتون خريد ڪندڙن کي خامين، گمراهه ڪندڙ دعوائن ۽ غير منصفانه طريقن کان تحفظ ڏين ٿا ۽ اهڙيون ڪنزيومر ڪورٽون قائم ڪن ٿا جيڪي عام ديواني عدالتن کان سادي ۽ سستي آهن. توهان جا سڀ کان مضبوط هٿيار ڪاغذ آهن: رسيد، وارنٽي ڪارڊ، اشتهار ۽ تاريخ وارو لکت وارو شڪايت نامو. ڪانٽريڪٽ ايڪٽ 1872 به لاڳو ٿئي ٿو ڇاڪاڻ ته خريداري هڪ معاهدو آهي."),
    [L("Keep the receipt, warranty card, advertisement and photographs of the defect.", "رسید، وارنٹی کارڈ، اشتہار اور نقص کی تصاویر رکھیں۔", "رسيد، وارنٽي ڪارڊ، اشتهار ۽ خامي جون تصويرون رکو."),
     L("Complain to the seller in writing; state what remedy you want (repair, replacement, refund).", "فروخت کنندہ کو تحریری شکایت دیں؛ بتائیں کہ آپ کیا حل چاہتے ہیں (مرمت، تبدیلی، رقم واپسی)۔", "وڪرو ڪندڙ کي لکت ۾ شڪايت ڏيو؛ ٻڌايو ته توهان ڪهڙو حل چاهيو ٿا (مرمت، مٽاسٽا، رقم واپسي)."),
     L("If unresolved, check the consumer law for your province and any required notice and time limit.", "حل نہ ہو تو اپنے صوبے کے صارف قانون، مطلوبہ نوٹس اور مدت دیکھیں۔", "حل نه ٿئي ته پنهنجي صوبي جو صارف قانون، گهربل نوٽيس ۽ مدت ڏسو."),
     L("File the complaint in the Consumer Court with your documents and a copy of your written complaint.", "اپنے کاغذات اور تحریری شکایت کی نقل کے ساتھ کنزیومر کورٹ میں شکایت دائر کریں۔", "پنهنجن ڪاغذن ۽ لکت وارين شڪايت جي ڪاپي سان ڪنزيومر ڪورٽ ۾ شڪايت داخل ڪريو.")],
    ["faq-consumer-complaint"],
    [(L("Why is a written complaint useful?", "تحریری شکایت کیوں مفید ہے؟", "لکت وارو شڪايتنامو ڇو مفيد آهي؟"), L("It proves you gave the seller a chance to fix the problem and fixes the date.", "یہ ثابت کرتی ہے کہ آپ نے فروخت کنندہ کو مسئلہ حل کرنے کا موقع دیا اور تاریخ طے کرتی ہے۔", "هي ثابت ڪري ٿو ته توهان وڪرو ڪندڙ کي مسئلو حل ڪرڻ جو موقعو ڏنو ۽ تاريخ مقرر ڪري ٿو."))],
    ["contract"],
    [("sindh-consumer-protection-2014"), ("punjab-consumer-protection-2005"), ("ict-consumer-protection-1995"), ("contract-act-1872", "ca-73")],
    ["consumer", "defective", "refund", "warranty", "complaint", "service"], 5))

# ============================================================ 15 Cyber
FAQS += [
    faq("faq-cyber-harassment",
        L("What should I do if I am being harassed or blackmailed online?", "اگر مجھے آن لائن ہراساں یا بلیک میل کیا جا رہا ہو تو مجھے کیا کرنا چاہیے؟", "جيڪڏهن مون کي آن لائن تنگ يا بليڪ ميل ڪيو پيو وڃي ته مون کي ڇا ڪرڻ گهرجي؟"),
        L("Do not delete anything. Take screenshots showing the account, messages, dates and URLs, and save them in more than one place. Do not pay or comply with threats. Report the content to the platform and complain to the FIA's cybercrime wing (NR3C) or your nearest police station; the Prevention of Electronic Crimes Act, 2016 covers offences such as cyber stalking and offences against modesty and dignity. Reach out to a trusted person or a legal-aid or support organisation.",
          "کچھ بھی ڈیلیٹ نہ کریں۔ اکاؤنٹ، پیغامات، تاریخیں اور یو آر ایل دکھانے والے اسکرین شاٹس لیں اور انہیں ایک سے زیادہ جگہ محفوظ کریں۔ دھمکیوں پر ادائیگی یا عمل نہ کریں۔ مواد کی اطلاع پلیٹ فارم کو دیں اور ایف آئی اے کے سائبر کرائم ونگ (این آر تھری سی) یا قریبی تھانے میں شکایت کریں؛ الیکٹرانک جرائم کی روک تھام کا ایکٹ 2016 سائبر اسٹاکنگ اور حیا و وقار کے خلاف جرائم جیسے جرائم کا احاطہ کرتا ہے۔ کسی قابلِ اعتماد شخص یا قانونی امداد/معاونتی تنظیم سے رابطہ کریں۔",
          "ڪجهه به ڊيليٽ نه ڪريو. اڪائونٽ، پيغام، تاريخون ۽ يو آر ايل ڏيکارڻ وارا اسڪرين شاٽ وٺو ۽ انهن کي هڪ کان وڌيڪ هنڌ محفوظ ڪريو. ڌمڪين تي ادائيگي يا عمل نه ڪريو. مواد جي اطلاع پليٽ فارم کي ڏيو ۽ ايف آءِ اي جي سائبر ڪرائم ونگ (اين آر ٿري سي) يا ويجهي ٿاڻي ۾ شڪايت ڪريو؛ پريوينشن آف اليڪٽرانڪ ڪرائمز ايڪٽ 2016 سائبر اسٽاڪنگ ۽ حيا ۽ وقار خلاف ڏوهن جهڙن ڏوهن کي ڍڪي ٿو. ڪنهن ڀروسي جوڳي شخص يا قانوني مدد/معاون تنظيم سان رابطو ڪريو."),
        ["cyber", "harassment", "blackmail", "online", "fia", "nr3c", "peca", "screenshots"],
        [("peca-2016", "peca-21"), ("peca-2016", "peca-24")]),
]
CH.append(ch(
    15, "cyber-harassment-online-crime", 4, "cyber",
    L("Cyber harassment and online crime", "سائبر ہراسانی اور آن لائن جرائم", "سائبر تنگ ڪرڻ ۽ آن لائن ڏوهه"),
    L("Preserving evidence, reporting to the right agency and the offences covered by PECA.",
      "شواہد محفوظ کرنا، درست ادارے کو رپورٹ کرنا اور پیکا کے تحت جرائم۔",
      "ثبوت محفوظ ڪرڻ، صحيح اداري کي رپورٽ ڪرڻ ۽ پيڪا تحت ڏوهه."),
    L("The Prevention of Electronic Crimes Act, 2016 (PECA) covers offences committed through computers, phones and the internet — such as unauthorised access, misuse of identity information, offences against a person's dignity and modesty, and cyber stalking. The law has been amended, so check the current text. In practice, the most important step is preserving evidence immediately: screenshots with dates and URLs, original files and the account details of the offender. Electronic records can be used as evidence, but only if they are properly preserved.",
      "الیکٹرانک جرائم کی روک تھام کا ایکٹ 2016 (پیکا) کمپیوٹر، فون اور انٹرنیٹ کے ذریعے کیے گئے جرائم کا احاطہ کرتا ہے — جیسے غیر مجاز رسائی، شناختی معلومات کا غلط استعمال، کسی شخص کے وقار اور حیا کے خلاف جرائم اور سائبر اسٹاکنگ۔ قانون میں ترمیم ہوئی ہے، اس لیے موجودہ متن دیکھیں۔ عملاً سب سے اہم قدم فوراً شواہد محفوظ کرنا ہے: تاریخ اور یو آر ایل کے ساتھ اسکرین شاٹس، اصل فائلیں اور مجرم کے اکاؤنٹ کی تفصیلات۔ برقی ریکارڈ بطور ثبوت استعمال ہو سکتے ہیں مگر صرف اس صورت میں جب انہیں درست طور پر محفوظ کیا گیا ہو۔",
      "پريوينشن آف اليڪٽرانڪ ڪرائمز ايڪٽ 2016 (پيڪا) ڪمپيوٽر، فون ۽ انٽرنيٽ ذريعي ٿيل ڏوهن کي ڍڪي ٿو — جهڙوڪ غير مجاز رسائي، سڃاڻپ جي معلومات جو غلط استعمال، ڪنهن شخص جي وقار ۽ حيا خلاف ڏوهه ۽ سائبر اسٽاڪنگ. قانون ۾ ترميم ٿي آهي، تنهن ڪري موجوده متن ڏسو. عملي طور سڀ کان اهم قدم فوري ثبوت محفوظ ڪرڻ آهي: تاريخ ۽ يو آر ايل سان اسڪرين شاٽ، اصل فائلون ۽ ڏوهاري جي اڪائونٽ جا تفصيل. اليڪٽرانڪ رڪارڊ ثبوت طور استعمال ٿي سگهن ٿا پر رڳو ان صورت ۾ جڏهن انهن کي صحيح طرح محفوظ ڪيو ويو هجي."),
    [L("Do not delete messages or posts. Take dated screenshots showing the profile, URL and content.", "پیغامات یا پوسٹس ڈیلیٹ نہ کریں۔ پروفائل، یو آر ایل اور مواد دکھانے والے تاریخ والے اسکرین شاٹس لیں۔", "پيغام يا پوسٽون ڊيليٽ نه ڪريو. پروفائل، يو آر ايل ۽ مواد ڏيکارڻ وارا تاريخ وارا اسڪرين شاٽ وٺو."),
     L("Secure your accounts: change passwords, enable two-step verification, and restrict privacy settings.", "اپنے اکاؤنٹس محفوظ کریں: پاس ورڈ بدلیں، ٹو اسٹیپ ویریفکیشن فعال کریں اور پرائیویسی سیٹنگز محدود کریں۔", "پنهنجا اڪائونٽ محفوظ ڪريو: پاس ورڊ بدلايو، ٻه قدمي تصديق فعال ڪريو ۽ پرائيويسي سيٽنگون محدود ڪريو."),
     L("Report the content to the platform and file a complaint with the FIA cybercrime wing (NR3C) or the police.", "مواد پلیٹ فارم کو رپورٹ کریں اور ایف آئی اے کے سائبر کرائم ونگ (این آر تھری سی) یا پولیس میں شکایت درج کرائیں۔", "مواد پليٽ فارم کي رپورٽ ڪريو ۽ ايف آءِ اي جي سائبر ڪرائم ونگ (اين آر ٿري سي) يا پوليس ۾ شڪايت داخل ڪريو."),
     L("Do not pay blackmailers or delete evidence; tell a trusted person and consider legal aid or a support organisation.", "بلیک میلرز کو ادائیگی نہ کریں اور شواہد ڈیلیٹ نہ کریں؛ کسی قابلِ اعتماد شخص کو بتائیں اور قانونی امداد یا معاونتی تنظیم پر غور کریں۔", "بليڪ ميلرن کي ادائيگي نه ڪريو ۽ ثبوت ڊيليٽ نه ڪريو؛ ڪنهن ڀروسي جوڳي شخص کي ٻڌايو ۽ قانوني مدد يا معاون تنظيم تي غور ڪريو.")],
    ["faq-cyber-harassment"],
    [(L("Should you delete abusive messages?", "کیا آپ کو توہین آمیز پیغامات ڈیلیٹ کرنے چاہئیں؟", "ڇا توهان کي بدسلوڪي وارا پيغام ڊيليٽ ڪرڻ گهرجن؟"), L("No. Preserve them as evidence first.", "نہیں۔ پہلے انہیں ثبوت کے طور پر محفوظ کریں۔", "نه. پهرين انهن کي ثبوت طور محفوظ ڪريو.")),
     (L("Which agency commonly receives cybercrime complaints?", "سائبر کرائم کی شکایات عموماً کون سا ادارہ وصول کرتا ہے؟", "سائبر ڪرائم جون شڪايتون عام طور ڪهڙو ادارو وصول ڪري ٿو؟"), L("The FIA's cybercrime wing (NR3C); police may also register complaints.", "ایف آئی اے کا سائبر کرائم ونگ (این آر تھری سی)؛ پولیس بھی شکایات درج کر سکتی ہے۔", "ايف آءِ اي جو سائبر ڪرائم ونگ (اين آر ٿري سي)؛ پوليس به شڪايتون داخل ڪري سگهي ٿي."))],
    ["harassment", "evidence", "fir"],
    [("peca-2016", "peca-16"), ("peca-2016", "peca-20"), ("peca-2016", "peca-21"), ("peca-2016", "peca-24"), ("qanun-e-shahadat-1984")],
    ["cyber", "online", "harassment", "blackmail", "peca", "fia", "evidence"], 6))

# ============================================================ 16 Traffic
FAQS += [
    faq("faq-challan",
        L("What should I do if I receive a traffic challan I disagree with?", "اگر مجھے ٹریفک چالان ملے جس سے میں متفق نہ ہوں تو کیا کروں؟", "جيڪڏهن مون کي ٽريفڪ چالان ملي جنهن سان مان متفق نه هجان ته ڇا ڪريان؟"),
        L("Read the challan carefully: the offence, date, location and amount. Most provinces let you pay at designated banks or online, and also let you contest it before the traffic court or magistrate within a stated time. Keep your licence, registration and the challan copy, and check the process with your provincial traffic police or authority because fines and procedures differ.",
          "چالان غور سے پڑھیں: جرم، تاریخ، مقام اور رقم۔ زیادہ تر صوبوں میں مقررہ بینکوں یا آن لائن ادائیگی ممکن ہے، اور مقررہ مدت میں ٹریفک کورٹ یا مجسٹریٹ کے سامنے اسے چیلنج بھی کیا جا سکتا ہے۔ لائسنس، رجسٹریشن اور چالان کی نقل رکھیں اور اپنی صوبائی ٹریفک پولیس یا اتھارٹی سے طریقہ پوچھیں کیونکہ جرمانے اور طریقۂ کار مختلف ہیں۔",
          "چالان غور سان پڙهو: ڏوهه، تاريخ، جڳهه ۽ رقم. گهڻن صوبن ۾ مقرر بئنڪن يا آن لائن ادائيگي ممڪن آهي، ۽ مقرر مدت اندر ٽريفڪ ڪورٽ يا مئجسٽريٽ آڏو ان کي چئلينج به ڪري سگهجي ٿو. لائسنس، رجسٽريشن ۽ چالان جي ڪاپي رکو ۽ پنهنجي صوبائي ٽريفڪ پوليس يا اٿارٽيءَ کان طريقو پڇو ڇاڪاڻ ته ڏنڊ ۽ طريقا مختلف آهن."),
        ["challan", "traffic", "fine", "licence", "e-challan"], [("mvo-1965")], True),
]
CH.append(ch(
    16, "traffic-challans-licences", 4, "traffic",
    L("Traffic challans and driving licences", "ٹریفک چالان اور ڈرائیونگ لائسنس", "ٽريفڪ چالان ۽ ڊرائيونگ لائسنس"),
    L("What a challan means, how to pay or contest it, and why rules differ by province.",
      "چالان کا مطلب کیا ہے، ادائیگی یا چیلنج کیسے کریں، اور قواعد صوبوں میں مختلف کیوں ہیں۔",
      "چالان جو مطلب ڇا آهي، ادائيگي يا چئلينج ڪيئن ڪجي، ۽ قاعدا صوبن ۾ مختلف ڇو آهن."),
    L("Traffic law is based on the Motor Vehicles Ordinance, 1965, but each province issues its own rules, fines and enforcement systems — including e-challan systems in some cities. You are generally expected to carry your driving licence and vehicle documents. A challan is a notice of a traffic offence and the fine; ignoring it can lead to larger penalties, so pay it or contest it within the allowed time.",
      "ٹریفک قانون موٹر وہیکلز آرڈیننس 1965 پر مبنی ہے مگر ہر صوبہ اپنے قواعد، جرمانے اور نفاذی نظام جاری کرتا ہے — بعض شہروں میں ای چالان نظام بھی۔ عموماً توقع کی جاتی ہے کہ آپ ڈرائیونگ لائسنس اور گاڑی کے کاغذات ساتھ رکھیں۔ چالان ٹریفک جرم اور جرمانے کا نوٹس ہے؛ اسے نظرانداز کرنے سے بڑے جرمانے ہو سکتے ہیں، اس لیے اجازت شدہ مدت میں ادا کریں یا چیلنج کریں۔",
      "ٽريفڪ قانون موٽر وهيڪلز آرڊيننس 1965 تي ٻڌل آهي پر هر صوبو پنهنجا قاعدا، ڏنڊ ۽ لاڳو ڪرڻ جا سرشتا جاري ڪري ٿو — ڪجهه شهرن ۾ اي چالان سرشتو به. عام طور توقع ڪئي وڃي ٿي ته توهان ڊرائيونگ لائسنس ۽ گاڏيءَ جا ڪاغذ گڏ رکو. چالان ٽريفڪ ڏوهه ۽ ڏنڊ جو نوٽيس آهي؛ ان کي نظرانداز ڪرڻ سان وڏا ڏنڊ ٿي سگهن ٿا، تنهن ڪري اجازت ٿيل مدت اندر ادا ڪريو يا چئلينج ڪريو."),
    [L("Read the challan: offence, section, date, place and fine amount.", "چالان پڑھیں: جرم، دفعہ، تاریخ، مقام اور جرمانے کی رقم۔", "چالان پڙهو: ڏوهه، دفعو، تاريخ، جڳهه ۽ ڏنڊ جي رقم."),
     L("If correct, pay at the designated bank/online channel within the time shown and keep the receipt.", "درست ہو تو دکھائی گئی مدت میں مقررہ بینک/آن لائن ذریعے سے ادا کریں اور رسید رکھیں۔", "درست هجي ته ڏيکاريل مدت اندر مقرر بئنڪ/آن لائن ذريعي ادا ڪريو ۽ رسيد رکو."),
     L("If you disagree, ask the traffic office how to contest it before the traffic court/magistrate and do so within the time.", "اختلاف ہو تو ٹریفک دفتر سے پوچھیں کہ ٹریفک کورٹ/مجسٹریٹ کے سامنے اسے کیسے چیلنج کریں اور مدت میں ایسا کریں۔", "اختلاف هجي ته ٽريفڪ آفيس کان پڇو ته ٽريفڪ ڪورٽ/مئجسٽريٽ آڏو ان کي ڪيئن چئلينج ڪجي ۽ مدت اندر ائين ڪريو."),
     L("Keep your licence and vehicle registration valid and with you.", "اپنا لائسنس اور گاڑی کی رجسٹریشن درست رکھیں اور ساتھ رکھیں۔", "پنهنجو لائسنس ۽ گاڏيءَ جي رجسٽريشن صحيح رکو ۽ گڏ رکو.")],
    ["faq-challan"],
    [(L("Why do traffic fines differ between provinces?", "ٹریفک جرمانے صوبوں میں مختلف کیوں ہیں؟", "ٽريفڪ ڏنڊ صوبن ۾ مختلف ڇو آهن؟"), L("Each province issues its own rules and fines under the motor vehicles law.", "ہر صوبہ موٹر وہیکلز قانون کے تحت اپنے قواعد اور جرمانے جاری کرتا ہے۔", "هر صوبو موٽر وهيڪلز قانون تحت پنهنجا قاعدا ۽ ڏنڊ جاري ڪري ٿو."))],
    ["summons"],
    [("mvo-1965")],
    ["traffic", "challan", "licence", "fine", "vehicle", "e-challan"], 4))

# ============================================================ 17 RTI
FAQS += [
    faq("faq-rti-how",
        L("How do I request information from a government office?", "کسی سرکاری دفتر سے معلومات کیسے مانگوں؟", "ڪنهن سرڪاري آفيس کان ڄاڻ ڪيئن گهران؟"),
        L("Send a written request to the public body's designated information officer, describing the record you want as precisely as you can and giving your contact details. The law sets a deadline for a reply and allows fees only for copying. If your request is refused or ignored, you can complain to the relevant Information Commission. Use the right law: the federal Right of Access to Information Act, 2017 covers federal bodies; provinces have their own laws.",
          "عوامی ادارے کے مقررہ انفارمیشن آفیسر کو تحریری درخواست بھیجیں، مطلوبہ ریکارڈ کو ممکنہ حد تک درست بیان کریں اور اپنی رابطہ تفصیلات دیں۔ قانون جواب کی مدت مقرر کرتا ہے اور صرف نقل کی فیس کی اجازت دیتا ہے۔ درخواست رد یا نظرانداز ہو تو متعلقہ انفارمیشن کمیشن میں شکایت کی جا سکتی ہے۔ درست قانون استعمال کریں: وفاقی رائٹ آف ایکسس ٹو انفارمیشن ایکٹ 2017 وفاقی اداروں پر لاگو ہے؛ صوبوں کے اپنے قوانین ہیں۔",
          "عوامي اداري جي مقرر انفارميشن آفيسر کي لکت وارو درخواست موڪليو، گهربل رڪارڊ کي جيترو ٿي سگهي صحيح ٻڌايو ۽ پنهنجا رابطي جا تفصيل ڏيو. قانون جواب جي مدت مقرر ڪري ٿو ۽ رڳو ڪاپي جي فيس جي اجازت ڏئي ٿو. درخواست رد يا نظرانداز ٿئي ته لاڳاپيل انفارميشن ڪميشن ۾ شڪايت ڪري سگهجي ٿي. صحيح قانون استعمال ڪريو: وفاقي رائيٽ آف ايڪسيس ٽو انفارميشن ايڪٽ 2017 وفاقي ادارن تي لاڳو آهي؛ صوبن جا پنهنجا قانون آهن."),
        ["right to information", "rti", "request", "information commission", "records"],
        [("rti-federal-2017"), ("rti-sindh-2016"), ("rti-punjab-2013"), ("rti-kpk-2013"), ("constitution-1973", "art-19a")], True),
]
CH.append(ch(
    17, "right-to-information-government-services", 4, "government",
    L("Right to information and government services", "معلومات کا حق اور سرکاری خدمات", "ڄاڻ جو حق ۽ سرڪاري خدمتون"),
    L("Using Article 19A and RTI laws to get records, and how to complain about slow or unfair service.",
      "آرٹیکل 19A اور معلومات کے قوانین سے ریکارڈ کیسے حاصل کریں، اور سست یا غیر منصفانہ خدمات کی شکایت کیسے کریں۔",
      "آرٽيڪل 19A ۽ ڄاڻ جي قانونن سان رڪارڊ ڪيئن حاصل ڪجي، ۽ سست يا غير منصفانه خدمتن جي شڪايت ڪيئن ڪجي."),
    L("Article 19A gives every citizen the right of access to information in matters of public importance, subject to reasonable restrictions imposed by law. The federal Right of Access to Information Act, 2017 and provincial laws (for example in Sindh, Punjab and Khyber Pakhtunkhwa) turn this into a procedure: you request records in writing, the public body must reply within the time allowed, and a refusal can be taken to an Information Commission. If the real problem is delay or unfair treatment by an office, the Federal Ombudsman (Wafaqi Mohtasib) or the provincial Ombudsman can investigate, free of charge.",
      "آرٹیکل 19A ہر شہری کو عوامی اہمیت کے معاملات میں معلومات تک رسائی کا حق دیتا ہے، قانون کی عائد کردہ معقول پابندیوں کے تابع۔ وفاقی رائٹ آف ایکسس ٹو انفارمیشن ایکٹ 2017 اور صوبائی قوانین (مثلاً سندھ، پنجاب اور خیبر پختونخوا) اسے طریقۂ کار بناتے ہیں: آپ تحریری طور پر ریکارڈ مانگتے ہیں، عوامی ادارے کو مقررہ مدت میں جواب دینا ہوتا ہے، اور انکار انفارمیشن کمیشن میں لے جایا جا سکتا ہے۔ اگر اصل مسئلہ کسی دفتر کی تاخیر یا ناانصافی ہو تو وفاقی محتسب یا صوبائی محتسب مفت تحقیقات کر سکتا ہے۔",
      "آرٽيڪل 19A هر شهريءَ کي عوامي اهميت جي معاملن ۾ ڄاڻ تائين رسائيءَ جو حق ڏئي ٿو، قانون جي لڳايل معقول پابندين جي تابع. وفاقي رائيٽ آف ايڪسيس ٽو انفارميشن ايڪٽ 2017 ۽ صوبائي قانون (مثال طور سنڌ، پنجاب ۽ خيبر پختونخوا) ان کي طريقو بڻائين ٿا: توهان لکت ۾ رڪارڊ گهرو ٿا، عوامي اداري کي مقرر مدت اندر جواب ڏيڻو آهي، ۽ انڪار انفارميشن ڪميشن ڏانهن کڻي وڃي سگهجي ٿو. جيڪڏهن اصل مسئلو ڪنهن آفيس جي دير يا ناانصافي هجي ته وفاقي محتسب يا صوبائي محتسب مفت تحقيق ڪري سگهي ٿو."),
    [L("Identify the public body and whether a federal or provincial law applies.", "عوامی ادارے کی شناخت کریں اور دیکھیں کہ وفاقی یا صوبائی قانون لاگو ہے۔", "عوامي اداري جي سڃاڻپ ڪريو ۽ ڏسو ته وفاقي يا صوبائي قانون لاڳو آهي."),
     L("Write a clear request describing the records you want; keep a stamped copy or proof of delivery.", "مطلوبہ ریکارڈ بیان کرنے والی واضح درخواست لکیں؛ مہر شدہ نقل یا ڈیلیوری ثبوت رکھیں۔", "گهربل رڪارڊ بيان ڪندڙ واضح درخواست لکو؛ مهر ٿيل ڪاپي يا پهچائڻ جو ثبوت رکو."),
     L("If there is no reply or the request is refused, complain to the relevant Information Commission within the allowed time.", "جواب نہ آئے یا درخواست رد ہو تو مقررہ مدت میں متعلقہ انفارمیشن کمیشن میں شکایت کریں۔", "جواب نه اچي يا درخواست رد ٿئي ته مقرر مدت اندر لاڳاپيل انفارميشن ڪميشن ۾ شڪايت ڪريو."),
     L("For delay or unfair treatment, complain to the Federal or provincial Ombudsman.", "تاخیر یا ناانصافی پر وفاقی یا صوبائی محتسب کو شکایت کریں۔", "دير يا ناانصافي تي وفاقي يا صوبائي محتسب کي شڪايت ڪريو.")],
    ["faq-rti-how"],
    [(L("Which Article of the Constitution gives the right to information?", "آئین کا کون سا آرٹیکل معلومات کا حق دیتا ہے؟", "آئين جو ڪهڙو آرٽيڪل ڄاڻ جو حق ڏئي ٿو؟"), L("Article 19A.", "آرٹیکل 19A۔", "آرٽيڪل 19A.")),
     (L("Who can investigate maladministration by a federal office?", "وفاقی دفتر کی بدانتظامی کی تحقیقات کون کر سکتا ہے؟", "وفاقي آفيس جي بدانتظاميءَ جي تحقيق ڪير ڪري سگهي ٿو؟"), L("The Federal Ombudsman (Wafaqi Mohtasib).", "وفاقی محتسب۔", "وفاقي محتسب."))],
    ["right-to-information", "writ"],
    [("constitution-1973", "art-19a"), ("rti-federal-2017"), ("rti-sindh-2016"), ("rti-punjab-2013"), ("rti-kpk-2013"), ("wafaqi-mohtasib-1983")],
    ["right to information", "rti", "records", "ombudsman", "mohtasib", "government"], 5))

# ============================================================ 18 Legal aid
FAQS += [
    faq("faq-legal-aid",
        L("What if I cannot afford a lawyer?", "اگر میں وکیل کا خرچ نہ اٹھا سکوں تو؟", "جيڪڏهن مان وڪيل جو خرچ نه ڀري سگهان ته؟"),
        L("Legal aid exists for people who cannot afford a lawyer. The Legal Aid and Justice Authority Act, 2020 created a federal authority for this, and many district bar associations and courts run legal-aid committees or panels of lawyers. In criminal cases, ask the court whether a lawyer can be provided. Bring your CNIC and case papers, and verify the current procedure at the authority's office or website.",
          "قانونی امداد ان لوگوں کے لیے ہے جو وکیل کا خرچ نہیں اٹھا سکتے۔ لیگل ایڈ اینڈ جسٹس اتھارٹی ایکٹ 2020 نے اس کے لیے وفاقی اتھارٹی بنائی، اور کئی ضلعی بار ایسوسی ایشنز اور عدالتیں قانونی امداد کی کمیٹیاں یا وکلا کے پینل چلاتی ہیں۔ فوجداری مقدمات میں عدالت سے پوچھیں کہ وکیل فراہم ہو سکتا ہے یا نہیں۔ شناختی کارڈ اور مقدمے کے کاغذات ساتھ لائیں اور اتھارٹی کے دفتر یا ویب سائٹ پر موجودہ طریقہ تصدیق کریں۔",
          "قانوني مدد انهن ماڻهن لاءِ آهي جيڪي وڪيل جو خرچ نٿا ڀري سگهن. ليگل ايڊ اينڊ جسٽس اٿارٽي ايڪٽ 2020 ان لاءِ وفاقي اٿارٽي ٺاهي، ۽ ڪيتريون ئي ضلعي بار ايسوسيئيشنون ۽ عدالتون قانوني مدد جون ڪميٽيون يا وڪيلن جا پينل هلائين ٿيون. فوجداري ڪيسن ۾ عدالت کان پڇو ته وڪيل مهيا ٿي سگهي ٿو يا نه. شناختي ڪارڊ ۽ ڪيس جا ڪاغذ ساڻ آڻيو ۽ اٿارٽيءَ جي آفيس يا ويب سائيٽ تي موجوده طريقي جي تصديق ڪريو."),
        ["legal aid", "free lawyer", "cannot afford", "poor", "legal aid authority"], [("legal-aid-justice-authority-2020"), ("constitution-1973", "art-10")]),
]
CH.append(ch(
    18, "legal-aid-and-getting-help", 4, "legalaid",
    L("Legal aid and where to get help", "قانونی امداد اور مدد کہاں سے ملے", "قانوني مدد ۽ مدد ڪٿان ملي"),
    L("Free or low-cost help, ombudsmen, bar associations and how to choose a lawyer.",
      "مفت یا کم خرچ مدد، محتسب، بار ایسوسی ایشنز اور وکیل کا انتخاب کیسے کریں۔",
      "مفت يا گهٽ خرچ مدد، محتسب، بار ايسوسيئيشنون ۽ وڪيل جو چونڊ ڪيئن ڪجي."),
    L("Not being able to afford a lawyer should not mean being without justice. Article 10 gives an arrested person the right to a lawyer of their choice, and the Legal Aid and Justice Authority Act, 2020 provides for state-backed legal aid. District bar associations often run legal-aid committees, ombudsmen handle complaints against government offices without a lawyer, and Family Courts and Consumer Courts are designed to be accessible. When you do hire a lawyer, ask about fees in writing, ask for receipts, and keep copies of everything you sign.",
      "وکیل کا خرچ نہ اٹھا سکنے کا مطلب انصاف سے محرومی نہیں ہونا چاہیے۔ آرٹیکل 10 گرفتار شخص کو اپنی پسند کے وکیل کا حق دیتا ہے، اور لیگل ایڈ اینڈ جسٹس اتھارٹی ایکٹ 2020 ریاستی قانونی امداد فراہم کرتا ہے۔ ضلعی بار ایسوسی ایشنز اکثر قانونی امداد کی کمیٹیاں چلاتی ہیں، محتسب وکیل کے بغیر سرکاری دفاتر کے خلاف شکایات دیکھتے ہیں، اور فیملی کورٹس اور کنزیومر کورٹس قابلِ رسائی ہونے کے لیے بنائی گئی ہیں۔ وکیل کرتے وقت فیس تحریری طور پر پوچھیں، رسیدیں لیں اور ہر دستخط شدہ کاغذ کی نقل رکھیں۔",
      "وڪيل جو خرچ نه ڀري سگهڻ جو مطلب انصاف کان محروم رهڻ نه هئڻ گهرجي. آرٽيڪل 10 گرفتار ٿيل شخص کي پنهنجي پسند جي وڪيل جو حق ڏئي ٿو، ۽ ليگل ايڊ اينڊ جسٽس اٿارٽي ايڪٽ 2020 رياستي قانوني مدد مهيا ڪري ٿو. ضلعي بار ايسوسيئيشنون گهڻو ڪري قانوني مدد جون ڪميٽيون هلائين ٿيون، محتسب وڪيل کانسواءِ سرڪاري آفيسن خلاف شڪايتون ڏسن ٿا، ۽ فئملي ڪورٽون ۽ ڪنزيومر ڪورٽون پهچ جوڳيون هجڻ لاءِ ٺهيل آهن. وڪيل رکڻ وقت فيس لکت ۾ پڇو، رسيدون وٺو ۽ هر صحيح ٿيل ڪاغذ جي ڪاپي رکو."),
    [L("Write down your problem briefly with dates, and collect your documents.", "اپنا مسئلہ تاریخوں کے ساتھ مختصراً لکیں اور کاغذات جمع کریں۔", "پنهنجو مسئلو تاريخن سان مختصر لکو ۽ ڪاغذ گڏ ڪريو."),
     L("Contact the legal-aid authority or the district bar association's legal-aid committee.", "قانونی امداد کی اتھارٹی یا ضلعی بار ایسوسی ایشن کی قانونی امداد کمیٹی سے رابطہ کریں۔", "قانوني مدد جي اٿارٽي يا ضلعي بار ايسوسيئيشن جي قانوني مدد ڪميٽي سان رابطو ڪريو."),
     L("For complaints about a government office, use the Federal or provincial Ombudsman.", "سرکاری دفتر کے خلاف شکایت کے لیے وفاقی یا صوبائی محتسب سے رجوع کریں۔", "سرڪاري آفيس خلاف شڪايت لاءِ وفاقي يا صوبائي محتسب ڏانهن وڃو."),
     L("If hiring a lawyer, agree fees in writing, get receipts and ask for copies of every filing.", "وکیل کرنا ہو تو فیس تحریری طے کریں، رسیدیں لیں اور ہر درخواست کی نقل مانگیں۔", "وڪيل رکڻو هجي ته فيس لکت ۾ طئه ڪريو، رسيدون وٺو ۽ هر درخواست جي ڪاپي گهرو.")],
    ["faq-legal-aid"],
    [(L("Which Act established a federal legal-aid authority?", "وفاقی قانونی امداد کی اتھارٹی کس ایکٹ نے قائم کی؟", "وفاقي قانوني مدد جي اٿارٽي ڪهڙي ايڪٽ قائم ڪئي؟"), L("The Legal Aid and Justice Authority Act, 2020.", "لیگل ایڈ اینڈ جسٹس اتھارٹی ایکٹ 2020۔", "ليگل ايڊ اينڊ جسٽس اٿارٽي ايڪٽ 2020."))],
    ["arrest", "bail"],
    [("legal-aid-justice-authority-2020"), ("constitution-1973", "art-10"), ("wafaqi-mohtasib-1983")],
    ["legal aid", "free lawyer", "bar association", "ombudsman", "help"], 4))
