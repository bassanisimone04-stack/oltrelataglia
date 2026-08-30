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
    {
        "slug": "ecoresort-il-cantico-della-natura",
        "nome": "EcoResort Il Cantico della Natura",
        "comune": "Magione (Perugia)",
        "regione": "Umbria",
        "regione_slug": "umbria",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/umbria/perugia/il-cantico-della-natura",
        "sito_url": "https://www.ilcanticodellanatura.it/",
        "tags": ["Ogni taglia", "Fino a 4 cani", "Nessun supplemento", "Area sgambamento recintata"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Ecoresort vicino al Lago Trasimeno, a Magione (Perugia). Secondo la scheda pubblica "
            "consultata, ammette cani di ogni taglia fino a un massimo di 4 per unità abitativa, "
            "senza alcun supplemento per gli animali. Dispone di un'area sgambamento recintata e "
            "di unità con giardino o déhors recintato privato — utile per chi viaggia con più "
            "cani grandi insieme."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia"),
            ("Numero di cani", "Fino a 4 per unità"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Area sgambamento recintata",
            "Unità con giardino/déhors recintato privato",
            "Vicino al Lago Trasimeno",
        ],
    },
    {
        "slug": "agriturismo-casale-degli-olmi",
        "nome": "Agriturismo Casale degli Olmi",
        "comune": "Perugia",
        "regione": "Umbria",
        "regione_slug": "umbria",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/umbria/perugia/agriturismo-casale-degli-olmi",
        "sito_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/umbria/perugia/agriturismo-casale-degli-olmi",
        "tags": ["Ogni taglia", "Fino a 2 cani", "Nessun supplemento", "Unità con zona recintata"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo nella campagna intorno a Perugia, in Umbria. Secondo la fonte pubblica "
            "consultata, ammette cani di tutte le taglie, fino a un massimo di 2 per prenotazione, "
            "senza alcun supplemento. L'appartamento \"Ceraso\", segnalato come particolarmente "
            "adatto a chi viaggia con un cane, si trova al piano terra con una zona recintata "
            "dedicata."
        ),
        "fatti": [
            ("Taglia massima", "Tutte le taglie"),
            ("Numero di cani", "Fino a 2 per prenotazione"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Appartamento al piano terra con zona recintata",
        ],
    },
    {
        "slug": "residence-mizar",
        "nome": "Residence Mizar",
        "comune": "Pietra Ligure (Savona)",
        "regione": "Liguria",
        "regione_slug": "liguria",
        "fonte_nome": "appartamentimizar.com",
        "fonte_url": "https://www.appartamentimizar.com/cani.php?lingua=italiano",
        "sito_url": "https://www.appartamentimizar.com/",
        "tags": ["Fino a taglia grande", "Nessun supplemento giornaliero", "Vicino a spiaggia per cani", "Pulizie 20€ a fine soggiorno"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Residence di appartamenti vacanza sulla Riviera di Ponente, a Pietra Ligure (Savona). "
            "Secondo la pagina dedicata sul sito ufficiale, accoglie cani fino a taglia grande "
            "senza alcun supplemento giornaliero — è previsto un contributo di 20€ a fine "
            "soggiorno per la pulizia extra, con un regolamento di convivenza da rispettare. Gli "
            "appartamenti hanno terrazzo, alcuni con giardino privato, e si trovano a circa 400 "
            "metri da una spiaggia attrezzata per cani."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Nessuno giornaliero; 20€ di pulizia a fine soggiorno"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "A circa 400 m da una spiaggia attrezzata per cani",
            "Area verde riservata agli animali",
            "Alcuni appartamenti con giardino privato",
        ],
    },
    {
        "slug": "podere-il-poggiolo",
        "nome": "Podere il Poggiolo",
        "comune": "Pontassieve, Chianti Rufina (Firenze)",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "podereilpoggiolo.it",
        "fonte_url": "https://www.podereilpoggiolo.it/en/services/holiday-with-your-pets.html",
        "sito_url": "https://www.podereilpoggiolo.it/en/",
        "tags": ["Taglia gigante ok", "Accesso ristorante", "50€/animale a settimana"],
        "taglia_bucket": "gigante",
        "descrizione": (
            "Azienda agricola biologica a conduzione familiare nel Chianti Rufina, a 23 km da "
            "Firenze. Secondo il sito ufficiale, l'intera fattoria è recintata e i cani di tutte "
            "le taglie — inclusa gigante — sono ammessi in alloggio, ristorante, aree comuni e "
            "piscina. Il costo dichiarato è di 50€ per animale a settimana."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "50€ per animale a settimana"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso a ristorante, aree comuni e piscina",
            "Intera proprietà recintata",
            "Azienda agricola biologica",
        ],
    },
    {
        "slug": "agriturismo-podere-bello",
        "nome": "Agriturismo Podere Bello",
        "comune": "Pitigliano, Maremma (Grosseto)",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/toscana/grosseto/agriturismo-podere-bello",
        "sito_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/toscana/grosseto/agriturismo-podere-bello",
        "tags": ["Fino a 3 cani", "Nessun supplemento", "Giardino privato recintato"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Agriturismo biologico nella Maremma toscana, vicino alle Terme di Saturnia e ai "
            "borghi di Sorano e Sovana. Secondo la fonte pubblica consultata, ammette cani fino a "
            "taglia grande (non oltre), massimo 3 per prenotazione, senza supplemento. Ogni "
            "alloggio ha un giardino privato recintato; su richiesta sono disponibili ciotole, "
            "dog-sitter e il contatto di un veterinario in zona."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (non XL)"),
            ("Numero di cani", "Fino a 3 per prenotazione"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Giardino privato recintato per ogni alloggio",
            "Ciotole su richiesta",
            "Dog-sitter su richiesta",
            "Veterinario disponibile in zona",
        ],
    },
    {
        "slug": "masseria-le-palmentelle",
        "nome": "Masseria le Palmentelle",
        "comune": "Lecce, Salento",
        "regione": "Puglia",
        "regione_slug": "puglia",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/puglia/lecce/masseria-le-palmentelle",
        "sito_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/puglia/lecce/masseria-le-palmentelle",
        "tags": ["Fino a taglia grande", "Un cane a camera", "Supplemento 5€/giorno"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Masseria nel Salento, in provincia di Lecce. Secondo la fonte pubblica consultata, "
            "accetta cani fino a taglia grande (non oltre), un animale per camera, con un "
            "supplemento dichiarato di 5€ al giorno. Le unità singole dispongono di giardino o "
            "déhors recintato privato."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (non XL)"),
            ("Numero di cani", "1 per camera"),
            ("Supplemento animali", "5€ al giorno"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Unità con giardino/déhors recintato privato",
        ],
    },
    {
        "slug": "agriturismo-il-podere",
        "nome": "Agriturismo il Podere",
        "comune": "Vedelago (Treviso)",
        "regione": "Veneto",
        "regione_slug": "veneto",
        "fonte_nome": "zampavacanza.it",
        "fonte_url": "https://www.zampavacanza.it/struttura-animali-ammessi/3904",
        "sito_url": "https://www.amicidelpodere.it/",
        "tags": ["Ogni taglia", "Accesso ristorante", "Supplemento 5€/giorno"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo a Vedelago, in provincia di Treviso, con animali della fattoria (tra cui "
            "un San Bernardo e alpaca) e un parco recintato dedicato ai cani. Secondo le fonti "
            "pubbliche consultate, ammette cani di tutte le taglie sia in camera sia in sala "
            "ristorante, con un supplemento dichiarato di 5€ al giorno che include ciotola, telo "
            "e tappetino. Il parco recintato ha aree ombreggiate distinte per cani grandi e "
            "piccoli."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "5€ al giorno (ciotola, telo e tappetino inclusi)"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso alla sala ristorante, non solo in camera",
            "Parco recintato con aree ombreggiate per cani grandi e piccoli",
            "Dog-sitter organizzabile su richiesta",
        ],
    },
    {
        "slug": "antico-cascinale-lombardo",
        "nome": "Antico Cascinale Lombardo",
        "comune": "Lonato del Garda (Brescia)",
        "regione": "Lombardia",
        "regione_slug": "lombardia",
        "fonte_nome": "zampavacanza.it",
        "fonte_url": "https://www.zampavacanza.it/struttura-animali-ammessi/4207",
        "sito_url": "https://www.anticocascinalelombardo.it/",
        "tags": ["Ogni taglia", "Quantità illimitata", "Gratis oltre 2 notti"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Bed & Breakfast a Lonato del Garda (Brescia), vicino al Lago di Garda. Secondo le "
            "fonti pubbliche consultate, gli animali di qualsiasi taglia e in qualsiasi numero "
            "soggiornano gratuitamente per soggiorni superiori alle 2 notti. La struttura dispone "
            "di un ampio cortile privato interamente recintato con cancello automatico, dove cani "
            "e bambini possono muoversi in sicurezza."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia"),
            ("Numero di cani", "Nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno per soggiorni oltre le 2 notti"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Cortile privato recintato con cancello automatico",
            "Vicino al Lago di Garda",
        ],
    },
]

ALL_TAGS = []
for _s in STRUTTURE:
    for _t in _s["tags"]:
        if _t not in ALL_TAGS:
            ALL_TAGS.append(_t)
