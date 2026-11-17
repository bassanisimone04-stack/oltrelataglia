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


# Coordinate reali (proiezione equirettangolare corretta per la latitudine,
# stessa trasformazione usata per la sagoma dell'Italia qui sotto) delle
# capitali/centri di ogni regione, in un viewBox 0 0 100 128. Longitudine e
# latitudine di partenza sono dati geografici noti, non stimati.
REGIONI_MAPPA = [
    ("valle-d-aosta", "Valle d'Aosta", 9.5, 19.1),
    ("piemonte", "Piemonte", 12.3, 26.0),
    ("lombardia", "Lombardia", 23.9, 21.9),
    ("trentino", "Trentino", 38.7, 15.7),
    ("veneto", "Veneto", 47.8, 22.2),
    ("friuli-venezia-giulia", "Friuli-Venezia Giulia", 54.9, 15.7),
    ("liguria", "Liguria", 21.9, 32.8),
    ("emilia-romagna", "Emilia-Romagna", 40.4, 31.9),
    ("toscana", "Toscana", 39.7, 39.4),
    ("umbria", "Umbria", 48.4, 46.2),
    ("marche", "Marche", 57.0, 41.0),
    ("lazio", "Lazio", 49.2, 58.6),
    ("abruzzo", "Abruzzo", 56.1, 54.0),
    ("molise", "Molise", 65.9, 62.2),
    ("campania", "Campania", 62.8, 69.5),
    ("puglia", "Puglia", 82.7, 66.7),
    ("basilicata", "Basilicata", 74.6, 71.7),
    ("calabria", "Calabria", 80.6, 89.5),
    ("sicilia", "Sicilia", 55.8, 97.7),
    ("sardegna", "Sardegna", 23.3, 86.3),
]

# Coordinate geografiche reali (lat, lon) dei capoluoghi/centri di regione,
# usate SOLO per calcolare la distanza in km da "vicino a me" su /cerca/
# (proiezione haversine lato client) — dati noti, non stimati.
REGIONI_LATLON = {
    "valle-d-aosta": (45.737, 7.315),
    "piemonte": (45.070, 7.686),
    "lombardia": (45.464, 9.190),
    "trentino": (46.068, 11.121),
    "veneto": (45.440, 12.315),
    "friuli-venezia-giulia": (46.064, 13.234),
    "liguria": (44.407, 8.934),
    "emilia-romagna": (44.494, 11.343),
    "toscana": (43.769, 11.256),
    "umbria": (43.112, 12.389),
    "marche": (43.616, 13.518),
    "lazio": (41.903, 12.496),
    "abruzzo": (42.351, 13.399),
    "molise": (41.561, 14.668),
    "campania": (40.852, 14.268),
    "puglia": (41.125, 16.867),
    "basilicata": (40.642, 15.805),
    "calabria": (38.910, 16.588),
    "sicilia": (38.116, 13.361),
    "sardegna": (39.223, 9.122),
}


TAGLIA_LABEL = {
    "ogni": "cani di ogni taglia ammessi",
    "gigante": "cani di taglia gigante ammessi",
    "grande": "cani di taglia grande ammessi",
    "media": "cani fino a taglia media ammessi",
}

# Versione compatta usata solo nel <title>: la versione lunga sopra, con
# nomi struttura reali di 25-35 caratteri, sforava spesso i 60-65 caratteri
# raccomandati per i risultati di ricerca (Google tronca il resto).
TAGLIA_LABEL_SHORT = {
    "ogni": "ogni taglia",
    "gigante": "taglia gigante",
    "grande": "taglia grande",
    "media": "taglia media",
}


def build_seo_title(nome, taglia_bucket, limit=65):
    """Costruisce il <title> di una scheda struttura, provando prima la
    forma descrittiva e degradando verso forme piu' corte solo se serve a
    stare sotto il limite — non tronca mai a meta' parola."""
    label = TAGLIA_LABEL.get(taglia_bucket, "cani grandi ammessi")
    full = f"{nome} — {label} | Taglia Libera"
    if len(full) <= limit:
        return full
    short_label = TAGLIA_LABEL_SHORT.get(taglia_bucket, "cani grandi")
    short = f"{nome} — {short_label} | Taglia Libera"
    if len(short) <= limit:
        return short
    return f"{nome} | Taglia Libera"


def truncate_desc(text, limit=155):
    """Accorcia una descrizione alla parola intera piu' vicina al limite,
    invece di tagliarla a meta' parola: una meta description troncata a
    caso in mezzo a una parola sembra rotta nei risultati di ricerca."""
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",.;:") + "…"


def build_faq(st):
    """FAQ della scheda costruite SOLO dai dati gia' presenti (fatti, fonte):
    nessun dato nuovo, e dove la fonte tace lo diciamo."""
    f = dict(st["fatti"])
    nome, fonte = st["nome"], st["fonte_nome"]
    taglia = f.get("Taglia massima", "")
    n_cani = f.get("Numero di cani", "")
    supp = f.get("Supplemento animali", "")
    conferma = "Il dato viene da una fonte pubblica e non è stato verificato per telefono: conferma con la struttura, meglio per iscritto, prima di prenotare."
    faqs = []
    if taglia:
        faqs.append((f"{nome} accetta cani di taglia grande?",
                     f"Taglia massima dichiarata da {fonte}: {taglia}. {conferma}"))
    if n_cani:
        if "Non specificato" in n_cani:
            r = f"La fonte consultata ({fonte}) non indica un numero massimo di cani. Chiedilo alla struttura prima di prenotare, soprattutto se viaggi con più di un cane."
        else:
            r = f"Numero di cani dichiarato da {fonte}: {n_cani}. {conferma}"
        faqs.append((f"Quanti cani si possono portare a {nome}?", r))
    if supp:
        if "Nessuno" in supp:
            r = f"{fonte} non dichiara alcun supplemento per gli animali. Verifica comunque il costo in fase di prenotazione: le condizioni possono cambiare."
        elif "Non" in supp and "fonte" in supp:
            r = f"La fonte consultata ({fonte}) non indica il costo per gli animali. Chiedilo alla struttura prima di prenotare."
        else:
            r = f"Supplemento dichiarato da {fonte}: {supp}. {conferma}"
        faqs.append((f"Quanto costa portare il cane a {nome}?", r))
    return faqs


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>\n(function(){", "</script>")

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
  .simili-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }
  @media (max-width:640px){ .simili-grid{ grid-template-columns:1fr; } }
  .simile-card{ display:block; border:1px solid var(--line); padding:16px; text-decoration:none; transition:border-color .15s ease; }
  .simile-card:hover{ border-color:var(--klein); }
  .simile-card .k{ font-family:'Martian Mono',monospace; font-size:10px; font-weight:600; letter-spacing:.04em; text-transform:uppercase; color:var(--ink-2); }
  .simile-card h3{ margin-top:6px; font-size:15.5px; color:var(--ink); }
  @media print{
    .no-print, header, footer, .simili-grid{ display:none !important; }
    .det-hero{ padding-top:20px !important; }
    body{ background:#fff; color:#000; }
  }
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
  .results-head{ display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; flex-wrap:wrap; gap:10px; }
  .results-count{ font-size:14.5px; font-weight:700; }
  .results-count span{ color:var(--klein-text); }
  .near-me-status{ font-size:13px; color:var(--ink-2); margin-bottom:14px; }
  .stay-dist{ font-family:'Martian Mono',monospace; font-size:11px; color:var(--klein-text); font-weight:600; margin-left:8px; }
  .no-results{ display:none; padding:60px 20px; text-align:center; color:var(--ink-2); border:1px solid var(--line); }
  .no-results.show{ display:block; }
  .map-sec{ border-bottom:1px solid var(--line); padding-block:44px; background:var(--surface-2); }
  .map-sec .wrap{ display:grid; grid-template-columns:1fr 1.3fr; gap:36px; align-items:center; }
  @media (max-width:860px){ .map-sec .wrap{ grid-template-columns:1fr; } }
  .map-sec h2{ font-size:20px; margin-bottom:8px; }
  .map-sec .map-note{ font-size:14px; color:var(--ink-2); max-width:42ch; }
  .map-svg-wrap{ display:flex; justify-content:center; }
  .map-svg-wrap svg{ width:100%; max-width:260px; height:auto; }
  .map-italy-outline{ fill:var(--surface); stroke:var(--line); stroke-width:1.1; }
  .map-region circle{ fill:var(--klein); stroke:var(--surface-2); stroke-width:1.4; transition:transform .15s ease, fill .15s ease; transform-origin:center; transform-box:fill-box; cursor:pointer; }
  .map-region text{ font-family:'Martian Mono',monospace; font-size:6.5px; font-weight:700; fill:var(--on-klein); pointer-events:none; text-anchor:middle; dominant-baseline:central; }
  .map-region:hover circle, .map-region.active circle{ transform:scale(1.22); fill:var(--klein-text); }
  .map-region-empty circle{ fill:var(--line); }
  .map-legend{ display:flex; flex-wrap:wrap; gap:8px 16px; margin-top:18px; }
  .map-legend a{ font-family:inherit; font-size:13px; background:none; border:1px solid var(--line); padding:6px 12px; cursor:pointer; color:var(--ink-2); text-decoration:none; display:inline-block; }
  .map-legend a.active{ border-color:var(--klein); color:var(--klein-text); font-weight:700; }
"""

    # ---------- pagine struttura ----------
    for st in STRUTTURE:
        facts_html = "".join(
            f'<div class="fact"><div class="k">{html.escape(k)}</div><div class="v">{html.escape(v)}</div></div>'
            for k, v in st["fatti"]
        )
        servizi_html = "".join(f"<li>{html.escape(sv)}</li>" for sv in st["servizi"])
        faqs = build_faq(st)
        faq_html = "".join(
            f"<h3 style=\"font-size:16px; margin:18px 0 6px;\">{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in faqs
        )
        faq_section = f'''
      <h2 class="art-h2" style="font-size:20px; margin:36px 0 6px;">Domande frequenti</h2>{faq_html}
      <p style="margin-top:22px;">Prima di prenotare leggi anche le <a href="/blog/domande-da-fare-prima-di-prenotare/">domande da fare alla struttura</a> e guarda le altre <a href="/regione/{st['regione_slug']}/">strutture in {html.escape(st['regione'])}</a>.</p>''' if faqs else ""
        faq_ld = ""
        if faqs:
            faq_ld = "<script type=\"application/ld+json\">\n" + json.dumps({
                "@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
            }, ensure_ascii=False, indent=2) + "\n</script>\n"
        tags_html = "".join(f'<span class="spec spec-hi">{html.escape(t)}</span>' for t in st["tags"])

        # strutture simili: stessa regione, fino a 3, escludendo la struttura stessa
        simili = [s for s in STRUTTURE if s["regione_slug"] == st["regione_slug"] and s["slug"] != st["slug"]][:3]
        simili_html = "".join(
            f'''<a class="simile-card" href="/struttura/{s['slug']}/">
        <span class="k">{html.escape(s['comune'])}</span>
        <h3>{html.escape(s['nome'])}</h3>
      </a>'''
            for s in simili
        )
        simili_section = ""
        if simili:
            simili_section = f'''
      <h2 class="art-h2 no-print" style="font-size:20px; margin:44px 0 14px;">Altre strutture in {html.escape(st['regione'])}</h2>
      <div class="simili-grid">{simili_html}</div>'''

        seo_title = build_seo_title(st['nome'], st.get("taglia_bucket"))
        # Meta description costruita dai dati strutturati (taglia, supplemento,
        # fonte): mette per primo cio' che cerca chi ha un cane grande, invece
        # di tagliare a meta' la descrizione discorsiva della scheda.
        tags_txt = ", ".join(t[0].lower() + t[1:] for t in st.get("tags", [])[:2])
        meta_desc = truncate_desc(
            f"{st['nome']}, {st['comune']}: {tags_txt}. Fonte: {st['fonte_nome']}, da confermare prima di prenotare."
            if tags_txt else st['descrizione'], 155)
        page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
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
      <p class="lbl"><a href="/cerca/" style="text-decoration:none; color:var(--ink-2);">Cerca</a> / <a href="/regione/{st['regione_slug']}/" style="text-decoration:none; color:var(--ink-2);">{html.escape(st['regione'])}</a></p>
      <h1 style="margin-top:10px;">{html.escape(st['nome'])}</h1>
      <p class="det-loc">{html.escape(st['comune'])} · {html.escape(st['regione'])}</p>
      <div class="stay-specs" style="margin-top:16px;">{tags_html}</div>
      <p class="det-source">Dati presi da fonte pubblica: <a href="{st['fonte_url']}" target="_blank" rel="noopener">{html.escape(st['fonte_nome'])}</a> — da confermare direttamente con la struttura prima di prenotare.</p>
      <div class="det-badge">Fonte pubblica, non ancora verificata telefonicamente dal team</div>
      <div class="det-actions">
        <a class="btn btn-klein" href="{st['sito_url']}" target="_blank" rel="noopener">Sito ufficiale ↗</a>
        <a class="btn btn-line" href="/cerca/">&larr; Torna alla ricerca</a>
        <button type="button" class="btn btn-line no-print" onclick="window.print()">Stampa scheda 🖨</button>
      </div>
    </div>
  </section>

  <article class="wrap">
    <div class="det-body">
      <div class="fact-grid">{facts_html}</div>
      <p>{html.escape(st['descrizione'])}</p>
      <h2 class="art-h2" style="font-size:20px; margin-bottom:14px;">Servizi dichiarati</h2>
      <ul class="det-servizi">{servizi_html}</ul>{faq_section}{simili_section}
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
{faq_ld}{header_script}
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

    def struttura_row(st):
        tags_attr = "|".join(st["tags"])
        tags_pill = "".join(f'<span class="spec spec-hi">{html.escape(t)}</span>' for t in st["tags"])
        return f'''      <a class="stay" href="/struttura/{st['slug']}/" data-tags="{html.escape(tags_attr)}" data-regione="{html.escape(st['regione_slug'])}">
        <span class="stay-badge">{st['regione_slug'][:2].upper()}</span>
        <div class="stay-main">
          <h3>{html.escape(st['nome'])}</h3>
          <p class="stay-where">{html.escape(st['comune'])} · {html.escape(st['regione'])}</p>
        </div>
        <div class="stay-specs">{tags_pill}</div>
        <span class="stay-go">Vedi la scheda →</span>
      </a>'''

    rows_html = [struttura_row(st) for st in STRUTTURE]

    # ---------- mappa regioni per /cerca/ ----------
    conteggio_regioni = {}
    for st in STRUTTURE:
        conteggio_regioni[st["regione_slug"]] = conteggio_regioni.get(st["regione_slug"], 0) + 1

    map_circles = []
    for slug, nome, x, y in REGIONI_MAPPA:
        n = conteggio_regioni.get(slug, 0)
        if n > 0:
            r = round(3.4 + (n ** 0.5) * 1.7, 1)
            title = f"{nome}: {n} struttur{'a' if n == 1 else 'e'}"
            map_circles.append(
                f'<a class="map-region" href="/regione/{slug}/" data-regione="{slug}" '
                f'onclick="return selectRegione(\'{slug}\', this)"><title>{html.escape(title)}</title>'
                f'<circle cx="{x}" cy="{y}" r="{r}"></circle>'
                f'<text x="{x}" y="{y}">{n}</text></a>'
            )
        else:
            map_circles.append(
                f'<g class="map-region-empty"><title>{html.escape(nome)}: nessuna struttura ancora</title>'
                f'<circle cx="{x}" cy="{y}" r="1.8"></circle></g>'
            )
    # Sagoma reale dell'Italia (penisola + Sicilia + Sardegna), estratta dal
    # dataset geografico Natural Earth (naturalearth_lowres) e proiettata con
    # una equirettangolare corretta per la latitudine (stessa trasformazione
    # usata per le coordinate di REGIONI_MAPPA sopra) — non e' un contorno
    # disegnato a mano, e' il confine reale semplificato per essere leggibile
    # a piccola scala.
    map_outline = (
        '<path class="map-italy-outline" d="'
        'M33.5 7.2 L38.1 8.6 L39.0 6.7 L46.6 4.9 L48.3 8.5 L59.2 11.1 L58.4 16.2 '
        'L60.3 20.6 L54.2 19.1 L47.9 22.8 L48.3 27.9 L47.4 30.8 L49.9 36.1 '
        'L57.1 41.3 L61.0 49.8 L69.5 58.1 L75.5 58.0 L77.4 60.3 L75.2 62.4 '
        'L87.7 69.2 L94.3 74.6 L95.1 76.5 L93.6 80.2 L89.4 75.4 L82.7 73.7 '
        'L79.5 80.4 L85.0 84.2 L84.1 89.6 L80.9 90.2 L76.8 99.1 L73.6 99.9 '
        'L73.7 96.7 L75.2 91.2 L76.9 89.0 L73.9 83.0 L71.6 77.8 L68.4 76.5 '
        'L66.1 72.0 L61.2 70.2 L57.9 66.0 L52.2 65.4 L46.2 60.7 L39.2 54.0 '
        'L34.0 48.0 L31.6 37.8 L27.8 36.6 L21.5 33.2 L18.0 34.6 L13.6 39.4 '
        'L10.4 40.2 L11.3 35.7 L7.1 34.4 L5.1 26.4 L7.8 23.3 L5.6 19.4 '
        'L5.9 16.5 L9.2 18.7 L12.9 18.2 L17.2 14.7 L18.5 16.3 L22.1 16.0 '
        'L23.8 11.8 L29.5 13.1 L32.9 11.4 Z" />'
        '<path class="map-italy-outline" d="'
        'M58.7 98.6 L72.4 96.5 L69.6 104.6 L70.8 107.8 L69.2 113.1 L63.3 109.3 '
        'L59.4 108.2 L48.7 102.9 L49.8 97.6 Z" />'
        '<path class="map-italy-outline" d="'
        'M20.2 69.0 L24.0 65.8 L28.6 73.1 L27.5 86.8 L24.0 86.1 L20.9 89.6 '
        'L18.0 86.8 L17.7 74.4 L16.0 68.5 Z" />'
    )
    map_svg = (
        '<svg viewBox="0 0 100 128" xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="Mappa dell\'Italia con le regioni e il numero di strutture verificate">'
        + map_outline + "".join(map_circles) + "</svg>"
    )
    map_legend = "".join(
        f'<a href="/regione/{slug}/" data-regione="{slug}" onclick="return selectRegione(\'{slug}\', this)">'
        f'{html.escape(nome)} <span style="color:var(--klein-text);font-weight:700;">{conteggio_regioni[slug]}</span></a>'
        for slug, nome, _, _ in REGIONI_MAPPA if conteggio_regioni.get(slug)
    )

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
<link rel="manifest" href="/manifest.json">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
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

  <section class="map-sec">
    <div class="wrap">
      <div>
        <p class="lbl" style="margin-bottom:8px;">Dove sono</p>
        <h2>La distribuzione geografica, regione per regione.</h2>
        <p class="map-note">
          Ogni cerchio è cliccabile e filtra subito i risultati per regione. Le regioni ancora
          senza strutture verificate restano come puntini grigi — la mappa cresce insieme alla
          directory, non è disegnata su dati che non abbiamo.
        </p>
        <div class="map-legend">{map_legend}</div>
      </div>
      <div class="map-svg-wrap">{map_svg}</div>
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
        <button type="button" class="btn btn-line" id="near-me-btn" style="font-size:13px; padding:9px 14px;">📍 Ordina per vicinanza</button>
      </div>
      <p class="near-me-status" id="near-me-status" hidden></p>
      <div class="stays-table">
        <div class="stays-head">
          <span></span>
          <span>Struttura</span>
          <span>Caratteristiche</span>
          <span>Scheda</span>
        </div>
        <div class="stays" id="stays-list">
{chr(10).join(rows_html)}
        </div>
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
  window.activeRegione = null;

  function setActiveRegioneUI(slug){{
    document.querySelectorAll('.map-region, .map-legend a').forEach(function(el){{
      el.classList.toggle('active', !!slug && el.getAttribute('data-regione') === slug);
    }});
  }}

  window.applyFilters = function applyFilters(){{
    var checked = Array.prototype.slice.call(document.querySelectorAll('.filt-opt input:checked')).map(function(el){{ return el.value; }});
    var rows = document.querySelectorAll('#stays-list .stay');
    var visible = 0;
    rows.forEach(function(row){{
      var tags = (row.getAttribute('data-tags') || '').split('|');
      var matchTag = checked.length === 0 || checked.some(function(c){{ return tags.indexOf(c) !== -1; }});
      var matchRegione = !window.activeRegione || (row.getAttribute('data-regione') || '').indexOf(window.activeRegione) !== -1;
      var match = matchTag && matchRegione;
      row.style.display = match ? '' : 'none';
      if (match) visible++;
    }});
    document.getElementById('results-count').innerHTML = '<span>' + visible + '</span> strutt' + (visible === 1 ? 'ura' : 'ure');
    document.getElementById('no-results').classList.toggle('show', visible === 0);
  }};
  window.resetFilters = function resetFilters(){{
    document.querySelectorAll('.filt-opt input').forEach(function(el){{ el.checked = false; }});
    window.activeRegione = null;
    setActiveRegioneUI(null);
    applyFilters();
    var url = new URL(window.location);
    url.search = '';
    history.replaceState(null, '', url);
    return false;
  }};
  window.selectRegione = function selectRegione(slug, el){{
    window.activeRegione = (window.activeRegione === slug) ? null : slug;
    setActiveRegioneUI(window.activeRegione);
    applyFilters();
    var url = new URL(window.location);
    if (window.activeRegione) url.searchParams.set('regione', window.activeRegione);
    else url.searchParams.delete('regione');
    history.replaceState(null, '', url);
    if (el) el.blur();
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
    window.activeRegione = regione;
    setActiveRegioneUI(regione);
  }}
  applyFilters();

  // "Vicino a me": geolocalizzazione del browser, nessun servizio esterno.
  // La distanza e' calcolata dalla posizione dell'utente al centro
  // geografico della regione di ogni struttura (dato noto, non la sede
  // esatta della struttura, che non abbiamo) — un'approssimazione onesta,
  // dichiarata nel testo del pulsante e nel messaggio di stato.
  var REGIONI_LATLON = {json.dumps({k: list(v) for k, v in REGIONI_LATLON.items()}, ensure_ascii=False)};
  var nearBtn = document.getElementById('near-me-btn');
  var nearStatus = document.getElementById('near-me-status');

  function haversineKm(lat1, lon1, lat2, lon2){{
    var R = 6371;
    var dLat = (lat2 - lat1) * Math.PI / 180;
    var dLon = (lon2 - lon1) * Math.PI / 180;
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
      Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }}

  if (nearBtn) {{
    nearBtn.addEventListener('click', function(){{
      if (!('geolocation' in navigator)) {{
        nearStatus.hidden = false;
        nearStatus.textContent = 'Il browser non supporta la geolocalizzazione.';
        return;
      }}
      nearBtn.disabled = true;
      nearBtn.textContent = 'Sto localizzando…';
      navigator.geolocation.getCurrentPosition(function(pos){{
        var uLat = pos.coords.latitude, uLon = pos.coords.longitude;
        var list = document.getElementById('stays-list');
        var rows = Array.prototype.slice.call(list.querySelectorAll('.stay'));
        rows.forEach(function(row){{
          var rSlug = row.getAttribute('data-regione');
          var coords = REGIONI_LATLON[rSlug];
          var dist = coords ? haversineKm(uLat, uLon, coords[0], coords[1]) : Infinity;
          row.setAttribute('data-dist-km', dist);
          var where = row.querySelector('.stay-where');
          if (where) {{
            var existing = where.querySelector('.stay-dist');
            if (existing) existing.remove();
            var badge = document.createElement('span');
            badge.className = 'stay-dist';
            badge.textContent = isFinite(dist) ? '~' + Math.round(dist) + ' km' : '';
            where.appendChild(badge);
          }}
        }});
        rows.sort(function(a, b){{
          return parseFloat(a.getAttribute('data-dist-km')) - parseFloat(b.getAttribute('data-dist-km'));
        }});
        rows.forEach(function(row){{ list.appendChild(row); }});
        nearBtn.textContent = '📍 Ordinato per vicinanza';
        nearStatus.hidden = false;
        nearStatus.textContent = 'Distanza calcolata dal centro della regione di ogni struttura, non dall\\'indirizzo esatto — un\\'approssimazione, non un dato di precisione.';
      }}, function(){{
        nearBtn.disabled = false;
        nearBtn.textContent = '📍 Ordina per vicinanza';
        nearStatus.hidden = false;
        nearStatus.textContent = 'Non è stato possibile ottenere la tua posizione — controlla i permessi del browser.';
      }});
    }});
  }}
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

    # ---------- /regione/<slug>/index.html ----------
    # Una pagina solo per le regioni che hanno gia' almeno una struttura
    # verificata: una pagina "0 risultati" non porta nulla in piu' di
    # /cerca/ e rischia di leggere come contenuto vuoto per un motore
    # di ricerca.
    regione_slugs = []
    for r_slug, r_nome, _, _ in REGIONI_MAPPA:
        strutture_regione = [st for st in STRUTTURE if st["regione_slug"] == r_slug]
        if not strutture_regione:
            continue
        regione_slugs.append(r_slug)
        n = len(strutture_regione)
        regione_title = f"Hotel e agriturismi cani grandi in {r_nome} | Taglia Libera"
        regione_meta = truncate_desc(
            f"Le {n} struttur{'a' if n == 1 else 'e'} verificate per cani di taglia grande e gigante in "
            f"{r_nome}: hotel, agriturismi e B&B che accettano cani senza i soliti limiti di peso.",
            155,
        )
        regione_rows = "".join(struttura_row(st) for st in strutture_regione)
        regione_page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<title>{html.escape(regione_title)}</title>
<meta name="description" content="{html.escape(regione_meta)}">
<meta property="og:title" content="{html.escape(regione_title)}">
<meta property="og:description" content="{html.escape(regione_meta)}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.taglialibera.it/img/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.taglialibera.it/regione/{r_slug}/">
{style_block}
<style>{cerca_css}</style>
</head>
<body>

{header_block}

<main id="top">
  <section class="cerca-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / <a href="/cerca/" style="text-decoration:none; color:var(--ink-2);">Cerca</a> / {html.escape(r_nome)}</p>
      <h1 style="margin-top:10px;">Cani grandi e giganti benvenuti in {html.escape(r_nome)}.</h1>
      <p style="margin-top:16px; max-width:60ch; font-size:16px; color:var(--ink-2);">
        {n} struttur{'a' if n == 1 else 'e'} verificat{'a' if n == 1 else 'e'} in {html.escape(r_nome)}, ognuna con la fonte citata
        nella scheda. Per filtrare anche per taglia o servizi, usa la
        <a href="/cerca/?regione={r_slug}" style="color:var(--klein-text); text-decoration:underline;">ricerca completa</a>.
      </p>
    </div>
  </section>

  <div class="wrap" style="padding-block:44px 90px;">
    <div class="stays-table">
      <div class="stays-head">
        <span></span>
        <span>Struttura</span>
        <span>Caratteristiche</span>
        <span>Scheda</span>
      </div>
      <div class="stays">
{regione_rows}
      </div>
    </div>
  </div>
</main>

{footer_block}

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.taglialibera.it/"},
        {"@type": "ListItem", "position": 2, "name": "Cerca", "item": "https://www.taglialibera.it/cerca/"},
        {"@type": "ListItem", "position": 3, "name": r_nome, "item": f"https://www.taglialibera.it/regione/{r_slug}/"},
    ],
}, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": i + 1,
            "name": st["nome"],
            "url": f"https://www.taglialibera.it/struttura/{st['slug']}/",
        }
        for i, st in enumerate(strutture_regione)
    ],
}, ensure_ascii=False, indent=2)}
</script>
{header_script}
</body>
</html>
"""
        r_out_dir = os.path.join(ROOT, "regione", r_slug)
        os.makedirs(r_out_dir, exist_ok=True)
        with open(os.path.join(r_out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(regione_page)
        print("generata:", f"/regione/{r_slug}/")

    return {
        "struttura_slugs": [st["slug"] for st in STRUTTURE],
        "regione_slugs": regione_slugs,
    }


if __name__ == "__main__":
    build()
