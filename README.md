# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

* **Repository GitHub:** [Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico](https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico)
* **Web-Book Navigabile:** [Clicca qui per visualizzare il Web-Book su GitHub Pages](https://envalope.github.io/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico/)

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File di partenza inseriti dall'autore (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Regole grafiche e di impaginazione (`epub.css`).
* **`03_Script/`**: Il motore di automazione del progetto (`main.py`).
* **`04_Output/`**: I documenti e i dati generati automaticamente (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: La cartella dedicata al sito statico Web-Book (`index.html`).

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: File descrittivo del libro (titolo, autore, ecc.) secondo lo standard per librerie e distributori.
* **`output_schema_org.json`**: File che aiuta i motori di ricerca a comprendere e indicizzare semanticamente l'opera.

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato impaginato a pagina fissa per la stampa tradizionale.
* **`output.epub`**: Formato per la lettura ottimizzata su e-reader.
* **`index.html`**: Il libro in formato sito web (Web-Book statico) interattivo.

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi dell'editoria digitale automatizzando il flusso da una singola sorgente (*Single Source Publishing*). Lo script **`main.py`** agisce come orchestratore centrale delle operazioni:

1. **Ideazione:** Scelta del tema ("One Health").
2. **Acquisizione:** I contenuti base vengono scritti nei file `input.md` e `metadati.yaml`.
3. **Revisione e Redazione (`main.py`):** Lo script preleva i file sorgenti e pulisce il testo di `input.md` correggendo spaziature e inserendo i collegamenti ipertestuali per il glossario.
4. **Progettazione Grafica:** I fogli di stile, in particolare `epub.css` (fondamentale per la resa visiva del sito statico e dell'e-book), vengono preparati per essere associati al testo.
5. **Produzione (`main.py` + `Pandoc`):** In questa fase avvengono due processi paralleli. Da un lato, lo script estrae i dati da `metadati.yaml` per creare i file JSON. Dall'altro, passa il testo pulito e la grafica al convertitore `Pandoc`, che genera simultaneamente i documenti per la stampa (`output.pdf`) e i formati digitali (`index.html` e `output.epub`).
6. **Distribuzione:** Tutti gli output vengono inviati alla repository e il Web-Book viene ospitato online su GitHub Pages.

### Schema Visivo del Processo

Il seguente diagramma mostra in modo compatto come i file sorgenti attraversino lo script e i compilatori fino a diventare un prodotto finito, seguendo le 6 fasi editoriali.

```mermaid
graph LR
    %% 1. IDEAZIONE & 2. ACQUISIZIONE
    ID[1. Ideazione:<br/>Tema One Health] --> IN[2. Acquisizione:<br/>input.md, metadati.yaml]
    
    %% 3. REVISIONE
    IN --> MAIN((3. Revisione testuale:<br/>Script main.py))
    
    %% 4. GRAFICA
    MAIN -->|Testo pulito| GRAF[4. Progettazione Grafica:<br/>Applica epub.css]
    
    %% 5. PRODUZIONE (Divisa tra main.py per i dati e Pandoc per i documenti)
    MAIN -->|Estrae dati JSON| META[5. Produzione Metadati:<br/>output_onix.json<br/>output_schema_org.json]
    GRAF --> PANDOC((5. Produzione Documenti:<br/>Compilatore Pandoc))
    
    PANDOC --> DOCS[Documenti:<br/>output.pdf, output.epub]
    PANDOC --> WEB[Sito Web-Book:<br/>index.html]
    
    %% 6. DISTRIBUZIONE
    META --> OUT{6. Distribuzione:<br/>GitHub Pages}
    DOCS --> OUT
    WEB --> OUT

    %% STILI COMPATTI
    classDef fase fill:#f8f9fa,stroke:#adb5bd,stroke-width:2px,color:#000
    classDef script fill:#fff3cd,stroke:#ffc107,stroke-width:3px,color:#000
    classDef output fill:#e2e3e5,stroke:#6c757d,stroke-width:2px,color:#000
    
    class ID,IN,GRAF fase
    class MAIN,PANDOC script
    class META,DOCS,WEB output
    class OUT fase