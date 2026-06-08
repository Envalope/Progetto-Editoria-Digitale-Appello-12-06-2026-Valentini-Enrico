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

Il seguente diagramma espande le 6 fasi editoriali, mostrando esattamente come i file sorgenti attraversino lo script e i compilatori fino a diventare un prodotto finito.

```mermaid
graph TD
    %% FASE 1
    subgraph Fase 1 [1. Ideazione]
        TEMA[Scelta del Tema:<br/>One Health]
    end

    %% FASE 2
    subgraph Fase 2 [2. Acquisizione dei Contenuti]
        MD_IN[Testo sorgente:<br/>input.md]
        YAML_IN[Dati e configurazioni:<br/>metadati.yaml]
    end

    %% FASE 3
    subgraph Fase 3 [3. Revisione e Redazione]
        MAIN((Orchestratore:<br/>Script main.py))
        PULIZIA[Modifica file .md:<br/>Pulizia testo automatica<br/>e iniezione glossario]
    end

    %% FASE 4
    subgraph Fase 4 [4. Progettazione Grafica]
        STILI[Applicazione fogli di stile:<br/>epub.css per Web-Book/EPUB<br/>e regole per PDF]
    end

    %% FASE 5
    subgraph Fase 5 [5. Produzione]
        JSON_OUT[Metadati generati:<br/>output_onix.json<br/>output_schema_org.json]
        PANDOC((Compilazione finale:<br/>Pandoc & XeLaTeX))
        DOCS[Documenti Editoriali:<br/>output.pdf, output.epub]
        WEB[Sito Web-Book:<br/>index.html]
    end

    %% FASE 6
    subgraph Fase 6 [6. Distribuzione]
        GITHUB{Caricamento finale:<br/>GitHub Pages}
    end

    %% FLUSSO DEI COLLEGAMENTI
    TEMA --> MD_IN & YAML_IN
    
    %% Acquisizione verso il Main
    MD_IN --> MAIN
    YAML_IN --> MAIN
    
    %% Il Main smista le operazioni
    MAIN -->|Legge metadati.yaml| JSON_OUT
    MAIN -->|Elabora input.md| PULIZIA
    
    %% Dal testo pulito si passa alla grafica
    PULIZIA --> STILI
    
    %% Invio al compilatore
    STILI -->|Testo pulito + CSS| PANDOC
    
    %% Generazione dei file finali
    PANDOC --> DOCS
    PANDOC --> WEB
    
    %% Rilascio online
    JSON_OUT --> GITHUB
    DOCS --> GITHUB
    WEB --> GITHUB

    %% STILI DEI NODI (Colori per differenziare documenti, azioni e fine)
    classDef file fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    classDef script fill:#fff9c4,stroke:#fbc02d,stroke-width:3px,color:#000
    classDef fine fill:#eceff1,stroke:#546e7a,stroke-width:3px,color:#000
    
    class TEMA,MD_IN,YAML_IN,PULIZIA,STILI,JSON_OUT,DOCS,WEB file
    class MAIN,PANDOC script
    class GITHUB fine