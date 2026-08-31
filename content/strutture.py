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
    {
        "slug": "agriturismo-delizia-deste",
        "nome": "Agriturismo Delizia d'Este",
        "comune": "Ferrara",
        "regione": "Emilia-Romagna",
        "regione_slug": "emilia-romagna",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/emilia-romagna/ferrara/agriturismo-delizia-d-este",
        "sito_url": "https://www.deliziadeste.it/",
        "tags": ["Ogni taglia", "Più cani ammessi", "Nessun supplemento", "Piscina e laghetto per cani"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo a pochi chilometri da Ferrara, con un parco recintato di 2 ettari "
            "attrezzato apposta per i cani. Secondo la fonte pubblica consultata, ammette cani di "
            "ogni taglia, anche più di uno per prenotazione, senza supplemento. Dispone di una "
            "piscina ad uso condiviso cani-umani, un laghetto dedicato al nuoto dei cani e "
            "un'area di lavaggio self-service."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia"),
            ("Numero di cani", "Più di uno, nessun limite specificato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Parco recintato di 2 ettari",
            "Piscina ad uso condiviso cani-umani",
            "Laghetto dedicato al nuoto dei cani",
            "Area di lavaggio self-service per cani",
        ],
    },
    {
        "slug": "agriturismo-baglio-don-bartolo",
        "nome": "Agriturismo Baglio Don Bartolo",
        "comune": "Castelluzzo, San Vito Lo Capo (Trapani)",
        "regione": "Sicilia",
        "regione_slug": "sicilia",
        "fonte_nome": "agriturismo.it",
        "fonte_url": "https://en.agriturismo.it/farmhouse/sicily/trapani/BaglioDonBartolo-8871927/index.html",
        "sito_url": "https://www.bagliodonbartolo.com/",
        "tags": ["Fino a taglia grande", "Accesso ristorante", "Pulizie 10€/giorno"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Agriturismo a Castelluzzo, vicino a San Vito Lo Capo (Trapani), in Sicilia. Secondo "
            "la fonte pubblica consultata, ammette cani fino a taglia grande (25–45 kg) in "
            "alloggio, ristorante e aree comuni, con museruola e guinzaglio obbligatori negli "
            "spazi esterni. È previsto un supplemento di pulizia di 10€ al giorno."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (25–45 kg)"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "10€ al giorno di pulizia extra"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso a ristorante e aree comuni",
            "Museruola e guinzaglio obbligatori all'esterno",
            "A pochi km dalla spiaggia di San Vito Lo Capo",
        ],
    },
    {
        "slug": "agriturismo-il-cerro-zagarese",
        "nome": "Agriturismo Il Cerro - Zagarese",
        "comune": "Fuscaldo (Cosenza)",
        "regione": "Calabria",
        "regione_slug": "calabria",
        "fonte_nome": "agriturismo.it",
        "fonte_url": "https://www.agriturismo.it/it/agriturismi/calabria/cosenza/IlCerro-AgriturismoZagarese-8501151/index.html",
        "sito_url": "https://www.agriturismozagarese.it/",
        "tags": ["Ogni taglia", "Supplemento richiesto"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo su un rilievo collinare a dieci minuti dal mare, a Fuscaldo, in "
            "provincia di Cosenza, Calabria. Secondo la fonte pubblica consultata, ammette cani "
            "di ogni taglia, inclusa quella gigante (oltre 45 kg), con obbligo di guinzaglio "
            "negli ambienti interni e la necessità di segnalare la presenza dell'animale al "
            "momento della prenotazione. È previsto un supplemento per gli animali, il cui "
            "importo va confermato direttamente con la struttura: le fonti consultate non sono "
            "concordi su cifra esatta e periodicità."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Richiesto, importo da confermare con la struttura"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Piscina con vista mare",
            "Cucina calabrese in loco",
            "A dieci minuti dal mare",
        ],
    },
    {
        "slug": "casale-civetta",
        "nome": "Casale Civetta",
        "comune": "Trecastelli (Ancona)",
        "regione": "Marche",
        "regione_slug": "marche",
        "fonte_nome": "zampavacanza.it",
        "fonte_url": "https://www.zampavacanza.it/struttura-animali-ammessi/4534",
        "sito_url": "https://www.casalecivetta.it/",
        "tags": ["Ogni taglia", "Più cani ammessi", "Accesso piscina"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo ecosostenibile tra il mare Adriatico vicino Senigallia e il borgo "
            "medievale di Corinaldo, a Trecastelli, in provincia di Ancona, Marche. Secondo la "
            "fonte pubblica consultata, ammette cani di ogni taglia e più di tre animali a "
            "prenotazione, con accesso libero a tutte le aree della struttura, compresa la zona "
            "piscina panoramica. È previsto un supplemento di 10€ a notte per un solo cane (8€ a "
            "notte per cane se più di uno), più 10€ di pulizie extra a soggiorno."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Più di tre a prenotazione"),
            ("Supplemento animali", "10€/notte (8€/notte/cane se più di uno) + 10€ pulizie"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso alla piscina panoramica",
            "Parco alberato con percorsi pedonali",
            "Vicino al mare di Senigallia e al borgo di Corinaldo",
        ],
    },
    {
        "slug": "monferrato-nel-cuore",
        "nome": "Monferrato nel Cuore",
        "comune": "Casalborgone (Torino)",
        "regione": "Piemonte",
        "regione_slug": "piemonte",
        "fonte_nome": "agriturismo.it",
        "fonte_url": "https://www.agriturismo.it/it/agriturismi/piemonte/torino/Monferratonelcuore-7560096/index.html",
        "sito_url": "https://www.monferratonelcuore.com/",
        "tags": ["Ogni taglia"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo a Casalborgone, nel Monferrato torinese, in Piemonte. Secondo la fonte "
            "pubblica consultata, ammette cani di ogni taglia, inclusa quella gigante (oltre 45 "
            "kg), a condizione che siano educati e sorvegliati dal proprietario; la presenza "
            "dell'animale va segnalata al momento della prenotazione. Supplemento e numero "
            "massimo di cani per prenotazione non sono specificati nella fonte consultata."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Non specificato nella fonte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Nel cuore del Monferrato torinese",
            "Animali ammessi a condizione di essere sorvegliati",
        ],
    },
    {
        "slug": "agriturismo-colja-jozko",
        "nome": "Agriturismo Colja Jozko",
        "comune": "Samatorza, Sgonico (Trieste)",
        "regione": "Friuli-Venezia Giulia",
        "regione_slug": "friuli-venezia-giulia",
        "fonte_nome": "zampavacanza.it",
        "fonte_url": "https://www.zampavacanza.it/struttura-animali-ammessi/2729",
        "sito_url": "https://agriturismocolja.it/",
        "tags": ["Fino a taglia grande", "Area sgambamento", "Accesso ristorante"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Azienda agricola nel Carso triestino, a Samatorza (Sgonico), a pochi chilometri dal "
            "mare e dal confine con la Slovenia, nella Denominazione di Origine Controllata "
            "Friuli Carso. Secondo la fonte pubblica consultata, ammette cani fino a taglia "
            "grande, con area sgambamento dedicata, accesso al ristorante interno e percorsi "
            "pensati per le passeggiate con il cane. Supplemento e numero massimo di animali per "
            "prenotazione non sono specificati nella fonte consultata."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (25–45 kg)"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Non specificato nella fonte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Area sgambamento dedicata ai cani",
            "Accesso al ristorante interno",
            "Percorsi per passeggiate con il cane",
            "A pochi km dal mare e dal confine sloveno",
        ],
    },
    {
        "slug": "agriturismo-le-tre-poiane",
        "nome": "Agriturismo Le Tre Poiane",
        "comune": "Penne (Pescara)",
        "regione": "Abruzzo",
        "regione_slug": "abruzzo",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/abruzzo/pescara/le-tre-poiane",
        "sito_url": "https://www.letrepoiane.it/",
        "tags": ["Ogni taglia", "Più cani ammessi", "Nessun supplemento", "Accesso ristorante"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Azienda agricola biologica di 11 ettari sulle colline del pescarese, a circa 250 "
            "metri di altitudine, a Penne. Secondo la fonte pubblica consultata, ammette cani di "
            "ogni taglia — più di uno a prenotazione — senza alcun supplemento, con accesso al "
            "punto ristoro interno. La piscina della struttura affaccia sulla Majella e sulle "
            "valli circostanti."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Più di uno, nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso al punto ristoro interno",
            "Piscina con vista sulla Majella",
            "Azienda agricola biologica di 11 ettari",
        ],
    },
    {
        "slug": "podere-vignali",
        "nome": "Agriturismo Podere Vignali",
        "comune": "Pari, Civitella Paganico (Grosseto)",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/agriturismo-masi-case-rurali/italia/toscana/grosseto/agriturismo-podere-vignali",
        "sito_url": "https://www.poderevignali.it/",
        "tags": ["Ogni taglia", "Nessun supplemento"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo tra uliveti e bosco sulle colline della Maremma, a Pari, nel comune di "
            "Civitella Paganico (Grosseto), Toscana. Secondo la fonte pubblica consultata, ammette "
            "cani di ogni taglia senza alcun supplemento. La struttura ha 4 camere, tutte con "
            "ingresso indipendente dall'esterno, e una piscina panoramica."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Camere con ingresso indipendente dall'esterno",
            "Piscina panoramica",
            "Circondato da uliveti e bosco",
        ],
    },
    {
        "slug": "poggio-al-vento",
        "nome": "Agriturismo Poggio al Vento",
        "comune": "Castiglione d'Orcia (Siena)",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "agriturismo.it",
        "fonte_url": "https://www.agriturismo.it/it/agriturismi/toscana/siena/PoggioalventoinValdOrcia-9100147/index.html",
        "sito_url": "https://www.poggioalvento.net/",
        "tags": ["Ogni taglia"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo biologico nel cuore della Val d'Orcia, tra vigneti e ulivi, a Castiglione "
            "d'Orcia (Siena), Toscana. Secondo la fonte pubblica consultata, ammette cani di ogni "
            "taglia, inclusa quella gigante (oltre 45 kg), a condizione che siano educati e "
            "sorvegliati; guinzaglio richiesto all'esterno e museruola in alcune aree. Numero "
            "massimo di animali e supplemento non specificati nella fonte."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Non specificato nella fonte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "4 appartamenti indipendenti",
            "Agricoltura biologica",
            "Nel cuore della Val d'Orcia",
        ],
    },
]

STRUTTURE += [
    {
        "slug": "hotel-ville-bianchi",
        "nome": "Hotel Ville Bianchi",
        "comune": "Grado (Gorizia)",
        "regione": "Friuli-Venezia Giulia",
        "regione_slug": "friuli-venezia-giulia",
        "fonte_nome": "villebianchi.com",
        "fonte_url": "https://www.villebianchi.com/pet-friendly/",
        "sito_url": "https://www.villebianchi.com/",
        "tags": ["Fino a taglia grande", "Supplemento 20€/notte"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Hotel 4 stelle con appartamenti sul mare a Grado, Friuli-Venezia Giulia. Secondo la "
            "fonte pubblica consultata (il sito ufficiale), ammette cani di taglia grande fino a "
            "40 kg, ben educati, con un supplemento di 20€ a notte. L'accesso al ristorante non è "
            "consentito agli animali. La struttura fornisce un kit di benvenuto per il cane e ha "
            "un'ampia area sgambamento ombreggiata."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (40 kg)"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "20€ a notte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Kit di benvenuto per il cane",
            "Ampia area sgambamento ombreggiata",
            "Accesso al mare",
            "Non ammessi nell'area ristorante",
        ],
    },
    {
        "slug": "casa-mori",
        "nome": "Casa Mori",
        "comune": "Certaldo (Firenze)",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "casamori.com",
        "fonte_url": "https://www.casamori.com/",
        "sito_url": "https://www.casamori.com/",
        "tags": ["Ogni taglia", "Accesso ovunque", "Veterinario in loco"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Agriturismo ricavato dalla ristrutturazione di un fienile del Seicento, nella "
            "campagna a circa 6 km da Certaldo, in provincia di Firenze, Toscana. Secondo la "
            "fonte pubblica consultata (il sito ufficiale), ammette cani di ogni taglia con "
            "accesso a tutti gli spazi della struttura. Uno dei proprietari è veterinario, con "
            "disponibilità di assistenza in loco."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Non specificato nella fonte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso a tutti gli spazi della struttura",
            "Uno dei proprietari è veterinario",
            "Nella campagna a 6 km da Certaldo",
        ],
    },
    {
        "slug": "hotel-imperiale-bellaria",
        "nome": "Hotel Imperiale",
        "comune": "Bellaria-Igea Marina (Rimini)",
        "regione": "Emilia-Romagna",
        "regione_slug": "emilia-romagna",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/hotel/italia/emilia-romagna/rimini/hotel-imperiale",
        "sito_url": "https://www.hotelimperialebellaria.it/",
        "tags": ["Fino a taglia grande", "Più cani ammessi", "Nessun supplemento"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Hotel sul mare a Bellaria-Igea Marina, in provincia di Rimini, Emilia-Romagna. "
            "Secondo la fonte pubblica consultata, ammette cani fino a taglia grande (non "
            "gigante), anche più di uno a prenotazione, senza alcun supplemento. La struttura "
            "offre un kit di benvenuto, un giardino e un'area dedicata sulla spiaggia a pochi "
            "metri dall'hotel."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (non gigante)"),
            ("Numero di cani", "Più di uno, nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Kit di benvenuto per il cane",
            "Giardino con angolo ciotole",
            "Area dedicata in spiaggia a pochi metri dall'hotel",
        ],
    },
    {
        "slug": "bb-hotel-arezzo",
        "nome": "B&B Hotel Arezzo",
        "comune": "Arezzo",
        "regione": "Toscana",
        "regione_slug": "toscana",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/hotel/italia/toscana/arezzo/hotel-bb-arezzo",
        "sito_url": "https://www.hotel-bb.com/it/hotel/arezzo",
        "tags": ["Fino a taglia grande", "Supplemento 5€/notte"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Hotel della catena B&B Hotels a circa 3 km dal centro di Arezzo, Toscana. Secondo la "
            "fonte pubblica consultata, ammette cani di ogni razza fino a taglia grande, con un "
            "supplemento di 5€ a notte per animale, fino a un massimo di 2 cani per camera."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande"),
            ("Numero di cani", "Fino a 2 per camera"),
            ("Supplemento animali", "5€ a notte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "A 3 km dal centro di Arezzo",
            "Vicino al centro fieristico",
        ],
    },
    {
        "slug": "ai-pozzi-village-resort",
        "nome": "Ai Pozzi Village Resort & SPA",
        "comune": "Loano (Savona)",
        "regione": "Liguria",
        "regione_slug": "liguria",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/villaggi-vacanze-resort/italia/liguria/savona/ai-pozzi-village",
        "sito_url": "https://www.aipozzivillage.com/",
        "tags": ["Ogni taglia", "Supplemento 15€/giorno"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Hotel e residence con SPA a Loano, sulla Riviera delle Palme, Liguria. Secondo la "
            "fonte pubblica consultata, ammette cani di ogni taglia con un supplemento di 15€ al "
            "giorno per animale, senza costi di pulizia aggiuntivi. Kit di benvenuto con ciotole "
            "e snack, area cani dedicata con sabbia per il gioco."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "15€ al giorno"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Kit di benvenuto con ciotole e snack",
            "Area cani dedicata con sabbia per il gioco",
            "SPA in struttura",
        ],
    },
    {
        "slug": "villaggio-di-giuele",
        "nome": "Il Villaggio di GiuEle",
        "comune": "Finale Ligure (Savona)",
        "regione": "Liguria",
        "regione_slug": "liguria",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/villaggi-vacanze-resort/italia/liguria/savona/il-villaggio-di-giuele",
        "sito_url": "https://www.ilvillaggiodigiuele.it/",
        "tags": ["Ogni taglia", "Più cani ammessi", "Nessun supplemento"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Villaggio residence immerso nella macchia mediterranea a Finale Ligure, Savona, "
            "Liguria. Secondo la fonte pubblica consultata, ammette cani di ogni taglia, anche "
            "più di tre per cliente, senza alcun supplemento. La struttura ha convenzioni con "
            "diverse spiagge pet friendly della zona di Finale Ligure."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Più di tre, nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Convenzioni con spiagge pet friendly locali",
            "Ciotole per acqua e cibo su richiesta",
            "Due piscine, centro equestre di fronte",
        ],
    },
]

STRUTTURE += [
    {
        "slug": "chalet-du-lys-hotel-spa",
        "nome": "Chalet du Lys Hotel & SPA",
        "comune": "Gressoney-La-Trinité (Aosta)",
        "regione": "Valle d'Aosta",
        "regione_slug": "valle-d-aosta",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/hotel/italia/valle-d-aosta/aosta/chalet-du-lys",
        "sito_url": "https://chaletdulys.it/",
        "tags": ["Ogni taglia", "Nessun supplemento"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Hotel con SPA ai piedi del Monte Rosa, a Gressoney-La-Trinité, Valle d'Aosta. "
            "Secondo la fonte pubblica consultata, ammette cani di ogni taglia e razza, in "
            "camera e al ristorante, senza supplemento. Sulle funivie della zona è richiesto "
            "guinzaglio e museruola per il trasporto."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Accesso al ristorante dell'hotel",
            "Ampi spazi verdi ai piedi del Monte Rosa",
            "SPA in struttura",
        ],
    },
    {
        "slug": "summer-residence-bunte",
        "nome": "Summer Residence Bunte",
        "comune": "Olbia (Sassari)",
        "regione": "Sardegna",
        "regione_slug": "sardegna",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/residence-aparthotel/italia/sardegna/sassari/summer-residence-bunte",
        "sito_url": "https://www.residencebunte.it/",
        "tags": ["Fino a taglia grande", "Supplemento 5€/notte"],
        "taglia_bucket": "grande",
        "descrizione": (
            "Residence sulla costa orientale della Sardegna, a Murta Maria (Olbia), a pochi "
            "passi dal mare. Secondo la fonte pubblica consultata, ammette cani fino a taglia "
            "grande (non oltre), con un supplemento di 5€ a notte. Il residence ha un ampio "
            "giardino ed è vicino a spiagge pet friendly della zona."
        ),
        "fatti": [
            ("Taglia massima", "Fino a taglia grande (no XL)"),
            ("Numero di cani", "Non specificato nella fonte"),
            ("Supplemento animali", "5€ a notte"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Ampio giardino intorno alla struttura",
            "Vicino a spiagge pet friendly",
            "Appartamenti con angolo cottura",
        ],
    },
    {
        "slug": "case-vacanza-marina-porto-rotondo",
        "nome": "Case Vacanza Marina",
        "comune": "Porto Rotondo, Olbia (Sassari)",
        "regione": "Sardegna",
        "regione_slug": "sardegna",
        "fonte_nome": "dogwelcome.it",
        "fonte_url": "https://www.dogwelcome.it/strutture-cani-animali-ammessi/ville-case-vacanza-appartamenti-in-affitto/italia/sardegna/olbia-tempio/case-vacanza-marina-porto-rotondo",
        "sito_url": "https://beb.it/marinaportorotondo/",
        "tags": ["Ogni taglia", "Più cani ammessi", "Nessun supplemento"],
        "taglia_bucket": "ogni",
        "descrizione": (
            "Dieci appartamenti immersi in un parco di 5.000 mq a Porto Rotondo, frazione di "
            "Olbia, a 500 metri da una spiaggia pet friendly. Secondo la fonte pubblica "
            "consultata, ammette cani di ogni taglia, anche più di tre per cliente, senza "
            "supplemento; le recensioni degli ospiti confermano l'accoglienza di cani di "
            "taglia grande come i pastori maremmani. Soggiorno minimo di una settimana."
        ),
        "fatti": [
            ("Taglia massima", "Ogni taglia, inclusa gigante"),
            ("Numero di cani", "Più di tre, nessun limite dichiarato"),
            ("Supplemento animali", "Nessuno dichiarato"),
            ("Cauzione", "Non indicata nella fonte"),
        ],
        "servizi": [
            "Parco recintato di 5.000 mq",
            "Area lavaggio cani esterna",
            "A 500 metri da una spiaggia pet friendly",
        ],
    },
]

ALL_TAGS = []
for _s in STRUTTURE:
    for _t in _s["tags"]:
        if _t not in ALL_TAGS:
            ALL_TAGS.append(_t)
