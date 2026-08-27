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
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.join(ROOT, "mockup", "home.html")
BLOG_SRC = os.path.join(ROOT, "content", "blog")
OUT_BLOG_DIR = os.path.join(ROOT, "blog")


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
    return h1, "\n".join(out)


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>", "</script>")  # sticky header + scroll reveal

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
"""

    slug_meta = []
    for md_path in sorted(glob.glob(os.path.join(BLOG_SRC, "0*.md"))):
        raw = open(md_path, encoding="utf-8").read()
        fm, body = parse_frontmatter(raw)
        h1, body_html = render_body(body)
        slug = fm["slug"]
        title_seo = fm["titolo_seo"]
        meta_desc = fm["meta_description"]
        categoria = fm["categoria"]
        tempo = fm["tempo_lettura"]
        keyword = fm["keyword_principale"]

        page = f"""<title>{html.escape(title_seo)}</title>
<meta name="description" content="{html.escape(meta_desc)}">
<meta property="og:title" content="{html.escape(title_seo)}">
<meta property="og:description" content="{html.escape(meta_desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.oltrelataglia.it/blog/{slug}/">
<link rel="canonical" href="https://www.oltrelataglia.it/blog/{slug}/">
{style_block}
<style>{article_css}</style>

{header_block}

<main id="top">
  <section class="article-hero">
    <div class="wrap">
      <p class="breadcrumb-lbl lbl" style="margin-bottom:10px;"><a href="/blog/" style="text-decoration:none; color:var(--ink-2);">Guide</a> / {html.escape(categoria)}</p>
      <span class="lbl">{html.escape(categoria)} · {html.escape(tempo)}</span>
      <h1>{html.escape(h1)}</h1>
      <div class="article-meta">
        <span>Keyword principale: <strong style="color:var(--ink);">{html.escape(keyword)}</strong></span>
      </div>
    </div>
  </section>

  <article class="wrap">
    <div class="article-body">
{body_html}
      <div class="back-row">
        <a class="btn btn-line" href="/blog/">&larr; Tutte le guide</a>
      </div>
    </div>
  </article>
</main>

{footer_block}

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {html.escape(h1)!r},
  "description": {meta_desc!r},
  "inLanguage": "it-IT",
  "url": "https://www.oltrelataglia.it/blog/{slug}/",
  "publisher": {{ "@type": "Organization", "name": "Oltre la Taglia" }}
}}
</script>

<script>{header_script}</script>
"""
        out_dir = os.path.join(OUT_BLOG_DIR, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        slug_meta.append({
            "slug": slug, "title": h1, "categoria": categoria,
            "tempo": tempo, "meta_desc": meta_desc,
        })
        print("generata:", f"/blog/{slug}/")

    # ---- indice /blog/index.html ----
    cards = []
    for m in slug_meta:
        cards.append(f'''      <a class="post rv" href="/blog/{m['slug']}/">
        <div class="post-body">
          <span class="tag">{html.escape(m['categoria'])}</span>
          <h3>{html.escape(m['title'])}</h3>
          <p>{html.escape(m['meta_desc'])}</p>
          <span class="arrow">→</span>
        </div>
      </a>''')

    index_page = f"""<title>Guide</title>
<meta name="description" content="Guide pratiche per chi viaggia con cani di taglia grande e gigante: spiagge, mare, normativa, strutture pet friendly senza limiti di peso.">
<link rel="canonical" href="https://www.oltrelataglia.it/blog/">
{style_block}
<style>{article_css}
  .blog-index-grid{{ display:grid; grid-template-columns:repeat(2,1fr); border:1px solid var(--line); border-top:none; }}
  @media (max-width:820px){{ .blog-index-grid{{ grid-template-columns:1fr; }} }}
  .blog-index-grid .post{{ border-top:1px solid var(--line); }}
  .blog-index-grid .post:nth-child(odd){{ border-right:1px solid var(--line); }}
  @media (max-width:820px){{ .blog-index-grid .post:nth-child(odd){{ border-right:none; }} }}
</style>

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
    </div>
  </section>

  <section class="wrap" style="padding-block:0 90px;">
    <div class="blog-index-grid">
{chr(10).join(cards)}
    </div>
  </section>
</main>

{footer_block}
<script>{header_script}</script>
"""
    os.makedirs(OUT_BLOG_DIR, exist_ok=True)
    with open(os.path.join(OUT_BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)
    print("generata: /blog/index.html")

    return slug_meta


if __name__ == "__main__":
    build()
