import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from i18n import L
from i18n2 import L2
from i18n3 import X, EURLEX, EXTRA_SOURCES, austria, germany_overrides
from articles import ARTICLES, GUIDES, UPDATED
from articles_more import MORE, MORE_GUIDES
GUIDES.update(MORE_GUIDES)
for _a in ARTICLES:
    _a.update(MORE.get(_a["id"], {}))
import shutil
L.update(L2)
L["at"] = austria(L["de"])
germany_overrides(L["de"])

BASE = "https://www.dac7check.eu"           # change to the real domain before going live
LISTING = "https://www.etsy.com/listing/4616435248/eu-reseller-spreadsheet-202627-vinted"
ORDER = ["en", "bg", "cs", "da", "de", "at", "el", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
ART_LANGS = [c for c in ORDER if c in GUIDES]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
CSS = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "base.css"), encoding="utf-8").read()

EXTRA_CSS = """
.topbar { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
.lang { position: relative; background: none; border: 0; padding: 0; border-radius: 0; margin-left: auto; }
.lang summary { list-style: none; cursor: pointer; font-size: 14px; font-weight: 600; padding: 8px 14px; border-radius: 10px; border: 1px solid var(--input-border); background: var(--surface); color: var(--fg); }
.lang summary::-webkit-details-marker { display: none; }
.lang[open] summary { border-color: var(--accent); }
.lang ul { position: absolute; right: 0; top: calc(100% + 6px); z-index: 5; margin: 0; padding: 6px; list-style: none; background: var(--surface); border: 1px solid var(--line); border-radius: 12px; min-width: 190px; max-height: 60vh; overflow-y: auto; box-shadow: 0 12px 30px rgba(20, 38, 45, 0.15); }
.lang li a { display: block; padding: 8px 12px; border-radius: 8px; text-decoration: none; color: var(--fg); font-size: 15px; }
.lang li a:hover, .lang li a[aria-current="page"] { background: var(--bg); }
.lang li a[aria-current="page"] { font-weight: 700; }
.counts { display: flex; flex-wrap: wrap; gap: 8px; }
.summary:empty { display: none; }
.skip { position: absolute; left: -9999px; top: 8px; z-index: 20; background: var(--surface); color: var(--fg); padding: 10px 16px; border-radius: 10px; border: 2px solid var(--focus); font-weight: 600; }
.answer { font-size: 18px; font-weight: 600; max-width: 62ch; margin: 0; }
.guides ul, .sources ul { margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 8px; }
.guides p { color: var(--muted); }
.sources { font-size: 14px; color: var(--muted); }
.sources h2 { font-size: 18px; }
.skip:focus { left: max(16px, env(safe-area-inset-left, 0px)); }
"""

JS = r"""
(function () {
  var T = window.__T;
  var eur = new Intl.NumberFormat(T.locale, { style: "currency", currency: "EUR", maximumFractionDigits: 0 });
  var form = document.getElementById("form");
  var proposal = document.getElementById("proposal");
  var summary = document.getElementById("summary");
  var sampleNote = document.getElementById("sample-note");
  var sample = [[27, 640], [31, 1480], [6, 410], ["", ""], ["", ""]];
  var ids = T.platforms.map(function (_, i) { return "p" + i; });
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }
  function fmt(t, o) { return t.replace("{n}", o.n).replace("{a}", o.a).replace("{l}", o.l); }

  form.innerHTML = T.platforms.map(function (name, i) {
    var id = ids[i];
    return '<div class="row">' +
      '<div class="plat-name">' + esc(name) + '</div>' +
      '<div class="field"><label for="s-' + id + '">' + esc(T.sales) + '<span class="sr-only"> ' + esc(T.on) + ' ' + esc(name) + '</span></label>' +
      '<input id="s-' + id + '" type="number" inputmode="numeric" min="0" step="1" placeholder="0" value="' + sample[i][0] + '"></div>' +
      '<div class="field"><label for="a-' + id + '">' + esc(T.amount) + '<span class="sr-only"> ' + esc(T.on) + ' ' + esc(name) + '</span></label>' +
      '<input id="a-' + id + '" type="number" inputmode="decimal" min="0" step="0.01" placeholder="0" value="' + sample[i][1] + '"></div>' +
      '<div class="result" id="r-' + id + '"></div></div>';
  }).join("");

  function num(id) { var v = parseFloat(document.getElementById(id).value); return isFinite(v) && v > 0 ? v : 0; }
  function bar(label, value, limit, cls) {
    var pct = Math.min(100, (value / limit) * 100);
    return '<div class="bar"><span>' + esc(label) + '</span><div class="track"><div class="fill ' + cls + '" style="width:' + pct.toFixed(1) + '%"></div></div></div>';
  }

  function render() {
    var newRule = proposal.checked, countLimit = newRule ? null : 30, amountLimit = newRule ? 3000 : 2000;
    var c = { bad: 0, warn: 0, ok: 0 }, used = 0;
    ids.forEach(function (id) {
      var sales = num("s-" + id), amount = num("a-" + id), out = document.getElementById("r-" + id);
      if (!sales && !amount) { out.innerHTML = '<div class="result-top"><span class="pill none">' + esc(T.st_empty) + '</span></div>'; return; }
      used++;
      var hit = (countLimit !== null && sales >= countLimit) || amount > amountLimit;
      var near = !hit && ((countLimit !== null && sales >= countLimit * 0.8) || amount >= amountLimit * 0.8);
      var cls = hit ? "bad" : near ? "warn" : "ok";
      c[cls]++;
      var text;
      if (hit) {
        var why = [];
        if (countLimit !== null && sales >= countLimit) why.push(fmt(T.r_sales, { n: Math.round(sales) }));
        if (amount > amountLimit) why.push(fmt(T.r_amount, { a: eur.format(amount), l: eur.format(amountLimit) }));
        text = T.why + ": " + why.join(" · ");
      } else {
        var left = [];
        if (countLimit !== null) left.push(fmt(T.room_sales, { n: Math.round(countLimit - sales) }));
        left.push(fmt(T.room_amount, { a: eur.format(amountLimit - amount) }));
        text = T.room + ": " + left.join(" · ");
      }
      var bars = '<div class="bars" aria-hidden="true">' +
        (countLimit !== null ? bar(fmt(T.bar_sales, { n: Math.round(sales) }), sales, countLimit, cls) : '') +
        bar(fmt(T.bar_amount, { a: eur.format(amount), l: eur.format(amountLimit) }), amount, amountLimit, cls) + '</div>';
      out.innerHTML = '<div class="result-top"><span class="pill ' + cls + '">' + esc(T["st_" + cls]) + '</span><span class="result-text">' + esc(text) + '</span></div>' + bars;
    });
    if (!used) { summary.textContent = T.sum_empty; return; }
    summary.innerHTML = '<span class="counts">' +
      '<span class="pill bad">' + esc(T.st_bad) + ': ' + c.bad + '</span>' +
      '<span class="pill warn">' + esc(T.st_warn) + ': ' + c.warn + '</span>' +
      '<span class="pill ok">' + esc(T.st_ok) + ': ' + c.ok + '</span></span>';
  }

  form.addEventListener("input", function () { sampleNote.hidden = true; render(); });
  form.addEventListener("submit", function (e) { e.preventDefault(); });
  proposal.addEventListener("change", render);
  document.getElementById("clear").addEventListener("click", function () {
    form.querySelectorAll("input").forEach(function (i) { i.value = ""; });
    sampleNote.hidden = true; render(); document.getElementById("s-" + ids[0]).focus();
  });
  var menu = document.querySelector(".lang");
  if (menu) menu.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu.open) { menu.open = false; menu.querySelector("summary").focus(); }
  });
  render();
})();
"""

SKIP = {'en': 'Skip to the check', 'bg': 'Към проверката', 'cs': 'Přejít ke kontrole', 'da': 'Gå til tjekket', 'de': 'Zum Check springen', 'at': 'Zum Check springen', 'el': 'Μετάβαση στον έλεγχο', 'es': 'Ir al comprobador', 'et': 'Mine kontrolli juurde', 'fi': 'Siirry tarkistukseen', 'fr': 'Aller au simulateur', 'hr': 'Prijeđi na provjeru', 'hu': 'Ugrás az ellenőrzéshez', 'it': 'Vai alla verifica', 'lt': 'Pereiti prie patikros', 'lv': 'Pāriet uz pārbaudi', 'nl': 'Naar de check', 'pl': 'Przejdź do testu', 'pt': 'Ir para o verificador', 'ro': 'Mergi la verificare', 'sk': 'Prejsť na kontrolu', 'sl': 'Skoči na preverjanje', 'sv': 'Gå till kollen'}

HREF = {"at": "de-AT"}
def hl(code):
    return HREF.get(code, code)

def url(code):
    return f"{BASE}/{code}/"

ORG = {"@type": "Organization", "name": "SortwellStudios", "url": BASE + "/",
       "logo": BASE + "/apple-touch-icon.png", "address": {"@type": "PostalAddress", "addressLocality": "Wien", "addressCountry": "AT"}}

def social(title, desc, page_url, locale, kind="website"):
    return (f'<meta property="og:type" content="{kind}">\n<meta property="og:site_name" content="DAC7 Check">\n'
            f'<meta property="og:title" content="{html.escape(title)}">\n<meta property="og:description" content="{html.escape(desc)}">\n'
            f'<meta property="og:url" content="{page_url}">\n<meta property="og:locale" content="{locale.replace("-", "_")}">\n'
            f'<meta property="og:image" content="{BASE}/og-image.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n')

def head(code, fonts):
    t = L[code]
    alts = "\n".join(f'<link rel="alternate" hreflang="{hl(c)}" href="{url(c)}">' for c in ORDER)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    ld = {"@context": "https://schema.org", "@graph": [
          {"@type": "WebApplication", "name": t["title"], "url": url(code), "description": t["desc"], "inLanguage": hl(code),
           "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "isAccessibleForFree": True,
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}, "dateModified": UPDATED, "publisher": ORG},
          {"@type": "FAQPage", "inLanguage": hl(code),
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]}
    f = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap">\n') if fonts else ""
    return (f'<title>{t["title"]}</title>\n<meta name="description" content="{html.escape(t["desc"])}">\n'
            f'<link rel="canonical" href="{url(code)}">\n{alts}\n{f}' + social(t["title"], t["desc"], url(code), t["locale"]) +
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')

def body(code, prefix):
    t = L[code]
    links = "".join(
        f'<li><a href="{prefix}{c}/" lang="{hl(c)}" hreflang="{hl(c)}"' + (' aria-current="page"' if c == code else '') + f'>{L[c]["name"]}</a></li>'
        for c in ORDER)
    chips = "".join(f'<span class="chip">{c}</span>' for c in t["chips"])
    items = "".join(f"<li>{i}</li>" for i in t["cta_items"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    ans, src_title, directive = X[code]
    srcs = [(f"{directive} (EU) 2021/514 (DAC7) – EUR-Lex", f"https://eur-lex.europa.eu/legal-content/{EURLEX[code]}/TXT/?uri=CELEX:32021L0514")] + EXTRA_SOURCES.get(code, [])
    sources = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in srcs)
    gl = "de" if code in ("de", "at") else code
    guides = ""
    if gl in GUIDES:
        g = GUIDES[gl]
        gi = "".join(f'<li><a href="{prefix}{gl}/{g["dir"]}/{a[gl]["slug"]}/">{a[gl]["title"]}</a></li>' for a in ARTICLES)
        guides = f'<section class="guides" aria-labelledby="guides-title"><h2 id="guides-title">{g["title"]}</h2><p>{g["intro"]}</p><ul>{gi}</ul></section>'
    js_t = {k: t[k] for k in ["locale", "platforms", "sales", "amount", "on", "st_empty", "st_ok", "st_warn", "st_bad", "why",
                              "r_sales", "r_amount", "room", "room_sales", "room_amount", "bar_sales", "bar_amount", "sum_empty"]}
    return f"""<a class="skip" href="#check-title">{SKIP[code]}</a>
<div class="wrap">
  <header class="topbar">
    <span class="brand"><span class="brand-mark" aria-hidden="true"><span></span><span></span><span></span><span></span></span>Sortwell Studios</span>
    <details class="lang"><summary>{t["lang_label"]}: {t["name"]}</summary><ul>{links}</ul></details>
  </header>
  <main id="main" class="wrap" style="padding:0">
  <section class="intro" aria-labelledby="title">
    <div class="eyebrow">{t["eyebrow"]}</div>
    <h1 id="title">{t["h1"]}</h1>
    <p class="answer">{ans}</p>
    <p class="lead">{t["lead"]}</p>
    <div class="rule-chips">{chips}</div>
  </section>
  <section class="checker" aria-labelledby="check-title">
    <div class="checker-head"><h2 id="check-title" tabindex="-1">{t["check_title"]}</h2><span class="sample-note" id="sample-note">{t["sample"]}</span></div>
    <form id="form" class="rows" novalidate></form>
    <div class="summary" id="summary" aria-live="polite"></div>
    <div class="controls">
      <label class="toggle" for="proposal"><input type="checkbox" id="proposal"><span>{t["proposal"]}</span></label>
      <button type="button" class="btn-ghost" id="clear">{t["clear"]}</button>
    </div>
  </section>
  <section class="cta" aria-labelledby="cta-title">
    <h2 id="cta-title">{t["cta_title"]}</h2>
    <p>{t["cta_text"]}</p>
    <ul>{items}</ul>
    <a class="btn" href="{LISTING}">{t["cta_btn"]}</a>
  </section>
  <section class="explain" aria-labelledby="explain-title">
    <h2 id="explain-title">{t["ex_title"]}</h2>
    <p>{t["ex_p1"]}</p>
    <p>{t["ex_p2"]}</p>
    <div class="example"><div><strong>{t["ex_no_t"]}</strong>{t["ex_no"]}</div><div><strong>{t["ex_yes_t"]}</strong>{t["ex_yes"]}</div></div>
  </section>
  <section class="faq" aria-labelledby="faq-title"><h2 id="faq-title">{t["faq_title"]}</h2>{faq}</section>
  {guides}
  <section class="sources" aria-labelledby="sources-title"><h2 id="sources-title">{src_title}</h2><ul>{sources}</ul></section>
  </main>
  <footer>
    <p>{t["disclaimer"]}</p>
    <nav><a href="{prefix}impressum.html">{t["imprint"]}</a><a href="{prefix}datenschutz.html">{t["privacy"]}</a></nav>
  </footer>
</div>
<script>window.__T = {json.dumps(js_t, ensure_ascii=False)};</script>
<script>{JS}</script>
"""

def full(code):
    return (f'<!doctype html>\n<html lang="{hl(code)}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'{head(code, fonts=False)}<style>{CSS}{EXTRA_CSS}\nbody {{ margin: 0; }}\n</style>\n</head>\n<body>\n{body(code, "../")}</body>\n</html>\n')

CHOOSER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DAC7 Check for EU Sellers</title>
<meta name="description" content="Free DAC7 check for EU sellers on Vinted, eBay, Etsy and more. Choose your language.">
__ALTS__
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; background: #F3F6F5; color: #14262D; padding: 48px max(16px, env(safe-area-inset-left, 0px)); }
@media (prefers-color-scheme: dark) { body { background: #0F1A1E; color: #E6EEF0; } a { color: #7FC8A9; } }
main { max-width: 520px; margin: 0 auto; } h1 { font-size: 28px; } ul { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
a { color: #1F4E5F; font-weight: 600; font-size: 17px; }
</style>
<script>
(function () {
  var langs = __LANGS__;
  var tags = (navigator.languages || [navigator.language || "en"]).map(function (l) { return l.toLowerCase(); });
  for (var j = 0; j < tags.length; j++) if (tags[j] === "de-at") { location.replace("at/"); return; }
  var pref = tags.map(function (l) { return l.slice(0, 2); });
  for (var i = 0; i < pref.length; i++) if (langs.indexOf(pref[i]) > -1) { location.replace(pref[i] + "/"); return; }
  location.replace("en/");
})();
</script>
</head>
<body><main><h1>DAC7 Check</h1><ul>__LINKS__</ul></main></body>
</html>
"""


LEGAL_CSS = """body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.6;background:#F3F6F5;color:#14262D;padding:40px max(16px,env(safe-area-inset-left,0px)) 56px}
@media (prefers-color-scheme: dark){body{background:#0F1A1E;color:#E6EEF0}a{color:#7FC8A9}}
main{max-width:680px;margin:0 auto}h1{font-size:30px;line-height:1.2;hyphens:auto;overflow-wrap:break-word}h2{font-size:20px;margin-top:32px}a{color:#1F4E5F}hr{border:0;border-top:1px solid #D3DEE1;margin:40px 0}"""

def legal_page(title, html_body):
    return ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n<meta name="robots" content="noindex">\n<style>{LEGAL_CSS}</style>\n</head>\n'
            f'<body><main>{html_body}<p><a href="./">← DAC7 Check</a></p></main></body>\n</html>\n')

IMPRESSUM = legal_page("Impressum – DAC7 Check", """
<h1>Impressum</h1>
<p>Informationen gemäß § 5 E-Commerce-Gesetz und Offenlegung gemäß § 25 Mediengesetz</p>
<p><strong>SortwellStudios</strong><br>Wien, Österreich</p>
<p>Blattlinie: Informationen und ein kostenloses Rechenwerkzeug zu den DAC7-Meldepflichten für Online-Verkäufer.</p>
<hr lang="en">
<h1 lang="en">Legal notice</h1>
<p lang="en"><strong>SortwellStudios</strong><br>Vienna, Austria</p>
""")

DATENSCHUTZ = legal_page("Datenschutz – DAC7 Check", """
<h1>Datenschutzerklärung</h1>
<h2>Verantwortlich</h2>
<p>SortwellStudios, Wien, Österreich</p>
<h2>Keine Cookies, keine Analyse</h2>
<p>Diese Website setzt keine Cookies, verwendet keine Analyse- oder Tracking-Werkzeuge und lädt keine Inhalte von Drittanbietern. Die Zahlen, die du in den DAC7-Check eingibst, werden nur in deinem Browser berechnet und nicht übertragen oder gespeichert.</p>
<h2>Hosting</h2>
<p>Die Website wird von Netlify, Inc. (San Francisco, USA) bereitgestellt. Beim Aufruf verarbeitet Netlify technisch notwendige Daten wie IP-Adresse, Datum und Uhrzeit, aufgerufene Seite und Browsertyp in Server-Logfiles, um die Seite auszuliefern und vor Missbrauch zu schützen. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und funktionierenden Webauftritt (Art. 6 Abs. 1 lit. f DSGVO). Details: <a href="https://www.netlify.com/privacy/">netlify.com/privacy</a>.</p>
<h2>Links zu Etsy</h2>
<p>Die Website verlinkt auf ein Angebot bei Etsy. Erst wenn du den Link anklickst, gelten die Datenschutzbestimmungen von Etsy.</p>
<h2>Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Du kannst dich bei der österreichischen Datenschutzbehörde (<a href="https://www.dsb.gv.at">dsb.gv.at</a>) beschweren.</p>
<p>Stand: November 2026</p>
<hr lang="en">
<h1 lang="en">Privacy</h1>
<p lang="en">This website sets no cookies, uses no analytics or tracking and loads nothing from third parties. The numbers you enter in the DAC7 check are calculated in your browser only and are never sent or stored. The site is hosted by Netlify, Inc., which processes technically necessary data such as IP addresses in server logs to deliver the site (Art. 6(1)(f) GDPR). Controller: SortwellStudios, Vienna, Austria. You can complain to the Austrian Data Protection Authority (dsb.gv.at).</p>
""")

ART_CSS = """
.article { max-width: 720px; display: flex; flex-direction: column; gap: 20px; }
.article h2 { margin-top: 12px; }
.article p, .article li { max-width: 65ch; }
.article ul, .article ol { margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 6px; }
.crumbs { font-size: 14px; color: var(--muted); }
.crumbs ol { list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; gap: 6px; flex-direction: row; }
.crumbs li + li::before { content: "›"; margin-right: 6px; }
.meta { font-size: 14px; color: var(--muted); }
.answer-box { background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 18px 20px; font-size: 17px; font-weight: 600; }
.article .cta a { color: #FFFFFF; }
.article .cta a.btn { color: #0F1A1E; }
"""

def art_url(lang, slug):
    return f"{BASE}/{lang}/{GUIDES[lang]['dir']}/{slug}/"

def guides_url(lang):
    return f"{BASE}/{lang}/{GUIDES[lang]['dir']}/"

def page(lang_attr, head_html, body_html, extra_css=""):
    return (f'<!doctype html>\n<html lang="{lang_attr}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'{head_html}<style>{CSS}{EXTRA_CSS}{ART_CSS}{extra_css}\nbody {{ margin: 0; }}\n</style>\n</head>\n<body>\n{body_html}</body>\n</html>\n')

def topbar(home_href, lang_links_html, label):
    menu = f'<details class="lang"><summary>{label}</summary><ul>{lang_links_html}</ul></details>' if lang_links_html else ""
    return (f'<header class="topbar"><a class="brand" href="{home_href}" style="text-decoration:none">'
            '<span class="brand-mark" aria-hidden="true"><span></span><span></span><span></span><span></span></span>DAC7 Check</a>'
            f'{menu}</header>')

def footer(code, prefix):
    t = L[code]
    return (f'<footer><p>{GUIDES[code if code in GUIDES else "en"]["disclaimer"]}</p>'
            f'<nav><a href="{prefix}impressum.html">{t["imprint"]}</a><a href="{prefix}datenschutz.html">{t["privacy"]}</a></nav></footer>')

MENU_JS = """<script>(function(){var m=document.querySelector('.lang');if(m)m.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.open){m.open=false;m.querySelector('summary').focus();}});})();</script>"""

def alt_links(urls):
    """urls: {lang: url} -> hreflang link tags incl. de-AT and x-default"""
    out = "".join(f'<link rel="alternate" hreflang="{l}" href="{u}">\n' for l, u in urls.items())
    if "de" in urls:
        out += f'<link rel="alternate" hreflang="de-AT" href="{urls["de"]}">\n'
    return out + f'<link rel="alternate" hreflang="x-default" href="{urls["en"]}">\n'

def short_name(l):
    return L[l]["name"].split(" (")[0]

def article_page(a, lang):
    g, d = GUIDES[lang], a[lang]
    urls = {l: art_url(l, a[l]["slug"]) for l in ART_LANGS}
    me = urls[lang]
    home = f"../../../{lang}/"
    alts = alt_links(urls)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": d["title"], "description": d["desc"], "inLanguage": lang, "url": me,
         "datePublished": UPDATED, "dateModified": UPDATED, "author": ORG, "publisher": ORG, "image": BASE + "/og-image.png",
         "citation": [u for _, u in d["sources"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "DAC7 Check", "item": url(lang)},
            {"@type": "ListItem", "position": 2, "name": g["title"], "item": guides_url(lang)},
            {"@type": "ListItem", "position": 3, "name": d["title"], "item": me}]}]}
    head_html = (f'<title>{d["title"]} | DAC7 Check</title>\n<meta name="description" content="{html.escape(d["desc"])}">\n'
                 f'<link rel="canonical" href="{me}">\n{alts}' + social(d["title"], d["desc"], me, L[lang]["locale"], "article")
                 + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')
    links = "".join(f'<li><a href="../../../{l}/{GUIDES[l]["dir"]}/{a[l]["slug"]}/" lang="{l}" hreflang="{l}"' + (' aria-current="page"' if l == lang else '') + f'>{short_name(l)}</a></li>' for l in ART_LANGS)
    srcs = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in d["sources"])
    body_html = f"""<a class="skip" href="#article-title">{SKIP[lang]}</a>
<div class="wrap">
  {topbar(home, links, L[lang]["lang_label"] + ": " + short_name(lang))}
  <main id="main" class="article">
    <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="{home}">DAC7 Check</a></li><li><a href="../">{g["title"]}</a></li><li aria-current="page">{d["title"]}</li></ol></nav>
    <h1 id="article-title" tabindex="-1">{d["title"]}</h1>
    <p class="meta">{g["updated"]} · SortwellStudios</p>
    <p class="answer-box">{d["answer"]}</p>
    {d["body"]}
    <section class="cta" aria-labelledby="cta-title">
      <h2 id="cta-title">{g["cta_title"]}</h2>
      <p>{g["cta_text"]}</p>
      <a class="btn" href="{home}">{g["cta_btn"]}</a>
      <p>{g["track"]} <a href="{LISTING}">{g["track_link"]}</a>.</p>
    </section>
    <section class="sources" aria-labelledby="sources-title"><h2 id="sources-title">{g["sources"]}</h2><ul>{srcs}</ul></section>
  </main>
  {footer(lang, "../../../")}
</div>
{MENU_JS}
"""
    return page(lang, head_html, body_html)

def guides_index(lang):
    g = GUIDES[lang]
    urls = {l: guides_url(l) for l in ART_LANGS}
    me = urls[lang]
    alts = alt_links(urls)
    title = f'{g["title"]}: DAC7 &amp; Vinted | DAC7 Check'
    head_html = (f'<title>{title}</title>\n<meta name="description" content="{html.escape(g["intro"])}">\n<link rel="canonical" href="{me}">\n{alts}'
                 + social(html.unescape(title), g["intro"], me, L[lang]["locale"]))
    items = "".join(f'<li><a href="{a[lang]["slug"]}/"><strong>{a[lang]["title"]}</strong></a><br><span class="meta">{a[lang]["desc"]}</span></li>' for a in ARTICLES)
    links = "".join(f'<li><a href="../../{l}/{GUIDES[l]["dir"]}/" lang="{l}" hreflang="{l}"' + (' aria-current="page"' if l == lang else '') + f'>{short_name(l)}</a></li>' for l in ART_LANGS)
    home = f"../../{lang}/"
    body_html = f"""<a class="skip" href="#article-title">{SKIP[lang]}</a>
<div class="wrap">
  {topbar(home, links, L[lang]["lang_label"] + ": " + short_name(lang))}
  <main id="main" class="article">
    <h1 id="article-title" tabindex="-1">{g["title"]}</h1>
    <p>{g["intro"]}</p>
    <ul style="gap:16px">{items}</ul>
    <p><a href="{home}">{g["back"]}</a></p>
  </main>
  {footer(lang, "../../")}
</div>
{MENU_JS}
"""
    return page(lang, head_html, body_html)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(content)

def build():
    for c in ORDER:
        write(os.path.join(OUT, c, "index.html"), full(c))
    for lang in ART_LANGS:
        write(os.path.join(OUT, lang, GUIDES[lang]["dir"], "index.html"), guides_index(lang))
        for a in ARTICLES:
            write(os.path.join(OUT, lang, GUIDES[lang]["dir"], a[lang]["slug"], "index.html"), article_page(a, lang))
    for f in os.listdir(os.path.join(HERE, "static")):
        shutil.copy(os.path.join(HERE, "static", f), os.path.join(OUT, f))
    alts = "\n".join(f'<link rel="alternate" hreflang="{hl(c)}" href="{url(c)}">' for c in ORDER) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    links = "".join(f'<li><a href="{c}/" lang="{hl(c)}">{L[c]["name"]}</a></li>' for c in ORDER)
    write(os.path.join(OUT, "index.html"),
          CHOOSER.replace("__ALTS__", alts).replace("__LANGS__", json.dumps(ORDER)).replace("__LINKS__", links))
    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    def entry(loc, pairs):
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{UPDATED}</lastmod>")
        for h, u in pairs:
            sm.append(f'    <xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>')
        sm.append("  </url>")
    main_pairs = [(hl(c), url(c)) for c in ORDER] + [("x-default", BASE + "/")]
    for c in ORDER:
        entry(url(c), main_pairs)
    def pairs(urls):
        pr = list(urls.items()) + ([("de-AT", urls["de"])] if "de" in urls else [])
        return pr + [("x-default", urls["en"])]
    gu = {l: guides_url(l) for l in ART_LANGS}
    for lang in ART_LANGS:
        entry(gu[lang], pairs(gu))
    for a in ARTICLES:
        au = {l: art_url(l, a[l]["slug"]) for l in ART_LANGS}
        for lang in ART_LANGS:
            entry(au[lang], pairs(au))
    sm.append("</urlset>")
    write(os.path.join(OUT, "sitemap.xml"), "\n".join(sm) + "\n")
    write(os.path.join(OUT, "impressum.html"), IMPRESSUM)
    write(os.path.join(OUT, "datenschutz.html"), DATENSCHUTZ)
    write(os.path.join(OUT, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    # llms.txt: a plain summary for AI assistants
    llms = ["# DAC7 Check", "",
            "> Free calculator by SortwellStudios (Vienna) that shows EU online sellers whether a platform such as Vinted, eBay, Etsy, Kleinanzeigen or willhaben will report their sales to the tax office under the EU directive DAC7 (Council Directive (EU) 2021/514).",
            "", "Key facts: platforms report a seller who reaches 30 sales or receives more than EUR 2,000 on that platform in one calendar year; each platform counts separately; reports are sent by 31 January for the previous year; a report is not a tax bill. The European Commission proposed in 2026 to raise the limit to EUR 3,000 and drop the 30-sales rule from 2028 at the earliest; not yet adopted.",
            "", "## Checker (22 languages)"] + [f"- [{L[c]['name']}]({url(c)})" for c in ORDER] + ["", "## Guides"]
    for lang in ART_LANGS:
        llms += [f"- [{a[lang]['title']}]({art_url(lang, a[lang]['slug'])}): {a[lang]['desc']}" for a in ARTICLES]
    write(os.path.join(OUT, "llms.txt"), "\n".join(llms) + "\n")
    frag = (head("de", fonts=True) + '<meta name="claude:viewport-fit-sides" content="cover">\n'
            f"<style>{CSS}{EXTRA_CSS}</style>\n" + body("de", ""))
    open(os.path.join(HERE, "preview.html"), "w", encoding="utf-8").write(frag)
    print("built", len(ORDER), "checker pages +", len(ARTICLES) * len(ART_LANGS), "articles in", ART_LANGS)

build()
