# Articles: bg, cs, da, el, et
from articles_more import eurlex, S_EBAY, S_MOBI, S_CORRECTIV
OV = "../../../en/guides/eu-tax-on-selling-used-items/"

G = {
 "bg": {"dir": "statii", "title": "Статии", "intro": "Отговори на най-честите въпроси за DAC7, Vinted, OLX и данъците.",
        "updated": "Актуализация: 26 ноември 2026", "read": "Прочети", "back": "Обратно към DAC7 проверката",
        "cta_title": "Колко си близо до лимита?", "cta_text": "Провери всяка платформа за минута с безплатната DAC7 проверка.", "cta_btn": "Към DAC7 проверката",
        "track": "Или следи цяла година печалбата и DAC7 статуса си с", "track_link": "Reseller Profit &amp; DAC7 Tracker (на английски)",
        "sources": "Източници", "disclaimer": "Тази статия е обща информация, а не данъчен или правен съвет."},
 "cs": {"dir": "clanky", "title": "Články", "intro": "Odpovědi na nejčastější otázky o DAC7, Vintedu a finančním úřadu.",
        "updated": "Aktualizováno: 26. listopadu 2026", "read": "Číst dál", "back": "Zpět na kontrolu DAC7",
        "cta_title": "Jak blízko jsi limitu?", "cta_text": "Zkontroluj každou platformu za minutu v bezplatné kontrole DAC7.", "cta_btn": "Otevřít kontrolu DAC7",
        "track": "Nebo sleduj celý rok zisk a stav DAC7 v", "track_link": "Reseller Profit &amp; DAC7 Tracker (v angličtině)",
        "sources": "Zdroje", "disclaimer": "Tento článek je obecná informace, nikoli daňové ani právní poradenství."},
 "da": {"dir": "guides", "title": "Guides", "intro": "Svar på de mest stillede spørgsmål om DAC7, Vinted og Skattestyrelsen.",
        "updated": "Opdateret: 26. november 2026", "read": "Læs mere", "back": "Tilbage til DAC7-tjekket",
        "cta_title": "Hvor tæt er du på grænsen?", "cta_text": "Tjek hver platform på et minut med det gratis DAC7-tjek.", "cta_btn": "Åbn DAC7-tjekket",
        "track": "Eller hold styr på fortjeneste og DAC7-status hele året med", "track_link": "Reseller Profit &amp; DAC7 Tracker (på engelsk)",
        "sources": "Kilder", "disclaimer": "Denne artikel er generel information og ikke skattemæssig eller juridisk rådgivning."},
 "el": {"dir": "odigoi", "title": "Οδηγοί", "intro": "Απαντήσεις στις πιο συχνές ερωτήσεις για το DAC7, το Vinted και την εφορία.",
        "updated": "Ενημέρωση: 26 Νοεμβρίου 2026", "read": "Διάβασε", "back": "Πίσω στον έλεγχο DAC7",
        "cta_title": "Πόσο κοντά είσαι στο όριο;", "cta_text": "Έλεγξε κάθε πλατφόρμα σε ένα λεπτό με τον δωρεάν έλεγχο DAC7.", "cta_btn": "Άνοιξε τον έλεγχο DAC7",
        "track": "Ή παρακολούθησε όλη τη χρονιά το κέρδος και την κατάσταση DAC7 με το", "track_link": "Reseller Profit &amp; DAC7 Tracker (στα αγγλικά)",
        "sources": "Πηγές", "disclaimer": "Το άρθρο αυτό είναι γενική πληροφόρηση και όχι φορολογική ή νομική συμβουλή."},
 "et": {"dir": "juhendid", "title": "Juhendid", "intro": "Vastused levinumatele küsimustele DAC7, Vintedi ja maksuameti kohta.",
        "updated": "Uuendatud: 26. november 2026", "read": "Loe edasi", "back": "Tagasi DAC7 kontrolli juurde",
        "cta_title": "Kui lähedal oled piirile?", "cta_text": "Kontrolli iga platvormi minutiga tasuta DAC7 kontrolliga.", "cta_btn": "Ava DAC7 kontroll",
        "track": "Või jälgi kogu aasta kasumit ja DAC7 olekut tööriistaga", "track_link": "Reseller Profit &amp; DAC7 Tracker (inglise keeles)",
        "sources": "Allikad", "disclaimer": "See artikkel on üldine teave, mitte maksu- ega õigusnõustamine."},
}

def A(slug, title, desc, answer, body, sources):
    return {"slug": slug, "title": title, "desc": desc, "answer": answer, "body": body, "sources": sources}

M = {"tax-id": {}, "letter": {}, "platforms": {}, "business": {}}

# ---------------- Bulgarian
EU_BG = eurlex("BG", "Директива (ЕС) 2021/514 на Съвета (DAC7), EUR-Lex")
BG_SRC = ("Innovires: Онлайн продажби от физически лица (2026)", "https://www.innovires.com/en/blog/onlayn-prodazhbi-fl-danak-gdd-dac7.html")
M["tax-id"]["bg"] = A("vinted-egn-danachen-nomer", "Vinted иска данъчния ти номер: трябва ли да го дадеш?",
 "Защо Vinted, OLX и eBay искат ЕГН или данъчен номер, кои данни отиват в НАП и какво става, ако не ги дадеш.",
 "Да. Когато платформа поиска данъчния ти номер по правилата на DAC7, трябва да го дадеш, иначе тя може да задържи плащанията или да ограничи профила ти. Това не означава, че дължиш данък.",
 """<h2>Защо платформата пита?</h2>
<p>От 2023 г. онлайн платформите в ЕС събират данни за продавачите и веднъж годишно ги подават на данъчните органи. Основата е директивата на ЕС DAC7. Докладват те, ако в една платформа за календарна година достигнеш 30 продажби или получиш над 2000 €.</p>
<h2>Кои данни се подават?</h2>
<ul><li>Име, адрес и дата на раждане</li><li>Данъчният ти номер (в България – ЕГН)</li><li>Броят продажби и получените суми след таксите на платформата</li></ul>
<h2>Какво става, ако не го дадеш?</h2>
<p>Платформата трябва да ти напомни. Ако не отговориш, може да задържи плащанията или да ограничи правата ти на продавач. Отказът не спира докладването, само блокира профила.</p>
<h2>Безопасно</h2>
<ul><li>Въвеждай номера само в приложението или сайта на платформата, никога през линк от имейл или SMS.</li><li>Провери с DAC7 проверката дали изобщо ще достигнеш лимита.</li></ul>
<p>Докладването не е данъчно задължение. Виж <a href="../chastno-ili-targoviya/">Частна продажба или търговия?</a></p>""", [EU_BG, S_EBAY])
M["letter"]["bg"] = A("pismo-ot-nap-sled-dac7", "Писмо от НАП след DAC7 доклад: какво да направиш?",
 "Получи писмо от НАП след продажби в OLX, Vinted или eBay? Така отговаряш спокойно и правилно.",
 "Запази спокойствие, но не го пренебрегвай. Обикновено НАП иска да знае дали докладваните продажби съдържат облагаем доход. Продажбата на собствени лични вещи в България не се облага.",
 """<h2>Защо ти пишат?</h2>
<p>Всяка година до 31 януари платформите докладват кой е достигнал 30 продажби или над 2000 € при тях. НАП сравнява данните с декларацията ти и може да зададе въпроси. Въпросът не е глоба.</p>
<h2>Стъпка по стъпка</h2>
<ol><li><strong>Запиши срока</strong> в писмото.</li><li><strong>Събери продажбите</strong> от приложението: какво, кога, за колко.</li><li><strong>Раздели ги:</strong> собствени употребявани вещи или стоки, купени за препродажба?</li><li><strong>Отговори кратко и честно</strong>, например: „Става дума за продажба на употребявани дрехи от домакинството ми.“</li></ol>
<h2>Правилата в България</h2>
<p>Доходът от продажба на лични движими вещи е необлагаем (чл. 13, ал. 1, т. 2 ЗДДФЛ). Изключения: моторни превозни средства, продадени до една година след покупката, произведения на изкуството и колекции, както и търговия – покупка с цел препродажба по организиран начин.</p>
<p>Правилата за всички 27 държави от ЕС: <a href=\"""" + OV + """\">преглед (на английски)</a>.</p>
<h2>За следващата година</h2>
<p>Води прост списък какво купуваш и продаваш и на каква цена.</p>""", [BG_SRC, EU_BG])
M["platforms"]["bg"] = A("dac7-olx-vinted-ebay-kakvo-se-dokladva", "DAC7 в OLX, Vinted и eBay: какво се докладва?",
 "Кои продажби OLX, Vinted и eBay докладват на НАП, как се броят и защо обявите сами не се броят.",
 "Докладват се само завършени продажби, платени през платформата. Плащане в брой на ръка не се брои, защото платформата не го вижда. Всяка платформа брои отделно.",
 """<h2>Какво е продажба?</h2>
<p>DAC7 брои сделки: реално завършени и платени продажби. Броят обяви няма значение.</p>
<h2>Платформите накратко</h2>
<ul><li><strong>Vinted:</strong> почти всички продажби минават през плащането на Vinted и се броят.</li><li><strong>eBay и Etsy:</strong> обработват плащанията сами.</li><li><strong>OLX и други сайтове за обяви:</strong> броят се само продажби през тяхната услуга за плащане или доставка.</li></ul>
<h2>Всяка платформа отделно</h2>
<p>Лимитите от 30 продажби или над 2000 € важат за всяка платформа. За данъците обаче се брои целият ти доход.</p>
<h2>Какво се докладва?</h2>
<p>Сумите след таксите на платформата, името, адресът, датата на раждане и данъчният номер.</p>""", [EU_BG, S_MOBI])
M["business"]["bg"] = A("chastno-ili-targoviya", "Частна продажба или търговия: къде е границата?",
 "Кога продажбите в OLX или Vinted стават търговия? Основните критерии, обяснени просто.",
 "Няма фиксиран брой продажби. Важно е дали разчистваш собствени вещи или купуваш, за да препродаваш с печалба. Във втория случай дори първата продажба може да е търговия.",
 """<h2>Частно: разчистване</h2>
<p>Продажбата на дрехи, мебели или играчки от собственото домакинство е частна, дори да са много. В България този доход е необлагаем.</p>
<h2>Търговия: купуваш, за да препродадеш</h2>
<ul><li>Редовно купуваш стоки за препродажба.</li><li>Предлагаш много еднакви или нови артикули.</li><li>Профилът ти изглежда като магазин.</li></ul>
<p>Решаващо е намерението. Лице е търговец по характера на дейността, а не по регистрация; доходът от търговия се облага.</p>
<h2>Води сметка</h2>
<p>Записвай покупна цена, продажна цена и такси за всеки артикул – точно за това е Reseller Profit &amp; DAC7 Tracker.</p>""", [BG_SRC, EU_BG])

# ---------------- Czech
EU_CS = eurlex("CS", "Směrnice Rady (EU) 2021/514 (DAC7), EUR-Lex")
CS_SRC = ("Finanční správa: Příjmy z bazarového prodeje", "https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/dotazy-a-odpovedi/dan-z-prijmu-fyzickych-osob/prijmy-z-bazaroveho-prodeje")
M["tax-id"]["cs"] = A("vinted-danove-identifikacni-cislo", "Vinted chce tvé daňové číslo: musíš ho zadat?",
 "Proč Vinted, Aukro a eBay chtějí daňové identifikační číslo, jaké údaje jdou finančnímu úřadu a co se stane, když ho nezadáš.",
 "Ano. Když platforma podle pravidel DAC7 chce tvé daňové číslo, musíš ho zadat, jinak může zadržet výplaty nebo omezit tvůj prodejní účet. Neznamená to, že platíš daň.",
 """<h2>Proč se platforma ptá?</h2>
<p>Od roku 2023 musí online platformy v EU sbírat údaje o prodejcích a jednou ročně je předávat daňovým úřadům podle směrnice DAC7. Nahlášen budeš, pokud na jedné platformě za rok dosáhneš 30 prodejů nebo utržíš více než 2 000 €.</p>
<h2>Jaké údaje se předávají?</h2>
<ul><li>Jméno, adresa a datum narození</li><li>Daňové identifikační číslo (u fyzických osob v Česku obvykle rodné číslo)</li><li>Počet prodejů a obdržené částky po odečtení poplatků platformy</li></ul>
<h2>Co když ho nezadáš?</h2>
<p>Platforma tě musí upomenout. Pokud nereaguješ, může zadržet výplaty nebo omezit prodej. Odmítnutí nahlášení nezastaví, jen zablokuje účet.</p>
<h2>Bezpečně</h2>
<ul><li>Číslo zadávej jen v aplikaci nebo na webu platformy, nikdy přes odkaz z e-mailu či SMS.</li><li>Kontrolou DAC7 si ověř, zda limit vůbec dosáhneš.</li></ul>
<p>Nahlášení není daňová povinnost. Viz <a href="../soukrome-nebo-podnikani/">Soukromý prodej, nebo podnikání?</a></p>""", [EU_CS, S_EBAY])
M["letter"]["cs"] = A("dopis-z-financniho-uradu-po-dac7", "Dopis z finančního úřadu po nahlášení DAC7: co dělat?",
 "Dostal jsi dopis z finančního úřadu po prodejích na Vintedu, Aukru nebo eBayi? Takto odpovíš klidně a správně.",
 "Zachovej klid, ale dopis neignoruj. Úřad většinou chce vědět, zda nahlášené prodeje obsahují zdanitelný příjem. Prodej vlastních použitých věcí z domácnosti je v Česku od daně osvobozen.",
 """<h2>Proč ti úřad píše?</h2>
<p>Každý rok do 31. ledna platformy hlásí, kdo u nich v předchozím roce dosáhl 30 prodejů nebo více než 2 000 €. Úřad údaje porovná s tvým přiznáním a může se zeptat. Dotaz není pokuta.</p>
<h2>Krok za krokem</h2>
<ol><li><strong>Poznamenej si lhůtu</strong> z dopisu.</li><li><strong>Shromáždi prodeje</strong> z aplikace: co, kdy, za kolik.</li><li><strong>Roztřiď je:</strong> vlastní použité věci, nebo zboží koupené k dalšímu prodeji?</li><li><strong>Odpověz stručně a pravdivě</strong>, např.: „Jde o prodej použitého oblečení z mé domácnosti.“</li></ol>
<h2>Pravidla v Česku</h2>
<p>Příjem z prodeje vlastních použitých věcí z domácnosti (oblečení, hračky, kočárek, nábytek, kolo) je od daně osvobozen a do přiznání se neuvádí. Kdo opakovaně nakupuje věci, aby je se ziskem prodal, může podnikat a takový příjem se daní.</p>
<p>Pravidla všech 27 zemí EU: <a href=\"""" + OV + """\">přehled (anglicky)</a>.</p>
<h2>Na příští rok</h2>
<p>Veď si jednoduchý seznam, co kupuješ a prodáváš a za kolik.</p>""", [CS_SRC, EU_CS])
M["platforms"]["cs"] = A("dac7-vinted-aukro-ebay-co-se-hlasi", "DAC7 na Vintedu, Aukru a eBayi: co se hlásí?",
 "Které prodeje Vinted, Aukro, eBay a Etsy hlásí finančnímu úřadu, jak se počítají a proč samotné inzeráty nestačí.",
 "Hlásí se jen dokončené prodeje zaplacené přes platformu. Platba v hotovosti při převzetí se nepočítá, protože ji platforma nevidí. Každá platforma počítá zvlášť.",
 """<h2>Co je prodej?</h2>
<p>DAC7 počítá transakce: skutečně dokončené a zaplacené prodeje. Počet inzerátů nehraje roli.</p>
<h2>Platformy ve zkratce</h2>
<ul><li><strong>Vinted:</strong> téměř všechny prodeje jdou přes platby Vintedu, takže se počítají.</li><li><strong>Aukro, eBay a Etsy:</strong> zpracovávají platby samy.</li><li><strong>Inzertní weby</strong> jako Bazoš: počítají se jen prodeje přes jejich vlastní platební nebo doručovací službu.</li></ul>
<h2>Každá platforma zvlášť</h2>
<p>Limity 30 prodejů nebo více než 2 000 € platí pro každou platformu. Pro daně se ale počítá celý tvůj příjem.</p>
<h2>Co se hlásí?</h2>
<p>Částky po odečtení poplatků platformy, jméno, adresa, datum narození a daňové číslo.</p>""", [EU_CS, S_MOBI])
M["business"]["cs"] = A("soukrome-nebo-podnikani", "Soukromý prodej, nebo podnikání: kde je hranice?",
 "Kdy se prodej na Vintedu nebo Aukru stává podnikáním? Hlavní kritéria jednoduše.",
 "Pevný počet prodejů neexistuje. Rozhoduje, zda se zbavuješ vlastních věcí, nebo nakupuješ, abys prodával se ziskem. Ve druhém případě může být podnikáním už první prodej.",
 """<h2>Soukromě: vyklízení</h2>
<p>Prodej oblečení, nábytku nebo hraček z vlastní domácnosti je soukromý, i když je prodejů hodně. V Česku je tento příjem osvobozen.</p>
<h2>Podnikání: nákup za účelem prodeje</h2>
<ul><li>Pravidelně nakupuješ zboží k dalšímu prodeji.</li><li>Nabízíš mnoho stejných nebo nových věcí.</li><li>Tvůj profil vypadá jako obchod.</li></ul>
<p>Rozhoduje záměr dosáhnout zisku. Takový příjem se daní jako příjem ze samostatné činnosti.</p>
<h2>Veď si čísla</h2>
<p>Zapisuj nákupní cenu, prodejní cenu a poplatky u každé věci – přesně k tomu slouží Reseller Profit &amp; DAC7 Tracker.</p>""", [CS_SRC, EU_CS])

# ---------------- Danish
EU_DA = eurlex("DA", "Rådets direktiv (EU) 2021/514 (DAC7), EUR-Lex")
DA_SRC = ("Legal Desk: Hvornår skal jeg betale skat af privat salg? (2022)", "https://www.legaldesk.dk/artikler/hvornaar-skal-jeg-betale-skat-af-privat-salg")
M["tax-id"]["da"] = A("vinted-cpr-nummer", "Vinted beder om dit CPR-nummer: skal du give det?",
 "Hvorfor Vinted, DBA og eBay beder om dit skatte-ID, hvilke data der går til Skattestyrelsen, og hvad der sker, hvis du ikke giver det.",
 "Ja. Når en platform beder om dit skatte-ID efter DAC7-reglerne, skal du give det, ellers kan den tilbageholde udbetalinger eller begrænse din sælgerkonto. Det betyder ikke, at du skal betale skat.",
 """<h2>Hvorfor spørger platformen?</h2>
<p>Siden 2023 skal onlineplatforme i EU indsamle oplysninger om sælgere og indberette dem én gang om året efter DAC7-direktivet. Du indberettes, hvis du på én platform når 30 salg eller sælger for over 2.000 € i et kalenderår.</p>
<h2>Hvilke oplysninger indberettes?</h2>
<ul><li>Navn, adresse og fødselsdato</li><li>Dit skatte-ID (i Danmark dit CPR-nummer)</li><li>Antal salg og de beløb, du fik, efter platformens gebyrer</li></ul>
<h2>Hvad sker der, hvis du ikke giver det?</h2>
<p>Platformen skal minde dig om det. Svarer du ikke, kan den tilbageholde udbetalinger eller begrænse dit salg. Et afslag stopper ikke indberetningen; det blokerer kun kontoen.</p>
<h2>Sådan gør du det sikkert</h2>
<ul><li>Indtast kun nummeret i platformens app eller på dens hjemmeside, aldrig via et link i en mail eller sms.</li><li>Tjek med DAC7-tjekket, om du overhovedet når grænsen.</li></ul>
<p>Indberetning er ikke en skatteregning. Læs <a href="../privat-eller-erhverv/">Privat eller erhverv?</a></p>""", [EU_DA, S_EBAY])
M["letter"]["da"] = A("brev-fra-skattestyrelsen-efter-dac7", "Brev fra Skattestyrelsen efter en DAC7-indberetning: hvad nu?",
 "Har du fået brev fra Skattestyrelsen efter salg på Vinted, DBA eller eBay? Sådan svarer du roligt og korrekt.",
 "Bevar roen, men ignorer det ikke. Skattestyrelsen vil som regel vide, om de indberettede salg indeholder skattepligtig indkomst. Privat salg af egne brugte ting er som udgangspunkt ikke skattepligtigt i Danmark.",
 """<h2>Hvorfor skriver Skattestyrelsen?</h2>
<p>Hvert år inden 31. januar indberetter platformene, hvem der året før nåede 30 salg eller over 2.000 € hos dem. Skattestyrelsen sammenligner med din årsopgørelse og kan stille spørgsmål. Et spørgsmål er ikke en bøde.</p>
<h2>Trin for trin</h2>
<ol><li><strong>Noter fristen</strong> i brevet.</li><li><strong>Saml dine salg</strong> fra appen: hvad, hvornår og for hvor meget.</li><li><strong>Sorter dem:</strong> dine egne brugte ting eller varer købt for at sælge dem videre?</li><li><strong>Svar kort og ærligt</strong>, fx: „Det drejer sig om salg af brugt tøj fra min husstand.“</li></ol>
<h2>Reglerne i Danmark</h2>
<p>Udgangspunktet er, at privat salg ikke er skattepligtigt. Har du købt tingene for at sælge dem videre eller med spekulation for øje, er salget næsten altid skattepligtigt. Regelmæssigt salg kan være hobby- eller erhvervsvirksomhed.</p>
<p>Reglerne i alle 27 EU-lande: <a href=\"""" + OV + """\">oversigt (på engelsk)</a>.</p>
<h2>Til næste år</h2>
<p>Før en enkel liste over, hvad du køber og sælger, og til hvilken pris.</p>""", [DA_SRC, EU_DA])
M["platforms"]["da"] = A("dac7-vinted-dba-ebay-hvad-indberettes", "DAC7 på Vinted, DBA og eBay: hvad bliver indberettet?",
 "Hvilke salg Vinted, DBA, eBay og Etsy indberetter til Skattestyrelsen, hvordan de tælles, og hvorfor annoncer alene ikke tæller.",
 "Kun gennemførte salg betalt via platformen indberettes. Kontantbetaling ved afhentning tæller ikke, fordi platformen ikke ser den. Hver platform tæller for sig.",
 """<h2>Hvad tæller som et salg?</h2>
<p>DAC7 tæller transaktioner: salg, der faktisk er gennemført og betalt. Antallet af annoncer betyder intet.</p>
<h2>Platformene kort</h2>
<ul><li><strong>Vinted:</strong> næsten alle salg går gennem Vinteds betaling og tæller derfor.</li><li><strong>eBay og Etsy:</strong> håndterer selv betalingen.</li><li><strong>DBA og andre annoncesider:</strong> kun salg via deres egen betalings- eller fragtløsning tæller.</li></ul>
<h2>Hver platform for sig</h2>
<p>Grænserne på 30 salg eller over 2.000 € gælder pr. platform. Skattemæssigt tæller hele din indkomst dog.</p>
<h2>Hvad indberettes?</h2>
<p>Beløbene efter platformens gebyrer samt navn, adresse, fødselsdato og skatte-ID.</p>""", [EU_DA, S_MOBI])
M["business"]["da"] = A("privat-eller-erhverv", "Privat salg eller erhverv: hvor går grænsen?",
 "Hvornår bliver salg på Vinted eller DBA til erhverv? De vigtigste kriterier forklaret enkelt.",
 "Der er ikke et fast antal salg. Det afgørende er, om du rydder op i dine egne ting eller køber for at sælge videre med fortjeneste. I det sidste tilfælde kan selv første salg være skattepligtigt.",
 """<h2>Privat: oprydning</h2>
<p>At sælge tøj, møbler eller legetøj fra din egen husstand er privat salg, også selvom der er mange salg.</p>
<h2>Erhverv: køb for at sælge videre</h2>
<ul><li>Du køber regelmæssigt varer for at sælge dem videre.</li><li>Du sælger mange ens eller nye varer.</li><li>Din profil ligner en butik, fx via hjemmeside eller sociale medier.</li></ul>
<p>Regelmæssigt salg uden fortjenestemål kan være hobbyvirksomhed; professionelt salg er erhverv med momsregistrering og regnskab.</p>
<h2>Hold styr på tallene</h2>
<p>Noter købspris, salgspris og gebyrer for hver vare – det er præcis, hvad Reseller Profit &amp; DAC7 Tracker er til.</p>""", [DA_SRC, EU_DA])

# ---------------- Greek
EU_EL = eurlex("EL", "Οδηγία (ΕΕ) 2021/514 του Συμβουλίου (DAC7), EUR-Lex")
EL_SRC = ("Taxheaven: Πώληση ΙΧ και λοιπών κινητών πραγμάτων από ιδιώτη (2024)", "https://www.taxheaven.gr/circulars/48221/arora-pwlhsh-ix-kai-loipwn-kinhtwn-pragmatwn-apo-idiwth-forologikes-proektaseis")
CY_SRC = ("PwC Tax Summaries: Cyprus, income determination", "https://taxsummaries.pwc.com/cyprus/individual/income-determination")
M["tax-id"]["el"] = A("vinted-afm", "Το Vinted ζητά το ΑΦΜ σου: πρέπει να το δώσεις;",
 "Γιατί το Vinted και το eBay ζητούν ΑΦΜ, ποια στοιχεία πάνε στην εφορία και τι γίνεται αν δεν το δώσεις.",
 "Ναι. Όταν μια πλατφόρμα ζητά το ΑΦΜ σου βάσει του DAC7, πρέπει να το δώσεις, αλλιώς μπορεί να παρακρατήσει πληρωμές ή να περιορίσει τον λογαριασμό σου. Αυτό δεν σημαίνει ότι οφείλεις φόρο.",
 """<h2>Γιατί ρωτά η πλατφόρμα;</h2>
<p>Από το 2023 οι διαδικτυακές πλατφόρμες στην ΕΕ συλλέγουν στοιχεία πωλητών και τα διαβιβάζουν μία φορά τον χρόνο στις φορολογικές αρχές, βάσει της οδηγίας DAC7. Δηλώνεσαι αν σε μία πλατφόρμα φτάσεις τις 30 πωλήσεις ή ξεπεράσεις τα 2.000 € μέσα σε ένα έτος.</p>
<h2>Ποια στοιχεία διαβιβάζονται;</h2>
<ul><li>Όνομα, διεύθυνση και ημερομηνία γέννησης</li><li>Ο φορολογικός σου αριθμός (στην Ελλάδα και την Κύπρο ο ΑΦΜ / ΑΦΤ)</li><li>Ο αριθμός πωλήσεων και τα ποσά μετά τις χρεώσεις της πλατφόρμας</li></ul>
<h2>Τι γίνεται αν δεν το δώσεις;</h2>
<p>Η πλατφόρμα πρέπει να σου το υπενθυμίσει. Αν δεν απαντήσεις, μπορεί να παρακρατήσει πληρωμές ή να περιορίσει τις πωλήσεις σου. Η άρνηση δεν σταματά τη δήλωση· μόνο μπλοκάρει τον λογαριασμό.</p>
<h2>Με ασφάλεια</h2>
<ul><li>Γράψε τον αριθμό μόνο στην εφαρμογή ή στον ιστότοπο της πλατφόρμας, ποτέ μέσω συνδέσμου από email ή SMS.</li><li>Έλεγξε με τον έλεγχο DAC7 αν θα φτάσεις καν το όριο.</li></ul>
<p>Η δήλωση δεν είναι φόρος. Διάβασε <a href="../idiotis-i-epixeirisi/">Ιδιώτης ή επιχείρηση;</a></p>""", [EU_EL, S_EBAY])
M["letter"]["el"] = A("epistoli-eforias-meta-dac7", "Επιστολή από την εφορία μετά από δήλωση DAC7: τι κάνω;",
 "Πήρες επιστολή από την εφορία μετά από πωλήσεις στο Vinted ή στο eBay; Έτσι απαντάς ήρεμα και σωστά.",
 "Μείνε ήρεμος, αλλά μην την αγνοήσεις. Συνήθως η εφορία θέλει να μάθει αν οι πωλήσεις περιλαμβάνουν φορολογητέο εισόδημα. Η περιστασιακή πώληση δικών σου πραγμάτων δεν φορολογείται στην Ελλάδα.",
 """<h2>Γιατί σου γράφουν;</h2>
<p>Κάθε χρόνο έως τις 31 Ιανουαρίου οι πλατφόρμες δηλώνουν όσους έφτασαν τις 30 πωλήσεις ή ξεπέρασαν τα 2.000 € σε αυτές. Η εφορία συγκρίνει τα στοιχεία με τη δήλωσή σου και μπορεί να ρωτήσει. Μια ερώτηση δεν είναι πρόστιμο.</p>
<h2>Βήμα βήμα</h2>
<ol><li><strong>Σημείωσε την προθεσμία</strong> της επιστολής.</li><li><strong>Μάζεψε τις πωλήσεις</strong> από την εφαρμογή: τι, πότε, πόσο.</li><li><strong>Ξεχώρισέ τες:</strong> δικά σου μεταχειρισμένα ή αγαθά που αγόρασες για μεταπώληση;</li><li><strong>Απάντησε σύντομα και ειλικρινά</strong>, π.χ.: «Πρόκειται για πώληση μεταχειρισμένων ρούχων του νοικοκυριού μου.»</li></ol>
<h2>Οι κανόνες σε Ελλάδα και Κύπρο</h2>
<ul><li><strong>Ελλάδα:</strong> η περιστασιακή πώληση από ιδιώτη δεν φορολογείται. Τρεις όμοιες συναλλαγές μέσα σε έξι μήνες μπορούν να θεωρηθούν συστηματικές, δηλαδή επιχειρηματική δραστηριότητα (άρθρο 21 ΚΦΕ), και τότε φορολογείται το κέρδος.</li>
<li><strong>Κύπρος:</strong> τα κέρδη κεφαλαίου φορολογούνται μόνο για ακίνητα στην Κύπρο, οπότε η πώληση προσωπικών αντικειμένων δεν φορολογείται, εκτός αν πρόκειται για εμπορία.</li></ul>
<p>Οι κανόνες και των 27 χωρών της ΕΕ: <a href=\"""" + OV + """\">επισκόπηση (στα αγγλικά)</a>.</p>
<h2>Για την επόμενη χρονιά</h2>
<p>Κράτα μια απλή λίστα με όσα αγοράζεις και πουλάς και σε ποια τιμή.</p>""", [EL_SRC, CY_SRC, EU_EL])
M["platforms"]["el"] = A("dac7-vinted-ebay-ti-dilonetai", "DAC7 σε Vinted και eBay: τι δηλώνεται;",
 "Ποιες πωλήσεις δηλώνουν το Vinted, το eBay και το Etsy στην εφορία, πώς μετρώνται και γιατί οι αγγελίες μόνες τους δεν μετράνε.",
 "Δηλώνονται μόνο ολοκληρωμένες πωλήσεις που πληρώθηκαν μέσω της πλατφόρμας. Η πληρωμή με μετρητά στο χέρι δεν μετράει, γιατί η πλατφόρμα δεν τη βλέπει. Κάθε πλατφόρμα μετράει χωριστά.",
 """<h2>Τι μετράει ως πώληση;</h2>
<p>Το DAC7 μετράει συναλλαγές: πωλήσεις που ολοκληρώθηκαν και πληρώθηκαν. Ο αριθμός αγγελιών δεν παίζει ρόλο.</p>
<h2>Οι πλατφόρμες με λίγα λόγια</h2>
<ul><li><strong>Vinted:</strong> σχεδόν όλες οι πωλήσεις περνούν από την πληρωμή του Vinted και μετράνε.</li><li><strong>eBay και Etsy:</strong> διαχειρίζονται οι ίδιες τις πληρωμές.</li><li><strong>Ιστότοποι αγγελιών:</strong> μετράνε μόνο πωλήσεις μέσω της δικής τους υπηρεσίας πληρωμής ή αποστολής.</li></ul>
<h2>Κάθε πλατφόρμα χωριστά</h2>
<p>Τα όρια των 30 πωλήσεων ή πάνω από 2.000 € ισχύουν ανά πλατφόρμα. Για τον φόρο όμως μετράει όλο σου το εισόδημα.</p>
<h2>Τι δηλώνεται;</h2>
<p>Τα ποσά μετά τις χρεώσεις, όνομα, διεύθυνση, ημερομηνία γέννησης και φορολογικός αριθμός.</p>""", [EU_EL, S_MOBI])
M["business"]["el"] = A("idiotis-i-epixeirisi", "Ιδιώτης ή επιχείρηση: πού είναι το όριο;",
 "Πότε οι πωλήσεις στο Vinted ή στο eBay γίνονται επιχειρηματική δραστηριότητα; Τα βασικά κριτήρια απλά.",
 "Δεν υπάρχει σταθερός αριθμός πωλήσεων. Μετράει αν ξεφορτώνεσαι δικά σου πράγματα ή αγοράζεις για να μεταπωλήσεις με κέρδος. Στην Ελλάδα, τρεις όμοιες συναλλαγές σε έξι μήνες μπορεί να θεωρηθούν συστηματικές.",
 """<h2>Ιδιώτης: ξεκαθάρισμα</h2>
<p>Η πώληση ρούχων, επίπλων ή παιχνιδιών από το δικό σου νοικοκυριό είναι ιδιωτική, ακόμη κι αν είναι πολλές οι πωλήσεις.</p>
<h2>Επιχείρηση: αγορά για μεταπώληση</h2>
<ul><li>Αγοράζεις τακτικά αγαθά για να τα μεταπωλήσεις.</li><li>Προσφέρεις πολλά ίδια ή καινούργια είδη.</li><li>Ο λογαριασμός σου μοιάζει με κατάστημα.</li></ul>
<p>Μόλις η δραστηριότητα θεωρηθεί συστηματική, κάθε επόμενη πώληση τεκμαίρεται ότι γίνεται για κέρδος και το κέρδος φορολογείται ως επιχειρηματικό εισόδημα· μπορεί να προκύψει και ΦΠΑ.</p>
<h2>Κράτα αριθμούς</h2>
<p>Κατέγραφε τιμή αγοράς, τιμή πώλησης και χρεώσεις για κάθε είδος – γι' αυτό υπάρχει το Reseller Profit &amp; DAC7 Tracker.</p>""", [EL_SRC, EU_EL])

# ---------------- Estonian
EU_ET = eurlex("ET", "Nõukogu direktiiv (EL) 2021/514 (DAC7), EUR-Lex")
ET_SRC = ("Maksu- ja Tolliamet: Internetimüük", "https://emta.ee/eraklient/maksud-ja-tasumine/maksustatavad-tulud/internetimuuk")
M["tax-id"]["et"] = A("vinted-isikukood", "Vinted küsib sinu isikukoodi: kas pead selle andma?",
 "Miks Vinted, Okidoki ja eBay küsivad maksukohustuslase numbrit, millised andmed lähevad maksuametile ja mis juhtub, kui sa neid ei anna.",
 "Jah. Kui platvorm küsib DAC7 reeglite alusel sinu maksunumbrit, pead selle andma, muidu võib ta väljamakseid kinni pidada või müüjakontot piirata. See ei tähenda, et pead maksu maksma.",
 """<h2>Miks platvorm küsib?</h2>
<p>Alates 2023. aastast peavad ELi veebiplatvormid koguma müüjate andmeid ja edastama need kord aastas maksuhaldurile DAC7 direktiivi alusel. Sinust teatatakse, kui jõuad ühel platvormil aastas 30 müügini või teenid üle 2000 €.</p>
<h2>Milliseid andmeid edastatakse?</h2>
<ul><li>Nimi, aadress ja sünniaeg</li><li>Maksukohustuslase number (Eestis isikukood)</li><li>Müükide arv ja saadud summad pärast platvormi tasusid</li></ul>
<h2>Mis juhtub, kui sa seda ei anna?</h2>
<p>Platvorm peab sulle meelde tuletama. Kui sa ei vasta, võib ta väljamakseid kinni pidada või müüki piirata. Keeldumine ei peata teatamist, vaid blokeerib konto.</p>
<h2>Turvaliselt</h2>
<ul><li>Sisesta number ainult platvormi rakenduses või veebis, mitte kunagi e-kirja või SMS-i lingi kaudu.</li><li>Kontrolli DAC7 kontrolliga, kas üldse jõuad piirini.</li></ul>
<p>Teatamine ei ole maksuarve. Loe <a href="../eraisik-voi-ettevotja/">Eraisik või ettevõtja?</a></p>""", [EU_ET, S_EBAY])
M["letter"]["et"] = A("kiri-maksuametilt-parast-dac7", "Kiri maksuametilt pärast DAC7 teatamist: mis nüüd?",
 "Said maksuametilt kirja pärast müüke Vintedis, Okidokis või eBays? Nii vastad rahulikult ja õigesti.",
 "Jää rahulikuks, aga ära jäta kirja tähelepanuta. Maksuamet tahab tavaliselt teada, kas teatatud müükides on maksustatavat tulu. Isiklikuks kasutamiseks olnud asjade müük Eestis ei maksustata.",
 """<h2>Miks maksuamet kirjutab?</h2>
<p>Igal aastal 31. jaanuariks teatavad platvormid, kes jõudis eelmisel aastal nende juures 30 müügini või üle 2000 €. Maksuamet võrdleb andmeid sinu deklaratsiooniga ja võib küsida. Küsimus ei ole trahv.</p>
<h2>Samm-sammult</h2>
<ol><li><strong>Pane kirja tähtaeg.</strong></li><li><strong>Kogu müügid</strong> rakendusest: mida, millal, mis hinnaga.</li><li><strong>Sorteeri:</strong> oma kasutatud asjad või edasimüügiks ostetud kaubad?</li><li><strong>Vasta lühidalt ja ausalt</strong>, nt: „Tegemist on minu leibkonna kasutatud riiete müügiga.“</li></ol>
<h2>Reeglid Eestis</h2>
<p>Isiklikuks kasutamiseks olnud asjade müügist saadud tulu ei maksustata. Kui müüd asju, mida sa ise ei kasutanud, maksustatakse ostu- ja müügihinna vahe. Regulaarne müük kasumi eesmärgil on ettevõtlus ja nõuab registreerimist.</p>
<p>Kõigi 27 ELi riigi reeglid: <a href=\"""" + OV + """\">ülevaade (inglise keeles)</a>.</p>
<h2>Järgmiseks aastaks</h2>
<p>Pea lihtsat nimekirja, mida ostad ja müüd ning mis hinnaga.</p>""", [ET_SRC, EU_ET])
M["platforms"]["et"] = A("dac7-vinted-okidoki-ebay-mida-teatatakse", "DAC7 Vintedis, Okidokis ja eBays: mida teatatakse?",
 "Milliseid müüke Vinted, Okidoki, eBay ja Etsy maksuametile teatavad, kuidas neid loetakse ja miks kuulutused üksi ei loe.",
 "Teatatakse ainult lõpetatud müükidest, mis on makstud platvormi kaudu. Sularahamakse üleandmisel ei loe, sest platvorm seda ei näe. Iga platvorm loeb eraldi.",
 """<h2>Mis loeb müügiks?</h2>
<p>DAC7 loeb tehinguid: tegelikult lõpetatud ja makstud müüke. Kuulutuste arv ei loe.</p>
<h2>Platvormid lühidalt</h2>
<ul><li><strong>Vinted:</strong> peaaegu kõik müügid käivad Vintedi makse kaudu ja loevad.</li><li><strong>eBay ja Etsy:</strong> haldavad makseid ise.</li><li><strong>Kuulutusportaalid</strong> nagu Okidoki: loevad ainult müügid nende enda makse- või tarneteenuse kaudu.</li></ul>
<h2>Iga platvorm eraldi</h2>
<p>Piirid 30 müüki või üle 2000 € kehtivad platvormi kohta. Maksude jaoks loeb siiski kogu sinu tulu.</p>
<h2>Mida teatatakse?</h2>
<p>Summad pärast platvormi tasusid, nimi, aadress, sünniaeg ja isikukood.</p>""", [EU_ET, S_MOBI])
M["business"]["et"] = A("eraisik-voi-ettevotja", "Eraisik või ettevõtja: kus on piir?",
 "Millal muutub müük Vintedis või Okidokis ettevõtluseks? Peamised kriteeriumid lihtsalt.",
 "Kindlat müükide arvu pole. Oluline on, kas vabaned oma asjadest või ostad, et kasumiga edasi müüa. Teisel juhul võib juba esimene müük olla maksustatav.",
 """<h2>Eraisik: koristamine</h2>
<p>Oma leibkonna riiete, mööbli või mänguasjade müük on eramüük ega ole Eestis maksustatav.</p>
<h2>Ettevõtja: ostmine edasimüügiks</h2>
<ul><li>Ostad regulaarselt kaupu, et neid edasi müüa.</li><li>Pakud palju ühesuguseid või uusi esemeid.</li><li>Sinu konto näeb välja nagu pood.</li></ul>
<p>Üksikud edasimüügid maksustatakse kasumi pealt; regulaarne müük kasumi eesmärgil on ettevõtlus ja nõuab kandmist äriregistrisse.</p>
<h2>Pea arvestust</h2>
<p>Pane kirja iga eseme ostuhind, müügihind ja tasud – just selleks on Reseller Profit &amp; DAC7 Tracker.</p>""", [ET_SRC, EU_ET])
