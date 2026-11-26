# Articles: fi, hr, hu, lt, lv
from articles_more import eurlex, S_EBAY, S_MOBI
from articles_b1 import A, OV
OVL = OV

G = {
 "fi": {"dir": "oppaat", "title": "Oppaat", "intro": "Vastauksia yleisimpiin kysymyksiin DAC7:stä, Vintedistä ja verottajasta.",
        "updated": "Päivitetty: 26.11.2026", "read": "Lue lisää", "back": "Takaisin DAC7-tarkistukseen",
        "cta_title": "Kuinka lähellä rajaa olet?", "cta_text": "Tarkista jokainen alusta minuutissa ilmaisella DAC7-tarkistuksella.", "cta_btn": "Avaa DAC7-tarkistus",
        "track": "Tai seuraa koko vuoden voittoa ja DAC7-tilaa työkalulla", "track_link": "Reseller Profit &amp; DAC7 Tracker (englanniksi)",
        "sources": "Lähteet", "disclaimer": "Tämä artikkeli on yleistä tietoa eikä vero- tai oikeudellista neuvontaa."},
 "hr": {"dir": "vodici", "title": "Vodiči", "intro": "Odgovori na najčešća pitanja o DAC7, Vintedu i Poreznoj upravi.",
        "updated": "Ažurirano: 26. studenoga 2026.", "read": "Pročitaj", "back": "Natrag na DAC7 provjeru",
        "cta_title": "Koliko si blizu granice?", "cta_text": "Provjeri svaku platformu za minutu besplatnom DAC7 provjerom.", "cta_btn": "Otvori DAC7 provjeru",
        "track": "Ili prati cijelu godinu zaradu i DAC7 status uz", "track_link": "Reseller Profit &amp; DAC7 Tracker (na engleskom)",
        "sources": "Izvori", "disclaimer": "Ovaj članak je opća informacija, a ne porezni ili pravni savjet."},
 "hu": {"dir": "utmutatok", "title": "Útmutatók", "intro": "Válaszok a leggyakoribb kérdésekre a DAC7-ről, a Vintedről és a NAV-ról.",
        "updated": "Frissítve: 2026. november 26.", "read": "Tovább", "back": "Vissza a DAC7 ellenőrzéshez",
        "cta_title": "Milyen közel vagy a határhoz?", "cta_text": "Ellenőrizd platformonként egy perc alatt az ingyenes DAC7 ellenőrzéssel.", "cta_btn": "DAC7 ellenőrzés megnyitása",
        "track": "Vagy kövesd egész évben a hasznodat és a DAC7 állapotot a", "track_link": "Reseller Profit &amp; DAC7 Tracker (angol nyelvű) segítségével",
        "sources": "Források", "disclaimer": "Ez a cikk általános tájékoztatás, nem adó- vagy jogi tanácsadás."},
 "lt": {"dir": "gidai", "title": "Gidai", "intro": "Atsakymai į dažniausius klausimus apie DAC7, Vinted ir VMI.",
        "updated": "Atnaujinta: 2026 m. lapkričio 26 d.", "read": "Skaityti", "back": "Atgal į DAC7 patikrą",
        "cta_title": "Kiek tau liko iki ribos?", "cta_text": "Patikrink kiekvieną platformą per minutę su nemokama DAC7 patikra.", "cta_btn": "Atidaryti DAC7 patikrą",
        "track": "Arba visus metus sek pelną ir DAC7 būseną su", "track_link": "Reseller Profit &amp; DAC7 Tracker (anglų kalba)",
        "sources": "Šaltiniai", "disclaimer": "Šis straipsnis yra bendra informacija, o ne mokesčių ar teisinė konsultacija."},
 "lv": {"dir": "celveži", "title": "Ceļveži", "intro": "Atbildes uz biežākajiem jautājumiem par DAC7, Vinted un VID.",
        "updated": "Atjaunināts: 2026. gada 26. novembrī", "read": "Lasīt", "back": "Atpakaļ uz DAC7 pārbaudi",
        "cta_title": "Cik tuvu esi robežai?", "cta_text": "Pārbaudi katru platformu minūtē ar bezmaksas DAC7 pārbaudi.", "cta_btn": "Atvērt DAC7 pārbaudi",
        "track": "Vai seko peļņai un DAC7 statusam visu gadu ar", "track_link": "Reseller Profit &amp; DAC7 Tracker (angļu valodā)",
        "sources": "Avoti", "disclaimer": "Šis raksts ir vispārīga informācija, nevis nodokļu vai juridiska konsultācija."},
}
G["lv"]["dir"] = "celvezi"

M = {"tax-id": {}, "letter": {}, "platforms": {}, "business": {}}

# ---------------- Finnish
EU_FI = eurlex("FI", "Neuvoston direktiivi (EU) 2021/514 (DAC7), EUR-Lex")
FI_SRC = ("Vero.fi: Flea market sales", "https://vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/flea-market-sales/")
M["tax-id"]["fi"] = A("vinted-henkilotunnus", "Vinted kysyy henkilötunnustasi: pitääkö se antaa?",
 "Miksi Vinted, Tori ja eBay kysyvät verotunnistetta, mitä tietoja menee verottajalle ja mitä tapahtuu, jos et anna sitä.",
 "Kyllä. Kun alusta pyytää DAC7-sääntöjen perusteella verotunnistettasi, se on annettava, muuten alusta voi pidättää maksuja tai rajoittaa myyjätiliäsi. Se ei tarkoita, että sinun pitää maksaa veroa.",
 """<h2>Miksi alusta kysyy?</h2>
<p>Vuodesta 2023 EU:n verkkoalustojen on kerättävä myyjien tiedot ja ilmoitettava ne kerran vuodessa veroviranomaisille DAC7-direktiivin perusteella. Sinusta ilmoitetaan, jos teet yhdellä alustalla vuoden aikana 30 myyntiä tai myyt yli 2 000 eurolla.</p>
<h2>Mitä tietoja ilmoitetaan?</h2>
<ul><li>Nimi, osoite ja syntymäaika</li><li>Verotunniste (Suomessa henkilötunnus)</li><li>Myyntien määrä ja saadut summat alustan maksujen jälkeen</li></ul>
<h2>Mitä tapahtuu, jos et anna sitä?</h2>
<p>Alustan on muistutettava sinua. Jos et vastaa, se voi pidättää maksuja tai rajoittaa myyntiä. Kieltäytyminen ei estä ilmoitusta, vaan estää tilisi.</p>
<h2>Turvallisesti</h2>
<ul><li>Syötä tunnus vain alustan sovellukseen tai verkkosivuille, ei koskaan sähköpostin tai tekstiviestin linkin kautta.</li><li>Tarkista DAC7-tarkistuksella, saavutatko rajan ylipäätään.</li></ul>
<p>Ilmoitus ei ole verolasku. Lue <a href="../yksityinen-vai-elinkeino/">Yksityinen myyjä vai elinkeinonharjoittaja?</a></p>""", [EU_FI, S_EBAY])
M["letter"]["fi"] = A("kirje-verottajalta-dac7-ilmoituksen-jalkeen", "Kirje verottajalta DAC7-ilmoituksen jälkeen: mitä nyt?",
 "Saitko kirjeen Verohallinnolta Vinted-, Tori- tai eBay-myyntien jälkeen? Näin vastaat rauhallisesti ja oikein.",
 "Pysy rauhallisena, mutta älä jätä kirjettä huomiotta. Verottaja haluaa yleensä tietää, sisältävätkö ilmoitetut myynnit veronalaista tuloa. Oman käytetyn kotiirtaimiston myynti on Suomessa verovapaata 5 000 euron vuosittaiseen voittoon asti.",
 """<h2>Miksi verottaja kirjoittaa?</h2>
<p>Joka vuosi 31. tammikuuta mennessä alustat ilmoittavat, kuka saavutti edellisenä vuonna 30 myyntiä tai yli 2 000 euroa niillä. Verottaja vertaa tietoja veroilmoitukseesi ja voi kysyä lisää. Kysymys ei ole sakko.</p>
<h2>Vaihe vaiheelta</h2>
<ol><li><strong>Merkitse määräaika.</strong></li><li><strong>Kerää myynnit</strong> sovelluksesta: mitä, milloin, millä hinnalla.</li><li><strong>Lajittele:</strong> omia käytettyjä tavaroita vai jälleenmyyntiin ostettuja?</li><li><strong>Vastaa lyhyesti ja rehellisesti</strong>, esim.: ”Kyse on kotitalouteni käytettyjen vaatteiden myynnistä.”</li></ol>
<h2>Säännöt Suomessa</h2>
<p>Itse tai perheen käyttämän tavallisen kotiirtaimiston (vaatteet, astiat, huonekalut, kodinelektroniikka, harrastusvälineet) myynti on verovapaata, jos vuoden luovutusvoitot ovat enintään 5 000 euroa. Ylittävä osa verotetaan. Itse tehdyt tuotteet ja jatkuva jälleenmyynti ovat veronalaisia. Tappiot omasta käyttöomaisuudesta eivät ole vähennyskelpoisia.</p>
<p>Kaikkien 27 EU-maan säännöt: <a href=\"""" + OVL + """\">yleiskatsaus (englanniksi)</a>.</p>
<h2>Ensi vuodeksi</h2>
<p>Pidä yksinkertaista listaa ostoista ja myynneistä hintoineen.</p>""", [FI_SRC, EU_FI])
M["platforms"]["fi"] = A("dac7-vinted-tori-ebay-mita-ilmoitetaan", "DAC7 Vintedissä, Torissa ja eBayssa: mitä ilmoitetaan?",
 "Mitkä myynnit Vinted, Tori, eBay ja Etsy ilmoittavat verottajalle, miten ne lasketaan ja miksi pelkät ilmoitukset eivät riitä.",
 "Vain loppuun viedyt, alustan kautta maksetut myynnit ilmoitetaan. Käteismaksu noudettaessa ei lasketa, koska alusta ei näe sitä. Jokainen alusta laskee erikseen.",
 """<h2>Mikä lasketaan myynniksi?</h2>
<p>DAC7 laskee transaktiot: myynnit, jotka on todella tehty ja maksettu. Ilmoitusten määrällä ei ole väliä.</p>
<h2>Alustat lyhyesti</h2>
<ul><li><strong>Vinted:</strong> lähes kaikki myynnit kulkevat Vintedin maksun kautta ja lasketaan.</li><li><strong>eBay ja Etsy:</strong> hoitavat maksut itse.</li><li><strong>Tori ja muut ilmoitussivustot:</strong> vain niiden oman maksu- tai toimituspalvelun kautta tehdyt myynnit lasketaan.</li></ul>
<h2>Jokainen alusta erikseen</h2>
<p>Rajat 30 myyntiä tai yli 2 000 € koskevat alustaa kohden. Verotuksessa lasketaan kuitenkin kaikki tulosi.</p>
<h2>Mitä ilmoitetaan?</h2>
<p>Summat alustan maksujen jälkeen sekä nimi, osoite, syntymäaika ja henkilötunnus.</p>""", [EU_FI, S_MOBI])
M["business"]["fi"] = A("yksityinen-vai-elinkeino", "Yksityinen myyjä vai elinkeinonharjoittaja: missä raja kulkee?",
 "Milloin myynti Vintedissä tai Torissa muuttuu elinkeinotoiminnaksi? Tärkeimmät kriteerit yksinkertaisesti.",
 "Kiinteää myyntimäärää ei ole. Ratkaisevaa on, myytkö omia tavaroitasi vai ostatko myydäksesi voitolla. Jatkuva ja ammattimainen myynti on verotuksessa elinkeinotoimintaa.",
 """<h2>Yksityinen: tavaroista luopuminen</h2>
<p>Oman kotitalouden vaatteiden, huonekalujen tai lelujen myynti on yksityistä myyntiä ja usein verovapaata.</p>
<h2>Elinkeino: ostaminen jälleenmyyntiin</h2>
<ul><li>Ostat säännöllisesti tavaraa myydäksesi sen eteenpäin.</li><li>Tarjoat paljon samanlaisia tai uusia tuotteita.</li><li>Tilisi näyttää kaupalta.</li></ul>
<p>Satunnainen käytetyn tavaran jälleenmyynti ei ole elinkeinotoimintaa, mutta jatkuva ja ammattimainen on. Arvonlisäverovelvolliseksi on rekisteröidyttävä, kun liikevaihto ylittää 20 000 euroa.</p>
<h2>Pidä luvut tallessa</h2>
<p>Kirjaa jokaisen tuotteen ostohinta, myyntihinta ja kulut – juuri sitä varten on Reseller Profit &amp; DAC7 Tracker.</p>""", [FI_SRC, EU_FI])

# ---------------- Croatian
EU_HR = eurlex("HR", "Direktiva Vijeća (EU) 2021/514 (DAC7), EUR-Lex")
HR_SRC = ("RRiF: Razmjena dobara na „buvljaku“ (2015)", "https://www.rrif.hr/razmjena_dobara_na_buvljaku-2987-misljenje/")
M["tax-id"]["hr"] = A("vinted-oib", "Vinted traži tvoj OIB: moraš li ga dati?",
 "Zašto Vinted, Njuškalo i eBay traže OIB, koji podaci idu Poreznoj upravi i što se događa ako ga ne daš.",
 "Da. Kad platforma prema pravilima DAC7 traži tvoj OIB, moraš ga dati, inače može zadržati isplate ili ograničiti prodavački račun. To ne znači da moraš platiti porez.",
 """<h2>Zašto platforma pita?</h2>
<p>Od 2023. online platforme u EU-u moraju prikupljati podatke o prodavačima i jednom godišnje ih dostaviti poreznim tijelima prema direktivi DAC7. Prijavljen si ako na jednoj platformi u godini ostvariš 30 prodaja ili više od 2000 €.</p>
<h2>Koji se podaci dostavljaju?</h2>
<ul><li>Ime, adresa i datum rođenja</li><li>Porezni broj (u Hrvatskoj OIB)</li><li>Broj prodaja i primljeni iznosi nakon naknada platforme</li></ul>
<h2>Što ako ga ne daš?</h2>
<p>Platforma te mora podsjetiti. Ako ne odgovoriš, može zadržati isplate ili ograničiti prodaju. Odbijanje ne zaustavlja prijavu, samo blokira račun.</p>
<h2>Sigurno</h2>
<ul><li>Upiši OIB samo u aplikaciji ili na stranici platforme, nikad preko poveznice iz e-pošte ili SMS-a.</li><li>Provjeri DAC7 provjerom dosežeš li granicu uopće.</li></ul>
<p>Prijava nije porez. Pročitaj <a href="../privatno-ili-djelatnost/">Privatna prodaja ili djelatnost?</a></p>""", [EU_HR, S_EBAY])
M["letter"]["hr"] = A("pismo-porezne-uprave-nakon-dac7", "Pismo Porezne uprave nakon DAC7 prijave: što sada?",
 "Dobio si pismo Porezne uprave nakon prodaje na Vintedu, Njuškalu ili eBayu? Ovako odgovaraš mirno i ispravno.",
 "Ostani miran, ali pismo ne ignoriraj. Porezna uprava obično želi znati sadrže li prijavljene prodaje oporezivi dohodak. Primici od prodaje osobne imovine u Hrvatskoj se ne smatraju dohotkom.",
 """<h2>Zašto ti pišu?</h2>
<p>Svake godine do 31. siječnja platforme prijavljuju tko je prethodne godine kod njih ostvario 30 prodaja ili više od 2000 €. Porezna uprava uspoređuje podatke s tvojom prijavom i može pitati. Pitanje nije kazna.</p>
<h2>Korak po korak</h2>
<ol><li><strong>Zabilježi rok.</strong></li><li><strong>Skupi prodaje</strong> iz aplikacije: što, kada, za koliko.</li><li><strong>Razvrstaj ih:</strong> vlastite rabljene stvari ili roba kupljena za preprodaju?</li><li><strong>Odgovori kratko i iskreno</strong>, npr.: „Radi se o prodaji rabljene odjeće iz mog kućanstva.“</li></ol>
<h2>Pravila u Hrvatskoj</h2>
<p>Primici od otuđenja osobne imovine ne smatraju se dohotkom. Ako se prodaja obavlja kontinuirano, samostalno i s namjerom ostvarivanja dohotka, primici se oporezuju kao dohodak od samostalne djelatnosti.</p>
<p>Pravila svih 27 zemalja EU-a: <a href=\"""" + OVL + """\">pregled (na engleskom)</a>.</p>
<h2>Za iduću godinu</h2>
<p>Vodi jednostavan popis onoga što kupuješ i prodaješ i po kojoj cijeni.</p>""", [HR_SRC, EU_HR])
M["platforms"]["hr"] = A("dac7-vinted-njuskalo-ebay-sto-se-prijavljuje", "DAC7 na Vintedu, Njuškalu i eBayu: što se prijavljuje?",
 "Koje prodaje Vinted, Njuškalo, eBay i Etsy prijavljuju Poreznoj upravi, kako se broje i zašto sami oglasi ne broje.",
 "Prijavljuju se samo završene prodaje plaćene preko platforme. Gotovina pri preuzimanju se ne broji jer je platforma ne vidi. Svaka platforma broji zasebno.",
 """<h2>Što se broji kao prodaja?</h2>
<p>DAC7 broji transakcije: stvarno završene i plaćene prodaje. Broj oglasa nije važan.</p>
<h2>Platforme ukratko</h2>
<ul><li><strong>Vinted:</strong> gotovo sve prodaje idu preko Vinted plaćanja i broje se.</li><li><strong>eBay i Etsy:</strong> same obrađuju plaćanja.</li><li><strong>Njuškalo i drugi oglasnici:</strong> broje se samo prodaje preko njihove usluge plaćanja ili dostave.</li></ul>
<h2>Svaka platforma zasebno</h2>
<p>Granice od 30 prodaja ili više od 2000 € vrijede po platformi. Za porez se ipak računa sav tvoj dohodak.</p>
<h2>Što se prijavljuje?</h2>
<p>Iznosi nakon naknada platforme te ime, adresa, datum rođenja i OIB.</p>""", [EU_HR, S_MOBI])
M["business"]["hr"] = A("privatno-ili-djelatnost", "Privatna prodaja ili djelatnost: gdje je granica?",
 "Kada prodaja na Vintedu ili Njuškalu postaje djelatnost? Glavni kriteriji jednostavno.",
 "Nema fiksnog broja prodaja. Važno je prodaješ li vlastite stvari ili kupuješ da bi preprodavao uz zaradu. Kontinuirana prodaja s namjerom zarade oporezuje se kao samostalna djelatnost.",
 """<h2>Privatno: raščišćavanje</h2>
<p>Prodaja odjeće, namještaja ili igračaka iz vlastitog kućanstva je privatna i ne smatra se dohotkom.</p>
<h2>Djelatnost: kupnja radi preprodaje</h2>
<ul><li>Redovito kupuješ robu da je preprodaš.</li><li>Nudiš mnogo istih ili novih artikala.</li><li>Tvoj profil izgleda kao trgovina.</li></ul>
<p>Elementi samostalnosti i trajnosti s namjerom ostvarivanja dohotka znače djelatnost; tada se plaća porez na dohodak, a mogu nastati i obveze PDV-a.</p>
<h2>Vodi brojke</h2>
<p>Zapisuj nabavnu cijenu, prodajnu cijenu i naknade za svaki artikl – upravo za to služi Reseller Profit &amp; DAC7 Tracker.</p>""", [HR_SRC, EU_HR])

# ---------------- Hungarian
EU_HU = eurlex("HU", "A Tanács (EU) 2021/514 irányelve (DAC7), EUR-Lex")
HU_SRC = ("NAV: A megunt holmik eladása", "https://nav.gov.hu/Elethelyzetek-adozasa/vagyonugyek/A-megunt-holmik-eladasa")
M["tax-id"]["hu"] = A("vinted-adoazonosito-jel", "A Vinted kéri az adóazonosító jeledet: meg kell adnod?",
 "Miért kéri a Vinted, a Jófogás és az eBay az adóazonosító jelet, milyen adatok kerülnek a NAV-hoz, és mi történik, ha nem adod meg.",
 "Igen. Ha egy platform a DAC7 szabályai alapján kéri az adóazonosító jeledet, meg kell adnod, különben visszatarthatja a kifizetéseket vagy korlátozhatja az eladói fiókodat. Ez nem jelenti, hogy adót kell fizetned.",
 """<h2>Miért kérdez a platform?</h2>
<p>2023 óta az uniós online platformoknak a DAC7 irányelv alapján gyűjteniük kell az eladók adatait, és évente egyszer továbbítaniuk az adóhatóságnak. Akkor jelentenek be, ha egy platformon egy év alatt eléred a 30 eladást, vagy 2000 eurónál több bevételed lesz.</p>
<h2>Milyen adatokat továbbítanak?</h2>
<ul><li>Név, cím és születési dátum</li><li>Adóazonosító jel</li><li>Az eladások száma és a kapott összegek a platform díjai után</li></ul>
<h2>Mi történik, ha nem adod meg?</h2>
<p>A platformnak emlékeztetnie kell. Ha nem válaszolsz, visszatarthatja a kifizetéseket vagy korlátozhatja az eladást. Az elutasítás nem állítja meg a bejelentést, csak a fiókot blokkolja.</p>
<h2>Biztonságosan</h2>
<ul><li>A számot csak a platform alkalmazásában vagy weboldalán add meg, soha ne e-mailben vagy SMS-ben kapott linken.</li><li>A DAC7 ellenőrzéssel nézd meg, eléred-e egyáltalán a határt.</li></ul>
<p>A bejelentés nem adófizetés. Olvasd el: <a href="../maganszemely-vagy-vallalkozas/">Magánszemély vagy vállalkozás?</a></p>""", [EU_HU, S_EBAY])
M["letter"]["hu"] = A("level-a-navtol-dac7-utan", "Levél a NAV-tól DAC7 bejelentés után: mi a teendő?",
 "Levelet kaptál a NAV-tól Vinted-, Jófogás- vagy eBay-eladások után? Így válaszolsz nyugodtan és helyesen.",
 "Maradj nyugodt, de ne hagyd figyelmen kívül. A NAV általában azt akarja tudni, van-e adóköteles jövedelem a bejelentett eladásokban. Alkalmi eladásnál évi 600 000 forint bevételig nincs adó és bevallás sem.",
 """<h2>Miért ír a NAV?</h2>
<p>A platformok minden évben január 31-ig jelentik, ki érte el náluk az előző évben a 30 eladást vagy a 2000 eurót. A NAV összeveti ezt a bevallásoddal, és kérdezhet. A kérdés nem bírság.</p>
<h2>Lépésről lépésre</h2>
<ol><li><strong>Jegyezd fel a határidőt.</strong></li><li><strong>Gyűjtsd össze az eladásokat</strong> az alkalmazásból: mit, mikor, mennyiért.</li><li><strong>Válogasd szét:</strong> saját használt holmi vagy továbbeladásra vett áru?</li><li><strong>Válaszolj röviden és őszintén</strong>, pl.: „A háztartásom használt ruháinak eladásáról van szó.”</li></ol>
<h2>A szabályok Magyarországon</h2>
<p>Alkalmi eladásnál évi 600 000 forint bevételig nem kell bevallást készíteni és adót sem kell fizetni. E fölött a jövedelem (bevétel mínusz költségek, például a vételár) 200 000 forintig adómentes, a felette lévő rész után 15% szja-t kell fizetni. A rendszeres, haszonszerzési célú továbbértékesítés gazdasági tevékenység.</p>
<p>Mind a 27 uniós ország szabályai: <a href=\"""" + OVL + """\">áttekintés (angolul)</a>.</p>
<h2>Jövőre</h2>
<p>Vezess egyszerű listát arról, mit veszel és adsz el, és milyen áron.</p>""", [HU_SRC, EU_HU])
M["platforms"]["hu"] = A("dac7-vinted-jofogas-ebay-mit-jelentenek", "DAC7 a Vinteden, a Jófogáson és az eBayen: mit jelentenek?",
 "Mely eladásokat jelenti a Vinted, a Jófogás, az eBay és az Etsy a NAV-nak, hogyan számolják, és miért nem számítanak a hirdetések.",
 "Csak a platformon keresztül kifizetett, lezárt eladásokat jelentik. A személyes átvételkori készpénz nem számít, mert a platform nem látja. Minden platform külön számol.",
 """<h2>Mi számít eladásnak?</h2>
<p>A DAC7 tranzakciókat számol: ténylegesen lezárt és kifizetett eladásokat. A hirdetések száma nem számít.</p>
<h2>A platformok röviden</h2>
<ul><li><strong>Vinted:</strong> szinte minden eladás a Vinted fizetésén megy át, ezért számít.</li><li><strong>eBay és Etsy:</strong> maguk kezelik a fizetést.</li><li><strong>Jófogás és más hirdetési oldalak:</strong> csak a saját fizetési vagy szállítási szolgáltatásukon keresztüli eladások számítanak.</li></ul>
<h2>Minden platform külön</h2>
<p>A 30 eladásos vagy 2000 eurós határ platformonként érvényes. Az adónál viszont a teljes jövedelmed számít.</p>
<h2>Mit jelentenek?</h2>
<p>Az összegeket a díjak után, valamint a nevet, címet, születési dátumot és adóazonosító jelet.</p>""", [EU_HU, S_MOBI])
M["business"]["hu"] = A("maganszemely-vagy-vallalkozas", "Magánszemély vagy vállalkozás: hol a határ?",
 "Mikor válik a Vinted- vagy Jófogás-eladás gazdasági tevékenységgé? A fő szempontok egyszerűen.",
 "Nincs fix eladásszám. Az számít, hogy a saját holmidtól válsz meg, vagy azért veszel, hogy haszonnal továbbadd. Az utóbbi gazdasági tevékenység, adószámmal és számlaadással.",
 """<h2>Magánszemély: lomtalanítás</h2>
<p>A saját háztartásod ruháinak, bútorainak vagy játékainak eladása magáneladás.</p>
<h2>Vállalkozás: vásárlás továbbeladásra</h2>
<ul><li>Rendszeresen veszel árut, hogy továbbadd.</li><li>Sok egyforma vagy új terméket kínálsz.</li><li>A fiókod úgy néz ki, mint egy bolt.</li></ul>
<p>Gazdasági tevékenységnél adószámot kell kérni, számlát kell adni, és a jövedelem után szja és szociális hozzájárulási adó fizetendő; a 200 000 forintos mentesség ilyenkor nem jár.</p>
<h2>Vezesd a számokat</h2>
<p>Jegyezd fel minden tétel vételárát, eladási árát és díjait – erre való a Reseller Profit &amp; DAC7 Tracker.</p>""", [HU_SRC, EU_HU])

# ---------------- Lithuanian
EU_LT = eurlex("LT", "Tarybos direktyva (ES) 2021/514 (DAC7), EUR-Lex")
LT_SRC = ("VMI: Kito neregistruotino turto pardavimo pajamų apmokestinimas", "https://www.vmi.lt/evmi/en/kaip-apmokestinamos-kito-neregistruotino-turto-pardavimo-pajamos-")
M["tax-id"]["lt"] = A("vinted-asmens-kodas", "Vinted prašo tavo asmens kodo: ar turi jį pateikti?",
 "Kodėl Vinted, eBay ir kitos platformos prašo mokesčių mokėtojo kodo, kokie duomenys keliauja į VMI ir kas nutinka, jei jo nepateiki.",
 "Taip. Kai platforma pagal DAC7 taisykles prašo tavo mokesčių mokėtojo kodo, turi jį pateikti, kitaip ji gali sulaikyti išmokas arba apriboti pardavėjo paskyrą. Tai nereiškia, kad turi mokėti mokestį.",
 """<h2>Kodėl platforma klausia?</h2>
<p>Nuo 2023 m. ES internetinės platformos pagal DAC7 direktyvą renka pardavėjų duomenis ir kartą per metus teikia juos mokesčių administratoriui. Apie tave pranešama, jei vienoje platformoje per metus pasieki 30 pardavimų arba gauni daugiau nei 2000 €.</p>
<h2>Kokie duomenys teikiami?</h2>
<ul><li>Vardas, pavardė, adresas ir gimimo data</li><li>Mokesčių mokėtojo kodas (Lietuvoje – asmens kodas)</li><li>Pardavimų skaičius ir gautos sumos po platformos mokesčių</li></ul>
<h2>Kas, jei nepateiki?</h2>
<p>Platforma turi tau priminti. Jei neatsakai, ji gali sulaikyti išmokas arba apriboti pardavimą. Atsisakymas nesustabdo pranešimo, tik užblokuoja paskyrą.</p>
<h2>Saugiai</h2>
<ul><li>Kodą įvesk tik platformos programėlėje ar svetainėje, niekada per nuorodą iš el. laiško ar SMS.</li><li>Su DAC7 patikra pasitikrink, ar išvis pasieksi ribą.</li></ul>
<p>Pranešimas nėra mokestis. Skaityk <a href="../privatus-ar-veikla/">Privatus pardavimas ar veikla?</a></p>""", [EU_LT, S_EBAY])
M["letter"]["lt"] = A("laiskas-is-vmi-po-dac7", "Laiškas iš VMI po DAC7 pranešimo: ką daryti?",
 "Gavai laišką iš VMI po pardavimų Vinted ar eBay? Taip atsakysi ramiai ir teisingai.",
 "Išlik ramus, bet laiško neignoruok. VMI dažniausiai nori žinoti, ar praneštuose pardavimuose yra apmokestinamų pajamų. Neregistruotino turto pardavimo pajamos iki 2500 € per metus Lietuvoje neapmokestinamos.",
 """<h2>Kodėl tau rašo?</h2>
<p>Kasmet iki sausio 31 d. platformos praneša, kas praėjusiais metais jose pasiekė 30 pardavimų arba daugiau nei 2000 €. VMI palygina duomenis su tavo deklaracija ir gali paklausti. Klausimas nėra bauda.</p>
<h2>Žingsnis po žingsnio</h2>
<ol><li><strong>Užsirašyk terminą.</strong></li><li><strong>Surink pardavimus</strong> iš programėlės: ką, kada, už kiek.</li><li><strong>Suskirstyk:</strong> savi naudoti daiktai ar prekės, pirktos perpardavimui?</li><li><strong>Atsakyk trumpai ir sąžiningai</strong>, pvz.: „Tai mano namų ūkio dėvėtų drabužių pardavimas.“</li></ol>
<h2>Taisyklės Lietuvoje</h2>
<p>Jei neregistruotino turto (pvz., drabužių, baldų, buitinės technikos) pardavimo pajamos per metus neviršija 2500 €, gyventojų pajamų mokesčio mokėti nereikia. Viršijus: 15% nuo sumos, gautos atėmus įsigijimo kainą, būtinas išlaidas ir 2500 €. Ši tvarka netaikoma individualiai veiklai.</p>
<p>Visų 27 ES šalių taisyklės: <a href=\"""" + OVL + """\">apžvalga (anglų kalba)</a>.</p>
<h2>Kitiems metams</h2>
<p>Vesk paprastą sąrašą, ką perki ir parduodi ir už kiek.</p>""", [LT_SRC, EU_LT])
M["platforms"]["lt"] = A("dac7-vinted-ebay-kas-pranesama", "DAC7 Vinted ir eBay: kas pranešama?",
 "Kokius pardavimus Vinted, eBay ir Etsy praneša VMI, kaip jie skaičiuojami ir kodėl vien skelbimai nesiskaičiuoja.",
 "Pranešama tik apie užbaigtus pardavimus, apmokėtus per platformą. Grynieji atsiimant nesiskaičiuoja, nes platforma jų nemato. Kiekviena platforma skaičiuoja atskirai.",
 """<h2>Kas laikoma pardavimu?</h2>
<p>DAC7 skaičiuoja sandorius: realiai užbaigtus ir apmokėtus pardavimus. Skelbimų skaičius nesvarbus.</p>
<h2>Platformos trumpai</h2>
<ul><li><strong>Vinted:</strong> beveik visi pardavimai eina per Vinted mokėjimą ir skaičiuojami.</li><li><strong>eBay ir Etsy:</strong> mokėjimus tvarko pačios.</li><li><strong>Skelbimų svetainės:</strong> skaičiuojami tik pardavimai per jų mokėjimo ar pristatymo paslaugą.</li></ul>
<h2>Kiekviena platforma atskirai</h2>
<p>Ribos – 30 pardavimų arba daugiau nei 2000 € – taikomos kiekvienai platformai. Mokesčiams vis tiek svarbios visos tavo pajamos.</p>
<h2>Kas pranešama?</h2>
<p>Sumos po platformos mokesčių, vardas, adresas, gimimo data ir asmens kodas.</p>""", [EU_LT, S_MOBI])
M["business"]["lt"] = A("privatus-ar-veikla", "Privatus pardavimas ar individuali veikla: kur riba?",
 "Kada pardavimas Vinted tampa individualia veikla? Pagrindiniai kriterijai paprastai.",
 "Fiksuoto pardavimų skaičiaus nėra. Svarbu, ar atsikratai savų daiktų, ar perki, kad parduotum su pelnu. Antruoju atveju tai gali būti individuali veikla, kuriai netaikoma 2500 € lengvata.",
 """<h2>Privatus: tvarkymasis</h2>
<p>Drabužių, baldų ar žaislų iš savo namų ūkio pardavimas yra privatus pardavimas.</p>
<h2>Veikla: pirkimas perpardavimui</h2>
<ul><li>Reguliariai perki prekes, kad jas perparduotum.</li><li>Siūlai daug vienodų ar naujų prekių.</li><li>Tavo paskyra atrodo kaip parduotuvė.</li></ul>
<p>Individualios veiklos pajamos apmokestinamos kitaip nei privatus turto pardavimas, ir 2500 € neapmokestinamoji suma joms netaikoma.</p>
<h2>Vesk apskaitą</h2>
<p>Užsirašyk kiekvienos prekės pirkimo kainą, pardavimo kainą ir mokesčius – tam ir skirtas Reseller Profit &amp; DAC7 Tracker.</p>""", [LT_SRC, EU_LT])

# ---------------- Latvian
EU_LV = eurlex("LV", "Padomes direktīva (ES) 2021/514 (DAC7), EUR-Lex")
LV_SRC = ("LV portāls: Ienākums no personiskās mantas pārdošanas nav apliekams ar nodokli (2025)", "https://lvportals.lv/e-konsultacijas/36059-ienakums-no-personiskas-mantas-pardosanas-nav-apliekams-ar-nodokli-2025")
M["tax-id"]["lv"] = A("vinted-personas-kods", "Vinted prasa tavu personas kodu: vai tas jādod?",
 "Kāpēc Vinted, eBay un citas platformas prasa nodokļu maksātāja numuru, kādi dati nonāk VID un kas notiek, ja to nedod.",
 "Jā. Ja platforma saskaņā ar DAC7 noteikumiem prasa tavu nodokļu maksātāja numuru, tas jādod, citādi tā var aizturēt izmaksas vai ierobežot pārdevēja kontu. Tas nenozīmē, ka jāmaksā nodoklis.",
 """<h2>Kāpēc platforma jautā?</h2>
<p>Kopš 2023. gada ES tiešsaistes platformām saskaņā ar DAC7 direktīvu jāvāc pārdevēju dati un reizi gadā jānodod nodokļu iestādēm. Par tevi ziņo, ja vienā platformā gadā sasniedz 30 pārdošanas vai saņem vairāk nekā 2000 €.</p>
<h2>Kādi dati tiek nodoti?</h2>
<ul><li>Vārds, uzvārds, adrese un dzimšanas datums</li><li>Nodokļu maksātāja numurs (Latvijā personas kods)</li><li>Pārdošanu skaits un saņemtās summas pēc platformas komisijām</li></ul>
<h2>Kas notiek, ja to nedod?</h2>
<p>Platformai tev jāatgādina. Ja neatbildi, tā var aizturēt izmaksas vai ierobežot pārdošanu. Atteikums neaptur ziņošanu, tikai bloķē kontu.</p>
<h2>Droši</h2>
<ul><li>Ievadi kodu tikai platformas lietotnē vai vietnē, nekad caur saiti no e-pasta vai īsziņas.</li><li>Ar DAC7 pārbaudi noskaidro, vai vispār sasniegsi robežu.</li></ul>
<p>Ziņošana nav nodoklis. Lasi <a href="../privati-vai-darbiba/">Privāta pārdošana vai saimnieciskā darbība?</a></p>""", [EU_LV, S_EBAY])
M["letter"]["lv"] = A("vestule-no-vid-pec-dac7", "Vēstule no VID pēc DAC7 ziņojuma: ko darīt?",
 "Saņēmi vēstuli no VID pēc pārdošanas Vinted vai eBay? Tā atbildēsi mierīgi un pareizi.",
 "Saglabā mieru, bet neignorē vēstuli. VID parasti vēlas zināt, vai ziņotajās pārdošanās ir apliekams ienākums. Ienākums no personiskās lietošanas kustamās mantas pārdošanas Latvijā netiek aplikts ar nodokli.",
 """<h2>Kāpēc VID raksta?</h2>
<p>Katru gadu līdz 31. janvārim platformas ziņo, kurš iepriekšējā gadā pie tām sasniedza 30 pārdošanas vai vairāk nekā 2000 €. VID salīdzina datus ar tavu deklarāciju un var jautāt. Jautājums nav sods.</p>
<h2>Soli pa solim</h2>
<ol><li><strong>Pieraksti termiņu.</strong></li><li><strong>Savāc pārdošanas</strong> no lietotnes: ko, kad, par cik.</li><li><strong>Sašķiro:</strong> paša lietotas mantas vai preces, pirktas tālākpārdošanai?</li><li><strong>Atbildi īsi un godīgi</strong>, piem.: „Tā ir manas mājsaimniecības lietotu apģērbu pārdošana.“</li></ol>
<h2>Noteikumi Latvijā</h2>
<p>Ienākums no fiziskās personas personiskai lietošanai paredzētas kustamās mantas, piemēram, mēbeļu un apģērbu, atsavināšanas netiek aplikts ar iedzīvotāju ienākuma nodokli. Saimnieciskās darbības ienākumi tiek aplikti atsevišķi.</p>
<p>Visu 27 ES valstu noteikumi: <a href=\"""" + OVL + """\">pārskats (angļu valodā)</a>.</p>
<h2>Nākamajam gadam</h2>
<p>Vadi vienkāršu sarakstu, ko pērc un pārdod un par kādu cenu.</p>""", [LV_SRC, EU_LV])
M["platforms"]["lv"] = A("dac7-vinted-ebay-ko-zino", "DAC7 Vinted un eBay: par ko ziņo?",
 "Par kādām pārdošanām Vinted, eBay un Etsy ziņo VID, kā tās skaita un kāpēc sludinājumi vien neskaitās.",
 "Ziņo tikai par pabeigtām pārdošanām, kas apmaksātas caur platformu. Skaidra nauda saņemšanas brīdī neskaitās, jo platforma to neredz. Katra platforma skaita atsevišķi.",
 """<h2>Kas skaitās pārdošana?</h2>
<p>DAC7 skaita darījumus: reāli pabeigtas un apmaksātas pārdošanas. Sludinājumu skaitam nav nozīmes.</p>
<h2>Platformas īsumā</h2>
<ul><li><strong>Vinted:</strong> gandrīz visas pārdošanas notiek caur Vinted maksājumu un skaitās.</li><li><strong>eBay un Etsy:</strong> maksājumus apstrādā paši.</li><li><strong>Sludinājumu vietnes:</strong> skaitās tikai pārdošanas caur to maksājumu vai piegādes pakalpojumu.</li></ul>
<h2>Katra platforma atsevišķi</h2>
<p>Robežas – 30 pārdošanas vai vairāk nekā 2000 € – attiecas uz katru platformu. Nodokļiem tomēr skaitās visi tavi ienākumi.</p>
<h2>Par ko ziņo?</h2>
<p>Summas pēc platformas komisijām, vārds, adrese, dzimšanas datums un personas kods.</p>""", [EU_LV, S_MOBI])
M["business"]["lv"] = A("privati-vai-darbiba", "Privāta pārdošana vai saimnieciskā darbība: kur ir robeža?",
 "Kad pārdošana Vinted kļūst par saimniecisko darbību? Galvenie kritēriji vienkārši.",
 "Fiksēta pārdošanu skaita nav. Svarīgi, vai atbrīvojies no savām mantām vai pērc, lai pārdotu ar peļņu. Otrajā gadījumā tā var būt saimnieciskā darbība, kuras ienākumi tiek aplikti ar nodokli.",
 """<h2>Privāti: atbrīvošanās no mantām</h2>
<p>Savas mājsaimniecības apģērbu, mēbeļu vai rotaļlietu pārdošana ir privāta un netiek aplikta ar nodokli.</p>
<h2>Darbība: pirkšana tālākpārdošanai</h2>
<ul><li>Regulāri pērc preces, lai tās pārdotu tālāk.</li><li>Piedāvā daudz vienādu vai jaunu preču.</li><li>Tavs profils izskatās pēc veikala.</li></ul>
<h2>Uzskaiti skaitļus</h2>
<p>Pieraksti katras preces iepirkuma cenu, pārdošanas cenu un komisijas – tieši tam ir Reseller Profit &amp; DAC7 Tracker.</p>""", [LV_SRC, EU_LV])
