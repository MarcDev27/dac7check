import json, os, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from i18n import L
from i18n2 import L2
L.update(L2)

BASE = "https://www.dac7check.eu"           # change to the real domain before going live
LISTING = "https://www.etsy.com/listing/4616435248/eu-reseller-spreadsheet-202627-vinted"
ORDER = ["en", "bg", "cs", "da", "de", "el", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
CSS = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "base.css"), encoding="utf-8").read()

EXTRA_CSS = """
.topbar { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
.lang { position: relative; background: none; border: 0; padding: 0; border-radius: 0; }
.lang summary { list-style: none; cursor: pointer; font-size: 14px; font-weight: 600; padding: 8px 14px; border-radius: 10px; border: 1px solid var(--line); background: var(--surface); color: var(--fg); }
.lang summary::-webkit-details-marker { display: none; }
.lang[open] summary { border-color: var(--accent); }
.lang ul { position: absolute; right: 0; top: calc(100% + 6px); z-index: 5; margin: 0; padding: 6px; list-style: none; background: var(--surface); border: 1px solid var(--line); border-radius: 12px; min-width: 190px; max-height: 60vh; overflow-y: auto; box-shadow: 0 12px 30px rgba(20, 38, 45, 0.15); }
.lang li a { display: block; padding: 8px 12px; border-radius: 8px; text-decoration: none; color: var(--fg); font-size: 15px; }
.lang li a:hover, .lang li a[aria-current="page"] { background: var(--bg); }
.lang li a[aria-current="page"] { font-weight: 700; }
.counts { display: flex; flex-wrap: wrap; gap: 8px; }
.summary:empty { display: none; }
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
      var bars = '<div class="bars">' +
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
  render();
})();
"""

def url(code):
    return f"{BASE}/{code}/"

def head(code, fonts):
    t = L[code]
    alts = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{url(c)}">' for c in ORDER)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": code,
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    f = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap">\n') if fonts else ""
    return (f'<title>{t["title"]}</title>\n<meta name="description" content="{html.escape(t["desc"])}">\n'
            f'<link rel="canonical" href="{url(code)}">\n{alts}\n{f}'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')

def body(code, prefix):
    t = L[code]
    links = "".join(
        f'<li><a href="{prefix}{c}/index.html" lang="{c}" hreflang="{c}"' + (' aria-current="page"' if c == code else '') + f'>{L[c]["name"]}</a></li>'
        for c in ORDER)
    chips = "".join(f'<span class="chip">{c}</span>' for c in t["chips"])
    items = "".join(f"<li>{i}</li>" for i in t["cta_items"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    js_t = {k: t[k] for k in ["locale", "platforms", "sales", "amount", "on", "st_empty", "st_ok", "st_warn", "st_bad", "why",
                              "r_sales", "r_amount", "room", "room_sales", "room_amount", "bar_sales", "bar_amount", "sum_empty"]}
    return f"""<div class="wrap">
  <header class="topbar">
    <span class="brand"><span class="brand-mark" aria-hidden="true"><span></span><span></span><span></span><span></span></span>Sortwell Studios</span>
    <details class="lang"><summary>{t["lang_label"]}: {t["name"]}</summary><ul>{links}</ul></details>
  </header>
  <section class="intro" aria-labelledby="title">
    <div class="eyebrow">{t["eyebrow"]}</div>
    <h1 id="title">{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="rule-chips">{chips}</div>
  </section>
  <section class="checker" aria-labelledby="check-title">
    <div class="checker-head"><h2 id="check-title">{t["check_title"]}</h2><span class="sample-note" id="sample-note">{t["sample"]}</span></div>
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
  <footer>
    <p>{t["disclaimer"]}</p>
    <nav><a href="{prefix}impressum.html">{t["imprint"]}</a><a href="{prefix}datenschutz.html">{t["privacy"]}</a></nav>
  </footer>
</div>
<script>window.__T = {json.dumps(js_t, ensure_ascii=False)};</script>
<script>{JS}</script>
"""

def full(code):
    return (f'<!doctype html>\n<html lang="{code}">\n<head>\n<meta charset="utf-8">\n'
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
<style>
body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; background: #F3F6F5; color: #14262D; padding: 48px max(16px, env(safe-area-inset-left, 0px)); }
@media (prefers-color-scheme: dark) { body { background: #0F1A1E; color: #E6EEF0; } a { color: #7FC8A9; } }
main { max-width: 520px; margin: 0 auto; } h1 { font-size: 28px; } ul { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
a { color: #1F4E5F; font-weight: 600; font-size: 17px; }
</style>
<script>
(function () {
  var langs = __LANGS__;
  var pref = (navigator.languages || [navigator.language || "en"]).map(function (l) { return l.slice(0, 2).toLowerCase(); });
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
main{max-width:680px;margin:0 auto}h1{font-size:30px;line-height:1.2}h2{font-size:20px;margin-top:32px}a{color:#1F4E5F}hr{border:0;border-top:1px solid #D3DEE1;margin:40px 0}"""

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

def build():
    for c in ORDER:
        os.makedirs(os.path.join(OUT, c), exist_ok=True)
        open(os.path.join(OUT, c, "index.html"), "w", encoding="utf-8").write(full(c))
    alts = "\n".join(f'<link rel="alternate" hreflang="{c}" href="{url(c)}">' for c in ORDER) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    links = "".join(f'<li><a href="{c}/" lang="{c}">{L[c]["name"]}</a></li>' for c in ORDER)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        CHOOSER.replace("__ALTS__", alts).replace("__LANGS__", json.dumps(ORDER)).replace("__LINKS__", links))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for c in ORDER:
        sm.append(f"  <url><loc>{url(c)}</loc>")
        for d in ORDER:
            sm.append(f'    <xhtml:link rel="alternate" hreflang="{d}" href="{url(d)}"/>')
        sm.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>')
        sm.append("  </url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
    open(os.path.join(OUT, "impressum.html"), "w", encoding="utf-8").write(IMPRESSUM)
    open(os.path.join(OUT, "datenschutz.html"), "w", encoding="utf-8").write(DATENSCHUTZ)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    # preview page for the artifact: German, fragment form, links into the language folders
    frag = (head("de", fonts=True) + '<meta name="claude:viewport-fit-sides" content="cover">\n'
            f"<style>{CSS}{EXTRA_CSS}</style>\n" + body("de", ""))
    open(os.path.join(HERE, "preview.html"), "w", encoding="utf-8").write(frag)
    print("built", ORDER)

build()
