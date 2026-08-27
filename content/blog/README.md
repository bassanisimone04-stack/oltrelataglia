# Articoli del blog

Cinque articoli completi, pronti per essere pubblicati come pagine
`/blog/[slug]` una volta costruita quella parte del sito.

| File | Slug | Keyword principale |
|------|------|---------------------|
| `01-spiagge-cani-taglia-grande-gigante.md` | `spiagge-cani-taglia-grande-gigante` | spiagge per cani taglia grande |
| `02-colpo-di-calore-cane-gigante-mare.md` | `colpo-di-calore-cane-gigante-mare` | colpo di calore cane estate mare |
| `03-regolamento-cani-spiaggia-molossoidi.md` | `regolamento-cani-spiaggia-molossoidi` | regolamento cani in spiaggia italia |
| `04-hotel-villaggi-cani-taglia-gigante.md` | `hotel-villaggi-cani-taglia-gigante` | hotel pet friendly cani taglia grande |
| `05-bagno-mare-cane-gigante-sicurezza.md` | `bagno-mare-cane-gigante-sicurezza` | cani grandi bagno in mare |

## Formato

Markdown con front-matter YAML in testa a ogni file: `titolo_seo` (title
tag pronto, sotto i 60 caratteri dove possibile), `meta_description`
(sotto i 155 caratteri), `keyword_principale`, `keyword_correlate`,
`categoria`, `tempo_lettura`. Il corpo è già strutturato con H1/H2,
paragrafi e una mini-FAQ finale, coerente con lo stile del resto del sito.

## Una nota su cosa NON contengono

Seguendo la stessa regola applicata al resto del sito (vedi la sezione 7
di `STRATEGY.md` nel repository `avvisy` e i commit di pulizia dati di
`oltrelataglia`): **nessuna statistica, nome di struttura o dato tecnico
inventato**.

- Non sono stati inseriti elenchi di spiagge o hotel specifici non
  verificati — l'articolo 1 spiega il metodo per valutarli, non fornisce
  una lista fittizia.
- L'articolo 3 (normativa) descrive il quadro legale reale italiano
  (assenza di una legge nazionale unica, competenza di ordinanze
  comunali e Capitanerie di Porto, obbligo di iscrizione all'anagrafe
  canina) senza attribuire regole specifiche a comuni inventati.
- L'articolo 4 cita **una sola struttura reale** (Agriturismo Bellavita,
  già presente e verificato-alla-fonte nella home page), con link diretto
  alla pagina che dichiara le condizioni — non una lista di "catene
  alberghiere" inventate.
- Gli articoli 2 e 5 (salute/sicurezza) contengono solo informazioni
  di buon senso veterinario ampiamente condivise (rischio di colpo di
  calore, gestione del sale su pelle e orecchie, uso del salvagente),
  senza percentuali o studi citati che non potremmo verificare.

## Prossimo passo

Wireware le pagine `/blog/[slug]` nel sito vero e collegare le card già
presenti in home (`#guide`) ai rispettivi articoli.
