"""Site copy and session language helpers for English, Lithuanian, Latvian, and Estonian."""

from typing import Any

LANGUAGES = {
    "en": {"native": "English"},
    "lt": {"native": "Lietuvių"},
    "lv": {"native": "Latviešu"},
    "et": {"native": "Eesti"},
}
DEFAULT_LANG = "en"

# Copy is ordered EN / LT / LV / ET. Missing translations fall back to English.
_COPY = {
    "menu": ("Open menu", "Atidaryti meniu", "Atvērt izvēlni", "Ava menüü"),
    "nav_advisory": ("Advisory", "Konsultavimas", "Konsultācijas", "Nõustamine"),
    "nav_sectors": ("Sectors", "Sektoriai", "Nozares", "Sektorid"),
    "nav_platform": ("Platform", "Platforma", "Platforma", "Platvorm"),
    "nav_team": ("Team", "Komanda", "Komanda", "Meeskond"),
    "nav_contact": ("Contact", "Kontaktai", "Kontakti", "Kontakt"),
    "meta_description": (
        "Curonia Capital Ltd advises on mergers and acquisitions across the Baltics and Central and Eastern Europe, supported by LiquidRound.",
        "Curonia Capital Ltd konsultuoja susijungimų ir įsigijimų klausimais Baltijos šalyse bei Vidurio ir Rytų Europoje, pasitelkdama LiquidRound.",
        "Curonia Capital Ltd konsultē apvienošanās un iegādes darījumos Baltijā un Centrālajā un Austrumeiropā, izmantojot LiquidRound.",
        "Curonia Capital Ltd nõustab ühinemiste ja omandamistehingute vallas Baltikumis ning Kesk- ja Ida-Euroopas, kasutades LiquidRoundi.",
    ),
    "footer_tagline": (
        "Independent M&A advice for the Baltics and CEE, informed by technology and grounded in human judgment.",
        "Nepriklausomos M&A konsultacijos Baltijos šalims ir VRE, paremtos technologijomis ir žmogišku sprendimu.",
        "Neatkarīgas M&A konsultācijas Baltijā un CAE, apvienojot tehnoloģijas ar cilvēka spriedumu.",
        "Sõltumatu M&A nõustamine Baltikumis ja KIEs, ühendades tehnoloogia inimliku otsustusvõimega.",
    ),
    "footer_explore": ("Explore", "Naršyti", "Izpētīt", "Uuri"),
    "footer_company": ("Company details", "Įmonės duomenys", "Uzņēmuma dati", "Ettevõtte andmed"),
    "company_number": ("Company number", "Įmonės kodas", "Uzņēmuma numurs", "Registrikood"),
    "hero_eyebrow": (
        "Independent M&A advisory · Baltics & CEE",
        "Nepriklausomos M&A konsultacijos · Baltija ir VRE",
        "Neatkarīgas M&A konsultācijas · Baltija un CAE",
        "Sõltumatu M&A nõustamine · Baltikum ja KIE",
    ),
    "hero_heading": (
        "Cross-border deals. Clearer decisions.",
        "Tarptautiniai sandoriai. Aiškesni sprendimai.",
        "Pārrobežu darījumi. Skaidrāki lēmumi.",
        "Piiriülesed tehingud. Selgemad otsused.",
    ),
    "hero_lede": (
        "Curonia Capital Ltd advises owners, investors and companies on M&A across the Baltics and Central and Eastern Europe. We combine senior transaction judgment with LiquidRound-powered research, sourcing and analysis.",
        "Curonia Capital Ltd konsultuoja savininkus, investuotojus ir įmones M&A sandoriuose Baltijos šalyse bei Vidurio ir Rytų Europoje. Deriname patyrusių konsultantų sprendimus su LiquidRound tyrimais, paieška ir analize.",
        "Curonia Capital Ltd konsultē īpašniekus, investorus un uzņēmumus M&A darījumos Baltijā un Centrālajā un Austrumeiropā. Apvienojam pieredzējušu konsultantu spriedumu ar LiquidRound izpēti, atlasi un analīzi.",
        "Curonia Capital Ltd nõustab omanikke, investoreid ja ettevõtteid M&A tehingutes Baltikumis ning Kesk- ja Ida-Euroopas. Ühendame kogenud nõustamise LiquidRoundi uuringute, otsingu ja analüüsiga.",
    ),
    "hero_primary": ("Explore our advisory", "Mūsų paslaugos", "Mūsu konsultācijas", "Tutvu nõustamisega"),
    "hero_secondary": ("Explore the platform", "Apie platformą", "Par platformu", "Tutvu platvormiga"),
    "home_focus_eyebrow": ("What we do", "Ką darome", "Ko mēs darām", "Mida teeme"),
    "home_focus_heading": ("Advice for both sides of the transaction.", "Konsultacijos abiem sandorio pusėms.", "Konsultācijas abām darījuma pusēm.", "Nõustamine tehingu mõlemale poolele."),
    "home_focus_lede": (
        "From first strategic question to signed transaction, our work is tailored to the mandate and the market.",
        "Nuo pirmojo strateginio klausimo iki pasirašyto sandorio dirbame pagal kliento poreikius ir rinką.",
        "No pirmā stratēģiskā jautājuma līdz parakstītam darījumam strādājam atbilstoši uzdevumam un tirgum.",
        "Esimesest strateegilisest küsimusest allkirjastatud tehinguni lähtume kliendi eesmärgist ja turust.",
    ),
    "sell_title": ("Sell-side advisory", "Pardavėjo konsultavimas", "Pārdevēja konsultācijas", "Müüjapoole nõustamine"),
    "sell_body": (
        "Position the business, map credible buyers, prepare materials and run a disciplined process through negotiation and close.",
        "Padedame pristatyti verslą, nustatyti tinkamus pirkėjus, parengti medžiagą ir valdyti procesą iki sandorio užbaigimo.",
        "Pozicionējam uzņēmumu, apzinām pircējus, sagatavojam materiālus un vadām procesu līdz darījuma noslēgumam.",
        "Positsioneerime ettevõtte, kaardistame ostjad, valmistame ette materjalid ja juhime protsessi tehingu lõpuni.",
    ),
    "buy_title": ("Buy-side advisory", "Pirkėjo konsultavimas", "Pircēja konsultācijas", "Ostjapoole nõustamine"),
    "buy_body": (
        "Translate an acquisition thesis into target sourcing, screening, valuation support and coordinated diligence.",
        "Paverčiame įsigijimo strategiją taikinių paieška, atranka, vertinimo analize ir koordinuotu patikrinimu.",
        "Pārvēršam iegādes stratēģiju mērķu meklēšanā, atlasē, vērtēšanā un koordinētā izpētē.",
        "Muudame omandamisstrateegia sihtmärkide otsinguks, valikuks, hindamisanalüüsiks ja koordineeritud hoolsuskontrolliks.",
    ),
    "strategy_title": ("Strategic options", "Strateginės alternatyvos", "Stratēģiskās iespējas", "Strateegilised valikud"),
    "strategy_body": (
        "Assess exits, acquisitions, partnerships and transaction readiness before committing to a path.",
        "Įvertiname pardavimo, įsigijimo, partnerystės ir pasirengimo sandoriui galimybes prieš pasirenkant kryptį.",
        "Izvērtējam pārdošanu, iegādes, partnerības un gatavību darījumam pirms lēmuma pieņemšanas.",
        "Hindame müügi, omandamise, partnerluse ja tehinguvalmiduse võimalusi enne suuna valimist.",
    ),
    "home_region_eyebrow": ("Our market", "Mūsų rinka", "Mūsu tirgus", "Meie turg"),
    "home_region_heading": ("Baltic roots. CEE reach.", "Baltijos šaknys. VRE aprėptis.", "Baltijas saknes. CAE tvērums.", "Balti juured. KIE haare."),
    "home_region_body": (
        "We focus on Lithuania, Latvia and Estonia, with a cross-border lens on Poland and the wider CEE region. Sector work follows each client's mandate.",
        "Dirbame Lietuvoje, Latvijoje ir Estijoje, taip pat žvelgiame į Lenkiją ir platesnį VRE regioną. Sektorius renkamės pagal kliento tikslus.",
        "Strādājam Lietuvā, Latvijā un Igaunijā, kā arī skatāmies uz Poliju un plašāku CAE reģionu. Nozaru fokusu nosaka klienta uzdevums.",
        "Keskendume Leedule, Lätile ja Eestile ning vaatame ka Poola ja laiema KIE piirkonna võimalusi. Sektorid sõltuvad kliendi eesmärgist.",
    ),
    "home_platform_eyebrow": ("Technology in the workflow", "Technologijos darbe", "Tehnoloģijas darbā", "Tehnoloogia töös"),
    "home_platform_heading": ("Better prepared for every deal conversation.", "Geriau pasirengę kiekvienam sandorio pokalbiui.", "Labāk sagatavoti katrai darījuma sarunai.", "Paremini valmis igaks tehinguvestluseks."),
    "home_platform_body": (
        "LiquidRound supports target and buyer research, comparable-company analysis, document review and first drafts. Our advisers verify the output and remain accountable for the advice.",
        "LiquidRound padeda tirti pirkėjus ir įsigijimo objektus, analizuoti palyginamus duomenis, peržiūrėti dokumentus ir rengti juodraščius. Mūsų konsultantai tikrina rezultatus ir atsako už rekomendacijas.",
        "LiquidRound palīdz izpētīt pircējus un mērķus, analizēt salīdzināmos datus, pārskatīt dokumentus un sagatavot projektus. Mūsu konsultanti pārbauda rezultātus un atbild par padomu.",
        "LiquidRound aitab uurida ostjaid ja sihtettevõtteid, analüüsida võrdlusandmeid, vaadata läbi dokumente ning koostada mustandeid. Meie nõustajad kontrollivad tulemusi ja vastutavad nõu eest.",
    ),
    "learn_platform": ("See how the platform fits", "Kaip naudojame platformą", "Kā izmantojam platformu", "Vaata, kuidas platvorm sobitub"),
    "advisory_heading": ("M&A advice built around your objectives.", "M&A konsultacijos pagal jūsų tikslus.", "M&A konsultācijas jūsu mērķiem.", "M&A nõustamine teie eesmärkidest lähtudes."),
    "advisory_lede": (
        "Whether you are selling a company, seeking an acquisition or evaluating strategic options, we bring structure and independent judgment to complex cross-border decisions.",
        "Parduodant įmonę, ieškant įsigijimo ar vertinant strategines alternatyvas, sudėtingiems tarptautiniams sprendimams suteikiame struktūrą ir nepriklausomą požiūrį.",
        "Pārdodot uzņēmumu, meklējot iegādi vai izvērtējot stratēģiskās iespējas, sarežģītos pārrobežu lēmumos nodrošinām struktūru un neatkarīgu skatījumu.",
        "Ettevõtet müües, omandamist otsides või strateegilisi valikuid hinnates toome keerukatesse piiriülestesse otsustesse struktuuri ja sõltumatu vaate.",
    ),
    "advisory_process": ("A focused transaction process", "Kryptingas sandorio procesas", "Mērķtiecīgs darījuma process", "Sihipärane tehinguprotsess"),
    "process_1_title": ("Define the mandate", "Apibrėžti tikslą", "Definēt uzdevumu", "Määratle eesmärk"),
    "process_1_body": ("Agree objectives, constraints, timing and the decision makers.", "Sutariame dėl tikslų, ribų, laiko ir sprendimų priėmėjų.", "Vienojamies par mērķiem, ierobežojumiem, termiņiem un lēmumu pieņēmējiem.", "Lepime kokku eesmärgid, piirangud, ajakava ja otsustajad."),
    "process_2_title": ("Map the market", "Ištirti rinką", "Izpētīt tirgu", "Kaardista turg"),
    "process_2_body": ("Research the relevant buyers, targets and comparable transactions.", "Tiriame aktualius pirkėjus, įsigijimo objektus ir panašius sandorius.", "Izpētām atbilstošos pircējus, mērķus un salīdzināmus darījumus.", "Uurime sobivaid ostjaid, sihtettevõtteid ja võrreldavaid tehinguid."),
    "process_3_title": ("Build the case", "Parengti argumentus", "Sagatavot pamatojumu", "Koosta põhjendus"),
    "process_3_body": ("Prepare positioning, valuation work and materials for the next decision.", "Rengiame pozicionavimą, vertinimą ir medžiagą kitam sprendimui.", "Sagatavojam pozicionējumu, vērtējumu un materiālus nākamajam lēmumam.", "Valmistame ette positsioneerimise, hindamise ja materjalid järgmiseks otsuseks."),
    "process_4_title": ("Execute with care", "Įgyvendinti atsakingai", "Īstenot rūpīgi", "Vii hoolikalt ellu"),
    "process_4_body": ("Coordinate discussions, diligence and negotiations through close.", "Koordinuojame pokalbius, patikrinimą ir derybas iki užbaigimo.", "Koordinējam sarunas, izpēti un pārrunas līdz noslēgumam.", "Koordineerime arutelusid, hoolsuskontrolli ja läbirääkimisi kuni lõpuni."),
    "sectors_heading": ("Sector insight, guided by the mandate.", "Sektorių įžvalgos pagal kliento tikslus.", "Nozaru izpratne atbilstoši uzdevumam.", "Sektoritunnetus vastavalt eesmärgile."),
    "sectors_lede": (
        "Our advisory lens spans businesses where market structure, technology and cross-border reach shape value. We assess each opportunity on its own merits.",
        "Konsultuojame verslus, kurių vertę lemia rinkos struktūra, technologijos ir tarptautinė plėtra. Kiekvieną galimybę vertiname individualiai.",
        "Konsultējam uzņēmumus, kuru vērtību veido tirgus struktūra, tehnoloģijas un pārrobežu iespējas. Katru iespēju izvērtējam atsevišķi.",
        "Nõustame ettevõtteid, mille väärtust kujundavad turustruktuur, tehnoloogia ja piiriülene ulatus. Hindame iga võimalust eraldi.",
    ),
    "sector_1_title": ("Technology & software", "Technologijos ir programinė įranga", "Tehnoloģijas un programmatūra", "Tehnoloogia ja tarkvara"),
    "sector_1_body": ("Vertical software, IT services, data infrastructure and digital businesses.", "Specializuota programinė įranga, IT paslaugos, duomenų infrastruktūra ir skaitmeniniai verslai.", "Specializēta programmatūra, IT pakalpojumi, datu infrastruktūra un digitālie uzņēmumi.", "Valdkonnapõhine tarkvara, IT-teenused, andmetaristu ja digiettevõtted."),
    "sector_2_title": ("Healthcare & life sciences", "Sveikatos priežiūra ir gyvybės mokslai", "Veselības aprūpe un dzīvības zinātnes", "Tervishoid ja bioteadused"),
    "sector_2_body": ("Provider networks, health technology, diagnostics and specialist services.", "Paslaugų tinklai, sveikatos technologijos, diagnostika ir specializuotos paslaugos.", "Pakalpojumu tīkli, veselības tehnoloģijas, diagnostika un specializēti pakalpojumi.", "Teenusevõrgustikud, tervisetehnoloogia, diagnostika ja eriteenused."),
    "sector_3_title": ("Business services", "Verslo paslaugos", "Biznesa pakalpojumi", "Äriteenused"),
    "sector_3_body": ("Professional, outsourced and technology-enabled services.", "Profesinės, išorinės ir technologijomis grįstos paslaugos.", "Profesionālie, ārpakalpojumu un tehnoloģijās balstītie pakalpojumi.", "Professionaalsed, sisseostetud ja tehnoloogiapõhised teenused."),
    "sector_4_title": ("Industrials & infrastructure", "Pramonė ir infrastruktūra", "Rūpniecība un infrastruktūra", "Tööstus ja taristu"),
    "sector_4_body": ("Manufacturing, industrial technology, logistics and infrastructure services.", "Gamyba, pramonės technologijos, logistika ir infrastruktūros paslaugos.", "Ražošana, rūpnieciskās tehnoloģijas, loģistika un infrastruktūras pakalpojumi.", "Tootmine, tööstustehnoloogia, logistika ja taristuteenused."),
    "sector_5_title": ("Consumer & education", "Vartojimas ir švietimas", "Patēriņš un izglītība", "Tarbija ja haridus"),
    "sector_5_body": ("Consumer brands, education platforms and recurring-service models.", "Vartotojų prekės ženklai, švietimo platformos ir pasikartojančių paslaugų modeliai.", "Patēriņa zīmoli, izglītības platformas un atkārtotu pakalpojumu modeļi.", "Tarbijabrändid, haridusplatvormid ja korduva teenuse mudelid."),
    "platform_eyebrow": ("Our technology", "Mūsų technologija", "Mūsu tehnoloģija", "Meie tehnoloogia"),
    "platform_heading": ("LiquidRound in the advisory workflow.", "LiquidRound konsultavimo procese.", "LiquidRound konsultāciju procesā.", "LiquidRound nõustamisprotsessis."),
    "platform_lede": (
        "LiquidRound is an AI investment-banking platform for buyer- and seller-led work. Curonia uses its research and drafting capabilities to support our advisers across the transaction lifecycle.",
        "LiquidRound yra AI investicinės bankininkystės platforma pirkėjo ir pardavėjo procesams. Curonia jos tyrimų ir dokumentų rengimo galimybes naudoja konsultantų darbui visame sandorio cikle.",
        "LiquidRound ir AI investīciju banku platforma pircēja un pārdevēja procesiem. Curonia izmanto tās izpētes un dokumentu sagatavošanas iespējas konsultantu darbam visā darījuma ciklā.",
        "LiquidRound on AI investeerimispanganduse platvorm ostja ja müüja tööks. Curonia kasutab selle uuringu- ja koostamisvõimekust nõustajate toetamiseks kogu tehingutsükli vältel.",
    ),
    "platform_1_title": ("Source and screen", "Rasti ir atrinkti", "Atrast un atlasīt", "Leia ja sõelu"),
    "platform_1_body": ("Explore target and buyer universes, build profiles and triage fit against a mandate.", "Tiriame įsigijimo objektus ir pirkėjus, rengiame profilius ir vertiname atitiktį tikslui.", "Izpētām mērķus un pircējus, veidojam profilus un vērtējam atbilstību uzdevumam.", "Uurime sihtettevõtteid ja ostjaid, koostame profiile ning hindame sobivust."),
    "platform_2_title": ("Analyse and value", "Analizuoti ir vertinti", "Analizēt un vērtēt", "Analüüsi ja hinda"),
    "platform_2_body": ("Bring market data, comparables and source documents into structured analysis.", "Sujungiame rinkos duomenis, palyginimus ir pirminius dokumentus struktūruotai analizei.", "Apvienojam tirgus datus, salīdzināmos rādītājus un avota dokumentus strukturētai analīzei.", "Toome turuandmed, võrdlused ja algdokumendid struktureeritud analüüsi."),
    "platform_3_title": ("Prepare materials", "Parengti medžiagą", "Sagatavot materiālus", "Valmista materjalid"),
    "platform_3_body": ("Create first drafts of investment memos, presentations and transaction materials for adviser review.", "Rengiame pirminius investicinius memorandumus, pristatymus ir sandorio medžiagą konsultantų peržiūrai.", "Sagatavojam investīciju memorandu, prezentāciju un darījuma materiālu pirmos projektus konsultantu pārbaudei.", "Koostame investeerimismemode, esitluste ja tehingumaterjalide esimesed kavandid nõustaja ülevaatuseks."),
    "platform_note": (
        "Technology accelerates preparation; Curonia's people review sources, test assumptions and lead client decisions.",
        "Technologija pagreitina pasirengimą; Curonia specialistai tikrina šaltinius, prielaidas ir vadovauja sprendimams.",
        "Tehnoloģija paātrina sagatavošanos; Curonia speciālisti pārbauda avotus, pieņēmumus un vada klienta lēmumus.",
        "Tehnoloogia kiirendab ettevalmistust; Curonia inimesed kontrollivad allikaid ja eeldusi ning juhivad kliendi otsuseid.",
    ),
    "platform_link": ("Visit LiquidRound", "Aplankyti LiquidRound", "Apmeklēt LiquidRound", "Ava LiquidRound"),
    "team_heading": ("A focused advisory team.", "Kryptinga konsultantų komanda.", "Mērķtiecīga konsultantu komanda.", "Sihipärane nõustajate meeskond."),
    "team_lede": (
        "Direct senior involvement, regional perspective and practical technology experience.",
        "Tiesioginis patyrusių specialistų dalyvavimas, regioninė perspektyva ir praktinė technologijų patirtis.",
        "Tieša pieredzējušu speciālistu iesaiste, reģionāls skatījums un praktiska tehnoloģiju pieredze.",
        "Kogenud spetsialistide otsene panus, piirkondlik vaade ja praktiline tehnoloogiakogemus.",
    ),
    "julian_bio": (
        "Julian works at the intersection of investment banking and applied AI. His background includes investment banking roles at Goldman Sachs, Morgan Stanley, UBS and JPMorgan, and AI engineering at Microsoft and Indurent.",
        "Julian dirba investicinės bankininkystės ir taikomojo AI sankirtoje. Jo patirtis apima darbą Goldman Sachs, Morgan Stanley, UBS ir JPMorgan bei AI inžineriją Microsoft ir Indurent.",
        "Julian strādā investīciju banku un lietišķā AI krustpunktā. Viņa pieredze ietver darbu Goldman Sachs, Morgan Stanley, UBS un JPMorgan, kā arī AI inženieriju Microsoft un Indurent.",
        "Julian tegutseb investeerimispanganduse ja rakendusliku tehisintellekti piiril. Tema taust hõlmab Goldman Sachsi, Morgan Stanley, UBSi ja JPMorgani ning AI inseneritööd Microsoftis ja Indurentis.",
    ),
    "igors_bio": (
        "Igors brings an investment perspective to Curonia's cross-border advisory work. His public profile lists Mercury.Investments and the London School of Economics.",
        "Igors prisideda investiciniu požiūriu prie Curonia tarptautinių konsultacijų. Jo viešame profilyje nurodyti Mercury.Investments ir London School of Economics.",
        "Igors sniedz investīciju skatījumu Curonia pārrobežu konsultācijām. Viņa publiskajā profilā minēti Mercury.Investments un London School of Economics.",
        "Igors toob Curonia piiriülesesse nõustamisse investeerimisvaate. Tema avalikus profiilis on märgitud Mercury.Investments ja London School of Economics.",
    ),
    "contact_heading": ("Let's discuss your next move.", "Aptarkime kitą žingsnį.", "Apspriedīsim nākamo soli.", "Arutame teie järgmist sammu."),
    "contact_lede": (
        "Tell us whether you are considering a sale, an acquisition or a strategic review. A short outline of your business and objectives is enough to begin.",
        "Parašykite, ar svarstote pardavimą, įsigijimą ar strateginę peržiūrą. Pokalbiui pradėti pakanka trumpo verslo ir tikslų aprašymo.",
        "Pastāstiet, vai apsverat pārdošanu, iegādi vai stratēģisku izvērtējumu. Sarunas sākumam pietiek ar īsu uzņēmuma un mērķu aprakstu.",
        "Andke teada, kas kaalute müüki, omandamist või strateegilist ülevaadet. Alustuseks piisab lühikesest ettevõtte ja eesmärkide kirjeldusest.",
    ),
    "contact_email": ("Email us", "Rašykite mums", "Rakstiet mums", "Kirjuta meile"),
    "contact_office": ("Registered office", "Registruota buveinė", "Juridiskā adrese", "Registrijärgne aadress"),
    "cta_eyebrow": ("Start a conversation", "Pradėkime pokalbį", "Sāksim sarunu", "Alustame vestlust"),
    "cta_heading": ("Considering a transaction in the Baltics or CEE?", "Svarstote sandorį Baltijos šalyse ar VRE?", "Apsverat darījumu Baltijā vai CAE?", "Kaalute tehingut Baltikumis või KIEs?"),
    "cta_body": (
        "Share your objectives and we will discuss where Curonia Capital Ltd can help.",
        "Pasidalykite savo tikslais ir aptarsime, kaip Curonia Capital Ltd gali padėti.",
        "Pastāstiet par saviem mērķiem, un apspriedīsim, kā Curonia Capital Ltd var palīdzēt.",
        "Jagage oma eesmärke ja arutame, kuidas Curonia Capital Ltd saab aidata.",
    ),
    "cta_button": ("Get in touch", "Susisiekite", "Sazināties", "Võta ühendust"),
}

TRANSLATIONS = {
    key: dict(zip(LANGUAGES, values)) for key, values in _COPY.items()
}


def get_lang(sess: dict[str, Any]) -> str:
    code = str(sess.get("lang") or "").lower()
    return code if code in LANGUAGES else DEFAULT_LANG


def set_lang(sess: dict[str, Any], code: str) -> str:
    code = (code or "").lower()
    if code in LANGUAGES:
        sess["lang"] = code
    return get_lang(sess)


def t(key: str, lang: str = DEFAULT_LANG) -> str:
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang) or entry.get(DEFAULT_LANG) or key
