# Extra strings per language: answer-first sentence, sources heading, word for "Directive".
X = {
 "en": ("Short answer: a platform reports you once you reach 30 sales or take in more than €2,000 on it in one calendar year. Each platform counts separately.", "Sources", "Council Directive"),
 "bg": ("Накратко: платформата те докладва, щом в нея за една календарна година достигнеш 30 продажби или получиш над 2000 €. Всяка платформа брои отделно.", "Източници", "Директива на Съвета"),
 "cs": ("Stručně: platforma tě nahlásí, jakmile na ní v jednom kalendářním roce dosáhneš 30 prodejů nebo utržíš více než 2 000 €. Každá platforma počítá zvlášť.", "Zdroje", "Směrnice Rady"),
 "da": ("Kort svar: En platform indberetter dig, når du på den i ét kalenderår når 30 salg eller sælger for over 2.000 €. Hver platform tæller for sig.", "Kilder", "Rådets direktiv"),
 "de": ("Kurz gesagt: Eine Plattform meldet dich, sobald du dort in einem Kalenderjahr 30 Verkäufe erreichst oder mehr als 2.000 € einnimmst. Jede Plattform zählt für sich.", "Quellen", "Richtlinie des Rates"),
 "at": ("Kurz gesagt: Eine Plattform meldet dich, sobald du dort in einem Kalenderjahr 30 Verkäufe erreichst oder mehr als 2.000 € einnimmst. Jede Plattform zählt für sich.", "Quellen", "Richtlinie des Rates"),
 "el": ("Με λίγα λόγια: μια πλατφόρμα σε δηλώνει μόλις σε αυτήν, μέσα σε ένα ημερολογιακό έτος, φτάσεις τις 30 πωλήσεις ή εισπράξεις πάνω από 2.000 €. Κάθε πλατφόρμα μετράει χωριστά.", "Πηγές", "Οδηγία του Συμβουλίου"),
 "es": ("En resumen: una plataforma informa de ti en cuanto llegas a 30 ventas o ingresas más de 2.000 € en ella en un año natural. Cada plataforma cuenta por separado.", "Fuentes", "Directiva del Consejo"),
 "et": ("Lühidalt: platvorm teatab sinust, kui jõuad seal ühe kalendriaasta jooksul 30 müügini või teenid üle 2000 €. Iga platvorm loeb eraldi.", "Allikad", "Nõukogu direktiiv"),
 "fi": ("Lyhyesti: alusta ilmoittaa sinusta, kun teet sillä yhden kalenterivuoden aikana 30 myyntiä tai myyt yli 2 000 eurolla. Kukin alusta laskee erikseen.", "Lähteet", "Neuvoston direktiivi"),
 "fr": ("En bref : une plateforme vous déclare dès que vous y atteignez 30 ventes ou plus de 2 000 € sur une année civile. Chaque plateforme compte séparément.", "Sources", "Directive du Conseil"),
 "hr": ("Ukratko: platforma te prijavljuje čim na njoj u kalendarskoj godini ostvariš 30 prodaja ili više od 2000 €. Svaka platforma broji zasebno.", "Izvori", "Direktiva Vijeća"),
 "hu": ("Röviden: egy platform akkor jelent be, ha egy naptári évben eléred nála a 30 eladást, vagy 2000 eurónál több bevételed lesz. Minden platform külön számol.", "Források", "A Tanács irányelve"),
 "it": ("In breve: una piattaforma ti segnala appena raggiungi 30 vendite o incassi più di 2.000 € su di essa in un anno solare. Ogni piattaforma conta separatamente.", "Fonti", "Direttiva del Consiglio"),
 "lt": ("Trumpai: platforma apie tave praneša, kai joje per kalendorinius metus pasieki 30 pardavimų arba gauni daugiau nei 2000 €. Kiekviena platforma skaičiuoja atskirai.", "Šaltiniai", "Tarybos direktyva"),
 "lv": ("Īsumā: platforma par tevi ziņo, tiklīdz tajā viena kalendārā gada laikā sasniedz 30 pārdošanas vai saņem vairāk nekā 2000 €. Katra platforma skaita atsevišķi.", "Avoti", "Padomes direktīva"),
 "nl": ("Kort antwoord: een platform meldt je zodra je er in één kalenderjaar 30 verkopen haalt of meer dan € 2.000 ontvangt. Elk platform telt apart.", "Bronnen", "Richtlijn van de Raad"),
 "pl": ("W skrócie: platforma zgłasza Cię, gdy w ciągu roku kalendarzowego osiągniesz na niej 30 transakcji lub uzyskasz ponad 2000 €. Każda platforma liczy osobno.", "Źródła", "Dyrektywa Rady"),
 "pt": ("Em resumo: uma plataforma comunica-te assim que chegares a 30 vendas ou receberes mais de 2000 € nela num ano civil. Cada plataforma conta à parte.", "Fontes", "Diretiva do Conselho"),
 "ro": ("Pe scurt: o platformă te raportează imediat ce ajungi la 30 de vânzări sau încasezi peste 2.000 € pe ea într-un an calendaristic. Fiecare platformă numără separat.", "Surse", "Directiva Consiliului"),
 "sk": ("Stručne: platforma ťa nahlási, keď na nej v jednom kalendárnom roku dosiahneš 30 predajov alebo utŕžiš viac ako 2 000 €. Každá platforma počíta zvlášť.", "Zdroje", "Smernica Rady"),
 "sl": ("Na kratko: platforma te prijavi, ko na njej v enem koledarskem letu dosežeš 30 prodaj ali prejmeš več kot 2.000 €. Vsaka platforma šteje posebej.", "Viri", "Direktiva Sveta"),
 "sv": ("Kort svar: en plattform rapporterar dig när du under ett kalenderår når 30 försäljningar eller säljer för över 2 000 € där. Varje plattform räknas för sig.", "Källor", "Rådets direktiv"),
}

# EUR-Lex language codes
EURLEX = {"en":"EN","bg":"BG","cs":"CS","da":"DA","de":"DE","at":"DE","el":"EL","es":"ES","et":"ET","fi":"FI","fr":"FR","hr":"HR","hu":"HU",
          "it":"IT","lt":"LT","lv":"LV","nl":"NL","pl":"PL","pt":"PT","ro":"RO","sk":"SK","sl":"SL","sv":"SV"}

# Country-specific sources (verified pages)
EXTRA_SOURCES = {
 "de": [("Plattformen-Steuertransparenzgesetz (PStTG), gesetze-im-internet.de", "https://www.gesetze-im-internet.de/psttg/BJNR273010022.html"),
        ("Correctiv-Faktencheck: Keine Steuer auf private Verkäufe (29.10.2026)", "https://correctiv.org/faktencheck/2026/10/29/keine-steuer-auf-private-verkaeufe-flohmarkt-vinted-ebay/"),
        ("KPMG Austria: EU-Vorschlag zur Änderung der DAC7-Grenzen", "https://kpmg.com/at/de/media/newsletter/tax-news/2026/09/tn-dac-recast.html")],
 "at": [("Digitale Plattformen-Meldepflichtgesetz (DPMG), RIS", "https://www.ris.bka.gv.at/eli/bgbl/i/2022/108/P0/NOR40246155"),
        ("§ 31 EStG (Spekulationsgeschäfte, Freigrenze 440 €), JUSLINE", "https://www.jusline.at/gesetz/estg/paragraf/31"),
        ("Deloitte Österreich: Meldepflichten für Plattformen wie willhaben", "https://www.deloitte.com/at/de/what-we-do/regions/praxistipps/03-2024-rechtstipp-willhaben-airbnb.html"),
        ("KPMG Austria: EU-Vorschlag zur Änderung der DAC7-Grenzen", "https://kpmg.com/at/de/media/newsletter/tax-news/2026/09/tn-dac-recast.html")],
 "en": [("KPMG Austria (German): EU proposal to change the DAC7 limits", "https://kpmg.com/at/de/media/newsletter/tax-news/2026/09/tn-dac-recast.html")],
}

# Austria: a copy of the German page with country-specific changes
def austria(de):
    at = dict(de)
    at.update(
        name="Deutsch (Österreich)", locale="de-AT",
        title="DAC7-Check Österreich: Meldet willhaben oder Vinted deine Verkäufe?",
        desc="Kostenloser DAC7-Rechner für Österreich: Prüfe pro Plattform, ob willhaben, Vinted oder eBay deine Verkäufe ans Finanzamt melden – ab 30 Verkäufen oder mehr als 2.000 € im Jahr.",
        h1="Meldet willhaben, Vinted &amp; Co. deine Verkäufe ans Finanzamt?",
        platforms=["willhaben", "Vinted", "eBay", "shpock", "Andere Plattform"],
        cta_btn="Zum Tracker auf Etsy",
        ex_p1="DAC7 ist eine EU-Regel, die Online-Plattformen verpflichtet, Daten ihrer Verkäufer an die Steuerbehörden zu melden. In Österreich gilt sie seit 2023 als Digitale Plattformen-Meldepflichtgesetz (DPMG). Es ist eine Meldepflicht, keine neue Steuer.",
        ex_p2="Gemeldet wird, wer auf einer Plattform in einem Kalenderjahr <strong>30 oder mehr Verkäufe</strong> hat <strong>oder mehr als 2.000 €</strong> einnimmt. Eine der beiden Grenzen reicht. Gemeldet werden Verkäufe, deren Zahlung über die Plattform läuft. Die Plattform übermittelt die Daten bis 31. Jänner für das Vorjahr und muss dich darüber informieren.",
        ex_no="25 Verkäufe auf willhaben und 25 auf Vinted. Jede Plattform zählt für sich, beide bleiben unter 30.",
        ex_yes="31 Verkäufe nur auf willhaben, auch wenn du damit insgesamt nur 400 € eingenommen hast.",
        faq=[
            ("Ab wann meldet willhaben meine Verkäufe ans Finanzamt?", "Sobald du auf willhaben in einem Kalenderjahr 30 Verkäufe erreichst oder mehr als 2.000 € einnimmst. Gezählt werden Verkäufe, die über die Bezahlfunktion der Plattform laufen. Dasselbe gilt für Vinted, eBay und andere Plattformen, jeweils getrennt."),
            ("Muss ich in Österreich Steuern zahlen, wenn ich gemeldet werde?", "Nicht automatisch. Wer eigene, gebrauchte Sachen günstiger verkauft, als er sie gekauft hat, macht keinen Gewinn. Gewinne aus Verkäufen innerhalb eines Jahres nach dem Kauf sind Spekulationsgeschäfte, bleiben aber steuerfrei, solange sie im Jahr insgesamt 440 € nicht übersteigen. Wer gezielt einkauft, um mit Gewinn weiterzuverkaufen, kann als gewerblich gelten."),
            ("Zählen meine Verkäufe auf verschiedenen Plattformen zusammen?", "Für die Meldung nicht. Jede Plattform prüft nur die Verkäufe bei sich. Für deine Steuer zählt aber dein gesamtes Einkommen, egal auf welcher Plattform es entstanden ist."),
            ("Ändern sich die Grenzen bald?", "Die EU-Kommission hat 2026 vorgeschlagen, die Grenze für Warenverkäufe auf 3.000 € anzuheben und die 30-Verkäufe-Regel zu streichen. Das wäre frühestens ab 2028 der Fall und ist noch nicht beschlossen. Mit dem Schalter im Check kannst du ausprobieren, was das für dich ändern würde."),
        ],
        disclaimer="Dieser Check ist eine Orientierungshilfe und keine Steuer- oder Rechtsberatung. Im Zweifel frag beim Finanzamt Österreich oder einer Steuerberatung nach. Stand: November 2026.",
    )
    return at

def germany_overrides(de):
    de.update(
        name="Deutsch (Deutschland)",
        ex_p1="DAC7 ist eine EU-Regel, die Online-Plattformen verpflichtet, Daten ihrer Verkäufer an die Steuerbehörden zu melden. In Deutschland gilt sie seit 2023 als Plattformen-Steuertransparenzgesetz (PStTG); die Daten gehen an das Bundeszentralamt für Steuern. Es ist eine Meldepflicht, keine neue Steuer.",
    )
    de["faq"] = [de["faq"][0],
        ("Muss ich Steuern zahlen, wenn ich gemeldet werde?", "Nicht automatisch. Der Verkauf eigener, gebrauchter Alltagsgegenstände wie Kleidung oder Möbel ist steuerfrei. Gewinne aus Verkäufen innerhalb eines Jahres nach dem Kauf sind steuerpflichtig, wenn sie im Jahr 1.000 € erreichen. Wer gezielt einkauft, um mit Gewinn weiterzuverkaufen, kann als gewerblich gelten."),
        de["faq"][2], de["faq"][3]]
