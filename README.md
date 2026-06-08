# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

* **Repository GitHub:** [Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico](https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico)
* **Web-Book Navigabile:** [Clicca qui per visualizzare il Web-Book su GitHub Pages](https://envalope.github.io/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico/)

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File di partenza inseriti dall'autore (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Regole grafiche e di impaginazione (`epub.css` per sito web ed e-book).
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
3. **Azione di `main.py` (Revisione e Redazione):** Lo script preleva i file sorgenti e, parallelamente, svolge compiti di preparazione:
    * Pulisce il testo di `input.md` e inietta i riferimenti per il glossario.
    * Estrae le informazioni da `metadati.yaml` per generare i metadati JSON.
4. **Progettazione Grafica:** Lo script aggancia i fogli di stile, in particolare `epub.css`, fondamentale per la resa visiva del Web-Book (sito statico) e dell'EPUB.
5. **Compilazione:** `main.py` passa il testo elaborato e la grafica a `Pandoc`, il quale compila simultaneamente i documenti per la stampa (`output.pdf`) e i formati digitali, generando il sito statico (`index.html`) e l'e-book (`output.epub`).
6. **Distribuzione:** Tutti gli output vengono inviati alla repository e il Web-Book viene ospitato online su GitHub Pages.

### Schema Visivo del Processo

Il diagramma ricalca il percorso logico e tecnologico dei file, evidenziando le operazioni in parallelo gestite dallo script principale fino alla generazione del sito statico e dei documenti editoriali.

```mermaid
graph LR
    %% Definizione degli step base
    TEMA[Ideazione:<br/>Tema One Health]
    SORGENTI[Acquisizione contenuti:<br/>input.md e metadati.yaml]
    
    %% Nodi orchestratori (Cerchi)
    MAIN((Elaborazione con<br/>script main.py))
    PANDOC((Compilazione con<br/>Pandoc & XeLaTeX))
    
    %% Rami paralleli centrali
    MD[Modifica file .md:<br/>Pulizia testo e glossario]
    JSON[Generazione Metadati:<br/>output_onix e schema_org]
    GRAFICA[Applicazione foglio di stile:<br/>epub.css per Web-Book/EPUB<br/>e regole per PDF]
    
    %% Nodi di output finali
    WEB[Web-Book statico:<br/>index.html]
    DOCS[Documenti editoriali:<br/>output.pdf, output.epub]

    %% Nodo finale (Rombo)
    OUT{Caricamento finale:<br/>su GitHub Pages}

    %% Flusso delle operazioni
    TEMA --> SORGENTI
    SORGENTI --> MAIN

    %% Diramazione dal main.py
    MAIN --> MD
    MAIN --> GRAFICA
    MAIN --> JSON

    %% Convergenza verso il compilatore
    MD --> PANDOC
    GRAFICA --> PANDOC

    %% Creazione degli output
    PANDOC --> WEB
    PANDOC --> DOCS

    %% Pubblicazione
    WEB --> OUT
    DOCS --> OUT
    JSON --> OUT