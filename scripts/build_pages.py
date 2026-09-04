#!/usr/bin/env python3
"""
Genera le pagine statiche di servizio (non blog, non struttura):
  /chi-siamo/, /contatti/, /privacy/, /termini/

Stesso pattern di build_blog.py / build_strutture.py: riusa
style/header/footer/script estratti da mockup/home.html.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.join(ROOT, "mockup", "home.html")

CONTACT_EMAIL = "bassanisimone04+taglialibera@gmail.com"  # alias "+": recapita nella stessa inbox, mostrato diverso sul sito

CALC_CSS = """
  .calc-box{ border:1px solid var(--line); padding:32px; margin-bottom:40px; background:var(--surface-2); }
  .calc-box label{ font-family:'Martian Mono',monospace; font-size:11px; text-transform:uppercase; letter-spacing:.04em; color:var(--ink-2); }
  .calc-row{ display:flex; gap:10px; margin-top:10px; flex-wrap:wrap; }
  .calc-row input{
    flex:1; min-width:140px; padding:13px 16px; border:1px solid var(--line); background:var(--surface);
    color:var(--ink); font-family:'Onest',sans-serif; font-size:16px;
  }
  .calc-row input:focus{ outline:2.5px solid var(--klein); outline-offset:2px; }
  .calc-result{ margin-top:24px; padding-top:24px; border-top:1px solid var(--line); }
  .calc-result-taglia{ font-family:'Martian Mono',monospace; font-size:13px; text-transform:uppercase; letter-spacing:.04em; color:var(--klein-text); font-weight:600; margin-bottom:8px; }
  .calc-result p{ margin-bottom:16px; }
"""

CALC_SCRIPT = """
<script>
(function(){
  "use strict";
  var input = document.getElementById("peso-cane");
  var btn = document.getElementById("calc-btn");
  var result = document.getElementById("calc-result");
  var taglia = document.getElementById("calc-taglia");
  var desc = document.getElementById("calc-desc");
  var link = document.getElementById("calc-link");
  if (!btn) return;

  var FASCE = [
    { max: 10, nome: "Piccola", tag: "", desc: "Fino a 10 kg. La maggior parte dei portali \\"pet friendly\\" generici è pensata per questa taglia — questa directory invece si concentra su cani più grandi, ma tanti alloggi generalisti vanno bene." },
    { max: 25, nome: "Media", tag: "", desc: "Tra 10 e 25 kg. Molte strutture che accettano cani \\"di taglia media\\" si fermano qui: verifica sempre il limite esatto dichiarato." },
    { max: 45, nome: "Grande", tag: "Fino a taglia grande", desc: "Tra 25 e 45 kg. È la soglia dove iniziano i problemi con i filtri generici: molti hotel \\"pet friendly\\" si fermano prima. In questa directory trovi strutture che dichiarano esplicitamente di accettare questa taglia." },
    { max: Infinity, nome: "Gigante", tag: "Ogni taglia", desc: "Oltre 45 kg — Alani, San Bernardo, Mastini e simili. È la taglia per cui esiste questa directory: la maggior parte dei portali generalisti non è pensata per un cane di questa stazza." },
  ];

  function calcola(){
    var peso = parseFloat(input.value);
    if (!peso || peso <= 0) {
      input.focus();
      return;
    }
    var fascia = FASCE[0];
    for (var i = 0; i < FASCE.length; i++) {
      if (peso <= FASCE[i].max) { fascia = FASCE[i]; break; }
    }
    taglia.textContent = fascia.nome + " (" + peso + " kg)";
    desc.textContent = fascia.desc;
    link.href = fascia.tag ? "/cerca/?tag=" + encodeURIComponent(fascia.tag) : "/cerca/";
    result.hidden = false;
  }

  btn.addEventListener("click", calcola);
  input.addEventListener("keydown", function(e){ if (e.key === "Enter") calcola(); });
})();
</script>
"""

CHECKLIST_CSS = """
  .checklist{ list-style:none; padding:0; margin:0 0 8px; display:flex; flex-direction:column; gap:2px; }
  .checklist li{ border-bottom:1px solid var(--line); }
  .checklist label{
    display:flex; align-items:flex-start; gap:12px; padding:12px 4px; cursor:pointer;
    font-size:15.5px; color:var(--ink-2); line-height:1.5;
  }
  .checklist input[type="checkbox"]{ accent-color:var(--klein); width:18px; height:18px; flex-shrink:0; margin-top:2px; }
  .checklist label:has(input:checked){ color:var(--ink); text-decoration:line-through; text-decoration-color:var(--klein-text); }
  .checklist-note{ margin-top:32px; font-size:14px; color:var(--ink-2); }
  @media print{
    .no-print, header, footer{ display:none !important; }
    .static-hero{ padding-top:20px !important; }
    body{ background:#fff; color:#000; }
  }
"""

CHECKLIST_SCRIPT = """
<script>
(function(){
  "use strict";
  var boxes = document.querySelectorAll(".checklist input[type=checkbox]");
  var KEY = "checklist-viaggio-cane";
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch(e){}

  boxes.forEach(function(box){
    var id = box.getAttribute("data-item");
    if (saved[id]) box.checked = true;
    box.addEventListener("change", function(){
      saved[id] = box.checked;
      try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch(e){}
    });
  });

  var printBtn = document.getElementById("print-btn");
  if (printBtn) printBtn.addEventListener("click", function(){ window.print(); });
})();
</script>
"""


def extract(src, start_marker, end_marker):
    i1 = src.index(start_marker)
    i2 = src.index(end_marker, i1) + len(end_marker)
    return src[i1:i2]


def nestify_links(fragment):
    import re
    return re.sub(r'href="#', 'href="/#', fragment)


PAGE_CSS = """
  .static-hero{ padding:150px 0 40px; border-bottom:1px solid var(--line); }
  .static-hero h1{ font-size:clamp(28px,4vw,46px); max-width:24ch; }
  .static-body{ max-width:70ch; padding-block:56px; }
  .static-body h2{ font-size:clamp(19px,2.4vw,24px); margin-top:44px; margin-bottom:14px; }
  .static-body h2:first-child{ margin-top:0; }
  .static-body p{ font-size:16px; line-height:1.72; margin-bottom:16px; color:var(--ink-2); }
  .static-body ul{ margin:0 0 18px; padding-left:22px; display:flex; flex-direction:column; gap:8px; }
  .static-body li{ font-size:15.5px; line-height:1.6; color:var(--ink-2); }
  .static-body a{ color:var(--klein-text); text-decoration:underline; text-underline-offset:2px; }
  .static-body strong{ color:var(--ink); font-weight:700; }
  .contact-card{ border:1px solid var(--line); padding:28px; margin-bottom:28px; background:var(--surface-2); }
  .contact-card .k{ font-family:'Martian Mono',monospace; font-size:10px; font-weight:600; letter-spacing:.04em; text-transform:uppercase; color:var(--ink-2); }
  .contact-card .v{ margin-top:8px; font-size:19px; font-weight:700; color:var(--ink); }
"""


def page_shell(style_block, header_block, footer_block, header_script, title, description, path, body_html, extra_css="", extra_script=""):
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.taglialibera.it/{path}">
{style_block}
<style>{PAGE_CSS}
{extra_css}</style>
</head>
<body>

{header_block}

<main id="top">
{body_html}
</main>

{footer_block}
{header_script}
{extra_script}
</body>
</html>
"""


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>\n(function(){", "</script>")

    pages = {}

    # ---------- Chi siamo ----------
    pages["chi-siamo"] = {
        "title": "Chi siamo | Taglia Libera",
        "description": "Come e perché nasce Taglia Libera: un progetto indipendente, non affiliato alle strutture segnalate, che verifica a mano ogni scheda.",
        "body": """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Chi siamo</p>
      <h1 style="margin-top:10px;">Un progetto piccolo, fatto a mano.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <h2>Perché esiste Taglia Libera</h2>
      <p>Chi ha un cane di taglia grande o gigante conosce il problema: la maggior parte dei filtri "pet friendly" è pensata per cani piccoli, e scoprire che una struttura ha un limite di peso non dichiarato capita spesso solo all'arrivo. Taglia Libera nasce per raccogliere, in un unico posto, strutture che dichiarano esplicitamente di accogliere cani grandi, giganti o più di uno insieme — con la fonte del dato sempre citata.</p>
      <h2>Chi lo cura</h2>
      <p>Il progetto è curato in modo indipendente da una singola persona, non da un'azienda o un'agenzia. Non è un portale di prenotazione e non incassa commissioni sulle prenotazioni: ogni scheda rimanda al sito ufficiale della struttura o alla fonte pubblica da cui arriva il dato.</p>
      <h2>Come lavoriamo</h2>
      <p>Ogni struttura viene aggiunta a mano dopo aver trovato una fonte pubblica verificabile — il sito ufficiale della struttura o un portale specializzato — che dichiari esplicitamente le condizioni sui cani. Se un dato chiave (come la taglia massima ammessa) non è confermabile, la struttura non viene aggiunta, anche se altrove risulta "pet friendly" in modo generico. Altri dettagli sul metodo sono nelle <a href="/cerca/">domande frequenti della ricerca</a>.</p>
      <h2>Cosa NON siamo</h2>
      <ul>
        <li>Non siamo affiliati a nessuna delle strutture segnalate.</li>
        <li>Non abbiamo verificato le informazioni per telefono con ogni struttura: lo indichiamo sempre in modo esplicito nelle schede.</li>
        <li>Non pubblichiamo prezzi o valutazioni: se non li abbiamo verificati, preferiamo ometterli.</li>
      </ul>
      <h2>Segnala un errore</h2>
      <p>Se gestisci una delle strutture segnalate, o hai trovato un'informazione non più aggiornata, scrivici dalla pagina <a href="/contatti/">Contatti</a>: correggiamo volentieri ogni scheda su segnalazione.</p>
    </div>
  </article>
""",
    }

    # ---------- Contatti ----------
    pages["contatti"] = {
        "title": "Contatti | Taglia Libera",
        "description": "Come contattarci per segnalare una struttura, correggere un dato o proporre una nuova scheda per la directory.",
        "body": f"""
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Contatti</p>
      <h1 style="margin-top:10px;">Scrivici.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <div class="contact-card">
        <div class="k">Email</div>
        <div class="v"><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></div>
      </div>
      <h2>Per cosa scriverci</h2>
      <ul>
        <li><strong>Segnalare un errore</strong> in una scheda esistente — un dato cambiato, un supplemento diverso, una struttura che non accetta più cani grandi.</li>
        <li><strong>Proporre una struttura</strong> che accoglie davvero cani grandi o giganti senza i soliti limiti, con un link alla fonte pubblica dove è dichiarato.</li>
        <li><strong>Richieste sui dati personali</strong> — per esercitare i diritti descritti nella pagina <a href="/privacy/">Privacy</a>.</li>
      </ul>
      <h2>Tempi di risposta</h2>
      <p>Il progetto è curato da una sola persona nel tempo libero: non possiamo garantire un tempo di risposta fisso, ma leggiamo ogni messaggio.</p>
    </div>
  </article>
""",
    }

    # ---------- Privacy ----------
    pages["privacy"] = {
        "title": "Privacy | Taglia Libera",
        "description": "Informativa sul trattamento dei dati personali di Taglia Libera ai sensi del Regolamento UE 2016/679 (GDPR).",
        "body": f"""
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Privacy</p>
      <h1 style="margin-top:10px;">Informativa sulla privacy.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <p>Ultimo aggiornamento: questa pagina descrive come Taglia Libera tratta i dati personali di chi visita il sito, ai sensi del Regolamento (UE) 2016/679 (GDPR).</p>

      <h2>Titolare del trattamento</h2>
      <p>Taglia Libera è un progetto indipendente curato da una persona fisica, senza partita IVA. Per qualsiasi richiesta relativa ai dati personali, il titolare del trattamento è contattabile all'indirizzo <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>

      <h2>Il sito non usa cookie di profilazione</h2>
      <p>Taglia Libera non installa cookie di profilazione, non usa strumenti di analisi del traffico (come Google Analytics) e non effettua tracciamento pubblicitario. Non ci sono form che raccolgono dati se non l'eventuale email che ci scrivi.</p>

      <h2>Dati raccolti automaticamente dal fornitore di hosting</h2>
      <p>Il sito è ospitato tramite <strong>Vercel Inc.</strong> Come qualsiasi servizio di hosting, per motivi tecnici e di sicurezza il fornitore registra automaticamente alcuni dati di connessione (indirizzo IP, tipo di browser, data e ora della richiesta) nei log di sistema, per il tempo strettamente necessario a garantire il funzionamento e la sicurezza del servizio. Questi dati non vengono usati da noi per identificare i visitatori. Per maggiori informazioni: <a href="https://vercel.com/legal/privacy-policy" target="_blank" rel="noopener">informativa privacy di Vercel</a>.</p>

      <h2>Google Fonts</h2>
      <p>Il sito carica i caratteri tipografici (Onest, Martian Mono) direttamente dai server di Google Fonts. Questo comporta che il browser del visitatore invii una richiesta ai server di Google, che può includere l'indirizzo IP del dispositivo. Per maggiori informazioni: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">informativa privacy di Google</a>.</p>

      <h2>Se ci scrivi un'email</h2>
      <p>Se ci contatti via email, trattiamo l'indirizzo email e il contenuto del messaggio esclusivamente per rispondere alla tua richiesta. Non condividiamo questi dati con terzi e li conserviamo solo per il tempo necessario a gestire la richiesta, salvo obblighi di legge diversi.</p>

      <h2>Link a siti esterni</h2>
      <p>Le schede delle strutture rimandano a siti ufficiali di terzi (strutture ricettive, portali specializzati). Una volta lasciato il nostro sito, si applicano le informative privacy di quei siti, che non controlliamo.</p>

      <h2>I tuoi diritti</h2>
      <p>Ai sensi degli articoli 15-22 del GDPR, hai diritto di chiedere in qualsiasi momento l'accesso ai tuoi dati, la rettifica, la cancellazione, la limitazione del trattamento, la portabilità dei dati e di opporti al trattamento, scrivendo a <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>. Hai inoltre diritto di proporre reclamo al <a href="https://www.garanteprivacy.it/" target="_blank" rel="noopener">Garante per la protezione dei dati personali</a>.</p>

      <h2>Modifiche a questa informativa</h2>
      <p>Questa informativa può essere aggiornata nel tempo, ad esempio se cambiano gli strumenti usati dal sito. La versione in vigore è sempre quella pubblicata su questa pagina.</p>
    </div>
  </article>
""",
    }

    # ---------- Termini ----------
    pages["termini"] = {
        "title": "Termini e condizioni | Taglia Libera",
        "description": "Termini e condizioni d'uso del sito Taglia Libera: cosa offre il sito, i suoi limiti e le responsabilità sui contenuti.",
        "body": """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Termini</p>
      <h1 style="margin-top:10px;">Termini e condizioni d'uso.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <h2>Cos'è Taglia Libera</h2>
      <p>Taglia Libera è una directory informativa indipendente di strutture ricettive che, secondo fonti pubbliche consultate, accolgono cani di taglia grande o gigante. Il sito non è un portale di prenotazione: non gestisce prenotazioni, pagamenti né contratti tra utenti e strutture, e non incassa commissioni.</p>

      <h2>Natura delle informazioni pubblicate</h2>
      <p>Le informazioni su ogni struttura provengono da fonti pubbliche esplicitamente citate in ciascuna scheda (sito ufficiale della struttura o portale specializzato). Non tutte le informazioni sono state verificate telefonicamente con la struttura: quando è così, lo indichiamo in modo esplicito. Le condizioni sugli animali (taglia massima, numero di cani, supplementi) possono cambiare nel tempo per decisione della struttura: prima di prenotare, verifica sempre le condizioni attuali direttamente con la struttura.</p>

      <h2>Nessuna garanzia</h2>
      <p>Pur avendo verificato la fonte al momento della pubblicazione, non possiamo garantire che i dati siano sempre aggiornati o esenti da errori. Il sito è fornito "così com'è", senza garanzie di alcun tipo. Non siamo responsabili per decisioni di prenotazione prese sulla base delle informazioni pubblicate, né per eventuali danni derivanti dall'uso del sito o dei servizi delle strutture segnalate.</p>

      <h2>Link a siti di terzi</h2>
      <p>Il sito contiene link a siti ufficiali di strutture ricettive e a fonti pubbliche terze. Non abbiamo controllo su questi siti e non siamo responsabili dei loro contenuti, delle loro politiche sulla privacy o delle transazioni che vi si svolgono.</p>

      <h2>Proprietà dei contenuti</h2>
      <p>Testi, struttura e design del sito Taglia Libera sono di proprietà del progetto, salvo i contenuti espressamente attribuiti a fonti terze (dati citati dalle strutture, fotografie con relativa licenza). La riproduzione non autorizzata dei contenuti originali non è consentita senza permesso.</p>

      <h2>Segnalazioni e correzioni</h2>
      <p>Se sei il gestore di una struttura segnalata e ritieni che un dato non sia più corretto, o se vuoi segnalare un errore, scrivi a <a href="/contatti/">Contatti</a>: le correzioni vengono valutate e applicate il prima possibile.</p>

      <h2>Legge applicabile</h2>
      <p>Questi termini sono regolati dalla legge italiana.</p>

      <h2>Modifiche a questi termini</h2>
      <p>Questi termini possono essere aggiornati nel tempo. La versione in vigore è sempre quella pubblicata su questa pagina.</p>
    </div>
  </article>
""",
    }

    # ---------- Calcolatore taglia cane ----------
    pages["calcolatore-taglia-cane"] = {
        "title": "Calcolatore taglia cane: piccola, media, grande, gigante | Taglia Libera",
        "description": "Inserisci il peso del tuo cane in kg e scopri se rientra in taglia piccola, media, grande o gigante secondo le fasce usate in questa directory.",
        "extra_css": CALC_CSS,
        "extra_script": CALC_SCRIPT,
        "body": """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Calcolatore taglia</p>
      <h1 style="margin-top:10px;">Che taglia ha il tuo cane?</h1>
      <p style="margin-top:16px; max-width:56ch; font-size:16px; color:var(--ink-2);">
        Inserisci il peso in chilogrammi: usiamo la stessa classificazione con cui categorizziamo
        le strutture in questa directory, spiegata anche nella
        <a href="/blog/cani-taglia-gigante-razze-peso/">guida alle taglie e alle razze</a>.
      </p>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <div class="calc-box">
        <label for="peso-cane">Peso del cane (kg)</label>
        <div class="calc-row">
          <input type="number" id="peso-cane" min="0" step="0.1" placeholder="es. 38" inputmode="decimal">
          <button type="button" class="btn btn-klein" id="calc-btn">Calcola</button>
        </div>
        <div class="calc-result" id="calc-result" hidden>
          <div class="calc-result-taglia" id="calc-taglia"></div>
          <p id="calc-desc"></p>
          <a href="/cerca/" id="calc-link" class="btn btn-line">Cerca strutture per questa taglia →</a>
        </div>
      </div>
      <h2>Come classifichiamo le taglie</h2>
      <ul>
        <li><strong>Piccola</strong>: fino a 10 kg</li>
        <li><strong>Media</strong>: 10-25 kg</li>
        <li><strong>Grande</strong>: 25-45 kg</li>
        <li><strong>Gigante</strong>: oltre 45 kg</li>
      </ul>
      <p>Non è uno standard ufficiale unico — è la suddivisione più diffusa tra i portali specializzati in viaggi con animali, ed è quella che usiamo per classificare ogni struttura di questa directory. Il peso reale del tuo cane può variare rispetto al peso "tipico" della razza: usa sempre il peso effettivo, non quello da tabella.</p>
    </div>
  </article>
""",
    }

    # ---------- Checklist di viaggio ----------
    pages["checklist-viaggio-cane"] = {
        "title": "Checklist di viaggio con un cane grande | Taglia Libera",
        "description": "Checklist stampabile per partire con un cane di taglia grande o gigante: documenti, kit sanitario, attrezzatura auto, tutto in una pagina.",
        "extra_css": CHECKLIST_CSS,
        "extra_script": CHECKLIST_SCRIPT,
        "body": """
  <section class="static-hero no-print">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Checklist di viaggio</p>
      <h1 style="margin-top:10px;">Checklist di viaggio con un cane grande.</h1>
      <p style="margin-top:16px; max-width:56ch; font-size:16px; color:var(--ink-2);">
        Il riassunto di quello che abbiamo scritto nelle guide del blog, in un'unica pagina da
        spuntare prima di partire. Le tue spunte restano salvate solo su questo dispositivo.
      </p>
      <button type="button" class="btn btn-line" id="print-btn" style="margin-top:20px;">Stampa questa pagina</button>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body checklist-body">

      <h2>Documenti</h2>
      <ul class="checklist">
        <li><label><input type="checkbox" data-item="microchip"> Microchip registrato in anagrafe canina</label></li>
        <li><label><input type="checkbox" data-item="libretto"> Libretto sanitario aggiornato</label></li>
        <li><label><input type="checkbox" data-item="vaccini"> Vaccinazioni di base in corso di validità</label></li>
        <li><label><input type="checkbox" data-item="antirabbica"> Vaccinazione antirabbica (se attraversi confini regionali o vai all'estero — <a href="/blog/passaporto-europeo-cane-viaggiare-ue/">guida UE</a>)</label></li>
        <li><label><input type="checkbox" data-item="passaporto"> Passaporto europeo per animali (solo per viaggi in UE)</label></li>
        <li><label><input type="checkbox" data-item="foto-microchip"> Foto del numero di microchip salvata sul telefono</label></li>
      </ul>

      <h2>Kit sanitario e primo soccorso</h2>
      <ul class="checklist">
        <li><label><input type="checkbox" data-item="contatto-vet"> Contatto del veterinario di zona/destinazione già cercato</label></li>
        <li><label><input type="checkbox" data-item="acqua-fresca"> Acqua fresca sempre disponibile e ciotola pieghevole</label></li>
        <li><label><input type="checkbox" data-item="tappetino"> Tappetino rinfrescante XXL (viaggi estivi)</label></li>
        <li><label><input type="checkbox" data-item="museruola"> Museruola, anche dove non è obbligatoria per legge</label></li>
      </ul>

      <h2>Attrezzatura auto</h2>
      <ul class="checklist">
        <li><label><input type="checkbox" data-item="rete"> Rete divisoria o imbracatura omologata per il peso del cane</label></li>
        <li><label><input type="checkbox" data-item="asciugamano"> Asciugamano extra-large</label></li>
        <li><label><input type="checkbox" data-item="pause"> Soste programmate ogni ~2 ore</label></li>
      </ul>

      <h2>Prima di prenotare la struttura</h2>
      <ul class="checklist">
        <li><label><input type="checkbox" data-item="taglia-max"> Taglia massima ammessa confermata per iscritto</label></li>
        <li><label><input type="checkbox" data-item="n-cani"> Numero massimo di cani ammessi</label></li>
        <li><label><input type="checkbox" data-item="supplemento"> Supplemento ed eventuale cauzione, importo esatto</label></li>
        <li><label><input type="checkbox" data-item="aree-comuni"> Accesso alle aree comuni (ristorante, piscina) verificato</label></li>
      </ul>

      <p class="checklist-note">Ogni voce è spiegata nel dettaglio nelle guide del blog — in particolare <a href="/blog/documenti-vaccinazioni-viaggiare-cane-italia/">documenti e vaccinazioni</a>, <a href="/blog/viaggiare-in-auto-cane-gigante-sicurezza/">viaggio in auto</a> e <a href="/blog/domande-da-fare-prima-di-prenotare/">domande da fare prima di prenotare</a>.</p>
    </div>
  </article>
""",
    }

    for slug, data in pages.items():
        html_out = page_shell(
            style_block, header_block, footer_block, header_script,
            data["title"], data["description"], f"{slug}/", data["body"],
            data.get("extra_css", ""), data.get("extra_script", ""),
        )
        out_dir = os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)
        print("generata:", f"/{slug}/")

    write_404(style_block, header_block, footer_block, header_script)

    return list(pages.keys())


def write_404(style_block, header_block, footer_block, header_script):
    """Pagina 404 personalizzata: Vercel la serve automaticamente per
    qualunque URL non trovato se il file si chiama 404.html alla radice.
    noindex esplicito: non è un contenuto da far indicizzare."""
    body = """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl">Errore 404</p>
      <h1 style="margin-top:10px;">Questa pagina non esiste (più).</h1>
      <p style="margin-top:16px; max-width:56ch; font-size:16px; color:var(--ink-2);">
        Il link che hai seguito potrebbe essere sbagliato, o la pagina potrebbe essere stata
        spostata. Ecco dove trovare quello che cerchi:
      </p>
      <div style="margin-top:24px; display:flex; gap:10px; flex-wrap:wrap;">
        <a class="btn btn-klein" href="/">Torna alla home</a>
        <a class="btn btn-line" href="/cerca/">Cerca una struttura</a>
        <a class="btn btn-line" href="/blog/">Leggi le guide</a>
      </div>
    </div>
  </section>
"""
    html_out = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<title>Pagina non trovata | Taglia Libera</title>
<meta name="robots" content="noindex">
{style_block}
<style>{PAGE_CSS}</style>
</head>
<body>

{header_block}

<main id="top">
{body}
</main>

{footer_block}
{header_script}
</body>
</html>
"""
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html_out)
    print("generata: /404.html")


if __name__ == "__main__":
    build()
