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

CONTACT_EMAIL = "PLACEHOLDER_EMAIL@example.com"  # sostituire con l'email dedicata prima di pubblicare


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


def page_shell(style_block, header_block, footer_block, header_script, title, description, path, body_html):
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.oltrelataglia.it/{path}">
{style_block}
<style>{PAGE_CSS}</style>
</head>
<body>

{header_block}

<main id="top">
{body_html}
</main>

{footer_block}
{header_script}
</body>
</html>
"""


def build():
    home_src = open(HOME, encoding="utf-8").read()
    style_block = extract(home_src, "<style>", "</style>")
    header_block = nestify_links(extract(home_src, '<header id="hd">', "</header>"))
    footer_block = nestify_links(extract(home_src, "<footer>", "</footer>"))
    header_script = extract(home_src, "<script>", "</script>")

    pages = {}

    # ---------- Chi siamo ----------
    pages["chi-siamo"] = {
        "title": "Chi siamo | Oltre la Taglia",
        "description": "Come e perché nasce Oltre la Taglia: un progetto indipendente, non affiliato alle strutture segnalate, che verifica a mano ogni scheda.",
        "body": """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Chi siamo</p>
      <h1 style="margin-top:10px;">Un progetto piccolo, fatto a mano.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <h2>Perché esiste Oltre la Taglia</h2>
      <p>Chi ha un cane di taglia grande o gigante conosce il problema: la maggior parte dei filtri "pet friendly" è pensata per cani piccoli, e scoprire che una struttura ha un limite di peso non dichiarato capita spesso solo all'arrivo. Oltre la Taglia nasce per raccogliere, in un unico posto, strutture che dichiarano esplicitamente di accogliere cani grandi, giganti o più di uno insieme — con la fonte del dato sempre citata.</p>
      <h2>Chi lo cura</h2>
      <p>Il progetto è curato in modo indipendente da una singola persona, non da un'azienda o un'agenzia. Non è un portale di prenotazione e non incassa commissioni sulle prenotazioni: ogni scheda rimanda al sito ufficiale della struttura o alla fonte pubblica da cui arriva il dato.</p>
      <h2>Come lavoriamo</h2>
      <p>Ogni struttura viene aggiunta a mano dopo aver trovato una fonte pubblica verificabile — il sito ufficiale della struttura o un portale specializzato — che dichiari esplicitamente le condizioni sui cani. Se un dato chiave (come la taglia massima ammessa) non è confermabile, la struttura non viene aggiunta, anche se altrove risulta "pet friendly" in modo generico. Il metodo è descritto anche nella sezione <a href="/#come">Come funziona</a> della home e nelle <a href="/cerca/">domande frequenti della ricerca</a>.</p>
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
        "title": "Contatti | Oltre la Taglia",
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
        "title": "Privacy | Oltre la Taglia",
        "description": "Informativa sul trattamento dei dati personali di Oltre la Taglia ai sensi del Regolamento UE 2016/679 (GDPR).",
        "body": f"""
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Privacy</p>
      <h1 style="margin-top:10px;">Informativa sulla privacy.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <p>Ultimo aggiornamento: questa pagina descrive come Oltre la Taglia tratta i dati personali di chi visita il sito, ai sensi del Regolamento (UE) 2016/679 (GDPR).</p>

      <h2>Titolare del trattamento</h2>
      <p>Oltre la Taglia è un progetto indipendente curato da una persona fisica, senza partita IVA. Per qualsiasi richiesta relativa ai dati personali, il titolare del trattamento è contattabile all'indirizzo <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>

      <h2>Il sito non usa cookie di profilazione</h2>
      <p>Oltre la Taglia non installa cookie di profilazione, non usa strumenti di analisi del traffico (come Google Analytics) e non effettua tracciamento pubblicitario. Non ci sono form che raccolgono dati se non l'eventuale email che ci scrivi.</p>

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
        "title": "Termini e condizioni | Oltre la Taglia",
        "description": "Termini e condizioni d'uso del sito Oltre la Taglia: cosa offre il sito, i suoi limiti e le responsabilità sui contenuti.",
        "body": """
  <section class="static-hero">
    <div class="wrap">
      <p class="lbl"><a href="/" style="text-decoration:none; color:var(--ink-2);">Home</a> / Termini</p>
      <h1 style="margin-top:10px;">Termini e condizioni d'uso.</h1>
    </div>
  </section>
  <article class="wrap">
    <div class="static-body">
      <h2>Cos'è Oltre la Taglia</h2>
      <p>Oltre la Taglia è una directory informativa indipendente di strutture ricettive che, secondo fonti pubbliche consultate, accolgono cani di taglia grande o gigante. Il sito non è un portale di prenotazione: non gestisce prenotazioni, pagamenti né contratti tra utenti e strutture, e non incassa commissioni.</p>

      <h2>Natura delle informazioni pubblicate</h2>
      <p>Le informazioni su ogni struttura provengono da fonti pubbliche esplicitamente citate in ciascuna scheda (sito ufficiale della struttura o portale specializzato). Non tutte le informazioni sono state verificate telefonicamente con la struttura: quando è così, lo indichiamo in modo esplicito. Le condizioni sugli animali (taglia massima, numero di cani, supplementi) possono cambiare nel tempo per decisione della struttura: prima di prenotare, verifica sempre le condizioni attuali direttamente con la struttura.</p>

      <h2>Nessuna garanzia</h2>
      <p>Pur avendo verificato la fonte al momento della pubblicazione, non possiamo garantire che i dati siano sempre aggiornati o esenti da errori. Il sito è fornito "così com'è", senza garanzie di alcun tipo. Non siamo responsabili per decisioni di prenotazione prese sulla base delle informazioni pubblicate, né per eventuali danni derivanti dall'uso del sito o dei servizi delle strutture segnalate.</p>

      <h2>Link a siti di terzi</h2>
      <p>Il sito contiene link a siti ufficiali di strutture ricettive e a fonti pubbliche terze. Non abbiamo controllo su questi siti e non siamo responsabili dei loro contenuti, delle loro politiche sulla privacy o delle transazioni che vi si svolgono.</p>

      <h2>Proprietà dei contenuti</h2>
      <p>Testi, struttura e design del sito Oltre la Taglia sono di proprietà del progetto, salvo i contenuti espressamente attribuiti a fonti terze (dati citati dalle strutture, fotografie con relativa licenza). La riproduzione non autorizzata dei contenuti originali non è consentita senza permesso.</p>

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

    for slug, data in pages.items():
        html_out = page_shell(
            style_block, header_block, footer_block, header_script,
            data["title"], data["description"], f"{slug}/", data["body"],
        )
        out_dir = os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)
        print("generata:", f"/{slug}/")

    return list(pages.keys())


if __name__ == "__main__":
    build()
