# Guide articles in more languages. Same article ids as articles.py.
# These follow the EU-wide English versions; no country-specific tax figures unless sourced.

def eurlex(lang_code, label):
    return (label, f"https://eur-lex.europa.eu/legal-content/{lang_code}/TXT/?uri=CELEX:32021L0514")

S_EBAY = ("eBay: EU DAC7 und das Plattformen-Steuertransparenzgesetz (DE)", "https://www.ebay.de/help/selling/selling/eu-dac7-und-das-plattformensteuertransparenzgesetz-meldepflichten?id=5394")
S_MOBI = ("mobiflip: Kleinanzeigen erklärt, was gemeldet wird (DE, 15.06.2024)", "https://www.mobiflip.de/shortnews/dac7-kleinanzeigen-erklaert-was-den-finanzbehoerden-gemeldet-wird/")
S_CORRECTIV = ("Correctiv: Keine Steuer auf private Verkäufe (DE, 29.10.2026)", "https://correctiv.org/faktencheck/2026/10/29/keine-steuer-auf-private-verkaeufe-flohmarkt-vinted-ebay/")

MORE_GUIDES = {
 "fr": {"dir": "guides", "title": "Guides", "intro": "Réponses aux questions les plus fréquentes sur DAC7, Vinted et les impôts.",
        "updated": "Mis à jour : 26 novembre 2026", "read": "Lire la suite", "back": "Retour au simulateur DAC7",
        "cta_title": "À quelle distance êtes-vous de la limite ?", "cta_text": "Vérifiez chaque plateforme en une minute avec le simulateur DAC7 gratuit.", "cta_btn": "Ouvrir le simulateur DAC7",
        "track": "Ou suivez toute l'année votre bénéfice et votre statut DAC7 avec le", "track_link": "Reseller Profit &amp; DAC7 Tracker (en anglais)",
        "sources": "Sources", "disclaimer": "Cet article est une information générale et non un conseil fiscal ou juridique."},
 "it": {"dir": "guide", "title": "Guide", "intro": "Risposte alle domande più frequenti su DAC7, Vinted e il Fisco.",
        "updated": "Aggiornato: 26 novembre 2026", "read": "Leggi di più", "back": "Torna alla verifica DAC7",
        "cta_title": "Quanto sei vicino al limite?", "cta_text": "Controlla ogni piattaforma in un minuto con la verifica DAC7 gratuita.", "cta_btn": "Apri la verifica DAC7",
        "track": "Oppure tieni traccia tutto l'anno di guadagni e stato DAC7 con il", "track_link": "Reseller Profit &amp; DAC7 Tracker (in inglese)",
        "sources": "Fonti", "disclaimer": "Questo articolo è un'informazione generale e non costituisce consulenza fiscale o legale."},
 "es": {"dir": "guias", "title": "Guías", "intro": "Respuestas a las preguntas más frecuentes sobre DAC7, Vinted y Hacienda.",
        "updated": "Actualizado: 26 de noviembre de 2026", "read": "Leer más", "back": "Volver al comprobador DAC7",
        "cta_title": "¿Cuánto te falta para el límite?", "cta_text": "Compruébalo por plataforma en un minuto con el comprobador DAC7 gratuito.", "cta_btn": "Abrir el comprobador DAC7",
        "track": "O controla todo el año tu beneficio y tu estado DAC7 con el", "track_link": "Reseller Profit &amp; DAC7 Tracker (en inglés)",
        "sources": "Fuentes", "disclaimer": "Este artículo es información general, no asesoramiento fiscal ni jurídico."},
 "nl": {"dir": "gidsen", "title": "Gidsen", "intro": "Antwoorden op de meest gestelde vragen over DAC7, Vinted en de Belastingdienst.",
        "updated": "Bijgewerkt: 26 november 2026", "read": "Verder lezen", "back": "Terug naar de DAC7-check",
        "cta_title": "Hoe dicht zit je bij de grens?", "cta_text": "Check het per platform in een minuut met de gratis DAC7-check.", "cta_btn": "Open de DAC7-check",
        "track": "Of houd het hele jaar je winst en DAC7-status bij met de", "track_link": "Reseller Profit &amp; DAC7 Tracker (Engelstalig)",
        "sources": "Bronnen", "disclaimer": "Dit artikel is algemene informatie en geen fiscaal of juridisch advies."},
 "pl": {"dir": "poradniki", "title": "Poradniki", "intro": "Odpowiedzi na najczęstsze pytania o DAC7, Vinted i urząd skarbowy.",
        "updated": "Aktualizacja: 26 listopada 2026", "read": "Czytaj dalej", "back": "Wróć do testu DAC7",
        "cta_title": "Jak blisko jesteś limitu?", "cta_text": "Sprawdź każdą platformę w minutę w darmowym teście DAC7.", "cta_btn": "Otwórz test DAC7",
        "track": "Albo śledź przez cały rok zysk i status DAC7 w", "track_link": "Reseller Profit &amp; DAC7 Tracker (po angielsku)",
        "sources": "Źródła", "disclaimer": "Ten artykuł ma charakter ogólnej informacji i nie stanowi porady podatkowej ani prawnej."},
}

MORE = {
 # ---------------------------------------------------------------- tax ID
 "tax-id": {
  "fr": {"slug": "vinted-numero-fiscal",
   "title": "Vinted vous demande votre numéro fiscal : devez-vous le donner ?",
   "desc": "Pourquoi Vinted, Leboncoin et eBay demandent votre numéro fiscal, quelles données vont aux impôts et ce qui se passe si vous ne le donnez pas.",
   "answer": "Oui. Quand une plateforme vous demande votre numéro fiscal au titre de DAC7, vous devez le fournir, sinon elle peut bloquer vos versements ou limiter votre compte vendeur. Le donner ne signifie pas que vous devez payer des impôts.",
   "body": """
<h2>Pourquoi la plateforme le demande-t-elle ?</h2>
<p>Depuis 2023, les plateformes en ligne de l'UE doivent collecter des données sur leurs vendeurs et les transmettre une fois par an à l'administration fiscale. La base est la directive européenne DAC7, transposée dans chaque pays de l'UE.</p>
<p>Vous êtes déclaré si vous atteignez 30 ventes ou plus de 2 000 € sur une même plateforme au cours d'une année civile. Beaucoup de plateformes demandent vos informations plus tôt, pour qu'elles soient complètes à temps.</p>
<h2>Quelles données sont transmises ?</h2>
<ul>
<li>Vos nom, adresse et date de naissance</li>
<li>Votre numéro fiscal, attribué par votre pays de résidence</li>
<li>Le nombre de ventes et les montants reçus, après déduction des frais de la plateforme</li>
</ul>
<h2>Que se passe-t-il si vous ne le donnez pas ?</h2>
<p>La plateforme doit vous relancer. Sans réponse, elle peut retenir vos versements ou limiter vos droits de vendeur jusqu'à ce que vos informations soient complètes. Refuser n'empêche pas la déclaration ; cela bloque seulement votre compte.</p>
<h2>Comment procéder en toute sécurité</h2>
<ul>
<li>Saisissez votre numéro fiscal uniquement dans l'application ou sur le site de la plateforme, jamais via un lien reçu par e-mail ou SMS. Les escrocs utilisent volontiers DAC7 comme prétexte.</li>
<li>Votre numéro fiscal figure en général sur votre dernier avis d'imposition.</li>
<li>Vérifiez avec le simulateur DAC7 si vous atteindrez la limite cette année.</li>
</ul>
<h2>Est-ce que je dois payer des impôts ?</h2>
<p>Non. La déclaration informe seulement l'administration. L'impôt dépend de ce que vous vendez et du fait que vous vendiez à titre privé ou professionnel. Voir <a href="../vendeur-particulier-ou-professionnel/">Particulier ou professionnel ?</a></p>
""",
   "sources": [eurlex("FR", "Directive (UE) 2021/514 du Conseil (DAC7), EUR-Lex"), S_EBAY]},
  "it": {"slug": "vinted-codice-fiscale",
   "title": "Vinted ti chiede il codice fiscale: devi darlo?",
   "desc": "Perché Vinted, Subito ed eBay chiedono il codice fiscale, quali dati arrivano al Fisco e cosa succede se non lo fornisci.",
   "answer": "Sì. Quando una piattaforma ti chiede il codice fiscale per la DAC7, devi fornirlo, altrimenti può trattenere i pagamenti o limitare il tuo account venditore. Darlo non significa che devi pagare tasse.",
   "body": """
<h2>Perché la piattaforma lo chiede?</h2>
<p>Dal 2023 le piattaforme online nell'UE devono raccogliere dati sui venditori e comunicarli una volta l'anno alle autorità fiscali. La base è la direttiva europea DAC7, recepita in ogni paese dell'UE.</p>
<p>Vieni segnalato se raggiungi 30 vendite o incassi più di 2.000 € su una stessa piattaforma in un anno solare. Molte piattaforme chiedono i dati prima, perché siano completi in tempo.</p>
<h2>Quali dati vengono comunicati?</h2>
<ul>
<li>Nome, indirizzo e data di nascita</li>
<li>Il codice fiscale o numero di identificazione fiscale del tuo paese</li>
<li>Il numero di vendite e gli importi ricevuti, al netto delle commissioni della piattaforma</li>
</ul>
<h2>Cosa succede se non lo fornisci?</h2>
<p>La piattaforma deve sollecitarti. Se non rispondi, può trattenere i pagamenti o limitare i tuoi diritti di venditore finché i dati non sono completi. Rifiutare non evita la segnalazione: blocca solo il tuo account.</p>
<h2>Come farlo in sicurezza</h2>
<ul>
<li>Inserisci il codice fiscale solo nell'app o sul sito della piattaforma, mai tramite un link ricevuto via e-mail o SMS. I truffatori usano spesso la DAC7 come pretesto.</li>
<li>Controlla con la verifica DAC7 se quest'anno raggiungerai davvero il limite.</li>
</ul>
<h2>Devo pagare le tasse?</h2>
<p>No. La segnalazione informa soltanto il Fisco. Le tasse dipendono da cosa vendi e se vendi da privato o come attività. Leggi <a href="../venditore-privato-o-attivita/">Privato o attività commerciale?</a></p>
""",
   "sources": [eurlex("IT", "Direttiva (UE) 2021/514 del Consiglio (DAC7), EUR-Lex"), S_EBAY]},
  "es": {"slug": "vinted-nif",
   "title": "Vinted te pide el NIF: ¿tienes que darlo?",
   "desc": "Por qué Vinted, Wallapop y eBay piden tu NIF, qué datos llegan a Hacienda y qué pasa si no lo das.",
   "answer": "Sí. Cuando una plataforma te pide el NIF por la DAC7, tienes que darlo; si no, puede retener tus cobros o limitar tu cuenta de vendedor. Darlo no significa que tengas que pagar impuestos.",
   "body": """
<h2>¿Por qué lo pide la plataforma?</h2>
<p>Desde 2023, las plataformas online de la UE deben recopilar datos de sus vendedores y comunicarlos una vez al año a las autoridades fiscales. La base es la directiva europea DAC7, incorporada en todos los países de la UE.</p>
<p>Se informa sobre ti si llegas a 30 ventas o ingresas más de 2.000 € en una misma plataforma en un año natural. Muchas plataformas piden los datos antes, para tenerlos completos a tiempo.</p>
<h2>¿Qué datos se comunican?</h2>
<ul>
<li>Nombre, dirección y fecha de nacimiento</li>
<li>Tu número de identificación fiscal (en España, el NIF)</li>
<li>El número de ventas y los importes recibidos, descontadas las comisiones de la plataforma</li>
</ul>
<h2>¿Qué pasa si no lo das?</h2>
<p>La plataforma tiene que recordártelo. Si no respondes, puede retener tus cobros o limitar tus derechos de vendedor hasta que los datos estén completos. Negarte no evita la comunicación; solo bloquea tu cuenta.</p>
<h2>Cómo hacerlo con seguridad</h2>
<ul>
<li>Introduce el NIF solo en la app o en la web de la plataforma, nunca a través de un enlace recibido por correo o SMS. Los estafadores usan la DAC7 como excusa.</li>
<li>Comprueba con el comprobador DAC7 si este año llegarás al límite.</li>
</ul>
<h2>¿Tengo que pagar impuestos?</h2>
<p>No. La comunicación solo informa a Hacienda. Los impuestos dependen de lo que vendas y de si vendes como particular o como actividad económica. Lee <a href="../vendedor-particular-o-actividad/">¿Particular o actividad económica?</a></p>
""",
   "sources": [eurlex("ES", "Directiva (UE) 2021/514 del Consejo (DAC7), EUR-Lex"), S_EBAY]},
  "nl": {"slug": "vinted-fiscaal-nummer",
   "title": "Vinted vraagt je fiscaal nummer: moet je het geven?",
   "desc": "Waarom Vinted, Marktplaats en eBay om je fiscaal nummer vragen, welke gegevens naar de Belastingdienst gaan en wat er gebeurt als je het niet geeft.",
   "answer": "Ja. Als een platform op grond van DAC7 om je fiscaal nummer vraagt, moet je het geven; anders mag het uitbetalingen inhouden of je verkopersaccount beperken. Het geven betekent niet dat je belasting moet betalen.",
   "body": """
<h2>Waarom vraagt het platform erom?</h2>
<p>Sinds 2023 moeten onlineplatforms in de EU gegevens over hun verkopers verzamelen en eens per jaar doorgeven aan de belastingdienst. De basis is de Europese richtlijn DAC7, die elk EU-land heeft omgezet.</p>
<p>Je wordt gemeld als je op één platform in één kalenderjaar 30 verkopen haalt of meer dan € 2.000 ontvangt. Veel platforms vragen je gegevens al eerder op, zodat ze op tijd compleet zijn.</p>
<h2>Welke gegevens worden doorgegeven?</h2>
<ul>
<li>Naam, adres en geboortedatum</li>
<li>Je fiscaal identificatienummer (in Nederland je BSN)</li>
<li>Het aantal verkopen en de bedragen die je ontving, na aftrek van de platformkosten</li>
</ul>
<h2>Wat gebeurt er als je het niet geeft?</h2>
<p>Het platform moet je herinneren. Reageer je niet, dan mag het uitbetalingen inhouden of je verkoopmogelijkheden beperken tot je gegevens compleet zijn. Weigeren voorkomt de melding niet; het blokkeert alleen je account.</p>
<h2>Zo doe je het veilig</h2>
<ul>
<li>Vul je nummer alleen in de app of op de website van het platform in, nooit via een link in een e-mail of sms. Oplichters gebruiken DAC7 graag als smoes.</li>
<li>Check met de DAC7-check of je de grens dit jaar überhaupt haalt.</li>
</ul>
<h2>Moet ik belasting betalen?</h2>
<p>Nee. De melding informeert alleen de Belastingdienst. Of je belasting betaalt, hangt af van wat je verkoopt en of je als particulier of als ondernemer verkoopt. Lees <a href="../particulier-of-ondernemer/">Particulier of ondernemer?</a></p>
""",
   "sources": [eurlex("NL", "Richtlijn (EU) 2021/514 van de Raad (DAC7), EUR-Lex"), S_EBAY]},
  "pl": {"slug": "vinted-numer-podatkowy",
   "title": "Vinted prosi o numer podatkowy: czy musisz go podać?",
   "desc": "Dlaczego Vinted, Allegro i OLX proszą o numer podatkowy, jakie dane trafiają do urzędu skarbowego i co się stanie, jeśli go nie podasz.",
   "answer": "Tak. Gdy platforma prosi o numer podatkowy na podstawie DAC7, musisz go podać, inaczej może wstrzymać wypłaty lub ograniczyć Twoje konto sprzedawcy. Podanie numeru nie oznacza, że musisz zapłacić podatek.",
   "body": """
<h2>Dlaczego platforma o to prosi?</h2>
<p>Od 2023 roku platformy internetowe w UE muszą zbierać dane o sprzedawcach i raz w roku przekazywać je organom podatkowym. Podstawą jest unijna dyrektywa DAC7, wdrożona we wszystkich krajach UE.</p>
<p>Zostajesz zgłoszony, jeśli na jednej platformie w ciągu roku kalendarzowego osiągniesz 30 transakcji lub uzyskasz ponad 2000 €. Wiele platform prosi o dane wcześniej, aby mieć je na czas.</p>
<h2>Jakie dane są przekazywane?</h2>
<ul>
<li>Imię i nazwisko, adres i data urodzenia</li>
<li>Twój numer identyfikacji podatkowej (w Polsce PESEL lub NIP)</li>
<li>Liczba transakcji i otrzymane kwoty po odjęciu prowizji platformy</li>
</ul>
<h2>Co się stanie, jeśli go nie podasz?</h2>
<p>Platforma musi Ci przypomnieć. Jeśli nie odpowiesz, może wstrzymać wypłaty lub ograniczyć Twoje prawa sprzedawcy do czasu uzupełnienia danych. Odmowa nie zatrzymuje zgłoszenia, tylko blokuje konto.</p>
<h2>Jak zrobić to bezpiecznie</h2>
<ul>
<li>Wpisuj numer tylko w aplikacji lub na stronie platformy, nigdy przez link z e-maila lub SMS-a. Oszuści chętnie wykorzystują DAC7 jako pretekst.</li>
<li>Sprawdź w teście DAC7, czy w tym roku w ogóle osiągniesz limit.</li>
</ul>
<h2>Czy muszę zapłacić podatek?</h2>
<p>Nie. Zgłoszenie tylko informuje urząd skarbowy. Podatek zależy od tego, co sprzedajesz i czy robisz to prywatnie, czy w ramach działalności. Przeczytaj <a href="../sprzedaz-prywatna-czy-dzialalnosc/">Sprzedaż prywatna czy działalność?</a></p>
""",
   "sources": [eurlex("PL", "Dyrektywa Rady (UE) 2021/514 (DAC7), EUR-Lex"), S_EBAY]},
 },
 # ---------------------------------------------------------------- letter
 "letter": {
  "fr": {"slug": "courrier-des-impots-apres-declaration-dac7",
   "title": "Un courrier des impôts après une déclaration DAC7 : que faire ?",
   "desc": "Vous avez reçu un courrier de l'administration fiscale après des ventes sur Vinted, Leboncoin ou eBay ? Voici comment répondre calmement et correctement.",
   "answer": "Restez calme, mais ne l'ignorez pas. L'administration veut en général savoir si les ventes déclarées comprennent des revenus imposables. Si vous avez vendu vos propres affaires d'occasion, quelques lignes suffisent le plus souvent.",
   "body": """
<h2>Pourquoi l'administration vous écrit-elle ?</h2>
<p>Chaque année, avant le 31 janvier, les plateformes déclarent toutes les personnes qui ont atteint 30 ventes ou plus de 2 000 € chez elles l'année précédente. L'administration compare ces données avec votre déclaration. Si quelque chose ne colle pas, elle peut poser des questions. Une question n'est ni une amende ni un avis d'imposition.</p>
<h2>Étape par étape</h2>
<ol>
<li><strong>Notez le délai.</strong> Le courrier indique la date de réponse. Si vous avez besoin de plus de temps, vous pouvez en général demander un délai.</li>
<li><strong>Rassemblez vos ventes.</strong> Téléchargez dans l'application le récapitulatif de l'année : quoi, quand et à quel prix.</li>
<li><strong>Faites le tri.</strong> S'agissait-il de vos propres affaires d'occasion, ou d'articles achetés pour être revendus ?</li>
<li><strong>Répondez brièvement et honnêtement.</strong> Pour des ventes privées, une courte explication suffit souvent, par exemple : « Il s'agit de la vente de vêtements d'occasion de mon foyer, le plus souvent en dessous du prix d'achat. »</li>
</ol>
<h2>Quand l'impôt entre-t-il en jeu ?</h2>
<p>Dans la plupart des pays de l'UE, vendre vos propres objets d'occasion moins cher que vous ne les avez payés ne crée pas de bénéfice imposable. Les règles diffèrent pour les objets revendus peu après leur achat et pour ceux qui achètent pour revendre avec un bénéfice, ce qui peut constituer une activité professionnelle. Dans ce cas, renseignez-vous auprès de votre centre des impôts ou d'un conseiller.</p>
<h2>Pour l'année prochaine</h2>
<p>Tenez une liste simple de ce que vous achetez et vendez, et à quel prix. Toute question de l'administration se règle alors en quelques minutes.</p>
""",
   "sources": [eurlex("FR", "Directive (UE) 2021/514 du Conseil (DAC7), EUR-Lex")]},
  "it": {"slug": "lettera-agenzia-entrate-dopo-segnalazione-dac7",
   "title": "Una lettera dell'Agenzia delle Entrate dopo la segnalazione DAC7: che fare?",
   "desc": "Hai ricevuto una lettera dal Fisco dopo aver venduto su Vinted, Subito o eBay? Ecco come rispondere con calma e nel modo giusto.",
   "answer": "Mantieni la calma, ma non ignorarla. Di solito il Fisco vuole solo sapere se le vendite segnalate comprendono redditi tassabili. Se hai venduto le tue cose usate, in genere basta spiegarlo in poche righe.",
   "body": """
<h2>Perché ti scrive il Fisco?</h2>
<p>Ogni anno, entro il 31 gennaio, le piattaforme segnalano chi l'anno precedente ha raggiunto 30 vendite o incassato più di 2.000 € su di esse. Il Fisco confronta questi dati con la tua dichiarazione. Se qualcosa non torna, può chiedere chiarimenti. Una richiesta non è né una multa né un avviso di pagamento.</p>
<h2>Passo dopo passo</h2>
<ol>
<li><strong>Annota la scadenza.</strong> La lettera indica entro quando rispondere.</li>
<li><strong>Raccogli le vendite.</strong> Scarica dall'app il riepilogo dell'anno: cosa hai venduto, quando e a quanto.</li>
<li><strong>Classificale.</strong> Erano cose tue usate, oppure articoli comprati apposta per rivenderli?</li>
<li><strong>Rispondi in modo breve e onesto.</strong> Per vendite private spesso basta una breve spiegazione, ad esempio: «Si tratta della vendita di abiti usati della mia famiglia, per lo più a un prezzo inferiore a quello d'acquisto».</li>
</ol>
<h2>Quando entrano in gioco le tasse?</h2>
<p>Nella maggior parte dei paesi UE, vendere le proprie cose usate a meno di quanto le hai pagate non genera un guadagno tassabile. Le regole cambiano per gli oggetti rivenduti poco dopo l'acquisto e per chi compra per rivendere con un guadagno, che può essere considerato un'attività commerciale. In questi casi chiedi a un commercialista.</p>
<h2>Per il prossimo anno</h2>
<p>Tieni un semplice elenco di ciò che compri e vendi, con i prezzi. Così ogni domanda del Fisco si risolve in pochi minuti.</p>
""",
   "sources": [eurlex("IT", "Direttiva (UE) 2021/514 del Consiglio (DAC7), EUR-Lex")]},
  "es": {"slug": "carta-de-hacienda-tras-comunicacion-dac7",
   "title": "Una carta de Hacienda tras la comunicación DAC7: ¿qué hago?",
   "desc": "¿Has recibido una carta de Hacienda después de vender en Vinted, Wallapop o eBay? Así puedes responder con calma y correctamente.",
   "answer": "Mantén la calma, pero no la ignores. Normalmente Hacienda solo quiere saber si las ventas comunicadas incluyen ingresos que tributan. Si vendiste tus propias cosas usadas, suele bastar con explicarlo en pocas líneas.",
   "body": """
<h2>¿Por qué te escribe Hacienda?</h2>
<p>Cada año, antes del 31 de enero, las plataformas informan de quienes llegaron a 30 ventas o ingresaron más de 2.000 € en ellas el año anterior. Hacienda compara estos datos con tu declaración. Si algo no cuadra, puede preguntar. Una pregunta no es una multa ni una liquidación.</p>
<h2>Paso a paso</h2>
<ol>
<li><strong>Apunta el plazo.</strong> La carta indica hasta cuándo debes responder.</li>
<li><strong>Reúne tus ventas.</strong> Descarga en la app el resumen del año: qué vendiste, cuándo y por cuánto.</li>
<li><strong>Clasifícalas.</strong> ¿Eran tus propias cosas usadas o artículos comprados para revenderlos?</li>
<li><strong>Responde de forma breve y sincera.</strong> Para ventas particulares suele bastar una explicación corta, por ejemplo: «Se trata de la venta de ropa usada de mi hogar, en su mayoría por debajo del precio de compra».</li>
</ol>
<h2>¿Cuándo hay que tributar?</h2>
<p>En la mayoría de los países de la UE, vender tus cosas usadas por menos de lo que pagaste no genera una ganancia que tribute. Las reglas cambian para artículos revendidos poco después de comprarlos y para quien compra para revender con beneficio, lo que puede considerarse una actividad económica. En esos casos, consulta a un asesor fiscal.</p>
<h2>Para el año que viene</h2>
<p>Lleva una lista sencilla de lo que compras y vendes, con sus precios. Así cualquier pregunta de Hacienda se resuelve en minutos.</p>
""",
   "sources": [eurlex("ES", "Directiva (UE) 2021/514 del Consejo (DAC7), EUR-Lex")]},
  "nl": {"slug": "brief-van-de-belastingdienst-na-dac7-melding",
   "title": "Een brief van de Belastingdienst na een DAC7-melding: wat nu?",
   "desc": "Een brief van de Belastingdienst gekregen na verkopen op Vinted, Marktplaats of eBay? Zo reageer je rustig en correct.",
   "answer": "Blijf rustig, maar negeer hem niet. Meestal wil de Belastingdienst alleen weten of de gemelde verkopen belastbaar inkomen bevatten. Heb je je eigen gebruikte spullen verkocht, dan kun je dat meestal in een paar zinnen uitleggen.",
   "body": """
<h2>Waarom schrijft de Belastingdienst je?</h2>
<p>Elk jaar vóór 31 januari melden platforms iedereen die het jaar ervoor 30 verkopen haalde of meer dan € 2.000 bij hen ontving. De Belastingdienst vergelijkt die gegevens met je aangifte. Klopt er iets niet, dan kan hij vragen stellen. Een vraag is geen boete en geen aanslag.</p>
<h2>Stap voor stap</h2>
<ol>
<li><strong>Noteer de termijn.</strong> In de brief staat wanneer je moet reageren.</li>
<li><strong>Verzamel je verkopen.</strong> Download in de app het jaaroverzicht: wat je verkocht, wanneer en voor hoeveel.</li>
<li><strong>Deel ze in.</strong> Waren het je eigen gebruikte spullen of artikelen die je kocht om door te verkopen?</li>
<li><strong>Antwoord kort en eerlijk.</strong> Bij particuliere verkopen volstaat vaak een korte uitleg, bijvoorbeeld: "Het gaat om de verkoop van gebruikte kleding uit mijn huishouden, meestal onder de oorspronkelijke aankoopprijs."</li>
</ol>
<h2>Wanneer speelt belasting een rol?</h2>
<p>In de meeste EU-landen levert het verkopen van je eigen gebruikte spullen voor minder dan je ervoor betaalde geen belastbare winst op. Andere regels gelden voor spullen die je kort na aankoop doorverkoopt en voor wie inkoopt om met winst door te verkopen; dat kan als onderneming gelden. Vraag dan een belastingadviseur.</p>
<h2>Voor volgend jaar</h2>
<p>Houd een eenvoudige lijst bij van wat je koopt en verkoopt, met de prijzen. Dan is elke vraag van de Belastingdienst in een paar minuten beantwoord.</p>
""",
   "sources": [eurlex("NL", "Richtlijn (EU) 2021/514 van de Raad (DAC7), EUR-Lex")]},
  "pl": {"slug": "pismo-z-urzedu-skarbowego-po-zgloszeniu-dac7",
   "title": "Pismo z urzędu skarbowego po zgłoszeniu DAC7: co teraz?",
   "desc": "Dostałeś pismo z urzędu skarbowego po sprzedaży na Vinted, Allegro lub OLX? Tak odpowiesz spokojnie i poprawnie.",
   "answer": "Zachowaj spokój, ale nie ignoruj pisma. Urząd zwykle chce tylko wiedzieć, czy zgłoszona sprzedaż obejmuje dochód podlegający opodatkowaniu. Jeśli sprzedawałeś własne używane rzeczy, zwykle wystarczy krótko to wyjaśnić.",
   "body": """
<h2>Dlaczego urząd do Ciebie pisze?</h2>
<p>Co roku do 31 stycznia platformy zgłaszają osoby, które w poprzednim roku osiągnęły u nich 30 transakcji lub ponad 2000 €. Urząd porównuje te dane z Twoim zeznaniem. Jeśli coś się nie zgadza, może zadać pytania. Pytanie to ani kara, ani decyzja podatkowa.</p>
<h2>Krok po kroku</h2>
<ol>
<li><strong>Zapisz termin.</strong> W piśmie jest data, do której trzeba odpowiedzieć.</li>
<li><strong>Zbierz swoje transakcje.</strong> Pobierz w aplikacji podsumowanie roku: co sprzedałeś, kiedy i za ile.</li>
<li><strong>Uporządkuj je.</strong> Czy były to Twoje własne używane rzeczy, czy przedmioty kupione z myślą o odsprzedaży?</li>
<li><strong>Odpowiedz krótko i szczerze.</strong> Przy sprzedaży prywatnej często wystarczy krótkie wyjaśnienie, np.: „Chodzi o sprzedaż używanych ubrań z mojego gospodarstwa domowego, w większości poniżej ceny zakupu."</li>
</ol>
<h2>Kiedy pojawia się podatek?</h2>
<p>W większości krajów UE sprzedaż własnych używanych rzeczy taniej, niż je kupiłeś, nie daje dochodu do opodatkowania. Inne zasady dotyczą rzeczy odsprzedanych wkrótce po zakupie oraz osób, które kupują, by odsprzedać z zyskiem, co może być uznane za działalność gospodarczą. Wtedy warto zapytać doradcę podatkowego.</p>
<h2>Na przyszły rok</h2>
<p>Prowadź prostą listę tego, co kupujesz i sprzedajesz, wraz z cenami. Wtedy każde pytanie z urzędu załatwisz w kilka minut.</p>
""",
   "sources": [eurlex("PL", "Dyrektywa Rady (UE) 2021/514 (DAC7), EUR-Lex")]},
 },
 # ---------------------------------------------------------------- platforms
 "platforms": {
  "fr": {"slug": "dac7-vinted-leboncoin-ebay-ce-qui-est-declare",
   "title": "DAC7 sur Vinted, Leboncoin et eBay : qu'est-ce qui est déclaré ?",
   "desc": "Quelles ventes Vinted, Leboncoin, eBay et Etsy déclarent aux impôts, comment elles sont comptées et pourquoi les annonces seules ne comptent pas.",
   "answer": "Seules les ventes conclues et payées via la plateforme sont déclarées. Sur les sites de petites annonces, les ventes en espèces à la remise ne comptent pas, car la plateforme ne les voit pas. Chaque plateforme compte séparément.",
   "body": """
<h2>Qu'est-ce qui compte comme une vente ?</h2>
<p>DAC7 compte les transactions : des ventes réellement conclues et payées. Le nombre d'annonces en ligne ne joue aucun rôle. Une plateforme ne peut déclarer que ce qu'elle traite elle-même.</p>
<h2>Les plateformes en bref</h2>
<ul>
<li><strong>Vinted :</strong> presque toutes les ventes passent par le paiement Vinted et comptent donc toutes.</li>
<li><strong>eBay et Etsy :</strong> ils gèrent eux-mêmes les paiements, chaque article vendu compte.</li>
<li><strong>Sites de petites annonces</strong> comme Leboncoin : seules les ventes conclues via leur propre service de paiement ou de livraison sont comptées. Le paiement en espèces à la remise leur est invisible.</li>
</ul>
<h2>Chaque plateforme compte séparément</h2>
<p>Les limites de 30 ventes ou plus de 2 000 € s'appliquent par plateforme. 25 ventes sur Vinted et 25 sur Leboncoin ne déclenchent aucune déclaration. Pour vos impôts, en revanche, c'est l'ensemble de vos revenus qui compte.</p>
<h2>Qu'est-ce qui est déclaré avec les montants ?</h2>
<p>Les montants reçus pour vos ventes, moins les frais retenus par la plateforme, ainsi que vos nom, adresse, date de naissance et numéro fiscal.</p>
""",
   "sources": [eurlex("FR", "Directive (UE) 2021/514 du Conseil (DAC7), EUR-Lex"), S_MOBI]},
  "it": {"slug": "dac7-vinted-subito-ebay-cosa-viene-segnalato",
   "title": "DAC7 su Vinted, Subito ed eBay: cosa viene segnalato?",
   "desc": "Quali vendite Vinted, Subito, eBay ed Etsy segnalano al Fisco, come vengono contate e perché gli annunci da soli non contano.",
   "answer": "Vengono segnalate solo le vendite concluse e pagate tramite la piattaforma. Sui siti di annunci, le vendite in contanti alla consegna non contano, perché la piattaforma non le vede. Ogni piattaforma conta separatamente.",
   "body": """
<h2>Cosa conta come vendita?</h2>
<p>La DAC7 conta le transazioni: vendite effettivamente concluse e pagate. Il numero di annunci online non conta. Una piattaforma può segnalare solo ciò che gestisce direttamente.</p>
<h2>Le piattaforme in breve</h2>
<ul>
<li><strong>Vinted:</strong> quasi tutte le vendite passano dal sistema di pagamento di Vinted e quindi contano.</li>
<li><strong>eBay ed Etsy:</strong> gestiscono loro i pagamenti, ogni articolo venduto conta.</li>
<li><strong>Siti di annunci</strong> come Subito: contano solo le vendite concluse tramite il loro servizio di pagamento o spedizione. Il contante alla consegna non lo vedono.</li>
</ul>
<h2>Ogni piattaforma conta a parte</h2>
<p>I limiti di 30 vendite o più di 2.000 € valgono per piattaforma. 25 vendite su Vinted e 25 su Subito non fanno scattare la segnalazione. Per le tasse, invece, conta tutto il tuo reddito.</p>
<h2>Cosa viene segnalato insieme agli importi?</h2>
<p>Gli importi ricevuti per le vendite, meno le commissioni trattenute dalla piattaforma, oltre a nome, indirizzo, data di nascita e codice fiscale.</p>
""",
   "sources": [eurlex("IT", "Direttiva (UE) 2021/514 del Consiglio (DAC7), EUR-Lex"), S_MOBI]},
  "es": {"slug": "dac7-vinted-wallapop-ebay-que-se-comunica",
   "title": "DAC7 en Vinted, Wallapop y eBay: ¿qué se comunica?",
   "desc": "Qué ventas comunican Vinted, Wallapop, eBay y Etsy a Hacienda, cómo se cuentan y por qué los anuncios por sí solos no cuentan.",
   "answer": "Solo se comunican las ventas cerradas y pagadas a través de la plataforma. Las ventas en efectivo en mano no cuentan, porque la plataforma no las ve. Cada plataforma cuenta por separado.",
   "body": """
<h2>¿Qué cuenta como venta?</h2>
<p>La DAC7 cuenta transacciones: ventas realmente cerradas y pagadas. Cuántos anuncios tengas publicados no importa. Una plataforma solo puede comunicar lo que gestiona ella misma.</p>
<h2>Las plataformas de un vistazo</h2>
<ul>
<li><strong>Vinted:</strong> casi todas las ventas pasan por el pago de Vinted, así que cuentan.</li>
<li><strong>eBay y Etsy:</strong> gestionan ellos los pagos, cada artículo vendido cuenta.</li>
<li><strong>Webs de anuncios</strong> como Wallapop: solo cuentan las ventas cerradas con su propio sistema de pago o envío. El efectivo en mano no lo ven.</li>
</ul>
<h2>Cada plataforma cuenta por separado</h2>
<p>Los límites de 30 ventas o más de 2.000 € se aplican por plataforma. 25 ventas en Vinted y 25 en Wallapop no generan comunicación. Para tus impuestos, en cambio, cuentan todos tus ingresos.</p>
<h2>¿Qué se comunica junto con los importes?</h2>
<p>Lo que recibiste por tus ventas, menos las comisiones que retuvo la plataforma, junto con tu nombre, dirección, fecha de nacimiento y NIF.</p>
""",
   "sources": [eurlex("ES", "Directiva (UE) 2021/514 del Consejo (DAC7), EUR-Lex"), S_MOBI]},
  "nl": {"slug": "dac7-vinted-marktplaats-ebay-wat-wordt-gemeld",
   "title": "DAC7 bij Vinted, Marktplaats en eBay: wat wordt er gemeld?",
   "desc": "Welke verkopen Vinted, Marktplaats, eBay en Etsy aan de Belastingdienst melden, hoe ze worden geteld en waarom advertenties alleen niet meetellen.",
   "answer": "Alleen afgeronde verkopen die via het platform zijn betaald, worden gemeld. Contante verkopen bij ophalen tellen niet mee, want het platform ziet ze niet. Elk platform telt apart.",
   "body": """
<h2>Wat telt als verkoop?</h2>
<p>DAC7 telt transacties: verkopen die echt zijn afgerond en betaald. Hoeveel advertenties je online hebt, maakt niet uit. Een platform kan alleen melden wat het zelf afhandelt.</p>
<h2>De platforms in het kort</h2>
<ul>
<li><strong>Vinted:</strong> bijna alle verkopen lopen via de betaalfunctie van Vinted en tellen dus mee.</li>
<li><strong>eBay en Etsy:</strong> regelen de betaling zelf, elk verkocht artikel telt.</li>
<li><strong>Advertentiesites</strong> zoals Marktplaats en 2dehands: alleen verkopen via hun eigen betaal- of verzendservice tellen. Contant bij ophalen zien ze niet.</li>
</ul>
<h2>Elk platform telt apart</h2>
<p>De grenzen van 30 verkopen of meer dan € 2.000 gelden per platform. 25 verkopen op Vinted en 25 op Marktplaats leiden niet tot een melding. Voor je belasting telt wel je totale inkomen.</p>
<h2>Wat wordt er samen met de bedragen gemeld?</h2>
<p>De bedragen die je voor je verkopen ontving, min de kosten die het platform inhield, plus je naam, adres, geboortedatum en fiscaal nummer.</p>
""",
   "sources": [eurlex("NL", "Richtlijn (EU) 2021/514 van de Raad (DAC7), EUR-Lex"), S_MOBI]},
  "pl": {"slug": "dac7-vinted-allegro-olx-co-jest-zglaszane",
   "title": "DAC7 na Vinted, Allegro i OLX: co jest zgłaszane?",
   "desc": "Jakie transakcje Vinted, Allegro, OLX i eBay zgłaszają do urzędu skarbowego, jak są liczone i dlaczego same ogłoszenia się nie liczą.",
   "answer": "Zgłaszane są tylko zakończone transakcje opłacone przez platformę. Sprzedaż za gotówkę przy odbiorze się nie liczy, bo platforma jej nie widzi. Każda platforma liczy osobno.",
   "body": """
<h2>Co liczy się jako transakcja?</h2>
<p>DAC7 liczy transakcje: sprzedaż faktycznie zakończoną i opłaconą. Liczba ogłoszeń w sieci nie ma znaczenia. Platforma może zgłosić tylko to, co sama obsługuje.</p>
<h2>Platformy w skrócie</h2>
<ul>
<li><strong>Vinted:</strong> prawie cała sprzedaż przechodzi przez płatności Vinted, więc się liczy.</li>
<li><strong>Allegro i eBay:</strong> obsługują płatności same, liczy się każdy sprzedany przedmiot.</li>
<li><strong>Serwisy ogłoszeniowe</strong> jak OLX: liczą się tylko transakcje zawarte przez ich własną usługę płatności lub wysyłki. Gotówki przy odbiorze nie widzą.</li>
</ul>
<h2>Każda platforma liczy osobno</h2>
<p>Limity 30 transakcji lub ponad 2000 € obowiązują na każdą platformę. 25 transakcji na Vinted i 25 na OLX nie powoduje zgłoszenia. W podatkach liczy się jednak cały Twój dochód.</p>
<h2>Co jest zgłaszane razem z kwotami?</h2>
<p>Kwoty otrzymane za sprzedaż po odjęciu prowizji platformy oraz imię i nazwisko, adres, data urodzenia i numer podatkowy.</p>
""",
   "sources": [eurlex("PL", "Dyrektywa Rady (UE) 2021/514 (DAC7), EUR-Lex"), S_MOBI]},
 },
 # ---------------------------------------------------------------- business
 "business": {
  "fr": {"slug": "vendeur-particulier-ou-professionnel",
   "title": "Vendeur particulier ou professionnel : où est la limite ?",
   "desc": "Quand vendre sur Vinted, Leboncoin ou eBay devient-il une activité professionnelle ? Les principaux critères expliqués simplement.",
   "answer": "Il n'y a pas de nombre fixe de ventes. Ce qui compte, c'est si vous videz vos placards ou si vous achetez pour revendre avec un bénéfice. Dans le second cas, même la première vente peut relever d'une activité professionnelle.",
   "body": """
<h2>Particulier : vider ses placards</h2>
<p>Vendre des vêtements, meubles, livres ou jouets de votre foyer est une vente entre particuliers, même avec beaucoup de ventes. Les objets d'occasion se vendent en général moins cher qu'ils n'ont coûté : il n'y a donc pas de bénéfice à imposer.</p>
<h2>Professionnel : acheter pour revendre</h2>
<p>L'administration et les tribunaux regardent l'ensemble. Signes typiques d'une activité professionnelle :</p>
<ul>
<li>Vous achetez régulièrement des articles pour les revendre, par exemple en brocante, en outlet ou en déstockage.</li>
<li>Vous proposez beaucoup d'articles identiques ou neufs.</li>
<li>Votre compte ressemble à une boutique : offre permanente, photos uniformes, routines fixes.</li>
</ul>
<p>L'intention est déterminante. Si vous achetez dans le but de revendre avec un bénéfice, l'activité peut être professionnelle dès la première vente.</p>
<h2>Ce qui s'applique alors</h2>
<p>Les vendeurs professionnels doivent en général s'enregistrer, déclarer leurs bénéfices et s'occuper de la TVA. La plupart des pays de l'UE ont un régime simplifié pour les petites activités. Renseignez-vous auprès d'un conseiller avant que l'administration ne pose la question.</p>
<h2>Gardez vos chiffres</h2>
<p>Si vous revendez, sachez ce qui vous reste à la fin. Notez le prix d'achat, le prix de vente et les frais de chaque article. C'est exactement le rôle du Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [eurlex("FR", "Directive (UE) 2021/514 du Conseil (DAC7), EUR-Lex"), S_CORRECTIV]},
  "it": {"slug": "venditore-privato-o-attivita",
   "title": "Venditore privato o attività commerciale: dov'è il limite?",
   "desc": "Quando vendere su Vinted, Subito o eBay diventa un'attività commerciale? I criteri principali spiegati in modo semplice.",
   "answer": "Non esiste un numero fisso di vendite. Conta se ti stai liberando delle tue cose o se compri per rivendere con un guadagno. Nel secondo caso anche la prima vendita può essere attività commerciale.",
   "body": """
<h2>Privato: fare spazio</h2>
<p>Vendere vestiti, mobili, libri o giocattoli di casa tua è una vendita tra privati, anche se le vendite sono tante. Le cose usate di solito si vendono a meno di quanto sono costate, quindi non c'è un guadagno da tassare.</p>
<h2>Attività: comprare per rivendere</h2>
<p>Fisco e tribunali guardano il quadro complessivo. Segnali tipici di un'attività:</p>
<ul>
<li>Compri regolarmente merce per rivenderla, per esempio ai mercatini, negli outlet o negli stock.</li>
<li>Offri molti articoli uguali o nuovi.</li>
<li>Il tuo profilo sembra un negozio: offerta permanente, foto uniformi, procedure fisse.</li>
</ul>
<p>Conta l'intenzione. Se compri con l'idea di rivendere con un guadagno, l'attività può essere commerciale fin dalla prima vendita.</p>
<h2>Cosa vale in quel caso</h2>
<p>Chi vende come attività di solito deve aprire una posizione fiscale, dichiarare i guadagni e occuparsi dell'IVA. Molti paesi UE prevedono regimi semplificati per le piccole attività. Chiedi a un commercialista prima che lo chieda il Fisco.</p>
<h2>Tieni i conti</h2>
<p>Se rivendi, devi sapere cosa ti resta alla fine. Annota prezzo d'acquisto, prezzo di vendita e commissioni di ogni articolo. È proprio a questo che serve il Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [eurlex("IT", "Direttiva (UE) 2021/514 del Consiglio (DAC7), EUR-Lex"), S_CORRECTIV]},
  "es": {"slug": "vendedor-particular-o-actividad",
   "title": "¿Vendedor particular o actividad económica? Dónde está el límite",
   "desc": "¿Cuándo vender en Vinted, Wallapop o eBay pasa a ser una actividad económica? Los criterios principales explicados de forma sencilla.",
   "answer": "No hay un número fijo de ventas. Lo que importa es si te estás deshaciendo de tus cosas o si compras para revender con beneficio. En el segundo caso, incluso la primera venta puede ser actividad económica.",
   "body": """
<h2>Particular: hacer limpieza</h2>
<p>Vender ropa, muebles, libros o juguetes de tu casa es una venta entre particulares, aunque sean muchas ventas. Las cosas usadas suelen venderse por menos de lo que costaron, así que no hay ganancia que tribute.</p>
<h2>Actividad: comprar para revender</h2>
<p>Hacienda y los tribunales miran el conjunto. Señales típicas de una actividad económica:</p>
<ul>
<li>Compras con regularidad para revender, por ejemplo en rastros, outlets o liquidaciones.</li>
<li>Ofreces muchos artículos iguales o nuevos.</li>
<li>Tu perfil parece una tienda: oferta permanente, fotos uniformes, rutinas fijas.</li>
</ul>
<p>Lo decisivo es la intención. Si compras con la idea de revender con beneficio, puede haber actividad económica desde la primera venta.</p>
<h2>Qué se aplica entonces</h2>
<p>Quien vende como actividad suele tener que darse de alta, declarar sus beneficios y ocuparse del IVA. Muchos países de la UE tienen regímenes simplificados para pequeños negocios. Consulta a un asesor antes de que pregunte Hacienda.</p>
<h2>Lleva las cuentas</h2>
<p>Si revendes, debes saber cuánto te queda al final. Apunta el precio de compra, el de venta y las comisiones de cada artículo. Para eso está el Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [eurlex("ES", "Directiva (UE) 2021/514 del Consejo (DAC7), EUR-Lex"), S_CORRECTIV]},
  "nl": {"slug": "particulier-of-ondernemer",
   "title": "Particulier of ondernemer: waar ligt de grens?",
   "desc": "Wanneer wordt verkopen op Vinted, Marktplaats of eBay een onderneming? De belangrijkste criteria eenvoudig uitgelegd.",
   "answer": "Er is geen vast aantal verkopen. Het gaat erom of je je eigen spullen opruimt of inkoopt om met winst door te verkopen. In het tweede geval kan zelfs je eerste verkoop als onderneming gelden.",
   "body": """
<h2>Particulier: opruimen</h2>
<p>Kleding, meubels, boeken of speelgoed uit je eigen huishouden verkopen is particuliere verkoop, ook als het om veel verkopen gaat. Gebruikte spullen gaan meestal weg voor minder dan ze kostten, dus er is geen winst om te belasten.</p>
<h2>Ondernemer: inkopen om door te verkopen</h2>
<p>De Belastingdienst en rechters kijken naar het totaalbeeld. Typische kenmerken van een onderneming:</p>
<ul>
<li>Je koopt regelmatig spullen in om ze door te verkopen, bijvoorbeeld op rommelmarkten, in outlets of als restpartij.</li>
<li>Je biedt veel dezelfde of nieuwe artikelen aan.</li>
<li>Je account lijkt op een winkel: vast aanbod, uniforme foto's, vaste routines.</li>
</ul>
<p>De bedoeling is doorslaggevend. Wie inkoopt om met winst door te verkopen, kan vanaf de eerste verkoop ondernemer zijn.</p>
<h2>Wat dan geldt</h2>
<p>Ondernemers moeten zich meestal inschrijven, belasting over hun winst betalen en btw regelen. De meeste EU-landen hebben vereenvoudigde regels voor kleine ondernemers. Vraag een adviseur voordat de Belastingdienst het vraagt.</p>
<h2>Houd je cijfers bij</h2>
<p>Verkoop je door, dan wil je weten wat er overblijft. Noteer per artikel de inkoopprijs, verkoopprijs en kosten. Precies daarvoor is de Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [eurlex("NL", "Richtlijn (EU) 2021/514 van de Raad (DAC7), EUR-Lex"), S_CORRECTIV]},
  "pl": {"slug": "sprzedaz-prywatna-czy-dzialalnosc",
   "title": "Sprzedaż prywatna czy działalność gospodarcza: gdzie jest granica?",
   "desc": "Kiedy sprzedaż na Vinted, Allegro lub OLX staje się działalnością gospodarczą? Najważniejsze kryteria wyjaśnione po prostu.",
   "answer": "Nie ma stałej liczby transakcji. Liczy się to, czy pozbywasz się własnych rzeczy, czy kupujesz, by odsprzedać z zyskiem. W drugim przypadku nawet pierwsza sprzedaż może być działalnością.",
   "body": """
<h2>Prywatnie: porządki w szafie</h2>
<p>Sprzedaż ubrań, mebli, książek czy zabawek z własnego domu to sprzedaż prywatna, nawet jeśli transakcji jest dużo. Używane rzeczy zwykle sprzedają się taniej, niż kosztowały, więc nie ma zysku do opodatkowania.</p>
<h2>Działalność: kupowanie, by odsprzedać</h2>
<p>Urząd i sądy patrzą na całość. Typowe oznaki działalności:</p>
<ul>
<li>Regularnie kupujesz towar, by go odsprzedać, np. na pchlich targach, w outletach lub z wyprzedaży.</li>
<li>Oferujesz wiele takich samych lub nowych przedmiotów.</li>
<li>Twoje konto wygląda jak sklep: stała oferta, jednolite zdjęcia, ustalone procedury.</li>
</ul>
<p>Decyduje zamiar. Jeśli kupujesz z myślą o odsprzedaży z zyskiem, działalność może zacząć się od pierwszej sprzedaży.</p>
<h2>Co wtedy obowiązuje</h2>
<p>Sprzedawcy prowadzący działalność zwykle muszą ją zarejestrować, rozliczać dochód i zająć się VAT. Większość krajów UE ma uproszczone zasady dla małych firm. Zapytaj doradcę, zanim zapyta urząd.</p>
<h2>Prowadź liczby</h2>
<p>Jeśli odsprzedajesz, musisz wiedzieć, ile zostaje na koniec. Zapisuj cenę zakupu, cenę sprzedaży i prowizje dla każdego przedmiotu. Do tego właśnie służy Reseller Profit &amp; DAC7 Tracker.</p>
""",
   "sources": [eurlex("PL", "Dyrektywa Rady (UE) 2021/514 (DAC7), EUR-Lex"), S_CORRECTIV]},
 },
}
