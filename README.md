# Taglia Libera

Directory-blog italiana di alloggi pet-friendly (hotel, B&B, agriturismi) per
cani di taglia grande e gigante, senza restrizioni di taglia o numero di
animali. Payoff: *"Il tuo cane, senza taglia, senza limiti."*

## Contenuto del repository

- **`STRATEGY.md`** — brief completo: identità visiva, palette, tipografia,
  copy strategico sezione per sezione, SEO on-page (title/meta/schema
  markup), 11 FAQ, architettura del sito, piano editoriale blog.
- **`mockup/home.html`** — home page statica HTML/CSS/JS, autonoma (nessuna
  dipendenza esterna oltre Google Fonts). Contiene 5 fotografie reali
  incorporate come data URI.
- **`mockup/img/`** — cartella sorgente delle fotografie (vedi il
  `README.md` al suo interno per nomi attesi, formato e licenza).
- **`content/blog/`** — i 5 articoli del blog, in Markdown con frontmatter
  SEO (title tag, meta description, keyword, categoria).
- **`blog/`** — le stesse pagine, già generate in HTML pronto per il deploy
  (`blog/index.html` + una cartella `blog/<slug>/index.html` per articolo),
  con lo stesso sistema di design della home.
- **`scripts/build_all.py`** — punto di ingresso unico: rigenera `blog/`,
  `struttura/`, `cerca/`, sincronizza `index.html` e scrive `sitemap.xml`.
  Va rilanciato (`python3 scripts/build_all.py`) ogni volta che si
  modifica un articolo, una struttura in `content/strutture.py`, o si
  tocca il design della home — altrimenti le pagine generate restano
  disallineate. Usa `scripts/build_blog.py` e `scripts/build_strutture.py`
  internamente; lanciarli da soli rigenera solo la propria parte (utile in
  sviluppo, ma poi va comunque fatto girare `build_all.py` per la sitemap).
- **`index.html`** (radice) — copia di `mockup/home.html`, generata dallo
  script sopra. È quella che Vercel serve per `/`: **non va editata a
  mano**, si edita sempre `mockup/home.html` e poi si rilancia lo script.

## Stato del progetto

Fase di design/contenuti: pagine statiche, dati reali sulle strutture presi
da fonti pubbliche citate (non da verifica telefonica — vedi la sezione
"Come funziona" in home), foto reali montate. Non è un progetto Next.js/
React — è HTML statico generato da uno script Python, pensato per essere
smontato in un vero framework in un secondo momento se serve.

**Rimosso invece di lasciarlo finto:** il bottone "Inserisci la tua
struttura" e i link "Chi siamo / Contatti / Privacy e termini / Accesso
proprietari" in footer non sono stati implementati — richiedono
un'identità legale reale (per la privacy policy) e un'email vera (per il
contatto) che questo progetto non ha ancora. Non li ho lasciati come
placeholder rotti: sono stati tolti finché non c'è un dato vero da
metterci. Quando ci sono, si aggiungono facilmente.

## Deploy

Il repository è pensato per essere collegato come progetto indipendente su
Vercel (o qualsiasi host statico): non condivide root, build o dominio con
altri progetti. Root directory: `/`. Nessuna build necessaria — `index.html`
alla radice e `blog/**/index.html` sono già pronti, basta servirli così
come sono.
