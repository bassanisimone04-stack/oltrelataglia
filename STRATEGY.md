# Oltre la Taglia — Directory-Blog per Alloggi Pet-Friendly Senza Restrizioni

> **Nicchia**: hotel, B&B e agriturismi italiani che accettano cani di taglia
> grande/gigante e/o più di un cane, senza le limitazioni tipiche del
> "pet-friendly generico" (1 cane, max 10kg).
> **Nome**: **Oltre la Taglia** (dominio `oltrelataglia.it`) — payoff:
> *"Il tuo cane, senza taglia, senza limiti."*
> Nomi alternativi valutati: CaniGrandi.it (troppo simile a un exact-match
> domain, poco protetto/proteggibile), DogSizeFree, SenzaTaglia. "Cani
> grandi"/"taglia grande" restano comunque le keyword a maggior volume
> **nei title tag, nelle meta description e nei contenuti**, anche se il
> brand non le contiene letteralmente — è la keyword strategy a portare
> traffico, non il nome del dominio.
> 🖼️ **Mockup**: la home in versione definitiva vive nel repo come file vero
> — `pet-friendly-directory/mockup/home.html` — ed è pubblicata come artifact
> (link nei messaggi dell'assistente). Direzione v3: blu Klein, tipografia
> Onest + Martian Mono, campo 3D di ossi renderizzato in tempo reale. Le
> pagine `/cerca` e `/struttura/[slug]` esistono come artifact nella
> direzione v2 (Fraunces) e vanno riallineate alla v3.
>
> 📸 **Sulle foto**: i mockup non contengono fotografie. L'ambiente in cui
> vengono pubblicati questi artifact blocca il caricamento di immagini da
> host esterni (niente stock photo, niente foto delle strutture) e in questa
> sessione non è disponibile uno strumento di generazione immagini. Il campo
> 3D è la risposta progettuale a quel vincolo, non un segnaposto. In sviluppo
> reale servono fotografie vere delle strutture (con licenza o permesso del
> gestore) ovunque si voglia mostrare *la struttura*; il 3D resta dove si
> vuole mostrare *il brand*, cioè hero e testate di sezione.
>
> 🐕 **Dati reali nelle card struttura**: le strutture mostrate nei mockup
> (Agriturismo Bellavita, Baita Gorck, Masseria Le Terrazze di Serranova,
> Podere il Poggiolo, Agriturismo Podere Bello) sono reali, con taglia/numero
> cani e servizi presi da fonti pubbliche citate in ogni card — non da
> verifica telefonica diretta (il processo descritto nella sezione 3 resta
> il metodo da applicare prima del lancio). Nessun prezzo o punteggio è
> stato inventato: dove non disponibile, il dato è stato omesso invece di
> stimarlo. Fonti: [agriturismobellavita.it](https://www.agriturismobellavita.it/agriturismo-per-animali/),
> [dogwelcome.it — Baita Gorck](https://www.dogwelcome.it/strutture-cani-animali-ammessi/rifugi-e-baite/italia/trentino-alto-adige/trento/rifugio-gorck),
> [dogwelcome.it — Terrazze di Serranova](https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/puglia/brindisi/masseria-le-terrazze-di-serranova),
> [podereilpoggiolo.it](https://www.podereilpoggiolo.it/en/services/holiday-with-your-pets.html),
> [dogwelcome.it — Podere Bello](https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/toscana/grosseto/agriturismo-podere-bello).

Documento di riferimento per Design (UI/UX), Copy strategico e SEO on-page
della home page e dell'architettura del sito. Pensato per essere passato
direttamente a uno sviluppatore front-end (stack consigliato: Next.js 15 +
Tailwind CSS v4, coerente con gli altri progetti del repository).

---

## 0. Posizionamento e razionale

Il mercato "pet-friendly" in Italia è enorme ma **generico e inaffidabile**:
la maggior parte delle OTA (Booking, Airbnb) etichetta come "pet friendly"
strutture che in realtà impongono un tetto di peso (spesso 10 kg) o un solo
animale, scoperto solo al check-in. Chi possiede un Alano, un Pastore
Maremmano, due Labrador o un branco di cani da soccorso deve scrivere email
una per una per verificare le regole reali.

**La promessa del brand**: ogni struttura in vetrina è stata *verificata
manualmente* sui 4 punti che contano davvero — taglia massima ammessa,
numero massimo di animali, spazi comuni accessibili, eventuali supplementi —
zero sorprese al check-in.

Questo è anche il differenziale SEO: intercettiamo query transazionali che
i grandi portali non filtrano ("hotel cani taglia grande", "b&b 2 cani
ammessi"), a bassa concorrenza e altissima intenzione.

---

## 1. IDENTITÀ VISIVA E LINEE GUIDA DI DESIGN (UI/UX)

### 1.1 Palette colori

> ⚠️ **Palette definitiva (v3)** — derivata dal riferimento visivo fornito
> dal committente. Il principio è **un solo accento a piena forza**: niente
> corallo, niente giallo, niente verde semantico. Tutta l'energia della
> pagina sta nel blu Klein; tutto il resto è nero, off-white e una scala di
> grigi con bias lavanda (i neutri "tendono" verso l'accento, non sono grigi
> neutri di default).

| Ruolo | Colore | Hex | Uso |
|---|---|---|---|
| Accento unico | Blu Klein | `#1B1BE8` | Ticker, CTA finale, tag, etichette dati, hover dei chip |
| Nero | Inchiostro | `#0B0B11` | Testo, bottoni pieni, campo 3D |
| Sfondo pagina | Off-white lavanda | `#F0EFF7` | Ground chiaro (mai bianco puro) |
| Superficie | Bianco | `#FFFFFF` | Card, righe struttura in hover |
| Superficie alt. | Lavanda chiara | `#E7E6F1` | Fascia sezione strutture |
| Testo secondario | Grigio-lavanda | `#56566A` | Paragrafi, etichette |
| Filetti | Lavanda tenue | `#D9D8E6` | Bordi e separatori a 1px |

In tema scuro il blu passa a `#2E2EF5` per i riempimenti e `#8E8EFF` per il
testo, così l'accento resta leggibile su fondo nero. **Il campo 3D resta
scuro in entrambi i temi**: è un oggetto grafico, non una superficie di
lettura, ed è dipinto con token propri (`--band`, `--band-ink`).

**Regola di contrasto ereditata dalle versioni precedenti, ancora valida.**
Ogni colore ad alto impatto ha una variante *fill* (decorativa) e una
variante *text-safe* (più scura o più chiara a seconda del fondo): non
riusare mai il valore decorativo come colore di testo. Nella palette v3 lo
si vede sul blu, che in tema scuro si sdoppia in `#2E2EF5` per i
riempimenti e `#8E8EFF` per il testo.

### 1.2 Tipografia

> ⚠️ **Direzione definitiva (v3)**. Le versioni precedenti sono state
> scartate dal committente: i font "bubble" (Fredoka, Baloo 2, Grandstander)
> risultavano infantili, la successiva serif editoriale (Fraunces) risultava
> priva di carattere. La direzione attuale nasce da un riferimento visivo
> fornito dal committente — sito di uno studio 3D, con blu elettrico su
> nero e off-white, tipografia enorme e un oggetto tridimensionale come
> protagonista della hero.

- **Titoli e corpo — un'unica famiglia**: *Onest* (400–800), grottesca
  geometrica con x-height alta e terminali netti; è il parente libero più
  vicino alle neo-grottesche svizzere usate dagli studi di design. Usare un
  solo carattere su tutta la pagina è una scelta deliberata: è ciò che fanno
  i siti del riferimento, e sposta il carattere sulla **scala** (titoli fino
  a 88px, interlinea 0.94, tracking −0.035em) invece che sulla varietà di
  font. Fallback: `system-ui, sans-serif`.
- **Etichette dati**: *Martian Mono* (500), monospace molto larga, riservata
  alle micro-etichette maiuscole (taglia max, numero cani, numerazione dei
  passaggi). La sua larghezza inusuale è il rischio estetico voluto: fa
  leggere quei dati come misurazioni strumentali, che è esattamente la
  promessa del brand. Fallback: `ui-monospace, monospace`.

### 1.2bis L'oggetto 3D

La hero non ospita una foto ma un **render tridimensionale in tempo reale**:
un grappolo di ossi che ruota lentamente, con parallasse legata al puntatore.
È scritto a mano come piccolo motore software su Canvas 2D — rotazione 3D,
proiezione prospettica, ordinamento per profondità, ombreggiatura di sfere e
cilindri — senza librerie esterne, perché l'ambiente di pubblicazione blocca
le CDN (quindi niente three.js). Pesa pochi KB e sospende il ciclo di
animazione quando esce dal viewport.

Ogni osso è modellato come un'asta con **quattro nocche**, due per estremità,
perché è la sagoma che si riconosce all'istante come osso da cane; una
capsula liscia leggeva come tubo astratto. Traduce nel mondo pet ciò che nel
riferimento fornito dal committente erano tubi geometrici: stessa idea di
oggetto scultoreo, ma inequivocabilmente canina. Sostituisce le illustrazioni
vettoriali piatte delle versioni precedenti.
- **Dati/etichette (taglia, n° cani, prezzo)**: *IBM Plex Mono* — lasciata
  volutamente "tecnica" e non arrotondata: il contrasto con il resto della
  UI rinforza il concetto di "specifica verificata" (come un'etichetta da
  scheda tecnica), usata per pillole informative, eyebrow ed etichette dei
  filtri.
- Scala tipografica mobile-first: H1 28–32px, H2 22–24px, body 16px, small 14px.
- Line-height generoso (1.5–1.6) per leggibilità in mobilità (turisti che
  cercano da smartphone in auto/in stazione).
- Tutti e tre i font sono disponibili su Google Fonts, caricabili con un
  singolo `<link>`/`@import` per performance.

### 1.3 Iconografia e immagini

- Iconografia a **linea arrotondata (rounded stroke)**, coerente con il tono
  "accogliente": zampa, valigia, casa, recinto, ciotola, guinzaglio.
- Fotografia: cani di **taglia grande/gigante reali** (mai stock con Chihuahua
  in borsetta — è l'errore numero uno che allontana il target). Foto
  luminose, ambienti open air, aree verdi, spiagge.
- Badge distintivo ricorrente: "✅ Verificato Oltre la Taglia — nessun limite di
  taglia" da usare su card, hero, meta immagini social.

### 1.4 Principi UX

1. **Mobile-first assoluto**: 70%+ del traffico stimato da mobile (ricerche
   last-minute in viaggio). Barra di ricerca sticky su scroll mobile.
2. **Zero attrito nel primo filtro**: nessun form lungo above the fold, solo
   3 campi (Dove / Quando / Filtro rapido taglia-numero cani) + bottone CTA.
3. **Trasparenza immediata**: ogni card struttura mostra da subito le 4 info
   chiave (taglia max, n° cani max, supplemento, giardino) come "pillole"
   colorate, senza dover aprire la scheda.
4. **Fiducia visiva**: badge "Verificato", numero di recensioni reali,
   iconografia di garanzia visibili fin dalla hero.
5. **Accessibilità**: contrasto AA, focus state visibili, tap target ≥44px,
   alt text descrittivi per ogni foto (rilevante anche per SEO immagini).

---

## 2. STRUTTURA DELLA HOME PAGE

### 2.1 Header (sticky)

Logo "Oltre la Taglia 🐾" — menu: `Cerca alloggi` · `Blog & Guide` · `Per le
strutture` · `Chi siamo` — CTA secondaria a destra: **"Inserisci la tua
struttura"** (bottone outline azzurro).

### 2.2 Hero Section (above the fold)

**H1 (headline orientata al beneficio):**
> ## Vacanze senza limiti di taglia. Trova l'alloggio perfetto per il tuo cane grande.

**Sottotitolo:**
> Oltre [N] hotel, B&B e agriturismi in tutta Italia verificati uno per uno:
> nessun limite di peso, nessun "massimo un cane". Solo strutture che
> accolgono davvero la tua famiglia a quattro zampe — comprese le taglie
> giganti e i branchi numerosi.

**Barra di ricerca avanzata — above the fold, non negoziabile.** Nel mockup
v3 è una barra unica a filo, bordo nero pieno, cinque campi separati da
filetti a 1px e il pulsante in blu Klein all'estremità:

```
[ Destinazione | Check-in | Check-out | Quanti cani | Taglia ] [ CERCA ]
   Toscana…      12 set     15 set      2 cani       45 kg+     ◼ Klein
```

- Le etichette dei campi sono in Martian Mono minuscolo maiuscoletto, i
  valori in Onest semibold: la stessa gerarchia "etichetta tecnica / dato"
  usata ovunque nel sito.
- Il pulsante è l'unico blu Klein della hero, così l'occhio ci finisce senza
  che nient'altro competa.
- Sotto la barra: micro-trust row — *"Zero sorprese al check-in · Regole
  verificate una per una · Recensioni di chi ha un cane grande"*, con un
  punto blu al posto delle emoji.

### 2.3 Filtri Rapidi in Evidenza (chip/icone cliccabili sotto la hero)

Riga orizzontale scrollabile su mobile, di pillole con icona:

- 🐻 **Cani oltre 40 kg benvenuti**
- 🐕‍🦺 **Più di 2 cani ammessi**
- 🌳 **Giardino/terreno recintato**
- 🍽️ **Cani ammessi in sala colazione/ristorante**
- 🏖️ **Vicino a spiagge pet-friendly**
- 🚫💰 **Nessun supplemento o cauzione**

Ogni chip porta a una pagina di ricerca pre-filtrata (utile anche per SEO —
vedi sezione 5, ogni filtro genera una landing page indicizzabile tipo
`/cerca/cani-oltre-40kg`).

### 2.4 Sezione Vetrina / Strutture in Evidenza

**Titolo sezione:** "Le strutture più amate dai cani grandi (e dai loro
umani)"
**Sottotitolo:** "Selezionate e verificate dal nostro team. Nessun limite,
solo accoglienza vera."

Griglia responsive (1 colonna mobile, 2 tablet, 3–4 desktop). Ogni **card
struttura** contiene:

- Foto principale (16:9) con badge overlay "✅ Verificata" in alto a sinistra
  e cuore/preferiti in alto a destra.
- Nome struttura + località (con icona pin) + rating a stelle (giallo senape).
- 4 pillole informative rapide (icone + testo breve):
  `🐕 Fino a 2 cani` · `📏 Nessun limite di taglia` · `🌳 Giardino recintato`
  · `🆓 Nessun supplemento`
- Prezzo indicativo "da €XX/notte" in corallo, in basso a destra.
- CTA "Vedi disponibilità" (bottone pieno corallo, full width su mobile).

CTA sezione: **"Esplora tutte le strutture verificate →"**

### 2.5 Sezione "Perché Affidarsi a Noi" (3 vantaggi)

Layout a 3 colonne (stack su mobile), icona grande + titolo + 2 righe di testo.

1. **🔍 Zero sorprese sulle regole**
   *Contattiamo ogni struttura prima di pubblicarla e verifichiamo taglia
   massima, numero di animali e costi extra. Quello che leggi qui è quello
   che troverai al check-in.*

2. **📏 Zero restrizioni di taglia**
   *Non pubblichiamo il "pet-friendly" generico che accetta solo cani sotto
   i 10 kg. Qui trovi solo strutture pensate per Alani, Maremmani, San
   Bernardo e branchi di più cani.*

3. **✅ Strutture testate, non solo elencate**
   *Ogni scheda include foto reali degli spazi esterni, recensioni di
   proprietari di cani grandi e, dove possibile, sopralluoghi diretti del
   nostro team.*

### 2.6 Sezione Blog / Guide Recenti

**Titolo:** "Guide e consigli per viaggiare con cani grandi"
**Sottotitolo:** "Itinerari, diritti, consigli pratici e recensioni per
chi non vuole lasciare a casa nessun membro della famiglia."

Griglia di 3–4 card articolo (immagine, categoria tag, titolo, estratto 1
riga, tempo di lettura). Esempi di titoli pronti (v. sezione 6 per il piano
editoriale completo):

- *"Le 10 spiagge libere in Italia dove i cani grandi possono correre liberi"*
- *"Agriturismi in Toscana per cani senza guinzaglio: la guida 2026"*
- *"Come viaggiare in traghetto con 2 cani di taglia gigante: documenti e regole"*
- *"Hotel vs B&B vs agriturismo pet-friendly: qual è il migliore per un cane grande?"*

CTA sezione: **"Leggi tutte le guide →"**

### 2.7 Sezione Community / Numeri (opzionale ma consigliata)

Striscia con contatori: "**[N]+ strutture verificate** · **[N]+ regioni
coperte** · **[N]+ recensioni da proprietari reali**" — rafforza fiducia
prima della FAQ.

### 2.8 Sezione FAQ

Vedi sezione 4 completa più sotto. Titolo sezione: **"Le domande più
frequenti di chi viaggia con cani grandi"**.

### 2.9 CTA finale / Sezione "Per le strutture"

Banner a tutta larghezza, sfondo blu petrolio `#03045E`, testo bianco:

> **Gestisci una struttura pet-friendly senza limiti?**
> Unisciti alla directory dedicata ai proprietari di cani grandi e raggiungi
> un pubblico che cerca esattamente quello che offri.
> [Inserisci la tua struttura gratis →] (bottone corallo)

### 2.10 Footer

Colonne: `Esplora` (Cerca alloggi, Blog, Destinazioni top) · `Per le
strutture` (Come funziona, Linee guida verifica, Login proprietari) ·
`Azienda` (Chi siamo, Contatti, Termini, Privacy) · Social + newsletter
("Ricevi ogni mese le nuove strutture verificate e le guide di viaggio").

---

## 3. OTTIMIZZAZIONE SEO ON-PAGE — HOME PAGE

### 3.1 Title tag (≤60 caratteri)

> `Hotel e B&B per Cani Grandi Senza Limiti | Oltre la Taglia`
(56 caratteri — include keyword transazionale "hotel per cani grandi" + brand)

Varianti A/B testabili:
- `Alloggi Pet Friendly per Cani Grandi, Senza Taglia` (52 car.)
- `Hotel Pet Friendly Senza Limiti di Taglia | Oltre la Taglia` (58 car.)

### 3.2 Meta description (≤155 caratteri)

> `Trova hotel, B&B e agriturismi che accettano cani grandi, giganti o più di uno. Nessun limite di taglia, regole verificate. Cerca ora la tua vacanza.`
(154 caratteri)

### 3.3 URL

`https://www.oltrelataglia.it/` (dominio) — struttura URL consigliata per le
sezioni interne, tutte in italiano e keyword-friendly:

- `/cerca` — motore di ricerca/listing principale
- `/cerca/cani-oltre-40kg`, `/cerca/piu-di-2-cani`, `/cerca/giardino-recintato`
  → landing di filtro pre-costruite (alto potenziale SEO long-tail)
- `/regione/toscana`, `/regione/puglia`, ... → hub geografici
- `/struttura/[slug]` — scheda singola struttura
- `/blog/[slug]` — articoli
- `/blog/categoria/spiagge-per-cani`, `/blog/categoria/normativa-viaggi`

### 3.3bis Keyword nel copy visibile (non solo nei tag)

Le keyword della sezione 3.4 sono state inserite anche nel **testo visibile**
dei mockup, non solo nei meta tag — pratica che aiuta sia l'utente (capisce
subito cosa trova) sia Google (contesto semantico coerente col title/meta):

- **Home**: eyebrow sopra l'H1 ("HOTEL PET FRIENDLY · CANI GRANDI E GIGANTI"),
  sottotitolo hero con "hotel per cani taglia grande", "b&b che accettano
  cani senza limiti", "agriturismi per cani giganti"; un breve paragrafo
  keyword-rich sotto i filtri rapidi con tutte le query transazionali della
  sezione 3.4 inserite in modo naturale (mai in un elenco/keyword-stuffing).
- **`/cerca`**: H1 riscritto in "Hotel, B&B e agriturismi per cani grandi in
  [regione]" (pattern riusabile per ogni landing geografica) con un
  sottotitolo che ripete "pet friendly", "taglia grande e gigante", "senza
  limiti di peso o di numero".
- I link di navigazione (header/footer) restano invece etichette brevi e
  naturali ("Cerca alloggi", "Blog & Guide") — il keyword stuffing nei menu
  peggiora la UX senza benefici SEO reali.

### 3.4 Keyword primarie target (Home)

Transazionali/commerciali ad alto intento (volume IT stimato medio-basso ma
altissima conversione, bassa competizione):

- hotel pet friendly cani grandi
- b&b che accettano cani senza limiti
- agriturismo cani taglia grande
- alloggi per cani giganti
- hotel 2 cani ammessi
- vacanze con cane senza restrizioni di taglia
- pet friendly no limiti di peso

### 3.5 Dati strutturati (Schema Markup)

Combinazione consigliata per la home:

1. **`WebSite`** con `SearchAction` (per abilitare la sitelinks search box
   di Google):
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Oltre la Taglia",
  "url": "https://www.oltrelataglia.it/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.oltrelataglia.it/cerca?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

2. **`ItemList`** per la sezione "Strutture in evidenza" (elenco di
   `LodgingBusiness`/`Hotel`), utile perché Google comprenda che la home è
   una directory/hub e non una singola scheda struttura:
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "url": "https://www.oltrelataglia.it/struttura/nome-struttura"
    }
  ]
}
```

3. Sulle **schede struttura** (non home, ma da prevedere subito
   nell'architettura dati): `LodgingBusiness` (specializzazione di
   `LocalBusiness`) con proprietà custom in `additionalProperty` per
   "taglia massima ammessa" e "numero massimo animali", più `AggregateRating`
   se ci sono recensioni reali.

4. **`FAQPage`** per la sezione FAQ della home (vedi sezione 4) — fondamentale
   per intercettare i featured snippet e la "People Also Ask".

5. **`BreadcrumbList`** su tutte le pagine interne (cerca → regione →
   struttura) per una migliore comprensione della gerarchia da parte di
   Google.

> Nota tecnica: **non** usare `LocalBusiness` sulla home stessa (la home non
> è la sede fisica di un'attività, ma un aggregatore) — è un errore comune
> che confonde Google. La home usa `WebSite` + `ItemList` + `FAQPage`; è la
> singola scheda struttura a usare `LodgingBusiness`.

### 3.6 Alt text immagini (esempio)

`alt="Golden Retriever di taglia grande in giardino recintato di un agriturismo pet-friendly in Toscana"` — descrittivo, include keyword naturalmente, mai keyword-stuffing.

---

## 4. SEZIONE FAQ APPROFONDITA (Home Page)

Testi pronti all'uso, ottimizzati per ricerca vocale (domande colloquiali,
risposte dirette nelle prime 1–2 frasi, dettaglio a seguire) e per People
Also Ask. Da marcare con `FAQPage` schema.

**1. Le strutture su Oltre la Taglia accettano davvero cani di qualsiasi taglia?**
Sì. A differenza dei portali generalisti, su Oltre la Taglia pubblichiamo solo
strutture che abbiamo verificato accettare cani di taglia grande (25–45 kg)
e gigante (oltre 45 kg), come Alani, Pastori del Caucaso, San Bernardo o
Mastini. Per ogni struttura indichiamo chiaramente la taglia massima
ammessa, così non ci sono sorprese al check-in.

**2. Posso portare più di un cane nella stessa struttura?**
Molte strutture della nostra directory accettano 2, 3 o più cani nella
stessa camera o appartamento, spesso senza supplemento aggiuntivo per ogni
animale extra. Usa il filtro "Più di 2 cani ammessi" nella home per vedere
subito solo queste opzioni: il numero massimo di animali è sempre indicato
nella scheda struttura.

**3. Ci sono supplementi nascosti da pagare al check-in?**
No, se prenoti tramite una struttura verificata Oltre la Taglia il costo per il
soggiorno con animali è sempre indicato in modo trasparente nella scheda,
prima della prenotazione. Alcune strutture applicano un piccolo supplemento
di pulizia forfettario (non "per cane"), altre non applicano alcun
supplemento: la voce "Costi extra animali" nella scheda riporta sempre
l'importo esatto o l'indicazione "nessun supplemento".

**4. Come viene richiesta la cauzione per gli animali?**
Non tutte le strutture la richiedono. Quando prevista, la cauzione è
generalmente una cifra fissa (indicativamente 20–50€) restituita al
check-out se non ci sono danni, e viene sempre dichiarata in anticipo nella
scheda della struttura, mai comunicata a sorpresa in loco. Ti consigliamo
comunque di richiedere conferma scritta (email o messaggio) prima di
partire, così hai una prova in caso di controversie.

**5. I cani possono accedere alla sala colazione o al ristorante interno?**
Dipende dalla struttura: alcune ammettono i cani anche negli spazi comuni
interni (sala colazione, area bar), altre solo negli spazi esterni o in
camera. Per questo ogni scheda include la pillola informativa "Accesso aree
comuni" con il dettaglio preciso — puoi anche filtrare direttamente per
"Cani ammessi in sala colazione/ristorante" nella home.

**6. Le strutture hanno un giardino o uno spazio recintato dove far correre il cane libero?**
Molte sì. Segnaliamo sempre nella scheda se la struttura dispone di un
giardino, terreno o area sgambamento recintata dove il cane può stare libero
senza guinzaglio in sicurezza. Usa il filtro "Giardino/terreno recintato"
per vedere solo queste strutture, ideali soprattutto per cani di taglia
grande abituati a muoversi molto.

**7. Come faccio a sapere se una struttura è vicina a spiagge o sentieri dog-friendly?**
Nella scheda di ogni struttura situata in zone costiere o montane indichiamo
le spiagge libere per cani, le aree sgambamento e i sentieri pet-friendly
più vicini, con relativa distanza in auto o a piedi. Trovi inoltre guide
dedicate nel nostro blog con l'elenco aggiornato delle spiagge per cani
regione per regione.

**8. Come verificate davvero le regole delle strutture prima di pubblicarle?**
Ogni struttura viene contattata direttamente dal nostro team (telefono o
email) per confermare quattro punti: taglia massima ammessa, numero massimo
di animali, eventuali supplementi/cauzioni e accesso agli spazi comuni.
Solo dopo questa verifica la struttura entra nella directory con il badge
"Verificato Oltre la Taglia". Le informazioni vengono aggiornate periodicamente
e ogni utente può segnalarci discrepanze trovate sul posto.

**9. Cosa succede se al check-in la struttura applica regole diverse da quelle indicate sul sito?**
Ti invitiamo a contattarci subito tramite il modulo di segnalazione presente
in ogni scheda struttura: verifichiamo la discrepanza con la struttura e, se
confermata, aggiorniamo immediatamente la scheda o rimuoviamo il badge
"Verificato". La trasparenza delle informazioni è il cuore del nostro
servizio, quindi ogni segnalazione viene gestita con priorità.

**10. Il servizio di ricerca su Oltre la Taglia è gratuito?**
Sì, la ricerca, la consultazione delle schede e delle guide del blog sono
completamente gratuite per chi viaggia. Il nostro modello si basa sulla
collaborazione con le strutture ricettive, che possono richiedere
l'inserimento nella directory secondo le nostre linee guida di verifica.

**11. Posso lasciare una recensione dopo il soggiorno?**
Sì, dopo il soggiorno puoi lasciare una recensione dedicata specificamente
all'esperienza con il tuo cane (comportamento del personale, rispetto delle
regole dichiarate, qualità degli spazi esterni), utile per aiutare altri
proprietari di cani grandi a scegliere con fiducia.

---

## 5. STRUTTURA / ARCHITETTURA DEL SITO (oltre la Home)

```
/                          Home
/cerca                     Motore di ricerca con filtri avanzati (mappa + lista)
/cerca/[filtro-slug]        Landing SEO per singolo filtro (taglia, n. cani, ecc.)
/regione/[slug]              Hub geografico regione (es. /regione/toscana)
/regione/[slug]/[citta]     Hub geografico città
/struttura/[slug]            Scheda struttura (LodgingBusiness schema)
/blog                       Indice blog
/blog/categoria/[slug]        Categorie: Destinazioni · Normativa & Viaggi ·
                             Guide per Taglia · Consigli Pratici
/blog/[slug]                Articolo singolo
/per-le-strutture           Landing B2B per acquisizione strutture
/per-le-strutture/come-funziona
/chi-siamo
/faq                        FAQ estesa (oltre quelle in home)
/contatti
/privacy  /termini  /cookie
```

### Piano editoriale blog — primi 12 articoli consigliati (pilastri SEO)

1. Hotel pet-friendly senza limiti di taglia: la guida definitiva 2026
2. Le migliori spiagge libere per cani grandi in Italia (regione per regione)
3. Agriturismi in Toscana per cani senza restrizioni: la mappa completa
4. Viaggiare in traghetto con più cani di taglia grande: documenti e regole
5. Cosa dice la legge italiana su cani in hotel e ristoranti (guida pratica)
6. Come scegliere un B&B pet-friendly se hai un cane oltre i 40 kg
7. 10 agriturismi in Puglia con giardino recintato per cani grandi
8. Weekend in montagna con il cane: rifugi e baite senza limiti di taglia
9. Hotel vs B&B vs agriturismo: quale scegliere con un cane gigante
10. Documenti e vaccinazioni per viaggiare con il cane in Italia: checklist
11. Le 5 domande da fare sempre prima di prenotare (e perché contano)
12. Come si comporta un cane di taglia grande in un B&B: consigli pratici

---

## 6. RIEPILOGO ASSET PRONTI PER LO SVILUPPO

- ✅ Palette colori + token esadecimali
- ✅ Font pairing consigliato
- ✅ Wireframe testuale sezione-per-sezione della home
- ✅ Copy pronto all'uso per hero, filtri, vantaggi, CTA, footer
- ✅ Title tag + meta description ottimizzati e testabili in A/B
- ✅ Struttura URL SEO-friendly per l'intero sito
- ✅ Schema Markup consigliato (WebSite+SearchAction, ItemList, FAQPage,
  LodgingBusiness, BreadcrumbList) con JSON-LD di esempio
- ✅ 11 FAQ complete con risposte pronte, ottimizzate voice search
- ✅ Piano editoriale blog (12 articoli pilastro)

Prossimo passo naturale: wireframe visivo (Figma o canvas design) e
implementazione front-end (Next.js + Tailwind, coerente con lo stack già
in uso nel repository).

---

## 7. Stato di implementazione nel mockup

Il file `mockup/home.html` implementa il brief originale sezione per sezione.
Riepilogo di cosa è già dentro la pagina e cosa resta da fare in sviluppo.

| Richiesta del brief | Stato nel mockup |
|---|---|
| Hero con titolo orientato al beneficio | ✅ H1 "Vacanze senza limiti di taglia…" |
| Barra di ricerca avanzata **above the fold** | ✅ 5 campi (destinazione, check-in/out, n° cani, taglia) + CTA |
| Filtri rapidi in evidenza | ✅ 6 chip, numerate, che puntano alle landing di filtro |
| Vetrina strutture in evidenza | ✅ 3 strutture reali con fonti pubbliche citate |
| Perché affidarsi a noi (3 vantaggi) | ✅ zero sorprese / zero restrizioni di taglia / strutture testate |
| Blog e guide recenti | ✅ guida in evidenza + 3 articoli |
| FAQ ricca (8–10) | ✅ **11 FAQ complete**, allineate al testo della sezione 4 |
| Title tag ≤ 60 caratteri | ✅ in `og:title` (58 car.); in produzione va nel `<title>` |
| Meta description ≤ 155 caratteri | ✅ `<meta name="description">` (154 car.) |
| Schema `WebSite` + `SearchAction` | ✅ JSON-LD |
| Schema `ItemList` (vetrina) | ✅ JSON-LD, 3 elementi |
| Schema `FAQPage` | ✅ JSON-LD, 11 domande — combacia con il markup visibile |
| Keyword nel copy visibile | ✅ eyebrow, H1, sottotitolo hero, paragrafo sotto i filtri |

**Da completare in sviluppo**, fuori dalla portata di un mockup statico:
`BreadcrumbList` (serve la gerarchia reale delle pagine interne),
`LodgingBusiness` sulle singole schede struttura, il `<title>` di produzione
al posto del nome brand, e la sostituzione del campo 3D con fotografie vere
dove si vuole mostrare la struttura e non il brand.

> ⚠️ **Coerenza fra markup e dati strutturati.** Le 11 domande nel `FAQPage`
> ripetono parola per parola quelle visibili nella pagina. Non è un vezzo:
> Google penalizza (e può ignorare del tutto) uno `FAQPage` le cui risposte
> non compaiono nel contenuto visibile. Se in futuro si modifica una FAQ nel
> markup, va aggiornata anche nel JSON-LD.
