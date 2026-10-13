"""Site copy and URL language helpers for English, Lithuanian, Latvian, and Estonian."""

LANGUAGES = {
    "en": {"native": "English", "locale": "en_GB", "hreflang": "en"},
    "lt": {"native": "Lietuvių", "locale": "lt_LT", "hreflang": "lt"},
    "lv": {"native": "Latviešu", "locale": "lv_LV", "hreflang": "lv"},
    "et": {"native": "Eesti", "locale": "et_EE", "hreflang": "et"},
}
DEFAULT_LANG = "en"

# Copy is ordered EN / LT / LV / ET. Missing translations fall back to English.
# Text between asterisks is rendered with emphasis (italic amber in headings).
_COPY = {
    # Navigation and shared chrome
    "skip": ("Skip to content", "Pereiti prie turinio", "Pāriet uz saturu", "Liigu sisu juurde"),
    "menu": ("Menu", "Meniu", "Izvēlne", "Menüü"),
    "language": ("Language", "Kalba", "Valoda", "Keel"),
    "nav_advisory": ("Advisory", "Konsultavimas", "Konsultācijas", "Nõustamine"),
    "nav_intelligence": ("Intelligence", "Analitika", "Analītika", "Analüütika"),
    "nav_sectors": ("Sectors", "Sektoriai", "Nozares", "Sektorid"),
    "nav_team": ("Team", "Komanda", "Komanda", "Meeskond"),
    "nav_contact": ("Contact", "Kontaktai", "Kontakti", "Kontakt"),
    "header_cta": ("Enquire", "Susisiekti", "Sazināties", "Võta ühendust"),
    "footer_tagline": (
        "Discreet M&A counsel for the Baltics and Central and Eastern Europe, sharpened by proprietary intelligence and led by senior judgement.",
        "Diskretiškos M&A konsultacijos Baltijos šalyse bei Vidurio ir Rytų Europoje, paremtos nuosava analitika ir patyrusių konsultantų sprendimais.",
        "Diskrētas M&A konsultācijas Baltijā un Centrālajā un Austrumeiropā, ko stiprina pašu izstrādāta analītika un pieredzējušu konsultantu spriedums.",
        "Diskreetne M&A nõustamine Baltikumis ning Kesk- ja Ida-Euroopas, mida toetab oma analüütikaplatvorm ja juhib kogenud nõustajate otsustusvõime.",
    ),
    "footer_explore": ("Explore", "Naršyti", "Izpētīt", "Sisukord"),
    "footer_company": ("Company", "Įmonė", "Uzņēmums", "Ettevõte"),
    "footer_contact": ("Contact", "Kontaktai", "Kontakti", "Kontakt"),
    "company_number": ("Company number", "Įmonės kodas", "Uzņēmuma numurs", "Registrikood"),
    "footer_registered": (
        "Curonia Capital Ltd is registered in England and Wales, company number 14537690.",
        "Curonia Capital Ltd registruota Anglijoje ir Velse, įmonės kodas 14537690.",
        "Curonia Capital Ltd ir reģistrēts Anglijā un Velsā, uzņēmuma numurs 14537690.",
        "Curonia Capital Ltd on registreeritud Inglismaal ja Walesis, registrikood 14537690.",
    ),
    "footer_rights": ("All rights reserved.", "Visos teisės saugomos.", "Visas tiesības aizsargātas.", "Kõik õigused kaitstud."),

    # Page titles and descriptions
    "title_home": (
        "Discreet M&A counsel for the Baltics and CEE",
        "Diskretiškos M&A konsultacijos Baltijos šalyse ir VRE",
        "Diskrētas M&A konsultācijas Baltijā un CAE",
        "Diskreetne M&A nõustamine Baltikumis ja KIEs",
    ),
    "desc_home": (
        "Senior-led M&A advisory for owners, investors and boards in the Baltics and CEE, sharpened by proprietary deal intelligence built on LiquidRound.",
        "Patyrusių konsultantų vadovaujamos M&A konsultacijos savininkams, investuotojams ir valdyboms Baltijos šalyse ir VRE, paremtos nuosava LiquidRound pagrindu sukurta analitika.",
        "Pieredzējušu konsultantu vadītas M&A konsultācijas īpašniekiem, investoriem un valdēm Baltijā un CAE, ko stiprina pašu analītika, veidota uz LiquidRound bāzes.",
        "Kogenud nõustajate juhitud M&A nõustamine omanikele, investoritele ja juhatustele Baltikumis ja KIEs, mida toetab LiquidRoundile ehitatud oma tehinguanalüütika.",
    ),
    "title_advisory": ("M&A advisory services", "M&A konsultavimo paslaugos", "M&A konsultāciju pakalpojumi", "M&A nõustamisteenused"),
    "desc_advisory": (
        "Sell-side, buy-side and strategic options advisory across the Baltics and CEE, led by senior advisers from mandate to completion.",
        "Pardavėjo, pirkėjo ir strateginių alternatyvų konsultacijos Baltijos šalyse ir VRE, kurioms nuo pavedimo iki užbaigimo vadovauja patyrę konsultantai.",
        "Pārdevēja, pircēja un stratēģisko iespēju konsultācijas Baltijā un CAE, ko no uzdevuma līdz noslēgumam vada pieredzējuši konsultanti.",
        "Müüja- ja ostjapoolne nõustamine ning strateegiliste valikute hindamine Baltikumis ja KIEs, mida juhivad kogenud nõustajad mandaadist tehingu lõpuni.",
    ),
    "title_intelligence": (
        "Proprietary deal intelligence",
        "Nuosava sandorių analitika",
        "Pašu izstrādāta darījumu analītika",
        "Oma tehinguanalüütika",
    ),
    "desc_intelligence": (
        "How Curonia's proprietary platform, built on LiquidRound, supports sourcing, analysis, document review and materials, with advisers accountable for every output.",
        "Kaip nuosava Curonia platforma, sukurta LiquidRound pagrindu, padeda paieškai, analizei, dokumentų peržiūrai ir medžiagos rengimui, o konsultantai atsako už kiekvieną rezultatą.",
        "Kā Curonia platforma, veidota uz LiquidRound bāzes, atbalsta atlasi, analīzi, dokumentu pārskatīšanu un materiālu sagatavošanu, konsultantiem atbildot par katru rezultātu.",
        "Kuidas Curonia LiquidRoundile ehitatud platvorm toetab otsingut, analüüsi, dokumentide läbivaatust ja materjalide koostamist, kusjuures iga tulemuse eest vastutab nõustaja.",
    ),
    "title_sectors": ("Sector focus", "Sektoriai", "Nozares", "Sektorid"),
    "desc_sectors": (
        "Technology, healthcare, business services, industrials and consumer: sectors where Curonia advises on M&A in the Baltics and CEE.",
        "Technologijos, sveikatos priežiūra, verslo paslaugos, pramonė ir vartojimas: sektoriai, kuriuose Curonia konsultuoja M&A klausimais Baltijos šalyse ir VRE.",
        "Tehnoloģijas, veselības aprūpe, biznesa pakalpojumi, rūpniecība un patēriņš: nozares, kurās Curonia konsultē M&A darījumos Baltijā un CAE.",
        "Tehnoloogia, tervishoid, äriteenused, tööstus ja tarbekaubad: sektorid, kus Curonia nõustab M&A tehinguid Baltikumis ja KIEs.",
    ),
    "title_team": ("Team", "Komanda", "Komanda", "Meeskond"),
    "desc_team": (
        "A small, senior team combining investment banking, investment and applied AI experience.",
        "Nedidelė patyrusi komanda, jungianti investicinės bankininkystės, investavimo ir taikomojo AI patirtį.",
        "Neliela, pieredzējusi komanda, kas apvieno investīciju banku, investīciju un lietišķā AI pieredzi.",
        "Väike kogenud meeskond, kes ühendab investeerimispanganduse, investeerimise ja rakendusliku tehisintellekti kogemuse.",
    ),
    "title_contact": ("Confidential enquiries", "Konfidencialūs užklausimai", "Konfidenciāli pieprasījumi", "Konfidentsiaalsed päringud"),
    "desc_contact": (
        "Arrange a confidential conversation with Curonia Capital about a sale, acquisition or strategic review.",
        "Susitarkite dėl konfidencialaus pokalbio su Curonia Capital apie pardavimą, įsigijimą ar strateginę peržiūrą.",
        "Vienojieties par konfidenciālu sarunu ar Curonia Capital par pārdošanu, iegādi vai stratēģisku izvērtējumu.",
        "Leppige Curonia Capitaliga kokku konfidentsiaalne vestlus müügi, omandamise või strateegilise ülevaate teemal.",
    ),
    "title_404": ("Page not found", "Puslapis nerastas", "Lapa nav atrasta", "Lehte ei leitud"),

    # Home: hero
    "hero_eyebrow": (
        "M&A advisory · Baltics & CEE",
        "M&A konsultacijos · Baltija ir VRE",
        "M&A konsultācijas · Baltija un CAE",
        "M&A nõustamine · Baltikum ja KIE",
    ),
    "hero_heading": (
        "Discreet counsel for *decisive* transactions.",
        "Diskretiški patarimai *lemiamiems* sandoriams.",
        "Diskrēts padoms *izšķirošos* darījumos.",
        "Diskreetne nõu *otsustavates* tehingutes.",
    ),
    "hero_lede": (
        "Senior-led advice for owners, investors and boards, sharpened by proprietary deal intelligence. The judgement is always ours, and every mandate has senior attention from first conversation to completion.",
        "Patyrusių konsultantų vadovaujamos konsultacijos savininkams, investuotojams ir valdyboms, sustiprintos nuosava sandorių analitika. Vertinimą visada atliekame patys, o kiekvienam pavedimui patyrę specialistai skiria dėmesį nuo pirmo pokalbio iki sandorio užbaigimo.",
        "Pieredzējušu konsultantu vadītas konsultācijas īpašniekiem, investoriem un valdēm, ko stiprina pašu izstrādāta darījumu analītika. Spriedums vienmēr ir mūsu, un katram uzdevumam pieredzējuši speciālisti pievēršas no pirmās sarunas līdz darījuma noslēgumam.",
        "Kogenud nõustajate juhitud nõu omanikele, investoritele ja juhatustele, mida teravdab meie oma tehinguanalüütika. Hinnangu anname alati ise ning iga mandaadiga tegeleb kogenud nõustaja esimesest vestlusest tehingu lõpuni.",
    ),
    "hero_primary": (
        "Arrange a confidential conversation",
        "Susitarti dėl konfidencialaus pokalbio",
        "Vienoties par konfidenciālu sarunu",
        "Lepi kokku konfidentsiaalne vestlus",
    ),
    "hero_secondary": ("Our intelligence", "Mūsų analitika", "Mūsu analītika", "Meie analüütika"),

    # Home: approach and principles
    "approach_label": ("Approach", "Požiūris", "Pieeja", "Lähenemine"),
    "approach_statement": (
        "We take on a deliberately small number of mandates. *Each is led by a senior adviser from the first question to signing, informed by intelligence that would otherwise take weeks to assemble.*",
        "Sąmoningai imamės nedidelio pavedimų skaičiaus. *Kiekvienam nuo pirmojo klausimo iki pasirašymo vadovauja patyręs konsultantas, remdamasis analitika, kurios surinkimas kitaip užtruktų savaites.*",
        "Mēs apzināti uzņemamies nelielu skaitu uzdevumu. *Katru no pirmā jautājuma līdz parakstīšanai vada pieredzējis konsultants, balstoties uz analītiku, kuras apkopošana citādi aizņemtu nedēļas.*",
        "Võtame teadlikult vastu vähe mandaate. *Igaüht juhib kogenud nõustaja esimesest küsimusest allkirjastamiseni, toetudes analüütikale, mille kokkupanek võtaks muidu nädalaid.*",
    ),
    "principles_label": ("Principles", "Principai", "Principi", "Põhimõtted"),
    "principle_1_title": ("Senior-led", "Vadovauja patyrę", "Vada pieredzējuši", "Kogenud juhtimine"),
    "principle_1_body": (
        "A senior adviser leads every mandate and attends every meeting that matters.",
        "Kiekvienam pavedimui vadovauja patyręs konsultantas, dalyvaujantis visuose svarbiuose susitikimuose.",
        "Katru uzdevumu vada pieredzējis konsultants, kas piedalās visās būtiskajās tikšanās reizēs.",
        "Iga mandaati juhib kogenud nõustaja, kes osaleb kõigil olulistel kohtumistel.",
    ),
    "principle_2_title": ("Selective", "Atrenkame kruopščiai", "Selektīvi", "Valikuline"),
    "principle_2_body": (
        "We accept a limited number of mandates so that each receives our full attention.",
        "Priimame ribotą pavedimų skaičių, kad kiekvienam galėtume skirti visą dėmesį.",
        "Pieņemam ierobežotu uzdevumu skaitu, lai katram varētu veltīt pilnu uzmanību.",
        "Võtame vastu piiratud arvu mandaate, et igaüks saaks meie täieliku tähelepanu.",
    ),
    "principle_3_title": ("Confidential", "Konfidencialiai", "Konfidenciāli", "Konfidentsiaalne"),
    "principle_3_body": (
        "Discretion shapes how we approach counterparties and how we handle every document.",
        "Diskretiškumas lemia, kaip kreipiamės į kitas šalis ir kaip tvarkome kiekvieną dokumentą.",
        "Diskrētums nosaka, kā uzrunājam darījuma puses un kā apstrādājam katru dokumentu.",
        "Diskreetsus määrab, kuidas läheneme vastaspooltele ja kuidas käsitleme iga dokumenti.",
    ),
    "principle_4_title": ("Considered", "Apgalvotai", "Pārdomāti", "Läbimõeldud"),
    "principle_4_body": (
        "Clear recommendations, including when the right answer is to wait.",
        "Aiškios rekomendacijos, net jei teisingas atsakymas yra palaukti.",
        "Skaidri ieteikumi, arī tad, ja pareizā atbilde ir nogaidīt.",
        "Selged soovitused, ka siis, kui õige vastus on oodata.",
    ),

    # Services
    "services_label": ("Advisory", "Konsultavimas", "Konsultācijas", "Nõustamine"),
    "services_heading": (
        "Advice for both sides of the *transaction*.",
        "Konsultacijos abiem *sandorio* pusėms.",
        "Konsultācijas abām *darījuma* pusēm.",
        "Nõustamine *tehingu* mõlemale poolele.",
    ),
    "sell_title": ("Sell-side advisory", "Pardavėjo konsultavimas", "Pārdevēja konsultācijas", "Müüjapoolne nõustamine"),
    "sell_body": (
        "Position the business, map credible buyers and run a disciplined process through negotiation to completion.",
        "Tinkamai pristatome verslą, nustatome patikimus pirkėjus ir nuosekliai valdome procesą per derybas iki sandorio užbaigimo.",
        "Pozicionējam uzņēmumu, apzinām nopietnus pircējus un disciplinēti vadām procesu cauri sarunām līdz darījuma noslēgumam.",
        "Positsioneerime ettevõtte, kaardistame tõsiseltvõetavad ostjad ning juhime distsiplineeritud protsessi läbirääkimistest tehingu lõpuni.",
    ),
    "buy_title": ("Buy-side advisory", "Pirkėjo konsultavimas", "Pircēja konsultācijas", "Ostjapoolne nõustamine"),
    "buy_body": (
        "Turn an acquisition thesis into sourced targets, valuation support and coordinated diligence.",
        "Įsigijimo strategiją paverčiame konkrečiais taikiniais, vertinimo analize ir koordinuotu išsamiu patikrinimu.",
        "Pārvēršam iegādes stratēģiju konkrētos mērķos, vērtēšanas atbalstā un koordinētā padziļinātā izpētē.",
        "Muudame omandamisstrateegia konkreetseteks sihtettevõteteks, hindamistoeks ja koordineeritud due diligence'iks.",
    ),
    "strategy_title": ("Strategic options", "Strateginės alternatyvos", "Stratēģiskās iespējas", "Strateegilised valikud"),
    "strategy_body": (
        "Weigh exits, acquisitions and partnerships before committing to a path.",
        "Įvertiname pardavimo, įsigijimo ir partnerystės galimybes prieš pasirenkant kryptį.",
        "Izvērtējam pārdošanu, iegādes un partnerības pirms konkrēta ceļa izvēles.",
        "Kaalume müüki, omandamisi ja partnerlusi enne, kui suund valitakse.",
    ),
    "services_link": ("Our advisory in detail", "Plačiau apie konsultavimą", "Sīkāk par konsultācijām", "Nõustamisest lähemalt"),

    # Intelligence band
    "intel_label": ("Intelligence", "Analitika", "Analītika", "Analüütika"),
    "intel_heading": (
        "Proprietary intelligence. *Human* judgement.",
        "Nuosava analitika. *Žmogaus* sprendimas.",
        "Pašu analītika. *Cilvēka* spriedums.",
        "Oma analüütika. *Inimese* otsustus.",
    ),
    "intel_lede": (
        "Our proprietary platform, built on LiquidRound, maps buyer and target universes, assembles comparables and prepares first drafts, so our time goes into judgement rather than assembly. Advisers verify every output and remain accountable for every recommendation.",
        "Mūsų nuosava platforma, sukurta LiquidRound pagrindu, sudaro pirkėjų ir taikinių žemėlapius, surenka palyginamuosius duomenis ir parengia pirminius juodraščius, todėl savo laiką skiriame vertinimui, o ne duomenų rinkimui. Konsultantai tikrina kiekvieną rezultatą ir atsako už kiekvieną rekomendaciją.",
        "Mūsu platforma, veidota uz LiquidRound bāzes, kartē pircēju un mērķu loku, apkopo salīdzināmos datus un sagatavo pirmos projektus, lai mūsu laiks tiktu veltīts spriedumam, nevis datu vākšanai. Konsultanti pārbauda katru rezultātu un atbild par katru ieteikumu.",
        "Meie LiquidRoundile ehitatud platvorm kaardistab ostjate ja sihtettevõtete ringi, koondab võrdlusandmed ja koostab esimesed mustandid, et meie aeg kuluks hinnangute andmisele, mitte andmete kogumisele. Nõustajad kontrollivad iga tulemust ja vastutavad iga soovituse eest.",
    ),
    "cap_1_kicker": ("Source", "Paieška", "Atlase", "Otsing"),
    "cap_1_title": ("Buyer and target universes", "Pirkėjai ir taikiniai", "Pircēji un mērķi", "Ostjad ja sihtettevõtted"),
    "cap_1_body": (
        "Screened and ranked against the mandate.",
        "Atrinkti ir įvertinti pagal pavedimo tikslus.",
        "Atlasīti un sarindoti atbilstoši uzdevumam.",
        "Sõelutud ja järjestatud mandaadi järgi.",
    ),
    "cap_2_kicker": ("Analyse", "Analizė", "Analīze", "Analüüs"),
    "cap_2_title": ("Comparables and value", "Palyginimai ir vertė", "Salīdzinājumi un vērtība", "Võrdlused ja väärtus"),
    "cap_2_body": (
        "Market data and source documents in one structured view.",
        "Rinkos duomenys ir pirminiai dokumentai vienoje struktūruotoje apžvalgoje.",
        "Tirgus dati un avota dokumenti vienā strukturētā skatā.",
        "Turuandmed ja algdokumendid ühes struktureeritud vaates.",
    ),
    "cap_3_kicker": ("Review", "Peržiūra", "Pārskate", "Läbivaatus"),
    "cap_3_title": ("Document intelligence", "Dokumentų analizė", "Dokumentu analīze", "Dokumendianalüüs"),
    "cap_3_body": (
        "Faster, more thorough reading of data rooms and filings.",
        "Greitesnė ir išsamesnė duomenų kambarių bei ataskaitų peržiūra.",
        "Ātrāka un rūpīgāka datu telpu un pārskatu izpēte.",
        "Andmeruumide ja aruannete kiirem ning põhjalikum läbitöötamine.",
    ),
    "cap_4_kicker": ("Prepare", "Rengimas", "Sagatavošana", "Koostamine"),
    "cap_4_title": ("First-draft materials", "Pirminė medžiaga", "Pirmie projekti", "Esimesed mustandid"),
    "cap_4_body": (
        "Memoranda and teasers, refined by advisers.",
        "Memorandumai ir trumpi pristatymai, kuriuos tobulina konsultantai.",
        "Memorandi un īsie apraksti, ko pilnveido konsultanti.",
        "Memod ja tutvustused, mida nõustajad lihvivad.",
    ),
    "intel_principle": (
        "Technology accelerates preparation. It never makes the decision.",
        "Technologija pagreitina pasirengimą. Sprendimų ji niekada nepriima.",
        "Tehnoloģija paātrina sagatavošanos. Lēmumus tā nepieņem nekad.",
        "Tehnoloogia kiirendab ettevalmistust. Otsuseid see kunagi ei tee.",
    ),
    "intel_link": ("How our intelligence works", "Kaip veikia mūsų analitika", "Kā darbojas mūsu analītika", "Kuidas meie analüütika töötab"),

    # Region
    "region_label": ("Region", "Regionas", "Reģions", "Piirkond"),
    "region_heading": (
        "Baltic roots. *CEE* reach.",
        "Baltijos šaknys. *VRE* aprėptis.",
        "Baltijas saknes. *CAE* tvērums.",
        "Balti juured. *KIE* haare.",
    ),
    "region_body": (
        "We focus on Lithuania, Latvia and Estonia, with a cross-border view of Poland and the wider region. Many of the buyers and investors who matter sit in London, the Nordics and Western Europe, and we bring them into the conversation.",
        "Daugiausia dirbame Lietuvoje, Latvijoje ir Estijoje, taip pat tarpvalstybiniu žvilgsniu aprėpiame Lenkiją ir platesnį regioną. Daug svarbių pirkėjų ir investuotojų yra Londone, Šiaurės šalyse ir Vakarų Europoje, ir mes juos įtraukiame į pokalbį.",
        "Galvenokārt strādājam Lietuvā, Latvijā un Igaunijā, ar pārrobežu skatījumu uz Poliju un plašāku reģionu. Daudzi nozīmīgi pircēji un investori atrodas Londonā, Ziemeļvalstīs un Rietumeiropā, un mēs viņus iesaistām sarunā.",
        "Keskendume Leedule, Lätile ja Eestile ning vaatame piiriüleselt ka Poolat ja laiemat piirkonda. Paljud olulised ostjad ja investorid asuvad Londonis, Põhjamaades ja Lääne-Euroopas ning me toome nad vestlusesse.",
    ),
    "market_lt": ("Lithuania", "Lietuva", "Lietuva", "Leedu"),
    "market_lv": ("Latvia", "Latvija", "Latvija", "Läti"),
    "market_ee": ("Estonia", "Estija", "Igaunija", "Eesti"),
    "market_pl": ("Poland", "Lenkija", "Polija", "Poola"),
    "market_cee": ("Wider CEE", "Platesnė VRE", "Plašāka CAE", "Laiem KIE"),
    "region_base": ("Advised from London", "Konsultuojame iš Londono", "Konsultējam no Londonas", "Nõustame Londonist"),

    # Team teaser
    "team_label": ("Team", "Komanda", "Komanda", "Meeskond"),
    "team_teaser_heading": (
        "Small by design. *Senior* throughout.",
        "Sąmoningai nedidelė. *Patyrusi* kiekviename žingsnyje.",
        "Apzināti neliela. *Pieredzējusi* ik solī.",
        "Teadlikult väike. *Kogenud* igas etapis.",
    ),
    "team_teaser_body": (
        "Investment banking, investment and applied AI experience in one compact team, so the people you meet are the people who do the work.",
        "Investicinės bankininkystės, investavimo ir taikomojo AI patirtis vienoje kompaktiškoje komandoje, todėl žmonės, su kuriais susitinkate, patys ir atlieka darbą.",
        "Investīciju banku, investīciju un lietišķā AI pieredze vienā kompaktā komandā, tāpēc cilvēki, ar kuriem tiekaties, paši arī veic darbu.",
        "Investeerimispanganduse, investeerimise ja rakendusliku tehisintellekti kogemus ühes kompaktses meeskonnas, nii et inimesed, kellega kohtute, teevad ka töö ise ära.",
    ),
    "team_link": ("Meet the team", "Susipažinkite su komanda", "Iepazīstieties ar komandu", "Tutvu meeskonnaga"),

    # Closing call to action
    "cta_label": ("Start a conversation", "Pradėkime pokalbį", "Sāksim sarunu", "Alustame vestlust"),
    "cta_heading": (
        "Considering a transaction in the Baltics or *CEE*?",
        "Svarstote sandorį Baltijos šalyse ar *VRE*?",
        "Apsverat darījumu Baltijā vai *CAE*?",
        "Kaalute tehingut Baltikumis või *KIEs*?",
    ),
    "cta_body": (
        "A short outline of your business and objectives is enough to begin. Every enquiry is read by a senior adviser and treated in confidence.",
        "Pradžiai pakanka trumpo verslo ir tikslų aprašymo. Kiekvieną užklausimą perskaito patyręs konsultantas ir jis traktuojamas konfidencialiai.",
        "Sākumam pietiek ar īsu uzņēmuma un mērķu aprakstu. Katru pieprasījumu izlasa pieredzējis konsultants, un tas tiek uzskatīts par konfidenciālu.",
        "Alustuseks piisab ettevõtte ja eesmärkide lühikirjeldusest. Iga päringu loeb läbi kogenud nõustaja ja seda käsitletakse konfidentsiaalselt.",
    ),
    "cta_button": (
        "Arrange a confidential conversation",
        "Susitarti dėl konfidencialaus pokalbio",
        "Vienoties par konfidenciālu sarunu",
        "Lepi kokku konfidentsiaalne vestlus",
    ),

    # Advisory page
    "advisory_heading": (
        "M&A advice built around your *objectives*.",
        "M&A konsultacijos pagal jūsų *tikslus*.",
        "M&A konsultācijas, veidotas ap jūsu *mērķiem*.",
        "M&A nõustamine teie *eesmärkidest* lähtudes.",
    ),
    "advisory_lede": (
        "Whether you are selling a company, pursuing an acquisition or weighing strategic options, we bring structure, market insight and independent judgement to complex cross-border decisions.",
        "Parduodant įmonę, siekiant įsigijimo ar vertinant strategines alternatyvas, sudėtingiems tarpvalstybiniams sprendimams suteikiame struktūrą, rinkos įžvalgų ir nepriklausomą vertinimą.",
        "Pārdodot uzņēmumu, īstenojot iegādi vai izvērtējot stratēģiskās iespējas, sarežģītos pārrobežu lēmumos ienesam struktūru, tirgus izpratni un neatkarīgu spriedumu.",
        "Olgu tegu ettevõtte müügi, omandamise või strateegiliste valikute kaalumisega, toome keerukatesse piiriülestesse otsustesse struktuuri, turutunnetuse ja sõltumatu hinnangu.",
    ),
    "includes": ("Includes", "Apima", "Ietver", "Sisaldab"),
    "sell_p1": ("Equity story and positioning", "Investicinė istorija ir pozicionavimas", "Investīciju stāsts un pozicionējums", "Investeerimislugu ja positsioneerimine"),
    "sell_p2": ("Buyer universe and outreach", "Pirkėjų ratas ir kontaktai", "Pircēju loks un uzrunāšana", "Ostjate ring ja pöördumised"),
    "sell_p3": ("Process management to completion", "Proceso valdymas iki užbaigimo", "Procesa vadība līdz noslēgumam", "Protsessi juhtimine tehingu lõpuni"),
    "buy_p1": ("Target sourcing and screening", "Taikinių paieška ir atranka", "Mērķu meklēšana un atlase", "Sihtettevõtete otsing ja sõelumine"),
    "buy_p2": ("Valuation and structuring support", "Vertinimo ir struktūravimo pagalba", "Vērtēšanas un strukturēšanas atbalsts", "Hindamis- ja struktureerimistugi"),
    "buy_p3": ("Diligence coordination", "Išsamaus patikrinimo koordinavimas", "Padziļinātās izpētes koordinēšana", "Due diligence'i koordineerimine"),
    "strategy_p1": ("Exit and ownership options", "Pasitraukimo ir nuosavybės alternatyvos", "Iziešanas un īpašumtiesību iespējas", "Väljumise ja omandi valikud"),
    "strategy_p2": ("Transaction readiness review", "Pasirengimo sandoriui peržiūra", "Gatavības darījumam izvērtējums", "Tehinguvalmiduse hindamine"),
    "strategy_p3": ("Partnership and joint venture assessment", "Partnerystės ir bendrų įmonių vertinimas", "Partnerību un kopuzņēmumu izvērtējums", "Partnerluste ja ühisettevõtete hindamine"),
    "clients_label": ("Clients", "Klientai", "Klienti", "Kliendid"),
    "clients_heading": ("Who we *advise*.", "Ką *konsultuojame*.", "Ko mēs *konsultējam*.", "Keda me *nõustame*."),
    "client_1_title": ("Founders and families", "Įkūrėjai ir šeimos", "Dibinātāji un ģimenes", "Asutajad ja perekonnad"),
    "client_1_body": (
        "Owners preparing for a sale, succession or a partner to fund the next stage.",
        "Savininkai, besiruošiantys pardavimui, verslo perdavimui ar ieškantys partnerio kitam augimo etapui finansuoti.",
        "Īpašnieki, kas gatavojas pārdošanai, paaudžu maiņai vai meklē partneri nākamā posma finansēšanai.",
        "Omanikud, kes valmistuvad müügiks, põlvkonnavahetuseks või otsivad partnerit järgmise etapi rahastamiseks.",
    ),
    "client_2_title": ("Investors", "Investuotojai", "Investori", "Investorid"),
    "client_2_body": (
        "Private equity and family offices building, adding to or exiting regional positions.",
        "Privataus kapitalo fondai ir šeimos biurai, kuriantys, didinantys ar parduodantys regionines pozicijas.",
        "Privātā kapitāla fondi un ģimenes biroji, kas veido, papildina vai pārdod reģionālās pozīcijas.",
        "Erakapitalifondid ja pereinvesteerimisettevõtted, kes loovad, suurendavad või müüvad piirkondlikke positsioone.",
    ),
    "client_3_title": ("Corporate boards", "Įmonių valdybos", "Uzņēmumu valdes", "Ettevõtete juhatused"),
    "client_3_body": (
        "Leadership teams considering acquisitions, carve-outs or entry to Baltic markets.",
        "Vadovų komandos, svarstančios įsigijimus, verslo dalių atskyrimą ar žengimą į Baltijos rinkas.",
        "Vadības komandas, kas apsver iegādes, uzņēmuma daļu nodalīšanu vai ienākšanu Baltijas tirgos.",
        "Juhtkonnad, kes kaaluvad omandamisi, äriüksuste eraldamist või Balti turgudele sisenemist.",
    ),
    "process_label": ("Process", "Procesas", "Process", "Protsess"),
    "advisory_process": (
        "A focused transaction *process*.",
        "Kryptingas sandorio *procesas*.",
        "Mērķtiecīgs darījuma *process*.",
        "Sihipärane *tehinguprotsess*.",
    ),
    "process_1_title": ("Define the mandate", "Apibrėžti pavedimą", "Definēt uzdevumu", "Määratle mandaat"),
    "process_1_body": (
        "Agree objectives, constraints, timing and who makes the decisions.",
        "Sutariame dėl tikslų, apribojimų, terminų ir sprendimų priėmėjų.",
        "Vienojamies par mērķiem, ierobežojumiem, termiņiem un lēmumu pieņēmējiem.",
        "Lepime kokku eesmärgid, piirangud, ajakava ja otsustajad.",
    ),
    "process_2_title": ("Map the market", "Ištirti rinką", "Izpētīt tirgu", "Kaardista turg"),
    "process_2_body": (
        "Research the relevant buyers, targets and comparable transactions.",
        "Tiriame aktualius pirkėjus, taikinius ir palyginamus sandorius.",
        "Izpētām atbilstošos pircējus, mērķus un salīdzināmos darījumus.",
        "Uurime asjakohaseid ostjaid, sihtettevõtteid ja võrreldavaid tehinguid.",
    ),
    "process_3_title": ("Build the case", "Parengti argumentus", "Sagatavot pamatojumu", "Koosta põhjendus"),
    "process_3_body": (
        "Prepare positioning, valuation work and materials for the next decision.",
        "Rengiame pozicionavimą, vertinimą ir medžiagą kitam sprendimui.",
        "Sagatavojam pozicionējumu, vērtējumu un materiālus nākamajam lēmumam.",
        "Valmistame ette positsioneerimise, hindamise ja materjalid järgmiseks otsuseks.",
    ),
    "process_4_title": ("Execute with care", "Įgyvendinti atsakingai", "Īstenot rūpīgi", "Vii hoolikalt ellu"),
    "process_4_body": (
        "Coordinate discussions, diligence and negotiations through to completion.",
        "Koordinuojame pokalbius, išsamų patikrinimą ir derybas iki sandorio užbaigimo.",
        "Koordinējam sarunas, padziļināto izpēti un pārrunas līdz darījuma noslēgumam.",
        "Koordineerime arutelusid, due diligence'i ja läbirääkimisi kuni tehingu lõpuni.",
    ),

    # Intelligence page
    "platform_heading": (
        "Proprietary intelligence for every stage of a *transaction*.",
        "Nuosava analitika kiekvienam *sandorio* etapui.",
        "Pašu analītika katram *darījuma* posmam.",
        "Oma analüütika *tehingu* igaks etapiks.",
    ),
    "platform_lede": (
        "Curonia's proprietary platform, built on LiquidRound, brings research, analysis and drafting into one workflow. It extends what a small senior team can see and prepare, without replacing the judgement clients rely on.",
        "Nuosava Curonia platforma, sukurta LiquidRound pagrindu, sujungia tyrimus, analizę ir dokumentų rengimą į vieną darbo eigą. Ji išplečia tai, ką nedidelė patyrusi komanda gali pamatyti ir parengti, nepakeisdama vertinimo, kuriuo pasikliauja klientai.",
        "Curonia platforma, veidota uz LiquidRound bāzes, apvieno izpēti, analīzi un dokumentu sagatavošanu vienā darba plūsmā. Tā paplašina to, ko neliela pieredzējusi komanda spēj redzēt un sagatavot, neaizstājot spriedumu, uz kuru paļaujas klienti.",
        "Curonia LiquidRoundile ehitatud platvorm koondab uuringud, analüüsi ja dokumentide koostamise ühte töövoogu. See avardab seda, mida väike kogenud meeskond suudab näha ja ette valmistada, asendamata otsustusvõimet, millele kliendid toetuvad.",
    ),
    "lifecycle_label": ("Lifecycle", "Ciklas", "Cikls", "Tehingu kulg"),
    "lifecycle_heading": (
        "Across the transaction *lifecycle*.",
        "Visame sandorio *cikle*.",
        "Visā darījuma *ciklā*.",
        "Kogu tehingu *vältel*.",
    ),
    "platform_1_title": ("Source and screen", "Rasti ir atrinkti", "Atrast un atlasīt", "Leia ja sõelu"),
    "platform_1_body": (
        "Explore buyer and target universes, build profiles and test fit against the mandate.",
        "Tiriame pirkėjų ir taikinių ratą, rengiame profilius ir vertiname atitiktį pavedimui.",
        "Izpētām pircēju un mērķu loku, veidojam profilus un vērtējam atbilstību uzdevumam.",
        "Uurime ostjate ja sihtettevõtete ringi, koostame profiile ning hindame sobivust mandaadiga.",
    ),
    "platform_2_title": ("Analyse and value", "Analizuoti ir vertinti", "Analizēt un vērtēt", "Analüüsi ja hinda"),
    "platform_2_body": (
        "Bring market data, comparables and source documents into structured analysis.",
        "Sujungiame rinkos duomenis, palyginamuosius rodiklius ir pirminius dokumentus į struktūruotą analizę.",
        "Apvienojam tirgus datus, salīdzināmos rādītājus un avota dokumentus strukturētā analīzē.",
        "Toome turuandmed, võrdlusandmed ja algdokumendid struktureeritud analüüsi.",
    ),
    "platform_3_title": ("Review documents", "Peržiūrėti dokumentus", "Pārskatīt dokumentus", "Vaata dokumendid läbi"),
    "platform_3_body": (
        "Read data rooms, contracts and filings faster, with issues flagged for adviser review.",
        "Greičiau peržiūrime duomenų kambarius, sutartis ir ataskaitas, o pastebėtus klausimus pažymime konsultantų peržiūrai.",
        "Ātrāk izskatām datu telpas, līgumus un pārskatus, atzīmējot jautājumus konsultantu pārbaudei.",
        "Töötame andmeruumid, lepingud ja aruanded kiiremini läbi ning märgime küsimused nõustaja ülevaatuseks.",
    ),
    "platform_4_title": ("Prepare materials", "Parengti medžiagą", "Sagatavot materiālus", "Valmista materjalid"),
    "platform_4_body": (
        "Draft memoranda, teasers and board materials for advisers to refine.",
        "Rengiame memorandumų, trumpų pristatymų ir valdybos medžiagos juodraščius, kuriuos tobulina konsultantai.",
        "Sagatavojam memorandu, īso aprakstu un valdes materiālu projektus, ko pilnveido konsultanti.",
        "Koostame memode, tutvustuste ja juhatuse materjalide mustandid, mida nõustajad lihvivad.",
    ),
    "gov_label": ("Governance", "Valdysena", "Pārvaldība", "Juhtimine"),
    "gov_heading": (
        "Judgement stays *human*.",
        "Sprendimai lieka *žmonių* rankose.",
        "Spriedums paliek *cilvēka* ziņā.",
        "Otsustab *inimene*.",
    ),
    "gov_1_title": ("Verified", "Patikrinta", "Pārbaudīts", "Kontrollitud"),
    "gov_1_body": (
        "Advisers check sources, test assumptions and sign off every output before it reaches a client.",
        "Konsultantai patikrina šaltinius, įvertina prielaidas ir patvirtina kiekvieną rezultatą prieš jam pasiekiant klientą.",
        "Konsultanti pārbauda avotus, izvērtē pieņēmumus un apstiprina katru rezultātu, pirms tas nonāk pie klienta.",
        "Nõustajad kontrollivad allikaid, testivad eeldusi ja kinnitavad iga tulemuse enne, kui see kliendini jõuab.",
    ),
    "gov_2_title": ("Confidential", "Konfidencialu", "Konfidenciāli", "Konfidentsiaalne"),
    "gov_2_body": (
        "Client information is handled on a need-to-know basis and used only for the mandate it was shared for.",
        "Kliento informacija tvarkoma tik būtinumo principu ir naudojama tik tam pavedimui, kuriam ji buvo pateikta.",
        "Klienta informācija tiek apstrādāta tikai nepieciešamības gadījumā un izmantota vienīgi tam uzdevumam, kuram tā sniegta.",
        "Kliendi teavet käsitletakse teadmisvajaduse põhimõttel ja kasutatakse ainult selle mandaadi jaoks, mille tarbeks see jagati.",
    ),
    "gov_3_title": ("Accountable", "Atsakinga", "Atbildīgi", "Vastutustundlik"),
    "gov_3_body": (
        "AI supports the work. Recommendations, and responsibility for them, remain with our advisers.",
        "AI padeda dirbti. Rekomendacijos ir atsakomybė už jas lieka mūsų konsultantams.",
        "AI atbalsta darbu. Ieteikumi un atbildība par tiem paliek mūsu konsultantiem.",
        "Tehisintellekt toetab tööd. Soovitused ja vastutus nende eest jäävad meie nõustajatele.",
    ),
    "platform_note": (
        "Technology accelerates preparation. Curonia's people review sources, test assumptions and lead every client decision.",
        "Technologija pagreitina pasirengimą. Curonia specialistai tikrina šaltinius, vertina prielaidas ir vadovauja kiekvienam kliento sprendimui.",
        "Tehnoloģija paātrina sagatavošanos. Curonia speciālisti pārbauda avotus, izvērtē pieņēmumus un vada katru klienta lēmumu.",
        "Tehnoloogia kiirendab ettevalmistust. Curonia inimesed kontrollivad allikaid, testivad eeldusi ja juhivad iga kliendi otsust.",
    ),
    "built_on": ("Built on LiquidRound", "Sukurta LiquidRound pagrindu", "Veidots uz LiquidRound bāzes", "Ehitatud LiquidRoundile"),
    "platform_link": ("Visit LiquidRound", "Aplankyti LiquidRound", "Apmeklēt LiquidRound", "Ava LiquidRound"),

    # Sectors page
    "sectors_heading": (
        "Sector insight, guided by the *mandate*.",
        "Sektorių įžvalgos pagal *pavedimą*.",
        "Nozaru izpratne atbilstoši *uzdevumam*.",
        "Sektoritundmine *mandaadist* lähtudes.",
    ),
    "sectors_lede": (
        "We advise businesses where market structure, technology and cross-border reach shape value, and assess each opportunity on its own merits.",
        "Konsultuojame verslus, kurių vertę lemia rinkos struktūra, technologijos ir tarpvalstybinė plėtra, o kiekvieną galimybę vertiname atskirai.",
        "Konsultējam uzņēmumus, kuru vērtību veido tirgus struktūra, tehnoloģijas un pārrobežu iespējas, un katru iespēju izvērtējam atsevišķi.",
        "Nõustame ettevõtteid, mille väärtust kujundavad turustruktuur, tehnoloogia ja piiriülene haare, ning hindame iga võimalust eraldi.",
    ),
    "sector_1_title": ("Technology and software", "Technologijos ir programinė įranga", "Tehnoloģijas un programmatūra", "Tehnoloogia ja tarkvara"),
    "sector_1_body": (
        "Vertical software, IT services, data infrastructure and digital businesses.",
        "Specializuota programinė įranga, IT paslaugos, duomenų infrastruktūra ir skaitmeniniai verslai.",
        "Specializēta programmatūra, IT pakalpojumi, datu infrastruktūra un digitālie uzņēmumi.",
        "Valdkonnapõhine tarkvara, IT-teenused, andmetaristu ja digiettevõtted.",
    ),
    "sector_2_title": ("Healthcare and life sciences", "Sveikatos priežiūra ir gyvybės mokslai", "Veselības aprūpe un dzīvības zinātnes", "Tervishoid ja bioteadused"),
    "sector_2_body": (
        "Provider networks, health technology, diagnostics and specialist services.",
        "Paslaugų teikėjų tinklai, sveikatos technologijos, diagnostika ir specializuotos paslaugos.",
        "Pakalpojumu sniedzēju tīkli, veselības tehnoloģijas, diagnostika un specializēti pakalpojumi.",
        "Teenusepakkujate võrgustikud, tervisetehnoloogia, diagnostika ja eriteenused.",
    ),
    "sector_3_title": ("Business services", "Verslo paslaugos", "Biznesa pakalpojumi", "Äriteenused"),
    "sector_3_body": (
        "Professional, outsourced and technology-enabled services.",
        "Profesinės, užsakomosios ir technologijomis grįstos paslaugos.",
        "Profesionālie, ārpakalpojumu un tehnoloģijās balstītie pakalpojumi.",
        "Professionaalsed, sisseostetavad ja tehnoloogiapõhised teenused.",
    ),
    "sector_4_title": ("Industrials and infrastructure", "Pramonė ir infrastruktūra", "Rūpniecība un infrastruktūra", "Tööstus ja taristu"),
    "sector_4_body": (
        "Manufacturing, industrial technology, logistics and infrastructure services.",
        "Gamyba, pramonės technologijos, logistika ir infrastruktūros paslaugos.",
        "Ražošana, rūpnieciskās tehnoloģijas, loģistika un infrastruktūras pakalpojumi.",
        "Tootmine, tööstustehnoloogia, logistika ja taristuteenused.",
    ),
    "sector_5_title": ("Consumer and education", "Vartojimas ir švietimas", "Patēriņš un izglītība", "Tarbekaubad ja haridus"),
    "sector_5_body": (
        "Consumer brands, education platforms and recurring-service models.",
        "Vartotojų prekių ženklai, švietimo platformos ir pasikartojančių paslaugų modeliai.",
        "Patēriņa zīmoli, izglītības platformas un regulāru pakalpojumu modeļi.",
        "Tarbijabrändid, haridusplatvormid ja püsiteenuse mudelid.",
    ),
    "sectors_note": (
        "Sector focus follows the mandate. If your business sits outside these areas, we are still glad to talk.",
        "Sektorių kryptį lemia pavedimas. Jei jūsų verslas nepatenka į šias sritis, vis tiek mielai pasikalbėsime.",
        "Nozaru fokusu nosaka uzdevums. Ja jūsu uzņēmums neietilpst šajās jomās, joprojām labprāt aprunāsimies.",
        "Sektorivaliku määrab mandaat. Kui teie ettevõte jääb nendest valdkondadest välja, räägime ikkagi hea meelega.",
    ),

    # Team page
    "team_heading": (
        "Small by design. *Senior* throughout.",
        "Sąmoningai nedidelė. *Patyrusi* kiekviename žingsnyje.",
        "Apzināti neliela. *Pieredzējusi* ik solī.",
        "Teadlikult väike. *Kogenud* igas etapis.",
    ),
    "team_lede": (
        "Direct senior involvement, a regional perspective and practical experience of applying technology to transactions.",
        "Tiesioginis patyrusių specialistų dalyvavimas, regioninė perspektyva ir praktinė technologijų taikymo sandoriuose patirtis.",
        "Tieša pieredzējušu speciālistu iesaiste, reģionāls skatījums un praktiska pieredze tehnoloģiju izmantošanā darījumos.",
        "Kogenud spetsialistide otsene osalus, piirkondlik vaade ja praktiline kogemus tehnoloogia rakendamisel tehingutes.",
    ),
    "julian_bio": (
        "Julian works at the intersection of investment banking and applied AI. His background includes investment banking roles at Goldman Sachs, Morgan Stanley, UBS and JPMorgan, and AI engineering at Microsoft and Indurent.",
        "Julian dirba investicinės bankininkystės ir taikomojo AI sankirtoje. Jo patirtis apima investicinės bankininkystės pareigas Goldman Sachs, Morgan Stanley, UBS ir JPMorgan bei AI inžineriją Microsoft ir Indurent.",
        "Julian strādā investīciju banku un lietišķā AI krustpunktā. Viņa pieredze ietver darbu investīciju bankās Goldman Sachs, Morgan Stanley, UBS un JPMorgan, kā arī AI inženieriju Microsoft un Indurent.",
        "Julian tegutseb investeerimispanganduse ja rakendusliku tehisintellekti ristumiskohas. Tema taust hõlmab investeerimispanganduse ameteid Goldman Sachsis, Morgan Stanleys, UBSis ja JPMorganis ning AI inseneritööd Microsoftis ja Indurentis.",
    ),
    "igors_bio": (
        "Igors brings an investment perspective to Curonia's cross-border advisory work. His public profile lists Mercury.Investments and the London School of Economics.",
        "Igors prie Curonia tarpvalstybinių konsultacijų prisideda investuotojo požiūriu. Jo viešame profilyje nurodyti Mercury.Investments ir London School of Economics.",
        "Igors Curonia pārrobežu konsultācijās ienes investora skatījumu. Viņa publiskajā profilā minēti Mercury.Investments un London School of Economics.",
        "Igors toob Curonia piiriülesesse nõustamistöösse investori vaate. Tema avalikus profiilis on märgitud Mercury.Investments ja London School of Economics.",
    ),
    "linkedin_label": ("LinkedIn profile", "LinkedIn profilis", "LinkedIn profils", "LinkedIni profiil"),
    "profile": ("Profile", "Apie", "Profils", "Taust"),

    # Contact page
    "contact_heading": (
        "Let’s discuss your next *move*.",
        "Aptarkime kitą jūsų *žingsnį*.",
        "Apspriedīsim jūsu nākamo *soli*.",
        "Arutame teie järgmist *sammu*.",
    ),
    "contact_lede": (
        "Tell us whether you are considering a sale, an acquisition or a strategic review. A short outline is enough to begin.",
        "Parašykite, ar svarstote pardavimą, įsigijimą ar strateginę peržiūrą. Pradžiai pakanka trumpo aprašymo.",
        "Pastāstiet, vai apsverat pārdošanu, iegādi vai stratēģisku izvērtējumu. Sākumam pietiek ar īsu aprakstu.",
        "Andke teada, kas kaalute müüki, omandamist või strateegilist ülevaadet. Alustuseks piisab lühikirjeldusest.",
    ),
    "contact_email": ("Write to us", "Rašykite mums", "Rakstiet mums", "Kirjutage meile"),
    "contact_subject": ("Confidential enquiry", "Konfidencialus užklausimas", "Konfidenciāls pieprasījums", "Konfidentsiaalne päring"),
    "include_label": ("What to include", "Ką nurodyti", "Ko norādīt", "Mida lisada"),
    "include_1": (
        "The nature of the opportunity: a sale, an acquisition or a broader review.",
        "Galimybės pobūdį: pardavimas, įsigijimas ar platesnė peržiūra.",
        "Iespējas raksturu: pārdošana, iegāde vai plašāks izvērtējums.",
        "Võimaluse olemus: müük, omandamine või laiem ülevaade.",
    ),
    "include_2": (
        "Indicative timing and any constraints we should know about.",
        "Numatomus terminus ir apribojimus, apie kuriuos turėtume žinoti.",
        "Aptuvenos termiņus un ierobežojumus, par kuriem mums būtu jāzina.",
        "Esialgne ajakava ja piirangud, millest peaksime teadma.",
    ),
    "include_3": (
        "The one or two decisions you are facing now.",
        "Vieną ar du sprendimus, kuriuos turite priimti dabar.",
        "Vienu vai divus lēmumus, kas jums jāpieņem tagad.",
        "Üks või kaks otsust, mis teil praegu ees seisavad.",
    ),
    "discretion_note": (
        "Enquiries are read by a senior adviser and treated in confidence. Please do not send confidential documents until we have agreed how to receive them.",
        "Užklausimus skaito patyręs konsultantas ir jie traktuojami konfidencialiai. Prašome nesiųsti konfidencialių dokumentų, kol nesusitarsime, kaip juos gauti.",
        "Pieprasījumus lasa pieredzējis konsultants, un tie tiek uzskatīti par konfidenciāliem. Lūdzu, nesūtiet konfidenciālus dokumentus, līdz neesam vienojušies, kā tos saņemt.",
        "Päringud loeb läbi kogenud nõustaja ja neid käsitletakse konfidentsiaalselt. Palun ärge saatke konfidentsiaalseid dokumente enne, kui oleme kokku leppinud, kuidas need vastu võtame.",
    ),
    "contact_office": ("Registered office", "Registruota buveinė", "Juridiskā adrese", "Registrijärgne aadress"),

    # Not found
    "nf_heading": (
        "This page has *moved* on.",
        "Šis puslapis *nebeegzistuoja*.",
        "Šī lapa vairs *nav pieejama*.",
        "Seda lehte enam *ei ole*.",
    ),
    "nf_body": (
        "The page you were looking for has moved or no longer exists.",
        "Ieškomas puslapis buvo perkeltas arba nebeegzistuoja.",
        "Meklētā lapa ir pārvietota vai vairs nepastāv.",
        "Otsitud leht on teisaldatud või seda enam ei ole.",
    ),
    "nf_link": ("Return to the home page", "Grįžti į pradžią", "Atgriezties sākumlapā", "Tagasi avalehele"),
}

TRANSLATIONS = {
    key: dict(zip(LANGUAGES, values)) for key, values in _COPY.items()
}


def t(key: str, lang: str = DEFAULT_LANG) -> str:
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang) or entry.get(DEFAULT_LANG) or key
