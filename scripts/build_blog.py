#!/usr/bin/env python3
"""
Genera le pagine /blog/index.html e /blog/<slug>/index.html a partire dai
file Markdown in content/blog/. Riusa lo stesso <style> e header/footer
della home (estratti da mockup/home.html) cosi' il sistema di design resta
uno solo, in un posto solo.

Nessuna dipendenza esterna: parser markdown scritto ad-hoc, perche' il
formato dei file sorgente e' controllato (li abbiamo scritti noi) e non
serve un parser generico.
"""
import re
import html
import glob
import json
import os
from datetime import date as _date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.join(ROOT, "mockup", "home.html")
BLOG_SRC = os.path.join(ROOT, "content", "blog")
OUT_BLOG_DIR = os.path.join(ROOT, "blog")
OG_IMAGE = "https://www.taglialibera.it/img/og-default.jpg"

MESI_IT = {
    "01": "gennaio", "02": "febbraio", "03": "marzo", "04": "aprile",
    "05": "maggio", "06": "giugno", "07": "luglio", "08": "agosto",
    "09": "settembre", "10": "ottobre", "11": "novembre", "12": "dicembre",
}


def data_leggibile(iso_date):
    """'2026-08-30' -> '30 agosto 2026'"""
    y, m, d = iso_date.split("-")
    return f"{int(d)} {MESI_IT[m]} {y}"


def extract(src, start_marker, end_marker):
    i1 = src.index(start_marker)
    i2 = src.index(end_marker, i1) + len(end_marker)
    return src[i1:i2]


def nestify_links(fragment):
    """Le pagine /blog/<slug>/ sono due livelli sotto la root: le ancore
    della home (#cerca, #guide, ecc.) e i link '#top' vanno riscritti come
    percorsi assoluti verso la home, altrimenti scrollano una pagina che
    non esiste."""
    return re.sub(r'href="#', 'href="/#', fragment)


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    assert m, "frontmatter mancante"
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.split("\n"):
        if not line.strip():
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip() for v in val[1:-1].split(",")]
            fm[key] = items
        else:
            fm[key] = val.strip('"')
    return fm, body


def inline_md(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = text.replace("&amp;nbsp;", "&nbsp;")  # &nbsp; nel sorgente non va sfuggito due volte
    return text


def plain_md(text):
    """Come inline_md, ma per il JSON-LD: niente tag, solo testo — i link
    diventano il loro anchor text, il resto non va scappato per l'HTML."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return text.replace("&nbsp;", " ").strip()


def render_body(body):
    """Converte il corpo markdown (H1 + H2 + paragrafi + liste + una
    sezione FAQ finale fatta di coppie **domanda** / risposta) in HTML,
    seguendo esattamente il formato con cui abbiamo scritto gli articoli."""
    lines = body.strip("\n").split("\n")
    out = []
    i = 0
    h1 = None
    in_faq = False
    faq_items = []

    def flush_faq():
        if not faq_items:
            return
        out.append('<div class="faq">')
        for idx, (q, a) in enumerate(faq_items):
            open_attr = " open" if idx == 0 else ""
            out.append(f"<details{open_attr}><summary>{inline_md(q)}<span class=\"plus\">+</span></summary><p>{inline_md(a)}</p></details>")
        out.append("</div>")

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith("# "):
            h1 = line[2:].strip()
            i += 1
            continue

        if line.startswith("## "):
            heading = line[3:].strip()
            if heading.lower().startswith("domande frequenti"):
                in_faq = True
                out.append(f'<h2 class="art-h2">{inline_md(heading)}</h2>')
                i += 1
                continue
            in_faq = False
            out.append(f'<h2 class="art-h2">{inline_md(heading)}</h2>')
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if in_faq and line.startswith("**") and line.rstrip().endswith("**"):
            question = line.strip("*").strip()
            i += 1
            answer_lines = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("**"):
                answer_lines.append(lines[i].strip())
                i += 1
            faq_items.append((question, " ".join(answer_lines)))
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline_md(it)}</li>" for it in items) + "</ul>")
            continue

        if re.match(r"^\d+\.\s", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                items.append(re.sub(r"^\d+\.\s", "", lines[i]).strip())
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline_md(it)}</li>" for it in items) + "</ol>")
            continue

        # paragrafo: accumula righe finche' non trova una riga vuota
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("- ") and not re.match(r"^\d+\.\s", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline_md(' '.join(para))}</p>")

    flush_faq()
    return h1, "\n".join(out), faq_items


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>\n(function(){", "</script>")  # sticky header + scroll reveal

    article_css = """
  .article-hero{ padding:150px 0 40px; border-bottom:1px solid var(--line); }
  .article-hero .lbl{ margin-bottom:14px; }
  .article-hero h1{ font-size:clamp(30px,4.6vw,54px); max-width:20ch; }
  .article-meta{ margin-top:18px; display:flex; gap:16px; flex-wrap:wrap; font-size:13.5px; color:var(--ink-2); }
  .article-body{ max-width:70ch; margin:0 auto; padding-block:64px; }
  .article-body .art-h2{ font-size:clamp(22px,2.8vw,30px); margin-top:52px; margin-bottom:18px; }
  .article-body .art-h2:first-child{ margin-top:0; }
  .article-body p{ font-size:16.5px; line-height:1.72; margin-bottom:18px; }
  .article-body ul, .article-body ol{ margin:0 0 22px; padding-left:22px; display:flex; flex-direction:column; gap:8px; }
  .article-body li{ font-size:16px; line-height:1.6; color:var(--ink-2); }
  .article-body strong{ color:var(--ink); font-weight:700; }
  .article-body a{ color:var(--klein-text); text-decoration:underline; text-underline-offset:2px; }
  .article-body .faq{ margin-top:40px; display:flex; flex-direction:column; gap:10px; }
  .back-row{ margin-top:52px; padding-top:28px; border-top:1px solid var(--line); }
  .related{ margin-top:48px; padding-top:32px; border-top:1px solid var(--line); }
  .related h2{ font-size:15px; margin-bottom:16px; }
  .related-grid{ display:flex; flex-direction:column; gap:12px; }
  .related-grid a{ text-decoration:none; color:var(--ink); font-size:15px; font-weight:600; display:flex; gap:8px; align-items:baseline; }
  .related-grid a span{ color:var(--klein-text); }
"""

    # ---- passata 1: parse di tutti gli articoli ----
    articles = []
    md_files = glob.glob(os.path.join(BLOG_SRC, "[0-9]*.md"))
    md_files.sort(key=lambda p: int(os.path.basename(p).split("-", 1)[0]))
    for md_path in md_files:
        raw = open(md_path, encoding="utf-8").read()
        fm, body = parse_frontmatter(raw)
        h1, body_html, faq_items = render_body(body)
        articles.append({"fm": fm, "h1": h1, "body_html": body_html, "faq_items": faq_items})

    # ---- passata 2: rendering, con "leggi anche" basato sulla stessa categoria ----
    slug_meta = []
    for idx, art in enumerate(articles):
        fm, h1, body_html, faq_items = art["fm"], art["h1"], art["body_html"], art["faq_items"]
        slug = fm["slug"]
        title_seo = fm["titolo_seo"]
        meta_desc = fm["meta_description"]
        categoria = fm["categoria"]
        tempo = fm["tempo_lettura"]
        keyword = fm["keyword_principale"]
        data_pub = fm.get("data_pubblicazione", "")

        stessa_categoria = [a for j, a in enumerate(articles) if j != idx and a["fm"]["categoria"] == categoria]
        altri = [a for j, a in enumerate(articles) if j != idx and a["fm"]["categoria"] != categoria]
        correlati = (stessa_categoria + altri)[:3]
        related_html = "".join(
            f'<a href="/blog/{a["fm"]["slug"]}/">{html.escape(a["h1"])} <span>&rarr;</span></a>'
            for a in correlati
        )

        date_meta = f'<span>Pubblicato il {data_leggibile(data_pub)}</span>' if data_pub else ""

        page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<title>{html.escape(title_seo)}</title>
<meta name="description" content="{html.escape(meta_desc)}">
<meta property="og:title" content="{html.escape(title_seo)}">
<meta property="og:description" content="{html.escape(meta_desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.taglialibera.it/blog/{slug}/">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.taglialibera.it/blog/{slug}/">
{style_block}
<style>{article_css}</style>
</head>
<body>

{header_block}

<main id="top">
  <section class="article-hero">
    <div class="wrap">
      <p class="breadcrumb-lbl lbl" style="margin-bottom:10px;"><a href="/blog/" style="text-decoration:none; color:var(--ink-2);">Guide</a> / {html.escape(categoria)}</p>
      <span class="lbl">{html.escape(categoria)} · {html.escape(tempo)}</span>
      <h1>{html.escape(h1)}</h1>
      <div class="article-meta">
        <span>Keyword principale: <strong style="color:var(--ink);">{html.escape(keyword)}</strong></span>
        {date_meta}
      </div>
    </div>
  </section>

  <article class="wrap">
    <div class="article-body">
{body_html}
      <div class="related">
        <h2 class="lbl">Leggi anche</h2>
        <div class="related-grid">
{related_html}
        </div>
      </div>
      <div class="back-row">
        <a class="btn btn-line" href="/blog/">&larr; Tutte le guide</a>
      </div>
    </div>
  </article>
</main>

{footer_block}

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": h1,
    "description": meta_desc,
    "image": OG_IMAGE,
    "inLanguage": "it-IT",
    "url": f"https://www.taglialibera.it/blog/{slug}/",
    **({"datePublished": data_pub} if data_pub else {}),
    "publisher": {"@type": "Organization", "name": "Taglia Libera"},
}, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.taglialibera.it/"},
        {"@type": "ListItem", "position": 2, "name": "Guide", "item": "https://www.taglialibera.it/blog/"},
        {"@type": "ListItem", "position": 3, "name": h1, "item": f"https://www.taglialibera.it/blog/{slug}/"},
    ],
}, ensure_ascii=False, indent=2)}
</script>
{("" if not faq_items else '''
<script type="application/ld+json">
''' + json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": plain_md(q), "acceptedAnswer": {"@type": "Answer", "text": plain_md(a)}}
        for q, a in faq_items
    ],
}, ensure_ascii=False, indent=2) + '''
</script>
''')}
{header_script}
</body>
</html>
"""
        out_dir = os.path.join(OUT_BLOG_DIR, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        slug_meta.append({
            "slug": slug, "title": h1, "categoria": categoria,
            "tempo": tempo, "meta_desc": meta_desc, "data_pubblicazione": data_pub,
        })
        print("generata:", f"/blog/{slug}/")

    # ---- indice /blog/index.html ----
    cards = []
    for m in slug_meta:
        cards.append(f'''      <a class="post rv" href="/blog/{m['slug']}/" data-categoria="{html.escape(m['categoria'])}">
        <div class="post-body">
          <span class="tag">{html.escape(m['categoria'])}</span>
          <h3>{html.escape(m['title'])}</h3>
          <p>{html.escape(m['meta_desc'])}</p>
          <span class="arrow">→</span>
        </div>
      </a>''')

    categorie = []
    for m in slug_meta:
        if m["categoria"] not in categorie:
            categorie.append(m["categoria"])
    filter_pills = "".join(
        f'<button type="button" class="cat-pill" data-cat="{html.escape(c)}">{html.escape(c)}</button>'
        for c in categorie
    )

    index_page = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<title>Guide per viaggiare con cani grandi | Taglia Libera</title>
<meta name="description" content="Guide pratiche per chi viaggia con cani di taglia grande e gigante: spiagge, mare, normativa, strutture pet friendly senza limiti di peso.">
<meta property="og:title" content="Guide per viaggiare con cani grandi | Taglia Libera">
<meta property="og:description" content="Guide pratiche per chi viaggia con cani di taglia grande e gigante: spiagge, mare, normativa, strutture pet friendly senza limiti di peso.">
<meta property="og:type" content="website">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://www.taglialibera.it/blog/">
<link rel="alternate" type="application/rss+xml" title="Taglia Libera — Guide" href="https://www.taglialibera.it/feed.xml">
{style_block}
<style>{article_css}
  .blog-index-grid{{ display:grid; grid-template-columns:repeat(2,1fr); border:1px solid var(--line); border-top:none; }}
  @media (max-width:820px){{ .blog-index-grid{{ grid-template-columns:1fr; }} }}
  .blog-index-grid .post{{ border-top:1px solid var(--line); }}
  .blog-index-grid .post:nth-child(odd){{ border-right:1px solid var(--line); }}
  @media (max-width:820px){{ .blog-index-grid .post:nth-child(odd){{ border-right:none; }} }}
  .cat-filters{{ display:flex; flex-wrap:wrap; gap:8px; margin-top:24px; }}
  .cat-pill{{ font-family:'Martian Mono',monospace; font-size:11px; text-transform:uppercase; letter-spacing:.04em;
    padding:8px 14px; border:1px solid var(--line); background:var(--surface); color:var(--ink-2); cursor:pointer; }}
  .cat-pill.active{{ background:var(--klein); border-color:var(--klein); color:var(--on-klein); }}
</style>
</head>
<body>

{header_block}

<main id="top">
  <section class="article-hero" style="padding-bottom:56px;">
    <div class="wrap">
      <p class="lbl">Guide</p>
      <h1>Guide per chi viaggia con un cane grande.</h1>
      <p style="margin-top:18px; max-width:62ch; font-size:17px; color:var(--ink-2);">
        Spiagge, mare, normativa e strutture: quello che serve sapere prima di partire con un
        cane di taglia grande o gigante — niente liste di posti non verificati, solo quello che
        possiamo dire con certezza.
      </p>
      <div class="cat-filters" id="cat-filters">
        <button type="button" class="cat-pill active" data-cat="">Tutte</button>
        {filter_pills}
      </div>
    </div>
  </section>

  <section class="wrap" style="padding-block:0 90px;">
    <div class="blog-index-grid" id="blog-grid">
{chr(10).join(cards)}
    </div>
  </section>
</main>

{footer_block}
{header_script}
<script>
(function(){{
  "use strict";
  var pills = document.querySelectorAll("#cat-filters .cat-pill");
  var posts = document.querySelectorAll("#blog-grid .post");
  pills.forEach(function(pill){{
    pill.addEventListener("click", function(){{
      pills.forEach(function(p){{ p.classList.remove("active"); }});
      pill.classList.add("active");
      var cat = pill.getAttribute("data-cat");
      posts.forEach(function(post){{
        var match = !cat || post.getAttribute("data-categoria") === cat;
        post.style.display = match ? "" : "none";
      }});
    }});
  }});
}})();
</script>
</body>
</html>
"""
    os.makedirs(OUT_BLOG_DIR, exist_ok=True)
    with open(os.path.join(OUT_BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)
    print("generata: /blog/index.html")

    return slug_meta


def sync_index():
    """Copia mockup/home.html in index.html alla radice: e' quello che
    Vercel serve per '/'. Tenerli sincronizzati a mano e' un errore
    facile da fare, quindi lo fa questo script."""
    import shutil
    shutil.copyfile(HOME, os.path.join(ROOT, "index.html"))
    print("sincronizzato: /index.html <- mockup/home.html")


if __name__ == "__main__":
    build()
    sync_index()
