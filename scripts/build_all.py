#!/usr/bin/env python3
"""
Punto di ingresso unico: rigenera blog, strutture/cerca, sincronizza
index.html e scrive sitemap.xml. Da lanciare cosi', invece dei singoli
script, ogni volta che si tocca un contenuto o il design della home:

    python3 scripts/build_all.py
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_blog
import build_strutture
import build_pages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://www.oltrelataglia.it"


def write_sitemap(blog_slugs, struttura_slugs, static_slugs):
    today = date.today().isoformat()
    urls = [("", 1.0), ("cerca/", 0.9), ("blog/", 0.8)]
    urls += [(f"blog/{s}/", 0.6) for s in blog_slugs]
    urls += [(f"struttura/{s}/", 0.7) for s in struttura_slugs]
    urls += [(f"{s}/", 0.3) for s in static_slugs]

    entries = "\n".join(
        f"""  <url>
    <loc>{BASE_URL}/{path}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>"""
        for path, priority in urls
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"generata: /sitemap.xml ({len(urls)} url)")


if __name__ == "__main__":
    blog_meta = build_blog.build()
    struttura_slugs = build_strutture.build()
    static_slugs = build_pages.build()
    build_blog.sync_index()
    blog_slugs = [m["slug"] for m in blog_meta]
    write_sitemap(blog_slugs, struttura_slugs, static_slugs)
