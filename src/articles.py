# Guide articles. Each article exists in German ("de") and English ("en"); same key = translations of each other.
# body: HTML. sources: (label, url) pairs actually used.

UPDATED = "2026-11-26"

GUIDES = {
 "de": {"dir": "ratgeber", "title": "Ratgeber", "intro": "Antworten auf die häufigsten Fragen rund um DAC7, Vinted und das Finanzamt.",
        "updated": "Stand: 26. November 2026", "read": "Weiterlesen", "back": "Zurück zum DAC7-Check",
        "cta_title": "Wie nah bist du an der Meldegrenze?", "cta_text": "Prüf es pro Plattform in einer Minute mit dem kostenlosen DAC7-Check.", "cta_btn": "Zum DAC7-Check",
        "track": "Oder führe das ganze Jahr Buch über Gewinn und DAC7-Stand mit dem", "track_link": "Reseller Profit &amp; DAC7 Tracker",
        "sources": "Quellen", "disclaimer": "Dieser Artikel ist eine allgemeine Information und keine Steuer- oder Rechtsberatung."},
 "en": {"dir": "guides", "title": "Guides", "intro": "Answers to the most common questions about DAC7, Vinted and the tax office.",
        "updated": "Last updated: 26 November 2026", "read": "Read more", "back": "Back to the DAC7 Check",
        "cta_title": "How close are you to the reporting limit?", "cta_text": "Check each platform in a minute with the free DAC7 Check.", "cta_btn": "Open the DAC7 Check",
        "track": "Or keep track of profit and DAC7 status all year with the", "track_link": "Reseller Profit &amp; DAC7 Tracker",
        "sources": "Sources", "disclaimer": "This article is general information, not tax or legal advice."},
}

S_EBAY = ("eBay Hilfe: EU DAC7 und das Plattformen-Steuertransparenzgesetz", "https://www.ebay.de/help/selling/selling/eu-dac7-und-das-plattformensteuertransparenzgesetz-meldepflichten?id=5394")
S_MOBI = ("mobiflip: Kleinanzeigen erklärt, was den Finanzbehörden gemeldet wird (15.06.2024)", "https://www.mobiflip.de/shortnews/dac7-kleinanzeigen-erklaert-was-den-finanzbehoerden-gemeldet-wird/")
S_PSTTG = ("Plattformen-Steuertransparenzgesetz (PStTG)", "https://www.gesetze-im-internet.de/psttg/BJNR273010022.html")
S_DPMG = ("Digitale Plattformen-Meldepflichtgesetz (DPMG), RIS", "https://www.ris.bka.gv.at/eli/bgbl/i/2022/108/P0/NOR40246155")
S_DELOITTE = ("Deloitte Österreich: Meldepflichten für Plattformen wie willhaben", "https://www.deloitte.com/at/de/what-we-do/regions/praxistipps/03-2024-rechtstipp-willhaben-airbnb.html")
S_CORRECTIV = ("Correctiv-Faktencheck: Keine Steuer auf private Verkäufe (29.10.2026)", "https://correctiv.org/faktencheck/2026/10/29/keine-steuer-auf-private-verkaeufe-flohmarkt-vinted-ebay/")
S_SMART = ("smartsteuer: Neue Meldepflicht – das weiß das Finanzamt jetzt über dich (20.09.2026)", "https://www.smartsteuer.de/online/blog/neue-meldepflicht-das-weiss-das-finanzamt-jetzt-ueber-dich/")
S_31 = ("§ 31 EStG Österreich (Spekulationsgeschäfte), JUSLINE", "https://www.jusline.at/gesetz/estg/paragraf/31")
S_EU = ("Council Directive (EU) 2021/514 (DAC7), EUR-Lex", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021L0514")
S_EU_DE = ("Richtlinie (EU) 2021/514 (DAC7), EUR-Lex", "https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021L0514")

ARTICLES = [
 {
  "id": "tax-id",
  "de": {"slug": "vinted-steuer-id-angeben",
   "title": "Vinted fragt nach deiner Steuer-ID: Musst du sie angeben?",
   "desc": "Warum Vinted, eBay und Co. nach deiner Steuer-ID fragen, welche Daten ans Finanzamt gehen und was passiert, wenn du sie nicht angibst.",
   "answer": "Ja. Wenn eine Plattform nach den DAC7-Regeln deine Steuer-ID verlangt, musst du sie angeben, sonst darf sie Auszahlungen zurückhalten oder dein Verkäuferkonto einschränken. Die Angabe allein bedeutet nicht, dass du Steuern zahlen musst.",
   "body": """
<h2>Warum fragt die Plattform überhaupt?</h2>
<p>Seit 2023 müssen Online-Plattformen in der EU Daten über ihre Verkäufer sammeln und einmal im Jahr an die Steuerbehörden melden. Grundlage ist die EU-Richtlinie DAC7, in Deutschland umgesetzt als Plattformen-Steuertransparenzgesetz (PStTG), in Österreich als Digitale Plattformen-Meldepflichtgesetz (DPMG).</p>
<p>Gemeldet wird, wer auf einer Plattform in einem Kalenderjahr 30 Verkäufe erreicht oder mehr als 2.000 € einnimmt. Viele Plattformen fragen deine Daten aber schon vorher ab, damit sie rechtzeitig vollständig sind.</p>
<h2>Welche Daten werden gemeldet?</h2>
<ul>
<li>Name, Anschrift und Geburtsdatum</li>
<li>deine Steuer-Identifikationsnummer (in Deutschland die 11-stellige Steuer-ID)</li>
<li>Anzahl deiner Verkäufe und die Beträge, die du dafür bekommen hast, nach Abzug der Plattformgebühren</li>
</ul>
<p>Hast du in Deutschland keine Steuer-ID, verlangt zum Beispiel eBay stattdessen deinen Geburtsort.</p>
<h2>Was passiert, wenn du sie nicht angibst?</h2>
<p>Die Plattform muss dich erinnern. Reagierst du nicht, darf sie Auszahlungen einbehalten oder deine Verkaufsrechte einschränken, bis die Angaben vollständig sind. eBay schreibt das ausdrücklich in seiner Hilfe. Die Meldung wird dadurch nicht verhindert, nur dein Konto blockiert.</p>
<h2>So gehst du sicher vor</h2>
<ul>
<li>Trag die Steuer-ID nur direkt in der App oder auf der Website der Plattform ein, nie über einen Link in einer E-Mail oder SMS. Betrüger nutzen DAC7 gerne als Vorwand.</li>
<li>Deine deutsche Steuer-ID steht auf deinem letzten Steuerbescheid oder deiner Lohnsteuerbescheinigung.</li>
<li>Prüf mit dem DAC7-Check, ob du die Grenze in diesem Jahr überhaupt erreichst.</li>
</ul>
<h2>Heißt das, ich muss Steuern zahlen?</h2>
<p>Nein. Die Meldung informiert nur das Finanzamt. Ob Steuern anfallen, hängt davon ab, was du verkaufst und ob du privat oder gewerblich handelst. Mehr dazu im Artikel <a href="../privat-oder-gewerblich-verkaufen/">Privat oder gewerblich verkaufen</a>.</p>
""",
   "sources": [S_EBAY, S_MOBI, S_PSTTG, S_DPMG]},
  "en": {"slug": "vinted-tax-id-request",
   "title": "Vinted asks for your tax ID: do you have to give it?",
   "desc": "Why Vinted, eBay and other platforms ask for your tax ID, which data goes to the tax office, and what happens if you don't provide it.",
   "answer": "Yes. When a platform asks for your tax ID under the DAC7 rules, you have to provide it, or it may withhold payouts or restrict your seller account. Giving it does not mean you owe tax.",
   "body": """
<h2>Why is the platform asking?</h2>
<p>Since 2023, online platforms in the EU must collect data about their sellers and report it to the tax authorities once a year. The legal basis is the EU directive DAC7, which every EU country has turned into national law.</p>
<p>You are reported if you reach 30 sales or take in more than €2,000 on one platform in a calendar year. Many platforms ask for your details earlier, so that they are complete in time.</p>
<h2>Which data is reported?</h2>
<ul>
<li>Your name, address and date of birth</li>
<li>Your tax identification number, issued by the country where you live</li>
<li>The number of sales and the amounts you received for them, after platform fees</li>
</ul>
<h2>What happens if you don't provide it?</h2>
<p>The platform has to remind you. If you don't respond, it may withhold payouts or restrict your selling rights until your details are complete. eBay says so explicitly in its help pages. Refusing does not stop the report; it only blocks your account.</p>
<h2>How to do it safely</h2>
<ul>
<li>Enter your tax ID only directly in the platform's app or website, never through a link in an email or text message. Scammers like to use DAC7 as a pretext.</li>
<li>Your tax ID is usually printed on your last tax assessment or payslip documents.</li>
<li>Use the DAC7 Check to see whether you will reach the limit this year at all.</li>
</ul>
<h2>Does this mean I have to pay tax?</h2>
<p>No. The report only informs the tax office. Whether tax is due depends on what you sell and whether you sell privately or as a business. Read more in <a href="../private-seller-or-business-reseller/">Private seller or business?</a></p>
""",
   "sources": [S_EBAY, S_EU]},
 },
 {
  "id": "letter",
  "de": {"slug": "post-vom-finanzamt-nach-dac7-meldung",
   "title": "Post vom Finanzamt nach der DAC7-Meldung: Was jetzt?",
   "desc": "Du hast nach Verkäufen auf Vinted, eBay oder willhaben einen Brief vom Finanzamt bekommen? So reagierst du richtig, in Deutschland und Österreich.",
   "answer": "Ruhig bleiben, aber nicht ignorieren. Das Finanzamt will meist nur wissen, ob hinter den gemeldeten Verkäufen steuerpflichtige Einkünfte stecken. Wer eigene gebrauchte Sachen verkauft hat, kann das in der Regel kurz erklären.",
   "body": """
<h2>Warum schreibt dir das Finanzamt?</h2>
<p>Plattformen melden jedes Jahr bis 31. Januar, wer im Vorjahr 30 Verkäufe erreicht oder mehr als 2.000 € eingenommen hat. Das Finanzamt gleicht diese Daten mit deiner Steuererklärung ab. Passt etwas nicht zusammen, kann es nachfragen. Eine Nachfrage ist keine Strafe und kein Steuerbescheid.</p>
<h2>Schritt für Schritt</h2>
<ol>
<li><strong>Frist notieren.</strong> Im Brief steht, bis wann du antworten sollst. Reicht die Zeit nicht, kannst du um Verlängerung bitten.</li>
<li><strong>Verkäufe zusammenstellen.</strong> Lade dir in der App deine Verkaufsübersicht für das Jahr herunter: was du verkauft hast, wann und für wie viel.</li>
<li><strong>Einordnen.</strong> Waren es eigene, gebrauchte Sachen? Oder hast du gezielt eingekauft, um weiterzuverkaufen?</li>
<li><strong>Kurz und ehrlich antworten.</strong> Bei Privatverkäufen reicht meist eine kurze Erklärung, zum Beispiel: „Es handelt sich um den Verkauf gebrauchter Kleidung aus meinem Haushalt, überwiegend unter dem ursprünglichen Kaufpreis."</li>
</ol>
<h2>Wann wird es steuerlich relevant?</h2>
<p><strong>In Deutschland</strong> ist der Verkauf eigener, gebrauchter Alltagsgegenstände wie Kleidung, Möbel oder Bücher steuerfrei. Steuerpflichtig können Gewinne aus Gegenständen sein, die du innerhalb eines Jahres nach dem Kauf wieder verkaufst. Sie bleiben steuerfrei, solange dein Gesamtgewinn daraus im Jahr unter 1.000 € liegt.</p>
<p><strong>In Österreich</strong> gelten Verkäufe innerhalb eines Jahres nach dem Kauf als Spekulationsgeschäfte. Gewinne daraus bleiben steuerfrei, solange sie im Kalenderjahr insgesamt 440 € nicht übersteigen. Wer eigene Sachen billiger verkauft, als er sie gekauft hat, macht ohnehin keinen Gewinn.</p>
<p>In beiden Ländern gilt: Wer regelmäßig einkauft, um mit Gewinn weiterzuverkaufen, handelt unter Umständen gewerblich. Dann gelten andere Regeln, und eine Steuerberatung lohnt sich.</p>
<h2>Für das nächste Jahr</h2>
<p>Führ eine einfache Liste: was du gekauft und verkauft hast und zu welchem Preis. Dann ist jede Rückfrage in wenigen Minuten beantwortet.</p>
""",
   "sources": [S_SMART, S_CORRECTIV, S_31, S_DPMG]},
  "en": {"slug": "letter-from-tax-office-after-dac7-report",
   "title": "A letter from the tax office after a DAC7 report: what now?",
   "desc": "You received a letter from the tax office after selling on Vinted, eBay or other platforms? Here is how to respond calmly and correctly.",
   "answer": "Stay calm, but don't ignore it. The tax office usually just wants to know whether the reported sales include taxable income. If you sold your own used things, you can normally explain that in a few lines.",
   "body": """
<h2>Why is the tax office writing to you?</h2>
<p>Every year, by 31 January, platforms report everyone who reached 30 sales or took in more than €2,000 on them in the previous year. The tax office compares this data with your tax return. If something doesn't match, it may ask. A question is neither a fine nor a tax bill.</p>
<h2>Step by step</h2>
<ol>
<li><strong>Note the deadline.</strong> The letter says when you need to reply. If you need more time, you can usually ask for an extension.</li>
<li><strong>Collect your sales.</strong> Download your sales overview for the year from the app: what you sold, when and for how much.</li>
<li><strong>Sort them.</strong> Were these your own used belongings? Or did you buy items specifically to resell them?</li>
<li><strong>Reply briefly and honestly.</strong> For private sales, a short explanation is usually enough, for example: "These were sales of used clothing from my household, mostly below the original purchase price."</li>
</ol>
<h2>When does tax come into play?</h2>
<p>In most EU countries, selling your own used everyday items below what you paid for them creates no taxable profit. Rules differ for items resold shortly after buying them and for anyone who buys goods to resell at a profit, which can count as a business. In Germany, for example, gains from items resold within a year stay tax-free below €1,000 per year; in Austria the limit is €440.</p>
<p>If you regularly buy to resell, or the amounts are large, it's worth asking a tax advisor in your country.</p>
<h2>For next year</h2>
<p>Keep a simple list of what you bought and sold, and at what price. Then any question from the tax office takes minutes to answer.</p>
""",
   "sources": [S_SMART, S_31, S_EU]},
 },
 {
  "id": "platforms",
  "de": {"slug": "dac7-vinted-ebay-kleinanzeigen-willhaben",
   "title": "DAC7 bei Vinted, eBay, Kleinanzeigen und willhaben: Was wird gemeldet?",
   "desc": "Welche Verkäufe Vinted, eBay, Kleinanzeigen und willhaben ans Finanzamt melden, wie gezählt wird und warum Inserate allein nicht zählen.",
   "answer": "Gemeldet werden nur abgeschlossene Verkäufe, deren Bezahlung über die Plattform läuft. Bei Kleinanzeigen und willhaben zählen also Verkäufe über die eigene Bezahlfunktion, nicht Barverkäufe bei Abholung. Jede Plattform zählt für sich.",
   "body": """
<h2>Was zählt als Verkauf?</h2>
<p>DAC7 zählt Transaktionen, also tatsächlich abgeschlossene und bezahlte Verkäufe. Wie viele Inserate du online hast, spielt keine Rolle. Die Plattform kann nur melden, was sie selbst abwickelt.</p>
<h2>Die Plattformen im Überblick</h2>
<ul>
<li><strong>Vinted:</strong> Fast alle Verkäufe laufen über die Bezahlfunktion von Vinted und zählen daher mit.</li>
<li><strong>eBay:</strong> eBay wickelt Zahlungen selbst ab. Gezählt werden deine verkauften Artikel; eBay erinnert dich im Verkäufer-Cockpit, wenn Daten fehlen.</li>
<li><strong>Kleinanzeigen:</strong> Gemeldet werden nur Verkäufe, die über das Bezahlsystem von Kleinanzeigen abgeschlossen wurden. Barzahlung bei Abholung kennt die Plattform nicht.</li>
<li><strong>willhaben:</strong> Nach dem österreichischen DPMG sind Verkäufe meldepflichtig, deren Zahlung über die Plattform läuft.</li>
</ul>
<h2>Jede Plattform zählt getrennt</h2>
<p>Die Grenzen von 30 Verkäufen oder mehr als 2.000 € gelten pro Plattform. 25 Verkäufe auf Vinted und 25 auf eBay lösen also keine Meldung aus. Für deine Steuer zählt aber dein gesamtes Einkommen, egal wo es entstanden ist.</p>
<h2>Was wird mit den Beträgen gemeldet?</h2>
<p>Gemeldet wird, was du für deine Verkäufe bekommen hast, abzüglich der Gebühren, die die Plattform einbehält, dazu Name, Anschrift, Geburtsdatum und Steuer-ID.</p>
""",
   "sources": [S_MOBI, S_EBAY, S_DELOITTE, S_EU_DE]},
  "en": {"slug": "dac7-vinted-ebay-etsy-what-gets-reported",
   "title": "DAC7 on Vinted, eBay and Etsy: what gets reported?",
   "desc": "Which sales Vinted, eBay, Etsy and local marketplaces report to the tax office, how they are counted, and why listings alone don't count.",
   "answer": "Only completed sales that are paid through the platform are reported. On classifieds sites, cash sales at pickup don't count, because the platform never sees them. Each platform counts separately.",
   "body": """
<h2>What counts as a sale?</h2>
<p>DAC7 counts transactions: sales that were actually completed and paid. How many listings you have online doesn't matter. A platform can only report what it processes itself.</p>
<h2>The platforms at a glance</h2>
<ul>
<li><strong>Vinted:</strong> almost all sales go through Vinted's own payment system, so they all count.</li>
<li><strong>eBay and Etsy:</strong> both handle payments themselves, so every sold item counts.</li>
<li><strong>Classifieds sites</strong> such as Kleinanzeigen, willhaben, Leboncoin or OLX: only sales completed through the site's own payment or shipping service are counted. Cash at pickup isn't visible to them.</li>
</ul>
<h2>Each platform counts separately</h2>
<p>The limits of 30 sales or more than €2,000 apply per platform. 25 sales on Vinted and 25 on eBay trigger no report. For your taxes, though, your total income counts, wherever it came from.</p>
<h2>What is reported with the amounts?</h2>
<p>The amounts you received for your sales, minus the fees the platform kept, together with your name, address, date of birth and tax ID.</p>
""",
   "sources": [S_MOBI, S_EBAY, S_EU]},
 },
 {
  "id": "business",
  "de": {"slug": "privat-oder-gewerblich-verkaufen",
   "title": "Privat oder gewerblich verkaufen: Wo liegt die Grenze?",
   "desc": "Ab wann gilt Verkaufen auf Vinted, eBay oder willhaben als Gewerbe? Die wichtigsten Kriterien für Deutschland und Österreich, verständlich erklärt.",
   "answer": "Es gibt keine feste Zahl. Entscheidend ist, ob du eigene Sachen loswirst oder gezielt einkaufst, um mit Gewinn weiterzuverkaufen. Im zweiten Fall kann schon der erste Verkauf gewerblich sein.",
   "body": """
<h2>Privat: Ausmisten</h2>
<p>Wer Kleidung, Möbel, Bücher oder Spielzeug aus dem eigenen Haushalt verkauft, handelt privat, auch wenn es viele Verkäufe sind. Da gebrauchte Sachen meist günstiger weggehen, als sie gekostet haben, entsteht kein Gewinn.</p>
<h2>Gewerblich: Handeln mit Gewinnabsicht</h2>
<p>Gerichte und Finanzämter schauen auf das Gesamtbild. Typische Anzeichen für ein Gewerbe:</p>
<ul>
<li>Du kaufst regelmäßig Ware ein, um sie weiterzuverkaufen, etwa auf Flohmärkten, im Outlet oder als Restposten.</li>
<li>Du bietest viele gleiche oder neue Artikel an.</li>
<li>Dein Auftritt wirkt wie ein Shop: dauerhaftes Angebot, einheitliche Fotos, feste Abläufe.</li>
</ul>
<p>Entscheidend ist die Absicht. Wer von Anfang an mit Gewinn weiterverkaufen will, kann schon ab dem ersten Verkauf gewerblich handeln.</p>
<h2>Was dann gilt</h2>
<p>Gewerbliche Verkäufer müssen in der Regel ein Gewerbe anmelden, Gewinne versteuern und sich um die Umsatzsteuer kümmern. Für kleine Umsätze gibt es in Deutschland und Österreich eine Kleinunternehmerregelung. Lass dich im Zweifel beraten, bevor das Finanzamt nachfragt.</p>
<h2>Dazwischen: gezielte Einzelverkäufe</h2>
<p>Verkaufst du privat etwas mit Gewinn, das du erst vor kurzem gekauft hast, kann das ein privates Veräußerungsgeschäft sein. In Deutschland bleibt der Gesamtgewinn daraus unter 1.000 € pro Jahr steuerfrei, in Österreich bis 440 €.</p>
<h2>Tipp</h2>
<p>Wer weiterverkauft, sollte wissen, was am Ende übrig bleibt. Halte Einkaufspreis, Verkaufspreis und Gebühren für jeden Artikel fest. Genau dafür gibt es den Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [S_CORRECTIV, S_SMART, S_31]},
  "en": {"slug": "private-seller-or-business-reseller",
   "title": "Private seller or business? Where the line is for resellers",
   "desc": "When does selling on Vinted, eBay or Etsy count as a business? The main criteria tax offices look at, explained simply.",
   "answer": "There is no fixed number of sales. What matters is whether you are clearing out your own things or buying items to resell at a profit. In the second case, even your first sale can count as business activity.",
   "body": """
<h2>Private: clearing out</h2>
<p>Selling clothes, furniture, books or toys from your own household is private selling, even if there are many sales. Used things usually sell for less than they cost, so there is no profit to tax.</p>
<h2>Business: trading for profit</h2>
<p>Tax offices and courts look at the overall picture. Typical signs of a business:</p>
<ul>
<li>You regularly buy goods in order to resell them, for example at flea markets, outlets or clearance sales.</li>
<li>You offer many identical or new items.</li>
<li>Your account looks like a shop: a permanent range, uniform photos, fixed routines.</li>
</ul>
<p>Intent is what counts. If you buy with the plan to resell at a profit, you can be trading as a business from the first sale.</p>
<h2>What applies then</h2>
<p>Business sellers usually have to register, pay income tax on their profits and deal with VAT. Most EU countries have simplified rules for small businesses. The details depend on your country, so ask a tax advisor before the tax office asks you.</p>
<h2>Keep the numbers</h2>
<p>If you resell, you should know what's left at the end. Record the purchase price, sale price and fees for every item. That is exactly what the Reseller Profit &amp; DAC7 Tracker is for.</p>
""",
   "sources": [S_CORRECTIV, S_SMART, S_EU]},
 },
]
