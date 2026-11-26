# Articles: pt, ro, sk, sl, sv
from articles_more import eurlex, S_EBAY, S_MOBI
from articles_b1 import A, OV

G = {
 "pt": {"dir": "guias", "title": "Guias", "intro": "Respostas às perguntas mais frequentes sobre a DAC7, a Vinted e as Finanças.",
        "updated": "Atualizado: 26 de novembro de 2026", "read": "Ler mais", "back": "Voltar ao verificador DAC7",
        "cta_title": "Quão perto estás do limite?", "cta_text": "Verifica cada plataforma num minuto com o verificador DAC7 gratuito.", "cta_btn": "Abrir o verificador DAC7",
        "track": "Ou acompanha o ano inteiro o lucro e o estado DAC7 com o", "track_link": "Reseller Profit &amp; DAC7 Tracker (em inglês)",
        "sources": "Fontes", "disclaimer": "Este artigo é informação geral e não aconselhamento fiscal ou jurídico."},
 "ro": {"dir": "ghiduri", "title": "Ghiduri", "intro": "Răspunsuri la cele mai frecvente întrebări despre DAC7, Vinted și ANAF.",
        "updated": "Actualizat: 26 noiembrie 2026", "read": "Citește", "back": "Înapoi la verificarea DAC7",
        "cta_title": "Cât de aproape ești de limită?", "cta_text": "Verifică fiecare platformă într-un minut cu verificarea DAC7 gratuită.", "cta_btn": "Deschide verificarea DAC7",
        "track": "Sau urmărește tot anul profitul și starea DAC7 cu", "track_link": "Reseller Profit &amp; DAC7 Tracker (în engleză)",
        "sources": "Surse", "disclaimer": "Acest articol este o informare generală, nu consultanță fiscală sau juridică."},
 "sk": {"dir": "clanky", "title": "Články", "intro": "Odpovede na najčastejšie otázky o DAC7, Vinted a finančnej správe.",
        "updated": "Aktualizované: 26. novembra 2026", "read": "Čítať ďalej", "back": "Späť na kontrolu DAC7",
        "cta_title": "Ako blízko si limitu?", "cta_text": "Skontroluj každú platformu za minútu v bezplatnej kontrole DAC7.", "cta_btn": "Otvoriť kontrolu DAC7",
        "track": "Alebo sleduj celý rok zisk a stav DAC7 v", "track_link": "Reseller Profit &amp; DAC7 Tracker (v angličtine)",
        "sources": "Zdroje", "disclaimer": "Tento článok je všeobecná informácia, nie daňové ani právne poradenstvo."},
 "sl": {"dir": "vodici", "title": "Vodiči", "intro": "Odgovori na najpogostejša vprašanja o DAC7, Vintedu in FURS.",
        "updated": "Posodobljeno: 26. novembra 2026", "read": "Preberi", "back": "Nazaj na preverjanje DAC7",
        "cta_title": "Kako blizu meje si?", "cta_text": "Preveri vsako platformo v minuti z brezplačnim preverjanjem DAC7.", "cta_btn": "Odpri preverjanje DAC7",
        "track": "Ali spremljaj vse leto dobiček in stanje DAC7 z", "track_link": "Reseller Profit &amp; DAC7 Tracker (v angleščini)",
        "sources": "Viri", "disclaimer": "Ta članek je splošna informacija, ne davčno ali pravno svetovanje."},
 "sv": {"dir": "guider", "title": "Guider", "intro": "Svar på de vanligaste frågorna om DAC7, Vinted och Skatteverket.",
        "updated": "Uppdaterad: 26 november 2026", "read": "Läs mer", "back": "Tillbaka till DAC7-kollen",
        "cta_title": "Hur nära gränsen är du?", "cta_text": "Kolla varje plattform på en minut med den kostnadsfria DAC7-kollen.", "cta_btn": "Öppna DAC7-kollen",
        "track": "Eller håll koll på vinst och DAC7-status hela året med", "track_link": "Reseller Profit &amp; DAC7 Tracker (på engelska)",
        "sources": "Källor", "disclaimer": "Den här artikeln är allmän information och inte skatte- eller juridisk rådgivning."},
}

M = {"tax-id": {}, "letter": {}, "platforms": {}, "business": {}}

# ---------------- Portuguese
EU_PT = eurlex("PT", "Diretiva (UE) 2021/514 do Conselho (DAC7), EUR-Lex")
PT_SRC = ("DECO PROteste: Vendas em segunda mão têm de ser declaradas no IRS?", "https://www.deco.proteste.pt/dinheiro/impostos/dicas/vendas-segunda-mao-tem-ser-declaradas-irs")
M["tax-id"]["pt"] = A("vinted-nif", "A Vinted pede o teu NIF: tens de o dar?",
 "Porque é que a Vinted, a OLX e o eBay pedem o NIF, que dados vão para as Finanças e o que acontece se não o deres.",
 "Sim. Quando uma plataforma pede o teu NIF ao abrigo da DAC7, tens de o fornecer; caso contrário pode suspender pagamentos ou limitar a tua conta de vendedor. Isso não significa que tenhas de pagar impostos.",
 """<h2>Porque é que a plataforma pede?</h2>
<p>Desde 2023, as plataformas online da UE recolhem dados dos vendedores e comunicam-nos uma vez por ano às autoridades fiscais, ao abrigo da diretiva DAC7. És comunicado se numa plataforma chegares a 30 vendas ou mais de 2000 € num ano civil.</p>
<h2>Que dados são comunicados?</h2>
<ul><li>Nome, morada e data de nascimento</li><li>O teu número de identificação fiscal (NIF)</li><li>O número de vendas e os valores recebidos após as comissões da plataforma</li></ul>
<h2>E se não o deres?</h2>
<p>A plataforma tem de te lembrar. Se não responderes, não podes continuar a vender e os pagamentos pendentes ficam suspensos até regularizares. Recusar não impede a comunicação.</p>
<h2>Com segurança</h2>
<ul><li>Introduz o NIF só na app ou no site da plataforma, nunca através de um link recebido por email ou SMS.</li><li>Verifica com o verificador DAC7 se chegas sequer ao limite.</li></ul>
<p>A comunicação não é um imposto. Lê <a href="../particular-ou-atividade/">Particular ou atividade comercial?</a></p>""", [PT_SRC, EU_PT])
M["letter"]["pt"] = A("carta-das-financas-apos-dac7", "Uma carta das Finanças após a comunicação DAC7: e agora?",
 "Recebeste uma carta das Finanças depois de vender na Vinted, na OLX ou no eBay? Eis como responder com calma e corretamente.",
 "Mantém a calma, mas não ignores. As Finanças querem normalmente saber se as vendas comunicadas incluem rendimentos tributáveis. As vendas de bens usados entre particulares não estão, por agora, sujeitas a IRS.",
 """<h2>Porque te escrevem?</h2>
<p>Todos os anos, até 31 de janeiro, as plataformas comunicam quem chegou a 30 vendas ou mais de 2000 € nelas no ano anterior. As Finanças cruzam os dados com a tua declaração e podem fazer perguntas. Uma pergunta não é uma coima.</p>
<h2>Passo a passo</h2>
<ol><li><strong>Anota o prazo.</strong></li><li><strong>Reúne as vendas</strong> na app: o quê, quando, por quanto.</li><li><strong>Separa-as:</strong> coisas tuas usadas ou artigos comprados para revender?</li><li><strong>Responde de forma breve e honesta</strong>, por exemplo: «Trata-se da venda de roupa usada do meu agregado familiar.»</li></ol>
<h2>As regras em Portugal</h2>
<p>As vendas online de bens usados entre particulares não estão, por agora, sujeitas a IRS nem a outro imposto. Quem vende de forma profissional, comprando para revender, exerce uma atividade e é tributado como tal.</p>
<p>As regras dos 27 países da UE: <a href=\"""" + OV + """\">resumo (em inglês)</a>.</p>
<h2>Para o próximo ano</h2>
<p>Mantém uma lista simples do que compras e vendes e a que preço.</p>""", [PT_SRC, EU_PT])
M["platforms"]["pt"] = A("dac7-vinted-olx-ebay-o-que-e-comunicado", "DAC7 na Vinted, OLX e eBay: o que é comunicado?",
 "Que vendas a Vinted, a OLX, o eBay e o Etsy comunicam às Finanças, como são contadas e porque é que os anúncios sozinhos não contam.",
 "Só são comunicadas vendas concluídas e pagas através da plataforma. Pagamentos em dinheiro na entrega não contam, porque a plataforma não os vê. Cada plataforma conta à parte.",
 """<h2>O que conta como venda?</h2>
<p>A DAC7 conta transações: vendas efetivamente concluídas e pagas. O número de anúncios não interessa.</p>
<h2>As plataformas em resumo</h2>
<ul><li><strong>Vinted:</strong> quase todas as vendas passam pelo pagamento da Vinted e contam.</li><li><strong>eBay e Etsy:</strong> tratam eles dos pagamentos.</li><li><strong>OLX e outros sites de anúncios:</strong> só contam vendas feitas através do seu serviço de pagamento ou envio.</li></ul>
<h2>Cada plataforma à parte</h2>
<p>Os limites de 30 vendas ou mais de 2000 € aplicam-se por plataforma. Para os impostos conta todo o teu rendimento.</p>
<h2>O que é comunicado?</h2>
<p>Os valores após comissões, o nome, a morada, a data de nascimento e o NIF.</p>""", [EU_PT, S_MOBI])
M["business"]["pt"] = A("particular-ou-atividade", "Particular ou atividade comercial: onde fica a linha?",
 "Quando é que vender na Vinted ou na OLX passa a ser uma atividade comercial? Os critérios principais de forma simples.",
 "Não há um número fixo de vendas. O que conta é se estás a desfazer-te das tuas coisas ou a comprar para revender com lucro. No segundo caso, já é uma atividade e é tributada como tal.",
 """<h2>Particular: arrumar a casa</h2>
<p>Vender roupa, móveis ou brinquedos da tua casa é venda entre particulares e, por agora, não está sujeita a IRS.</p>
<h2>Atividade: comprar para revender</h2>
<ul><li>Compras regularmente artigos para os revender.</li><li>Ofereces muitos artigos iguais ou novos.</li><li>A tua conta parece uma loja.</li></ul>
<p>Nesse caso tens de abrir atividade nas Finanças e declarar os rendimentos; pode também haver IVA.</p>
<h2>Faz contas</h2>
<p>Regista o preço de compra, o preço de venda e as comissões de cada artigo – é para isso que serve o Reseller Profit &amp; DAC7 Tracker.</p>""", [PT_SRC, EU_PT])

# ---------------- Romanian
EU_RO = eurlex("RO", "Directiva (UE) 2021/514 a Consiliului (DAC7), EUR-Lex")
RO_SRC = ("ANAF Cluj: Comerțul cu bunuri second-hand (iulie 2026)", "https://static.anaf.ro/static/10/Cluj/cj_second_hand_29iul2026.pdf")
M["tax-id"]["ro"] = A("vinted-cnp", "Vinted îți cere CNP-ul: trebuie să-l dai?",
 "De ce Vinted, OLX și eBay cer codul fiscal, ce date ajung la ANAF și ce se întâmplă dacă nu-l dai.",
 "Da. Când o platformă îți cere codul de identificare fiscală conform DAC7, trebuie să-l dai, altfel poate reține plățile sau îți poate limita contul de vânzător. Asta nu înseamnă că datorezi impozit.",
 """<h2>De ce întreabă platforma?</h2>
<p>Din 2023, platformele online din UE colectează datele vânzătorilor și le transmit o dată pe an autorităților fiscale, conform directivei DAC7. Ești raportat dacă pe o platformă ajungi la 30 de vânzări sau peste 2.000 € într-un an.</p>
<h2>Ce date se transmit?</h2>
<ul><li>Nume, adresă și data nașterii</li><li>Codul de identificare fiscală (în România, CNP-ul)</li><li>Numărul de vânzări și sumele încasate după comisioanele platformei</li></ul>
<h2>Ce se întâmplă dacă nu-l dai?</h2>
<p>Platforma trebuie să-ți reamintească. Dacă nu răspunzi, poate reține plățile sau limita vânzările. Refuzul nu oprește raportarea, doar blochează contul.</p>
<h2>În siguranță</h2>
<ul><li>Introdu CNP-ul doar în aplicația sau pe site-ul platformei, niciodată printr-un link primit pe email sau SMS.</li><li>Verifică cu verificarea DAC7 dacă ajungi la limită.</li></ul>
<p>Raportarea nu e impozit. Citește <a href="../persoana-fizica-sau-activitate/">Persoană fizică sau activitate economică?</a></p>""", [EU_RO, S_EBAY])
M["letter"]["ro"] = A("scrisoare-anaf-dupa-dac7", "Scrisoare de la ANAF după raportarea DAC7: ce faci?",
 "Ai primit o scrisoare de la ANAF după vânzări pe Vinted, OLX sau eBay? Iată cum răspunzi calm și corect.",
 "Păstrează-ți calmul, dar nu o ignora. ANAF vrea de obicei să știe dacă vânzările raportate conțin venituri impozabile. Veniturile din vânzarea bunurilor personale nu sunt impozabile în România.",
 """<h2>De ce îți scrie ANAF?</h2>
<p>În fiecare an, până la 31 ianuarie, platformele raportează cine a ajuns la 30 de vânzări sau peste 2.000 € la ele în anul anterior. ANAF compară datele și poate pune întrebări. O întrebare nu este o amendă.</p>
<h2>Pas cu pas</h2>
<ol><li><strong>Notează termenul.</strong></li><li><strong>Strânge vânzările</strong> din aplicație: ce, când, cu cât.</li><li><strong>Împarte-le:</strong> lucruri personale folosite sau produse cumpărate pentru revânzare?</li><li><strong>Răspunde scurt și sincer</strong>, de exemplu: „Este vorba de vânzarea hainelor folosite din gospodăria mea.”</li></ol>
<h2>Regulile în România</h2>
<p>Veniturile din vânzarea bunurilor personale nu sunt venituri impozabile. Cumpărarea și vânzarea continuă de bunuri second-hand este însă activitate economică, care trebuie înregistrată; activitatea neînregistrată se sancționează cu amendă.</p>
<p>Regulile din toate cele 27 de țări UE: <a href=\"""" + OV + """\">prezentare (în engleză)</a>.</p>
<h2>Pentru anul viitor</h2>
<p>Ține o listă simplă cu ce cumperi și vinzi și la ce preț.</p>""", [RO_SRC, EU_RO])
M["platforms"]["ro"] = A("dac7-vinted-olx-ebay-ce-se-raporteaza", "DAC7 pe Vinted, OLX și eBay: ce se raportează?",
 "Ce vânzări raportează Vinted, OLX, eBay și Etsy la ANAF, cum se numără și de ce anunțurile singure nu contează.",
 "Se raportează doar vânzările finalizate și plătite prin platformă. Plata cash la predare nu contează, pentru că platforma nu o vede. Fiecare platformă numără separat.",
 """<h2>Ce contează ca vânzare?</h2>
<p>DAC7 numără tranzacții: vânzări finalizate și plătite. Numărul de anunțuri nu contează.</p>
<h2>Platformele pe scurt</h2>
<ul><li><strong>Vinted:</strong> aproape toate vânzările trec prin plata Vinted și contează.</li><li><strong>eBay și Etsy:</strong> gestionează singure plățile.</li><li><strong>OLX și alte site-uri de anunțuri:</strong> contează doar vânzările prin serviciul lor de plată sau livrare.</li></ul>
<h2>Fiecare platformă separat</h2>
<p>Limitele de 30 de vânzări sau peste 2.000 € se aplică pe platformă. Pentru impozite contează însă toate veniturile tale.</p>
<h2>Ce se raportează?</h2>
<p>Sumele după comisioane, numele, adresa, data nașterii și CNP-ul.</p>""", [EU_RO, S_MOBI])
M["business"]["ro"] = A("persoana-fizica-sau-activitate", "Persoană fizică sau activitate economică: unde e limita?",
 "Când devine vânzarea pe Vinted sau OLX activitate economică? Criteriile principale, simplu.",
 "Nu există un număr fix de vânzări. Contează dacă scapi de lucrurile tale sau cumperi ca să revinzi cu profit. Cumpărarea și vânzarea continuă este activitate economică și trebuie înregistrată.",
 """<h2>Persoană fizică: faci curat</h2>
<p>Vânzarea hainelor, mobilei sau jucăriilor din propria gospodărie nu este venit impozabil.</p>
<h2>Activitate: cumperi ca să revinzi</h2>
<ul><li>Cumperi regulat produse ca să le revinzi.</li><li>Oferi multe articole identice sau noi.</li><li>Contul tău arată ca un magazin.</li></ul>
<p>Activitatea desfășurată independent și continuu este activitate economică; fără înregistrare, se pot aplica amenzi și confiscări.</p>
<h2>Ține socoteala</h2>
<p>Notează prețul de cumpărare, prețul de vânzare și comisioanele pentru fiecare articol – exact pentru asta e Reseller Profit &amp; DAC7 Tracker.</p>""", [RO_SRC, EU_RO])

# ---------------- Slovak
EU_SK = eurlex("SK", "Smernica Rady (EÚ) 2021/514 (DAC7), EUR-Lex")
SK_SRC = ("Finančná správa: Príjmy fyzickej osoby z predaja hnuteľnej veci", "https://podpora.financnasprava.sk/531745-Príjmy-fyzickej-osoby-z-predaja-hnuteľnej-veci-")
M["tax-id"]["sk"] = A("vinted-danove-identifikacne-cislo", "Vinted chce tvoje daňové číslo: musíš ho zadať?",
 "Prečo Vinted, Allegro a eBay chcú daňové identifikačné číslo, aké údaje idú finančnej správe a čo sa stane, ak ho nezadáš.",
 "Áno. Keď platforma podľa pravidiel DAC7 žiada tvoje daňové číslo, musíš ho zadať, inak môže zadržať výplaty alebo obmedziť tvoj predajný účet. Neznamená to, že platíš daň.",
 """<h2>Prečo sa platforma pýta?</h2>
<p>Od roku 2023 musia online platformy v EÚ zbierať údaje o predajcoch a raz ročne ich odovzdávať daňovým úradom podľa smernice DAC7. Nahlásený budeš, ak na jednej platforme za rok dosiahneš 30 predajov alebo utŕžiš viac ako 2 000 €.</p>
<h2>Aké údaje sa odovzdávajú?</h2>
<ul><li>Meno, adresa a dátum narodenia</li><li>Daňové identifikačné číslo (u fyzických osôb na Slovensku spravidla rodné číslo)</li><li>Počet predajov a prijaté sumy po odpočítaní poplatkov platformy</li></ul>
<h2>Čo ak ho nezadáš?</h2>
<p>Platforma ťa musí upozorniť. Ak nereaguješ, môže zadržať výplaty alebo obmedziť predaj. Odmietnutie nahlásenie nezastaví, len zablokuje účet.</p>
<h2>Bezpečne</h2>
<ul><li>Číslo zadávaj len v aplikácii alebo na webe platformy, nikdy cez odkaz z e-mailu či SMS.</li><li>Kontrolou DAC7 si over, či limit vôbec dosiahneš.</li></ul>
<p>Nahlásenie nie je daň. Pozri <a href="../sukromne-alebo-podnikanie/">Súkromný predaj, alebo podnikanie?</a></p>""", [EU_SK, S_EBAY])
M["letter"]["sk"] = A("list-z-financnej-spravy-po-dac7", "List z finančnej správy po nahlásení DAC7: čo robiť?",
 "Dostal si list z finančnej správy po predajoch na Vinted, Allegro alebo eBay? Takto odpovieš pokojne a správne.",
 "Zachovaj pokoj, ale list neignoruj. Úrad zvyčajne chce vedieť, či nahlásené predaje obsahujú zdaniteľný príjem. Príjem z predaja hnuteľnej veci, ktorá nebola v obchodnom majetku, je na Slovensku od dane oslobodený v plnej výške.",
 """<h2>Prečo ti úrad píše?</h2>
<p>Každý rok do 31. januára platformy hlásia, kto u nich v predchádzajúcom roku dosiahol 30 predajov alebo viac ako 2 000 €. Úrad údaje porovná s tvojím priznaním a môže sa opýtať. Otázka nie je pokuta.</p>
<h2>Krok za krokom</h2>
<ol><li><strong>Poznač si lehotu.</strong></li><li><strong>Zhromaždi predaje</strong> z aplikácie: čo, kedy, za koľko.</li><li><strong>Roztrieď ich:</strong> vlastné použité veci alebo tovar kúpený na ďalší predaj?</li><li><strong>Odpovedz stručne a pravdivo</strong>, napr.: „Ide o predaj použitého oblečenia z mojej domácnosti.“</li></ol>
<h2>Pravidlá na Slovensku</h2>
<p>Príjem z predaja hnuteľnej veci, ktorá nebola zaradená v obchodnom majetku, je oslobodený v plnej výške bez ohľadu na dĺžku vlastníctva a do priznania sa neuvádza. Veci z obchodného majetku sa zdaňujú, ak sa predajú do piatich rokov od vyradenia.</p>
<p>Pravidlá všetkých 27 krajín EÚ: <a href=\"""" + OV + """\">prehľad (v angličtine)</a>.</p>
<h2>Na budúci rok</h2>
<p>Veď si jednoduchý zoznam, čo kupuješ a predávaš a za koľko.</p>""", [SK_SRC, EU_SK])
M["platforms"]["sk"] = A("dac7-vinted-allegro-ebay-co-sa-hlasi", "DAC7 na Vinted, Allegro a eBay: čo sa hlási?",
 "Ktoré predaje Vinted, Allegro, eBay a Etsy hlásia finančnej správe, ako sa počítajú a prečo samotné inzeráty nestačia.",
 "Hlásia sa len dokončené predaje zaplatené cez platformu. Hotovosť pri prevzatí sa nepočíta, lebo ju platforma nevidí. Každá platforma počíta zvlášť.",
 """<h2>Čo je predaj?</h2>
<p>DAC7 počíta transakcie: skutočne dokončené a zaplatené predaje. Počet inzerátov nehrá rolu.</p>
<h2>Platformy v skratke</h2>
<ul><li><strong>Vinted:</strong> takmer všetky predaje idú cez platby Vinted, takže sa počítajú.</li><li><strong>Allegro, eBay a Etsy:</strong> spracúvajú platby samy.</li><li><strong>Inzertné weby</strong> ako Bazoš: počítajú sa len predaje cez ich vlastnú platobnú alebo doručovaciu službu.</li></ul>
<h2>Každá platforma zvlášť</h2>
<p>Limity 30 predajov alebo viac ako 2 000 € platia pre každú platformu. Pri daniach sa však počíta celý tvoj príjem.</p>
<h2>Čo sa hlási?</h2>
<p>Sumy po poplatkoch, meno, adresa, dátum narodenia a daňové číslo.</p>""", [EU_SK, S_MOBI])
M["business"]["sk"] = A("sukromne-alebo-podnikanie", "Súkromný predaj, alebo podnikanie: kde je hranica?",
 "Kedy sa predaj na Vinted alebo Bazoši stáva podnikaním? Hlavné kritériá jednoducho.",
 "Pevný počet predajov neexistuje. Rozhoduje, či sa zbavuješ vlastných vecí, alebo nakupuješ, aby si predával so ziskom. V druhom prípade ide o podnikanie a príjem sa daní.",
 """<h2>Súkromne: upratovanie</h2>
<p>Predaj oblečenia, nábytku alebo hračiek z vlastnej domácnosti je súkromný a na Slovensku oslobodený.</p>
<h2>Podnikanie: nákup na ďalší predaj</h2>
<ul><li>Pravidelne nakupuješ tovar na ďalší predaj.</li><li>Ponúkaš veľa rovnakých alebo nových vecí.</li><li>Tvoj profil vyzerá ako obchod.</li></ul>
<h2>Veď si čísla</h2>
<p>Zapisuj nákupnú cenu, predajnú cenu a poplatky pri každej veci – presne na to slúži Reseller Profit &amp; DAC7 Tracker.</p>""", [SK_SRC, EU_SK])

# ---------------- Slovenian
EU_SL = eurlex("SL", "Direktiva Sveta (EU) 2021/514 (DAC7), EUR-Lex")
SL_SRC = ("FURS: Dohodnina – dohodek iz kapitala", "https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_kapitala/")
SL_RTV = ("RTV SLO: FURS poziva k prijavi prihodkov iz poslovanja prek spletnih platform (2024)", "https://www.rtvslo.si/gospodarstvo/furs-poziva-k-prijavi-prihodkov-iz-poslovanja-prek-spletnih-platform/695760")
M["tax-id"]["sl"] = A("vinted-davcna-stevilka", "Vinted zahteva tvojo davčno številko: jo moraš dati?",
 "Zakaj Vinted, Bolha in eBay zahtevajo davčno številko, kateri podatki gredo na FURS in kaj se zgodi, če je ne daš.",
 "Da. Ko platforma po pravilih DAC7 zahteva tvojo davčno številko, jo moraš dati, sicer lahko zadrži izplačila ali omeji prodajni račun. To ne pomeni, da moraš plačati davek.",
 """<h2>Zakaj platforma sprašuje?</h2>
<p>Od leta 2023 morajo spletne platforme v EU zbirati podatke o prodajalcih in jih enkrat na leto sporočiti davčnim organom po direktivi DAC7. Prijavljen si, če na eni platformi v letu dosežeš 30 prodaj ali prejmeš več kot 2.000 €.</p>
<h2>Kateri podatki se sporočijo?</h2>
<ul><li>Ime, naslov in datum rojstva</li><li>Davčna številka</li><li>Število prodaj in prejeti zneski po odbitku provizij platforme</li></ul>
<h2>Kaj, če je ne daš?</h2>
<p>Platforma te mora opomniti. Če se ne odzoveš, lahko zadrži izplačila ali omeji prodajo. Zavrnitev ne ustavi prijave, le blokira račun.</p>
<h2>Varno</h2>
<ul><li>Številko vnesi samo v aplikaciji ali na spletni strani platforme, nikoli prek povezave iz e-pošte ali SMS.</li><li>S preverjanjem DAC7 preveri, ali mejo sploh dosežeš.</li></ul>
<p>Prijava ni davek. Preberi <a href="../zasebno-ali-dejavnost/">Zasebna prodaja ali dejavnost?</a></p>""", [EU_SL, S_EBAY])
M["letter"]["sl"] = A("pismo-furs-po-dac7", "Pismo FURS po prijavi DAC7: kaj zdaj?",
 "Si dobil pismo FURS po prodaji na Vintedu, Bolhi ali eBayu? Tako odgovoriš mirno in pravilno.",
 "Ostani miren, a pisma ne prezri. FURS običajno želi vedeti, ali prijavljene prodaje vsebujejo obdavčljiv dohodek. Premičnine za osebno rabo niso med sredstvi, pri katerih se obdavči dobiček iz kapitala.",
 """<h2>Zakaj ti pišejo?</h2>
<p>Vsako leto do 31. januarja platforme sporočijo, kdo je pri njih v preteklem letu dosegel 30 prodaj ali več kot 2.000 €. FURS podatke primerja z napovedjo in lahko vpraša. Vprašanje ni globa.</p>
<h2>Korak za korakom</h2>
<ol><li><strong>Zapiši si rok.</strong></li><li><strong>Zberi prodaje</strong> iz aplikacije: kaj, kdaj, za koliko.</li><li><strong>Razvrsti jih:</strong> lastne rabljene stvari ali blago, kupljeno za nadaljnjo prodajo?</li><li><strong>Odgovori kratko in iskreno</strong>, npr.: »Gre za prodajo rabljenih oblačil iz mojega gospodinjstva.«</li></ol>
<h2>Pravila v Sloveniji</h2>
<p>Dobiček iz kapitala se obdavči pri nepremičninah, vrednostnih papirjih, deležih in investicijskih kuponih; osebne premičnine med temi sredstvi niso navedene. Poslovanje prek spletnih platform kot dejavnost pa se praviloma šteje za dohodek iz dejavnosti in se obdavči.</p>
<p>Pravila vseh 27 držav EU: <a href=\"""" + OV + """\">pregled (v angleščini)</a>.</p>
<h2>Za prihodnje leto</h2>
<p>Vodi preprost seznam, kaj kupuješ in prodajaš ter po kateri ceni.</p>""", [SL_SRC, SL_RTV, EU_SL])
M["platforms"]["sl"] = A("dac7-vinted-bolha-ebay-kaj-se-sporoca", "DAC7 na Vintedu, Bolhi in eBayu: kaj se sporoča?",
 "Katere prodaje Vinted, Bolha, eBay in Etsy sporočajo FURS, kako se štejejo in zakaj oglasi sami ne štejejo.",
 "Sporočajo se le zaključene prodaje, plačane prek platforme. Gotovina ob prevzemu ne šteje, ker je platforma ne vidi. Vsaka platforma šteje posebej.",
 """<h2>Kaj šteje kot prodaja?</h2>
<p>DAC7 šteje transakcije: dejansko zaključene in plačane prodaje. Število oglasov ni pomembno.</p>
<h2>Platforme na kratko</h2>
<ul><li><strong>Vinted:</strong> skoraj vse prodaje gredo prek plačila Vinted in štejejo.</li><li><strong>eBay in Etsy:</strong> plačila obdelujeta sama.</li><li><strong>Bolha in drugi oglasniki:</strong> štejejo le prodaje prek njihove plačilne ali dostavne storitve.</li></ul>
<h2>Vsaka platforma posebej</h2>
<p>Meje 30 prodaj ali več kot 2.000 € veljajo za vsako platformo. Pri davku pa šteje ves tvoj dohodek.</p>
<h2>Kaj se sporoča?</h2>
<p>Zneski po provizijah, ime, naslov, datum rojstva in davčna številka.</p>""", [EU_SL, S_MOBI])
M["business"]["sl"] = A("zasebno-ali-dejavnost", "Zasebna prodaja ali dejavnost: kje je meja?",
 "Kdaj prodaja na Vintedu ali Bolhi postane dejavnost? Glavna merila preprosto.",
 "Fiksnega števila prodaj ni. Pomembno je, ali se znebiš lastnih stvari ali kupuješ, da bi prodajal z dobičkom. Poslovanje prek platform kot dejavnost je obdavčeno kot dohodek iz dejavnosti.",
 """<h2>Zasebno: pospravljanje</h2>
<p>Prodaja oblačil, pohištva ali igrač iz lastnega gospodinjstva je zasebna prodaja.</p>
<h2>Dejavnost: nakup za nadaljnjo prodajo</h2>
<ul><li>Redno kupuješ blago, da ga prodaš naprej.</li><li>Ponujaš veliko enakih ali novih izdelkov.</li><li>Tvoj profil je videti kot trgovina.</li></ul>
<h2>Vodi številke</h2>
<p>Zapisuj nabavno ceno, prodajno ceno in provizije za vsak izdelek – prav za to je Reseller Profit &amp; DAC7 Tracker.</p>""", [SL_RTV, EU_SL])

# ---------------- Swedish
EU_SV = eurlex("SV", "Rådets direktiv (EU) 2021/514 (DAC7), EUR-Lex")
SV_SRC = ("Skatteverket: Sälja och hyra ut på nätet", "https://skatteverket.se/saljahyraut")
M["tax-id"]["sv"] = A("vinted-personnummer", "Vinted ber om ditt personnummer: måste du lämna det?",
 "Varför Vinted, Tradera och Blocket ber om ditt skatteregistreringsnummer, vilka uppgifter som går till Skatteverket och vad som händer om du inte lämnar det.",
 "Ja. När en plattform ber om ditt skatteregistreringsnummer enligt DAC7 måste du lämna det, annars kan den hålla inne utbetalningar eller begränsa ditt säljkonto. Det betyder inte att du måste betala skatt.",
 """<h2>Varför frågar plattformen?</h2>
<p>Sedan 2023 måste onlineplattformar i EU samla in uppgifter om säljare och lämna dem till skattemyndigheterna en gång om året enligt DAC7-direktivet. Du rapporteras om du på en plattform når 30 försäljningar eller säljer för över 2 000 € under ett år.</p>
<h2>Vilka uppgifter lämnas?</h2>
<ul><li>Namn, adress och födelsedatum</li><li>Skatteregistreringsnummer (i Sverige personnummer)</li><li>Antal försäljningar och beloppen du fick efter plattformens avgifter</li></ul>
<h2>Vad händer om du inte lämnar det?</h2>
<p>Plattformen måste påminna dig. Svarar du inte kan den hålla inne utbetalningar eller begränsa försäljningen. Att vägra stoppar inte rapporteringen, det spärrar bara kontot.</p>
<h2>Gör det säkert</h2>
<ul><li>Fyll bara i numret i plattformens app eller på dess webbplats, aldrig via en länk i mejl eller sms.</li><li>Kolla med DAC7-kollen om du alls når gränsen.</li></ul>
<p>Rapportering är ingen skatt. Läs <a href="../privat-eller-naringsverksamhet/">Privat eller näringsverksamhet?</a></p>""", [EU_SV, S_EBAY])
M["letter"]["sv"] = A("brev-fran-skatteverket-efter-dac7", "Brev från Skatteverket efter en DAC7-rapport: vad nu?",
 "Har du fått brev från Skatteverket efter försäljning på Vinted, Tradera eller Blocket? Så svarar du lugnt och rätt.",
 "Behåll lugnet, men ignorera det inte. Skatteverket vill oftast veta om försäljningen innehåller skattepliktig inkomst. Vid enstaka försäljning av personliga tillhörigheter behöver du bara redovisa vinst över 50 000 kronor.",
 """<h2>Varför skriver Skatteverket?</h2>
<p>Varje år senast 31 januari rapporterar plattformarna vem som året före nådde 30 försäljningar eller över 2 000 € hos dem. Skatteverket jämför med din deklaration och kan ställa frågor. En fråga är ingen avgift.</p>
<h2>Steg för steg</h2>
<ol><li><strong>Notera sista dag för svar.</strong></li><li><strong>Samla din försäljning</strong> i appen: vad, när och för hur mycket.</li><li><strong>Sortera:</strong> egna begagnade saker eller varor köpta för att säljas vidare?</li><li><strong>Svara kort och ärligt</strong>, t.ex.: ”Det gäller försäljning av begagnade kläder från mitt hushåll.”</li></ol>
<h2>Reglerna i Sverige</h2>
<p>Vid enstaka försäljning av personliga tillhörigheter redovisar du bara försäljningen om vinsten överstiger 50 000 kronor; den del av vinsten som är över 50 000 kronor tas upp som inkomst av kapital. Säljer du varor regelbundet ska inkomsten redovisas oavsett belopp, och beroende på syfte och omfattning kan det vara hobby eller näringsverksamhet.</p>
<p>Reglerna i alla 27 EU-länder: <a href=\"""" + OV + """\">översikt (på engelska)</a>.</p>
<h2>Till nästa år</h2>
<p>För en enkel lista över vad du köper och säljer och till vilket pris.</p>""", [SV_SRC, EU_SV])
M["platforms"]["sv"] = A("dac7-vinted-tradera-blocket-vad-rapporteras", "DAC7 på Vinted, Tradera och Blocket: vad rapporteras?",
 "Vilken försäljning Vinted, Tradera, Blocket och eBay rapporterar till Skatteverket, hur den räknas och varför annonser ensamma inte räknas.",
 "Bara genomförda försäljningar som betalats via plattformen rapporteras. Kontant betalning vid upphämtning räknas inte, eftersom plattformen inte ser den. Varje plattform räknas för sig.",
 """<h2>Vad räknas som en försäljning?</h2>
<p>DAC7 räknar transaktioner: försäljningar som faktiskt genomförts och betalats. Antalet annonser spelar ingen roll.</p>
<h2>Plattformarna i korthet</h2>
<ul><li><strong>Vinted:</strong> nästan alla försäljningar går via Vinteds betalning och räknas.</li><li><strong>Tradera och eBay:</strong> hanterar betalningen själva.</li><li><strong>Blocket och andra annonssajter:</strong> bara försäljning via deras egen betal- eller frakttjänst räknas.</li></ul>
<h2>Varje plattform för sig</h2>
<p>Gränserna 30 försäljningar eller över 2 000 € gäller per plattform. Skattemässigt räknas dock hela din inkomst.</p>
<h2>Vad rapporteras?</h2>
<p>Beloppen efter avgifter samt namn, adress, födelsedatum och personnummer.</p>""", [EU_SV, S_MOBI])
M["business"]["sv"] = A("privat-eller-naringsverksamhet", "Privat försäljning eller näringsverksamhet: var går gränsen?",
 "När blir försäljning på Vinted, Tradera eller Blocket näringsverksamhet? De viktigaste kriterierna enkelt förklarade.",
 "Det finns inget fast antal försäljningar. Det avgörande är om du rensar bland egna saker eller köper för att sälja vidare med vinst. Regelbunden försäljning ska alltid redovisas.",
 """<h2>Privat: rensa hemma</h2>
<p>Att sälja kläder, möbler eller leksaker från det egna hushållet är privat försäljning.</p>
<h2>Näringsverksamhet: köpa för att sälja vidare</h2>
<ul><li>Du köper regelbundet varor för att sälja dem vidare.</li><li>Du säljer många likadana eller nya varor.</li><li>Ditt konto ser ut som en butik.</li></ul>
<p>Om det är hobby eller näringsverksamhet beror på verksamhetens syfte och omfattning; regelbunden försäljning ska redovisas oavsett belopp.</p>
<h2>Håll koll på siffrorna</h2>
<p>Anteckna inköpspris, försäljningspris och avgifter för varje vara – det är precis vad Reseller Profit &amp; DAC7 Tracker är till för.</p>""", [SV_SRC, EU_SV])
