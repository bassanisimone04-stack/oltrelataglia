#!/usr/bin/env python3
"""
Punto di ingresso unico: rigenera blog, strutture/cerca, sincronizza
index.html e scrive sitemap.xml. Da lanciare cosi', invece dei singoli
script, ogni volta che si tocca un contenuto o il design della home:

    python3 scripts/build_all.py
"""
import os
import sys
import html
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_blog
import build_strutture
import build_pages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://www.taglialibera.it"


def write_rss(blog_meta):
    """Feed RSS degli articoli del blog, ordinato dal piu' recente. La data
    di ogni articolo e' quella reale di prima pubblicazione (presa dal
    frontmatter, popolata a sua volta dalla cronologia git)."""
    items_meta = [m for m in blog_meta if m.get("data_pubblicazione")]
    items_meta.sort(key=lambda m: m["data_pubblicazione"], reverse=True)

    def rfc822(iso_date):
        dt = datetime.strptime(iso_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return dt.strftime("%a, %d %b %Y 00:00:00 +0000")

    items = "\n".join(
        f"""  <item>
    <title>{html.escape(m['title'])}</title>
    <link>{BASE_URL}/blog/{m['slug']}/</link>
    <guid>{BASE_URL}/blog/{m['slug']}/</guid>
    <description>{html.escape(m['meta_desc'])}</description>
    <category>{html.escape(m['categoria'])}</category>
    <pubDate>{rfc822(m['data_pubblicazione'])}</pubDate>
  </item>"""
        for m in items_meta
    )
    build_date = rfc822(date.today().isoformat())
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Taglia Libera — Guide</title>
  <link>{BASE_URL}/blog/</link>
  <description>Guide pratiche per chi viaggia con cani di taglia grande e gigante.</description>
  <language>it-IT</language>
  <lastBuildDate>{build_date}</lastBuildDate>
{items}
</channel>
</rss>
"""
    with open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"generata: /feed.xml ({len(items_meta)} articoli)")


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
    write_rss(blog_meta)
