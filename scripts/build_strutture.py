#!/usr/bin/env python3
"""
Genera:
  - /struttura/<slug>/index.html  — una pagina per ognuna delle strutture
    reali in content/strutture.py
  - /cerca/index.html             — elenco con filtro client-side (nessun
    backend: sono solo 3 strutture, il filtro e' un semplice show/hide
    via data-tags)

Riusa <style>/header/footer di mockup/home.html, come scripts/build_blog.py.
"""
import os
import sys
import html
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../content")
from strutture import STRUTTURE, ALL_TAGS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.join(ROOT, "mockup", "home.html")


def extract(src, start_marker, end_marker):
    i1 = src.index(start_marker)
    i2 = src.index(end_marker, i1) + len(end_marker)
    return src[i1:i2]


def nestify_links(fragment):
    import re
    return re.sub(r'href="#', 'href="/#', fragment)


TAGLIA_LABEL = {
    "ogni": "cani di ogni taglia ammessi",
    "gigante": "cani di taglia gigante ammessi",
    "grande": "cani di taglia grande ammessi",
    "media": "cani fino a taglia media ammessi",
}


def truncate_desc(text, limit=155):
    """Accorcia una descrizione alla parola intera piu' vicina al limite,
    invece di tagliarla a meta' parola: una meta description troncata a
    caso in mezzo a una parola sembra rotta nei risultati di ricerca."""
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "…"


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>", "</script>")

    detail_css = """
  .det-hero{ padding:150px 0 40px; border-bottom:1px solid var(--line); }
  .det-hero .lbl{ margin-bottom:10px; }
  .det-hero h1{ font-size:clamp(28px,4vw,46px); max-width:22ch; }
  .det-loc{ margin-top:10px; font-size:15px; color:var(--ink-2); }
  .det-source{ margin-top:14px; font-size:13.5px; color:var(--ink-2); }
  .det-source a{ color:var(--klein-text); text-decoration:underline; }
  .det-badge{
    display:inline-flex; align-items:center; gap:8px; margin-top:18px;
    background:var(--surface-2); border:1px solid var(--line); padding:9px 15px;
    font-size:12.5px; color:var(--ink-2);
  }
  .det-actions{ margin-top:24px; display:flex; gap:10px; flex-wrap:wrap; }
  .det-body{ max-width:70ch; padding-block:56px; }
  .det-body p{ font-size:16.5px; line-height:1.72; margin-bottom:18px; color:var(--ink-2); }
  .fact-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:1px; background:var(--line); border:1px solid var(--line); margin-bottom:40px; }
  @media (max-width:560px){ .fact-grid{ grid-template-columns:1fr; } }
  .fact{ background:var(--surface); padding:20px; }
  .fact .k{ font-family:'Martian Mono',monospace; font-size:10px; font-weight:600; letter-spacing:.04em; text-transform:uppercase; color:var(--ink-2); }
  .fact .v{ margin-top:6px; font-size:15.5px; font-weight:700; color:var(--ink); }
  .det-servizi{ display:flex; flex-direction:column; gap:10px; margin-bottom:20px; }
  .det-servizi li{ font-size:15px; color:var(--ink-2); list-style:none; padding-left:20px; position:relative; }
  .det-servizi li::before{ content:"—"; position:absolute; left:0; color:var(--klein-text); }
"""

    cerca_css = """
  .cerca-hero{ padding:150px 0 36px; border-bottom:1px solid var(--line); }
  .cerca-hero h1{ font-size:clamp(28px,4vw,46px); max-width:22ch; }
  .cerca-layout{ display:grid; grid-template-columns:260px 1fr; gap:32px; padding-block:44px 90px; align-items:start; }
  @media (max-width:860px){ .cerca-layout{ grid-template-columns:1fr; } }
  .filters{ border:1px solid var(--line); padding:22px; position:sticky; top:96px; display:flex; flex-direction:column; gap:14px; }
  @media (max-width:860px){ .filters{ position:static; } }
  .filters h2{ font-size:16px; }
  .filt-opt{ display:flex; align-items:center; gap:10px; font-size:14px; cursor:pointer; }
  .filt-opt input{ accent-color:var(--klein); width:16px; height:16px; flex-shrink:0; }
  .results-head{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:18px; flex-wrap:wrap; gap:10px; }
  .results-count{ font-size:14.5px; font-weight:700; }
  .results-count span{ color:var(--klein-text); }
  .no-results{ display:none; padding:60px 20px; text-align:center; color:var(--ink-2); border:1px solid var(--line); }
  .no-results.show{ display:block; }
"""

    # ---------- pagine struttura ----------
    for st in STRUTTURE:
        facts_html = "".join(
            f'<div class="fact"><div class="k">{html.escape(k)}</div><div class="v">{html.escape(v)}</div></div>'
            for k, v in st["fatti"]
        )
        servizi_html = "".join(f"<li>{html.escape(sv)}</li>" for sv in st["servizi"])
        tags_html = "".join(f'<span class="spec spec-hi">{html.escape(t)}</span>' for t in st["tags"])

        taglia_label = TAGLIA_LABEL.get(st.get("taglia_bucket"), "cani grandi ammessi")
        seo_title = f"{st['nome']} — {taglia_label} | Taglia Libera"
        meta_desc = truncate_desc(st['descrizione'], 155)
        page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<title>{html.escape(seo_title)}</title>
<meta name="description" content="{html.escape(meta_desc)}">
<meta property="og:title" content="{html.escape(seo_title)}">
<meta property="og:description" content="{html.escape(meta_desc)}">
<meta property="og:type" content="place">
<meta property="og:url" content="https://www.taglialibera.it/struttura/{st['slug']}/">
<meta property="og:image" content="https://www.taglialibera.it/img/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.taglialibera.it/struttura/{st['slug']}/">
{style_block}
<style>{detail_css}</style>
</head>
<body>

{header_block}

<main id="top">
  <section class="det-hero">
    <div class="wrap">
      <p class="lbl"><a href="/cerca/" style="text-decoration:none; color:var(--ink-2);">Cerca</a> / {html.escape(st['regione'])}</p>
      <h1 style="margin-top:10px;">{html.escape(st['nome'])}</h1>
      <p class="det-loc">{html.escape(st['comune'])} · {html.escape(st['regione'])}</p>
      <div class="stay-specs" style="margin-top:16px;">{tags_html}</div>
      <p class="det-source">Dati presi da fonte pubblica: <a href="{st['fonte_url']}" target="_blank" rel="noopener">{html.escape(st['fonte_nome'])}</a> — da confermare direttamente con la struttura prima di prenotare.</p>
      <div class="det-badge">Fonte pubblica, non ancora verificata telefonicamente dal team</div>
      <div class="det-actions">
        <a class="btn btn-klein" href="{st['sito_url']}" target="_blank" rel="noopener">Sito ufficiale ↗</a>
        <a class="btn btn-line" href="/cerca/">&larr; Torna alla ricerca</a>
      </div>
    </div>
  </section>

  <article class="wrap">
    <div class="det-body">
      <div class="fact-grid">{facts_html}</div>
      <p>{html.escape(st['descrizione'])}</p>
      <h2 class="art-h2" style="font-size:20px; margin-bottom:14px;">Servizi dichiarati</h2>
      <ul class="det-servizi">{servizi_html}</ul>
    </div>
  </article>
</main>

{footer_block}

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.taglialibera.it/"},
        {"@type": "ListItem", "position": 2, "name": "Cerca", "item": "https://www.taglialibera.it/cerca/"},
        {"@type": "ListItem", "position": 3, "name": st["nome"], "item": f"https://www.taglialibera.it/struttura/{st['slug']}/"},
    ],
}, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "LodgingBusiness",
    "name": st["nome"],
    "description": st["descrizione"],
    "url": st["sito_url"],
    "sameAs": [st["fonte_url"]],
    "address": {
        "@type": "PostalAddress",
        "addressLocality": st["comune"],
        "addressRegion": st["regione"],
        "addressCountry": "IT",
    },
    "additionalProperty": [
        {"@type": "PropertyValue", "name": k, "value": v} for k, v in st["fatti"]
    ],
}, ensure_ascii=False, indent=2)}
</script>
{header_script}
</body>
</html>
"""
        out_dir = os.path.join(ROOT, "struttura", st["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        print("generata:", f"/struttura/{st['slug']}/")

    # ---------- /cerca/index.html ----------
    filters_html = "".join(
        f'<label class="filt-opt"><input type="checkbox" value="{html.escape(t)}" onchange="applyFilters()">{html.escape(t)}</label>'
        for t in ALL_TAGS
    )

    rows_html = []
    for st in STRUTTURE:
        tags_attr = "|".join(st["tags"])
        tags_pill = "".join(f'<span class="spec spec-hi">{html.escape(t)}</span>' for t in st["tags"])
        rows_html.append(f'''      <a class="stay" href="/struttura/{st['slug']}/" data-tags="{html.escape(tags_attr)}" data-regione="{html.escape(st['regione'].lower())}">
        <div class="stay-main">
          <h3>{html.escape(st['nome'])}</h3>
          <p class="stay-where">{html.escape(st['comune'])} · {html.escape(st['regione'])}</p>
        </div>
        <div class="stay-specs">{tags_pill}</div>
        <span class="stay-go">Vedi la scheda →</span>
      </a>''')

    cerca_faq = [
        (
            f"Perché ci sono solo {len(STRUTTURE)} strutture e non centinaia?",
            "Perché ognuna viene aggiunta a mano, con la fonte controllata prima di pubblicarla — "
            "non importiamo automaticamente elenchi da altri portali. Cresce più lentamente di una "
            "directory aggregata, ma ogni scheda che vedi corrisponde a una verifica fatta davvero.",
        ),
        (
            "Da dove vengono i dati di ogni struttura?",
            "Da fonti pubbliche — il sito ufficiale della struttura o un portale specializzato — "
            "sempre linkate nella scheda. Non è ancora una verifica telefonica diretta: il "
            "percorso completo è descritto nella sezione \"Come funziona\" della home.",
        ),
        (
            "Cosa intendete esattamente per taglia \"grande\" e \"gigante\"?",
            "Taglia grande indica indicativamente 25–45 kg, gigante oltre i 45 kg. Quando una "
            "struttura dichiara \"ogni taglia\" senza specificare un tetto, lo riportiamo così "
            "com'è, senza tradurlo in un numero che la fonte non ha dato.",
        ),
        (
            "Posso fidarmi del filtro \"Nessun supplemento\"?",
            "Riflette quello che la fonte dichiarava al momento in cui abbiamo raccolto il dato. "
            "Le condizioni possono cambiare da una stagione all'altra: vale sempre la pena "
            "confermarlo con la struttura prima di prenotare, non solo fidarsi del filtro.",
        ),
        (
            "Perché non ci sono prezzi o valutazioni nelle schede?",
            "Perché non li abbiamo verificati. Un prezzo o un punteggio inventato sarebbe peggio "
            "di nessun dato: meglio una scheda incompleta che una scheda sbagliata.",
        ),
    ]
    cerca_faq_html = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{html.escape(q)}<span class="plus">+</span></summary><p>{html.escape(a)}</p></details>'
        for i, (q, a) in enumerate(cerca_faq)
    )

    cerca_page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<title>Cerca hotel e agriturismi per cani grandi | Taglia Libera</title>
<meta name="description" content="Cerca tra le strutture reali per cani grandi e giganti raccolte in questa directory: filtra per taglia, cani ammessi e servizi.">
<meta property="og:title" content="Cerca hotel e agriturismi per cani grandi | Taglia Libera">
<meta property="og:description" content="Cerca tra le strutture reali per cani grandi e giganti raccolte in questa directory: filtra per taglia, cani ammessi e servizi.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.taglialibera.it/img/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.taglialibera.it/cerca/">
{style_block}
<style>{cerca_css}
  .cerca-faq{{ padding-block:70px; border-top:1px solid var(--line); background:var(--surface); }}
  .cerca-faq .faq{{ max-width:760px; margin:0 auto; display:flex; flex-direction:column; gap:10px; }}
</style>
</head>
<body>

{header_block}

<main id="top">
  <section class="cerca-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Cerca</p>
      <h1 style="margin-top:10px;">Le strutture reali di questa directory.</h1>
      <p style="margin-top:16px; max-width:60ch; font-size:16px; color:var(--ink-2);">
        Sono {len(STRUTTURE)}, non 500: crescono una alla volta, verificata scheda per scheda.
        Filtra per quello che conta davvero con un cane grande.
      </p>
    </div>
  </section>

  <div class="wrap cerca-layout">
    <aside class="filters">
      <h2>Filtra</h2>
{filters_html}
      <a href="/cerca/" class="btn btn-line" style="justify-content:center; margin-top:6px;" onclick="return resetFilters()">Azzera filtri</a>
    </aside>

    <div>
      <div class="results-head">
        <div class="results-count" id="results-count"><span>{len(STRUTTURE)}</span> strutture</div>
      </div>
      <div class="stays-head">
        <span>Struttura</span>
        <span>Caratteristiche</span>
        <span>Scheda</span>
      </div>
      <div class="stays" id="stays-list">
{chr(10).join(rows_html)}
      </div>
      <div class="no-results" id="no-results">Nessuna struttura corrisponde a questi filtri. Prova ad azzerarli — la directory è ancora piccola.</div>
    </div>
  </div>

  <section class="cerca-faq">
    <div class="wrap">
      <p class="lbl" style="margin-bottom:10px; text-align:center;">Domande frequenti</p>
      <h2 style="text-align:center; font-size:clamp(24px,3vw,34px); margin-bottom:34px;">Come funziona questa ricerca.</h2>
      <div class="faq">{cerca_faq_html}</div>
    </div>
  </section>
</main>

{footer_block}

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.taglialibera.it/"},
        {"@type": "ListItem", "position": 2, "name": "Cerca", "item": "https://www.taglialibera.it/cerca/"},
    ],
}, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in cerca_faq
    ],
}, ensure_ascii=False, indent=2)}
</script>
{header_script}
<script>
(function(){{
  "use strict";
  window.applyFilters = function applyFilters(){{
    var checked = Array.prototype.slice.call(document.querySelectorAll('.filt-opt input:checked')).map(function(el){{ return el.value; }});
    var rows = document.querySelectorAll('#stays-list .stay');
    var visible = 0;
    rows.forEach(function(row){{
      var tags = (row.getAttribute('data-tags') || '').split('|');
      var match = checked.length === 0 || checked.some(function(c){{ return tags.indexOf(c) !== -1; }});
      row.style.display = match ? '' : 'none';
      if (match) visible++;
    }});
    document.getElementById('results-count').innerHTML = '<span>' + visible + '</span> strutt' + (visible === 1 ? 'ura' : 'ure');
    document.getElementById('no-results').classList.toggle('show', visible === 0);
  }};
  window.resetFilters = function resetFilters(){{
    document.querySelectorAll('.filt-opt input').forEach(function(el){{ el.checked = false; }});
    applyFilters();
    return false;
  }};

  // pre-filtro da querystring (?tag=..., ?regione=..., ?taglia=grande|gigante)
  var params = new URLSearchParams(window.location.search);
  var tag = params.get('tag');
  if (tag) {{
    var box = document.querySelector('.filt-opt input[value="' + CSS.escape(tag) + '"]');
    if (box) box.checked = true;
  }}
  var regione = (params.get('regione') || '').trim().toLowerCase();
  if (regione) {{
    document.querySelectorAll('#stays-list .stay').forEach(function(row){{
      if ((row.getAttribute('data-regione') || '').indexOf(regione) === -1) row.style.display = 'none';
    }});
  }}
  applyFilters();
}})();
</script>
</body>
</html>
"""
    out_dir = os.path.join(ROOT, "cerca")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(cerca_page)
    print("generata: /cerca/")

    return [st["slug"] for st in STRUTTURE]


if __name__ == "__main__":
    build()
