# Fonte unica di verità per le strutture reali della directory.
# Ogni fatto qui dentro deve poter essere ricondotto alla fonte citata.
# Non aggiungere prezzi, punteggi o servizi non confermati dalla fonte:
# se manca il dato, va omesso, non stimato (vedi STRATEGY.md sezione 7
# e i commit "fix: rimuove ogni affermazione non verificabile").

STRUTTURE = [
    {
        "slug": "agriturismo-bellavita",
        "nome": "Agriturismo Bellavita",
        "comune": "Lamporecchio, Pistoiese",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "agriturismobellavita.it",
        "fonte_url": "https://www.agriturismobellavita.it/agriturismo-per-animali/",
        "sito_url": "https://www.agriturismobellavita.it/",
        "tags": ["Ogni taglia", "Cani illimitati", "Nessun supplemento", "Piscina per cani"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo nel pistoiese, tra Firenze e Lucca, pensato per chi viaggia con cani "
            "di qualsiasi taglia — compresi i cani grandi e giganti che altrove trovano solo "
            "porte chiuse. Secondo quanto dichiarato sul sito ufficiale, la struttura accoglie "
            "più di un animale a prenotazione senza limiti di numero e senza supplemento, ed è "
            "convenzionata con un ambulatorio veterinario attivo 24 ore su 24. Dispone di una "
            "piscina dedicata ai cani e di un'area giochi recintata, con attività educative e "
            "ricreative seguite da un educatore cinofilo diplomato."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Più di uno, nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Piscina dedicata ai cani",
            "Area giochi recintata",
            "Attività con educatore cinofilo",
            "Convenzione ambulatorio veterinario h24",
        ],
    },
    {
        "slug": "baita-gorck",
        "nome": "Baita Gorck",
        "comune": "Val Rendena, Parco Adamello Brenta",
        "regione": "Trentino",
        "regione_slug": "trentino",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/rifugi-e-baite/italia/trentino-alto-adige/trento/rifugio-gorck",
        "sito_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/rifugi-e-baite/italia/trentino-alto-adige/trento/rifugio-gorck",
        "tags": ["Fino a taglia grande", "Ammessi al ristorante", "Pulizie +10€"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Baita immersa nel Parco Naturale Adamello Brenta, in Val Rendena (Trentino). "
            "Secondo la scheda pubblica consultata, accetta cani fino a taglia grande e li "
            "ammette al guinzaglio anche negli spazi del ristorante — una condizione che molte "
            "strutture di montagna non offrono. È previsto un supplemento di pulizia di 10€ a "
            "soggiorno per gli ospiti con animali."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (25–45 kg)"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "10€ di pulizia extra a soggiorno"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Cani ammessi al ristorante (al guinzaglio)",
            "Nel Parco Naturale Adamello Brenta",
        ],
    },
    {
        "slug": "masseria-le-terrazze-di-serranova",
        "nome": "Masseria Le Terrazze di Serranova",
        "comune": "Serranova, Carovigno (Brindisi)",
        "regione": "Puglia",
        "regione_slug": "puglia",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/puglia/brindisi/masseria-le-terrazze-di-serranova",
        "sito_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/puglia/brindisi/masseria-le-terrazze-di-serranova",
        "tags": ["Fino a 30 kg", "Nessun supplemento", "Area sgambamento"],
        "taglia_bucket": "media",
        "descrizione": (
            "Masseria nell'entroterra di Carovigno (Brindisi), in Puglia. Secondo le fonti "
            "pubbliche consultate, accoglie cani fino a 30 kg — un cane di taglia grande o "
            "media per camera, oppure due cani piccoli — senza alcun supplemento giornaliero "
            "per gli animali. Dispone di un'area dedicata allo sgambamento e di una piscina a "
            "uso esclusivo."
        ),
        "fatti": [
            ("Taglia massima", "Fino a 30 kg (un cane grande/medio per camera)"),
            ("Numero di cani", "1 se grande/medio, 2 se piccoli"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Area dedicata allo sgambamento",
            "Piscina a uso esclusivo",
            "Doccia esterna",
        ],
    },
]

ALL_TAGS = []
for _s in STRUTTURE:
    for _t in _s["tags"]:
        if _t not in ALL_TAGS:
            ALL_TAGS.append(_t)
