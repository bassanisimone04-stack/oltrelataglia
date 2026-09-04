#!/usr/bin/env python3
"""
Audit SEO automatico basato sulle parole chiave dichiarate in ogni
articolo/scheda struttura. Non inventa nulla e non riscrive contenuti:
segnala solo dove keyword_principale/keyword_correlate non compaiono
dove Google le cerca di più (title, meta description, H1, corpo).

Pensato per girare ad ogni build (richiamato da build_all.py) cosi'
un problema di copertura keyword si vede subito, non solo quando
qualcuno lo nota manualmente mesi dopo.

Uscita: un report testuale. Non blocca la build (nessun sys.exit
diverso da 0) — e' un controllo di qualita', non un errore fatale.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(ROOT, "content", "blog")

sys.path.insert(0, os.path.join(ROOT, "content"))
from strutture import STRUTTURE  # noqa: E402


def parse_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, ""
    fm_raw, body = parts[1], parts[2]
    fm = {}
    for line in fm_raw.strip().splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def parse_keyword_list(raw):
    """keyword_correlate: [a, b, c] -> ['a', 'b', 'c']"""
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [k.strip().strip('"') for k in raw.split(",") if k.strip()]


def norm(s):
    return re.sub(r"\s+", " ", s.lower().strip())


def check_presence(keyword, *texts):
    kw = norm(keyword)
    return any(kw in norm(t) for t in texts if t)


def audit_blog():
    issues = []
    files = sorted(f for f in os.listdir(BLOG_DIR) if f.endswith(".md") and f != "README.md")
    for fname in files:
        path = os.path.join(BLOG_DIR, fname)
        fm, body = parse_frontmatter(path)
        if fm is None:
            issues.append((fname, "frontmatter non trovato o malformato"))
            continue

        slug = fm.get("slug", fname)
        kw = fm.get("keyword_principale", "")
        titolo = fm.get("titolo_seo", "")
        meta = fm.get("meta_description", "").strip('"')
        correlate = parse_keyword_list(fm.get("keyword_correlate", ""))

        h1_match = re.search(r"^#\s+(.+)$", body, re.M)
        h1 = h1_match.group(1) if h1_match else ""
        # primi ~150 parole del corpo (esclude l'H1 stesso), per il check "keyword nel primo paragrafo"
        body_no_h1 = body[h1_match.end():] if h1_match else body
        first_words = " ".join(body_no_h1.split()[:150])

        if not kw:
            issues.append((slug, "nessuna keyword_principale dichiarata"))
            continue

        if not check_presence(kw, titolo):
            issues.append((slug, f'keyword_principale "{kw}" assente dal titolo_seo ("{titolo}")'))
        if not check_presence(kw, meta):
            issues.append((slug, f'keyword_principale "{kw}" assente dalla meta_description'))
        if not check_presence(kw, h1):
            issues.append((slug, f'keyword_principale "{kw}" assente dall\'H1 ("{h1}")'))
        if not check_presence(kw, first_words):
            issues.append((slug, f'keyword_principale "{kw}" assente dal primo paragrafo'))

        for ck in correlate:
            if not check_presence(ck, body):
                issues.append((slug, f'keyword_correlate "{ck}" mai citata nel corpo dell\'articolo'))

    return issues


def audit_strutture():
    issues = []
    seen_titles = {}
    for st in STRUTTURE:
        slug = st["slug"]
        # ogni scheda struttura deve poter essere trovata cercando "nome + comune"
        # e "nome + taglia grande/gigante": controlliamo che questi elementi
        # compaiano tutti nella descrizione, dato che il <title>/<meta> sono
        # generati automaticamente da essi (vedi build_seo_title in build_strutture.py)
        desc = st.get("descrizione", "")
        if st["comune"].split(",")[0].split("(")[0].strip() not in desc:
            issues.append((slug, f'il comune "{st["comune"]}" non compare nella descrizione'))
        seen_titles.setdefault(st["nome"], []).append(slug)

    for nome, slugs in seen_titles.items():
        if len(slugs) > 1:
            issues.append((", ".join(slugs), f'nome struttura duplicato: "{nome}"'))

    return issues


def main():
    print("=== SEO audit: articoli blog ===")
    blog_issues = audit_blog()
    if not blog_issues:
        print("Nessun problema di copertura keyword negli articoli.")
    else:
        for slug, msg in blog_issues:
            print(f"  [{slug}] {msg}")
        print(f"Totale: {len(blog_issues)} segnalazioni su articoli.")

    print()
    print("=== SEO audit: schede struttura ===")
    st_issues = audit_strutture()
    if not st_issues:
        print("Nessun problema sulle schede struttura.")
    else:
        for slug, msg in st_issues:
            print(f"  [{slug}] {msg}")
        print(f"Totale: {len(st_issues)} segnalazioni su strutture.")

    return len(blog_issues) + len(st_issues)


if __name__ == "__main__":
    main()
