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
* **`05_webook/site/`**: I file pronti per il sito web (`index.html`).

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: File descrittivo del libro (titolo, autore, ecc.) secondo lo standard per librerie e distributori.
* **`output_schema_org.json`**: File che aiuta i motori di ricerca a comprendere e indicizzare semanticamente l'opera.

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato impaginato a pagina fissa per la stampa tradizionale.
* **`output.epub`**: Formato per la lettura ottimizzata su e-reader.
* **`index.html`**: Il libro in formato sito web interattivo.

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi dell'editoria digitale automatizzando il flusso da una singola sorgente (*Single Source Publishing*). Lo script **`main.py`** agisce come orchestratore centrale delle operazioni:

1. **Ideazione:** Scelta del tema ("One Health").
2. **Acquisizione:** I contenuti base vengono scritti nei file `input.md` e `metadati.yaml`.
3. **Azione di `main.py` (Revisione e Redazione):** Lo script preleva i file sorgenti e, parallelamente, svolge tre compiti:
    * Pulisce automaticamente il testo di `input.md` e inietta i riferimenti per il glossario.
    * Estrae le informazioni da `metadati.yaml` per generare i file `output_onix.json` e `output_schema_org.json`.
    * Prepara l'applicazione delle regole grafiche presenti in `epub.css`.
4. **Progettazione Grafica:** I fogli di stile vengono associati al testo ripulito.
5. **Compilazione:** Lo script `main.py` passa tutti i dati elaborati a `Pandoc`, il quale genera definitivamente i formati finali (`output.pdf`, `output.epub`, `index.html`).
6. **Distribuzione:** I file finali vengono caricati su GitHub e pubblicati online.

### Schema Visivo del Processo

Il diagramma ricalca l'esatto percorso logico e tecnologico dei file, partendo dai documenti originali fino alla pubblicazione web.

```mermaid
graph LR
    %% Definizione degli step base
    TEMA[Ideazione:<br/>Tema One Health]
    SORGENTI[Acquisizione:<br/>input.md, metadati.yaml]
    
    %% Nodi orchestratori (Cerchi)
    MAIN((Azione automatica:<br/>script main.py))
    PANDOC((Compilazione finalizzata:<br/>Pandoc & XeLaTeX))
    
    %% Rami paralleli
    MD[Revisione:<br/>Pulizia testo input.md<br/>e iniezione Glossario]
    JSON[Metadati generati:<br/>output_onix.json,<br/>output_schema_org.json]
    CSS[Grafica applicata:<br/>Lettura epub.css<br/>e regole stampa]
    
    %% Nodo finale (Rombo)
    OUT{Caricamento finale:<br/>GitHub Pages}

    %% Flusso delle operazioni
    TEMA --> SORGENTI
    SORGENTI --> MAIN

    %% Diramazione dal main.py
    MAIN --> MD
    MAIN --> JSON
    MAIN --> CSS

    %% Convergenza verso il compilatore
    MD --> PANDOC
    JSON --> PANDOC
    CSS --> PANDOC

    %% Pubblicazione
    PANDOC --> OUT