# Oltre la Taglia

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
- **`scripts/build_blog.py`** — rigenera tutto `blog/` a partire da
  `content/blog/*.md` e dallo `<style>`/header/footer estratti da
  `mockup/home.html`; sincronizza anche `index.html` (radice) come copia
  di `mockup/home.html`. Va rilanciato (`python3 scripts/build_blog.py`)
  ogni volta che si modifica un articolo o si tocca il design della home,
  altrimenti le pagine blog e la home pubblicata restano disallineate.
- **`index.html`** (radice) — copia di `mockup/home.html`, generata dallo
  script sopra. È quella che Vercel serve per `/`: **non va editata a
  mano**, si edita sempre `mockup/home.html` e poi si rilancia lo script.

## Stato del progetto

Fase di design/contenuti: pagine statiche, dati reali sulle strutture presi
da fonti pubbliche citate (non da verifica telefonica — vedi la sezione
"Come funziona" in home), foto reali montate. Non è un progetto Next.js/
React — è HTML statico generato da uno script Python, pensato per essere
smontato in un vero framework in un secondo momento se serve.

**Non ancora funzionante, da sapere prima del lancio:**
- la barra di ricerca in home non è collegata a nulla (è un mockup visivo);
- il bottone "Inserisci la tua struttura" e i link di contatto in footer
  sono ancora placeholder (`#`), non un vero modulo o indirizzo.

## Deploy

Il repository è pensato per essere collegato come progetto indipendente su
Vercel (o qualsiasi host statico): non condivide root, build o dominio con
altri progetti. Root directory: `/`. Nessuna build necessaria — `index.html`
alla radice e `blog/**/index.html` sono già pronti, basta servirli così
come sono.
