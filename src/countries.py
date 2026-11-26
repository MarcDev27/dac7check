# Verified tax rules for private sales of used items, by country (checked 26 Nov 2026).
# EU: (country name, own used items, limits/exceptions, source label, source url)
EU = [
 ("Austria", "Not taxed when sold below what you paid.", "Resale within 1 year of purchase is a speculative transaction; gains stay tax-free up to €440 a year.", "§ 31 EStG, JUSLINE", "https://www.jusline.at/gesetz/estg/paragraf/31"),
 ("Belgium", "Not taxed (normal management of private assets).", "Buying to resell occasionally: miscellaneous income at 33%. Frequent trading: professional income.", "Test Achats", "https://www.test-achats.be/argent/impots/reponse-dexpert/vinted-et-taxes"),
 ("Bulgaria", "Not taxed (Art. 13(1)(2) ZDDFL).", "Exceptions: vehicles sold within 1 year of purchase, art and collectibles, trading.", "Innovires (Sept 2026)", "https://www.innovires.com/en/blog/onlayn-prodazhbi-fl-danak-gdd-dac7.html"),
 ("Croatia", "Not income under the Income Tax Act.", "Continuous selling with intent to earn income counts as self-employment.", "RRiF opinion (2015)", "https://www.rrif.hr/razmjena_dobara_na_buvljaku-2987-misljenje/"),
 ("Cyprus", "Not taxed: capital gains are taxed only on Cyprus real estate.", "Trading as a business is taxed as business income.", "PwC Tax Summaries", "https://taxsummaries.pwc.com/cyprus/individual/income-determination"),
 ("Czechia", "Exempt (used household items).", "Buying to resell repeatedly for profit counts as a business.", "Finanční správa", "https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/dotazy-a-odpovedi/dan-z-prijmu-fyzickych-osob/prijmy-z-bazaroveho-prodeje"),
 ("Denmark", "Generally not taxed.", "Taxable if items were bought for resale or speculation; regular selling can be a business.", "Legal Desk (2022)", "https://www.legaldesk.dk/artikler/hvornaar-skal-jeg-betale-skat-af-privat-salg"),
 ("Estonia", "Not taxed (items for personal use).", "Items not used personally: the profit is taxed. Regular selling for profit: register as a business.", "Maksu- ja Tolliamet", "https://emta.ee/eraklient/maksud-ja-tasumine/maksustatavad-tulud/internetimuuk"),
 ("Finland", "Tax-free if gains on household goods stay within €5,000 a year.", "The part of the gain above €5,000 is taxed. Self-made items and continuous reselling are taxable.", "Vero.fi", "https://vero.fi/en/individuals/tax-cards-and-tax-returns/income/earned-income/flea-market-sales/"),
 ("France", "Not taxed (occasional sales).", "Items sold for over €5,000 (except furniture, appliances and cars) fall under capital gains rules; jewellery, art and collectibles over €5,000 pay a flat tax.", "economie.gouv.fr", "https://www.economie.gouv.fr/particuliers/vente-biens-declarer-revenus"),
 ("Germany", "Not taxed (everyday items).", "Resale within 1 year of purchase: gains taxable once they reach €1,000 a year in total.", "Correctiv (Oct 2026)", "https://correctiv.org/faktencheck/2026/10/29/keine-steuer-auf-private-verkaeufe-flohmarkt-vinted-ebay/"),
 ("Greece", "Occasional private sales are not taxed.", "Three similar sales within 6 months can count as business activity (Art. 21 Income Tax Code).", "Taxheaven (2024)", "https://www.taxheaven.gr/circulars/48221/arora-pwlhsh-ix-kai-loipwn-kinhtwn-pragmatwn-apo-idiwth-forologikes-proektaseis"),
 ("Hungary", "No tax and no return if sales stay within HUF 600,000 a year.", "Above that, income (sales minus costs) is tax-free up to HUF 200,000; the rest is taxed at 15%.", "NAV", "https://nav.gov.hu/Elethelyzetek-adozasa/vagyonugyek/A-megunt-holmik-eladasa"),
 ("Ireland", "Gains on movable property up to €2,540 are exempt.", "Every individual also has a €1,270 annual capital gains exemption.", "Revenue", "https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx"),
 ("Italy", "Not taxed (occasional, non-commercial sales).", "Occasional sales at a profit: 'altri redditi' in the tax return. Organised selling needs a VAT number.", "Il Post (Nov 2025)", "https://www.ilpost.it/2025/11/09/vendita-usato-vinted-piattaforme-tasse-irpef-iva/"),
 ("Latvia", "Not taxed (personal movable property).", "Business activity is taxed separately.", "LV portāls (Apr 2025)", "https://lvportals.lv/e-konsultacijas/36059-ienakums-no-personiskas-mantas-pardosanas-nav-apliekams-ar-nodokli-2025"),
 ("Lithuania", "Tax-free up to €2,500 of sales a year.", "Above that: 15% on proceeds minus purchase price, costs and €2,500.", "VMI", "https://www.vmi.lt/evmi/en/kaip-apmokestinamos-kito-neregistruotino-turto-pardavimo-pajamos-"),
 ("Luxembourg", "No general tax on gains from movable property.", "Resale within 6 months of purchase: speculative gains taxable once they reach €500 a year.", "Margeo (Sept 2026)", "https://margeoapp.com/blog/vinted-luxembourg-impots"),
 ("Malta", "Outside capital gains tax (only listed assets such as property and shares are taxed).", "Trading as a business is taxed as business income.", "PwC Tax Summaries", "https://taxsummaries.pwc.com/malta/individual/income-determination"),
 ("Netherlands", "Usually no income tax (private or hobby sales).", "Buying to resell at a profit is a source of income, with no minimum amount.", "Belastingdienst", "https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/inkomstenbelasting-betalen-over-internetverkopen"),
 ("Poland", "Not taxed if sold more than 6 months after the end of the month of purchase.", "Earlier sales at a profit: the difference is taxed. Continuous selling: business.", "Podatnik.info (Nov 2025)", "https://www.podatnik.info/publikacje/podatek-od-vinted-olx-allegro-kiedy-trzeba-go-zaplacic,637677"),
 ("Portugal", "Not currently subject to IRS (private sales of used goods).", "Professional selling is taxed as business income.", "DECO PROteste", "https://www.deco.proteste.pt/dinheiro/impostos/dicas/vendas-segunda-mao-tem-ser-declaradas-irs"),
 ("Romania", "Not taxable (personal goods).", "Continuous buying and selling is an economic activity and must be registered.", "ANAF Cluj (Jul 2026)", "https://static.anaf.ro/static/10/Cluj/cj_second_hand_29iul2026.pdf"),
 ("Slovakia", "Fully exempt (items not held as business assets).", "Items from business assets: taxable if sold within 5 years.", "Finančná správa", "https://podpora.financnasprava.sk/531745-Príjmy-fyzickej-osoby-z-predaja-hnuteľnej-veci-"),
 ("Slovenia", "Not listed among taxable capital gains (only real estate, securities, shares and fund units).", "Selling through platforms as an activity counts as business income.", "FURS", "https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_kapitala/"),
 ("Spain", "Only a gain is taxed (selling for more than you paid).", "Losses from normal use can't be deducted.", "OCU", "https://www.ocu.org/dinero/renta-impuestos/noticias/tributacion-ventas-segunda-mano"),
 ("Sweden", "Occasional sales: gains only reported above SEK 50,000.", "Regular selling must be reported whatever the amount.", "Skatteverket", "https://skatteverket.se/saljahyraut"),
]

def src(country):
    for c in EU:
        if c[0] == country:
            return (f"{c[3]}", c[4])
    raise KeyError(country)

OVERVIEW = "../../../en/guides/eu-tax-on-selling-used-items/"

# Country section for the "letter from the tax office" article, per article language.
BLOCK = {
 "en": ("<h2>Rules in Ireland and Malta</h2><ul>"
        "<li><strong>Ireland:</strong> gains on movable property such as furniture are exempt up to €2,540, and every individual has a €1,270 annual capital gains exemption on top.</li>"
        "<li><strong>Malta:</strong> capital gains tax applies only to listed assets such as property and shares, so gains on personal items fall outside it.</li></ul>"
        f'<p>Rules for all 27 EU countries: <a href="{OVERVIEW}">Do you pay tax on selling used items? All EU countries</a>.</p>',
        ["Ireland", "Malta"]),
 "de": ('<p>Die Regeln aller 27 EU-Länder findest du in unserer <a href="' + OVERVIEW + '">Übersicht (auf Englisch)</a>.</p>', []),
 "fr": ("<h2>Les règles en France, en Belgique et au Luxembourg</h2><ul>"
        "<li><strong>France :</strong> les ventes occasionnelles de vos propres objets ne sont pas imposées. Un objet vendu plus de 5 000 € (hors meubles, électroménager et voitures) relève du régime des plus-values ; bijoux, art et objets de collection au-delà de 5 000 € paient une taxe forfaitaire.</li>"
        "<li><strong>Belgique :</strong> vendre vos propres affaires relève de la gestion normale du patrimoine privé et n'est pas imposé. Acheter pour revendre de façon occasionnelle : revenus divers taxés à 33 %. Activité fréquente : revenus professionnels.</li>"
        "<li><strong>Luxembourg :</strong> pas d'impôt général sur les plus-values de biens meubles. Revente dans les 6 mois suivant l'achat : plus-value spéculative imposable dès que le total atteint 500 € par an.</li></ul>"
        f'<p>Les règles des 27 pays de l\'UE : <a href="{OVERVIEW}">vue d\'ensemble (en anglais)</a>.</p>',
        ["France", "Belgium", "Luxembourg"]),
 "nl": ("<h2>De regels in Nederland en België</h2><ul>"
        "<li><strong>Nederland:</strong> particuliere verkoop van je eigen spullen levert meestal geen inkomstenbelasting op. Inkopen om met winst door te verkopen is een bron van inkomen, zonder minimumbedrag.</li>"
        "<li><strong>België:</strong> je eigen spullen verkopen valt onder het normale beheer van je privévermogen en wordt niet belast. Af en toe inkopen om door te verkopen: diverse inkomsten tegen 33%. Frequent handelen: beroepsinkomsten.</li></ul>"
        f'<p>De regels van alle 27 EU-landen: <a href="{OVERVIEW}">overzicht (Engelstalig)</a>.</p>',
        ["Netherlands", "Belgium"]),
 "it": ("<h2>Le regole in Italia</h2>"
        "<p>Le vendite occasionali e non commerciali delle tue cose usate non sono tassate. Le vendite occasionali con un guadagno vanno indicate in dichiarazione come «altri redditi» e sono soggette a IRPEF. Chi vende in modo organizzato deve aprire la partita IVA.</p>"
        f'<p>Le regole dei 27 paesi UE: <a href="{OVERVIEW}">panoramica (in inglese)</a>.</p>',
        ["Italy"]),
 "es": ("<h2>Las reglas en España</h2>"
        "<p>Solo tributa la ganancia, es decir, si vendes algo por más de lo que pagaste; se declara como renta del ahorro. Las pérdidas por el uso normal de los bienes no se pueden compensar.</p>"
        f'<p>Las reglas de los 27 países de la UE: <a href="{OVERVIEW}">resumen (en inglés)</a>.</p>',
        ["Spain"]),
 "pl": ("<h2>Zasady w Polsce</h2>"
        "<p>Sprzedaż rzeczy po upływie 6 miesięcy od końca miesiąca, w którym je kupiłeś, nie podlega podatkowi. Jeśli sprzedasz wcześniej i z zyskiem, podatek płacisz od różnicy między ceną sprzedaży a zakupu. Sprzedaż prowadzona w sposób ciągły to działalność gospodarcza.</p>"
        f'<p>Zasady we wszystkich 27 krajach UE: <a href="{OVERVIEW}">przegląd (po angielsku)</a>.</p>',
        ["Poland"]),
}

OVERVIEW_ARTICLE = {
 "slug": "eu-tax-on-selling-used-items",
 "title": "Do you pay tax on selling used items? Rules in all 27 EU countries",
 "desc": "Country-by-country overview: when selling your own used items on Vinted, eBay or local marketplaces is tax-free, and which limits apply, in every EU country.",
 "answer": "In almost every EU country, selling your own used items for less than you paid is tax-free. The differences lie in special limits, such as Finland's €5,000 or Lithuania's €2,500 a year, short resale periods in Austria, Germany, Luxembourg and Poland, and in when regular reselling counts as a business.",
}
