# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File sorgenti (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Fogli di stile (`epub.css` e asset grafici).
* **`03_Script/`**: Logica di sistema (`main.py`).
* **`04_Output/`**: File generati (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: File per la pubblicazione Web (`index.html` e asset).

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: Mappatura standard ONIX per la comunicazione commerciale editoriale (librerie, distributori).
* **`output_schema_org.json`**: JSON-LD per l'indicizzazione semantica (Rich Snippets Google).

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato editoriale a pagina fissa per stampa professionale.
* **`output.epub`**: Formato e-book fluido con CSS dedicato per e-reader.
* **`index.html`**: Web-Book interattivo, completo di glossario, navigazione e indice cliccabile.

## Il Flusso del Processo Editoriale

Il progetto automatizza le **6 fasi canoniche della produzione editoriale**, adottando il paradigma del *Single Source Publishing*. Il cuore pulsante dell'architettura è lo script `main.py`, che funge da orchestratore per le fasi di revisione testuale, generazione dei metadati e invocazione dei compilatori.

1. **Ideazione:** Definizione della tematica "One Health" e dell'architettura dell'informazione.
2. **Acquisizione dei contenuti:** Raccolta dei materiali grezzi in `01_Sorgenti/`. I contenuti testuali risiedono in `input.md` (Markdown), i parametri e i metadati in `metadati.yaml` (YAML) e le risorse visive in `copertina.png`.
3. **Revisione e redazione:** Lo script `main.py` (Python 3) legge il file `input.md` ed esegue una normalizzazione automatizzata. Utilizzando il modulo RegEx, corregge la formattazione e inietta dinamicamente gli apici di riferimento per il glossario, preparando un testo validato per la compilazione.
4. **Progettazione grafica:** Definizione delle regole visive. Vengono predisposti il foglio di stile `epub.css` per i formati a layout fluido (Web/EPUB) e le direttive tipografiche per il motore XeLaTeX (PDF).
5. **Produzione:** È la fase di compilazione orchestrata da `main.py`. Lo script esegue due compiti paralleli:
    * **Elaborazione dati:** Estrae i dati da `metadati.yaml` e genera direttamente i file `output_onix.json` e `output_schema_org.json`.
    * **Invocazione motore:** Richiama da riga di comando `Pandoc`, passandogli il testo revisionato e i file di stile, per generare in modo automatizzato `output.pdf`, `output.epub` e `index.html`.
6. **Distribuzione:** I file finali vengono versionati tramite `Git` e caricati sul repository online per essere hostati e resi navigabili pubblicamente tramite `GitHub Pages`.

### Schema di Processo Dettagliato

```mermaid
graph TD
    %% Fasi del Processo Editoriale
    subgraph F1 [1. Ideazione]
        ID[Definizione Tema: One Health]:::ideazione
    end

    subgraph F2 [2. Acquisizione dei contenuti]
        SRC[Testo: input.md<br/>Linguaggio: Markdown]:::acquisizione
        META[Parametri: metadati.yaml<br/>Linguaggio: YAML]:::acquisizione
        IMG[Grafica: copertina.png]:::acquisizione
    end

    subgraph F3 [3. Revisione e redazione]
        MAIN_REV[Script Orchestratore: main.py<br/>Azione: Normalizzazione e Glossario<br/>Linguaggio: Python / RegEx]:::revisione
    end

    subgraph F4 [4. Progettazione grafica]
        CSS[Stile E-book/Web: epub.css<br/>Linguaggio: CSS3]:::grafica
        TEX[Stile Stampa: Setup XeLaTeX<br/>Linguaggio: LaTeX]:::grafica
    end

    subgraph F5 [5. Produzione]
        MAIN_PROD[Script Orchestratore: main.py<br/>Azione: Estrazione JSON e Chiamata di Sistema]:::produzione
        PANDOC[Motore di Compilazione: Pandoc]:::produzione
        OUT_META[Metadati Generati:<br/>output_onix.json, output_schema_org.json]:::produzione
        OUT_DOC[Output Editoriali Generati:<br/>output.pdf, output.epub, index.html]:::produzione
    end

    subgraph F6 [6. Distribuzione]
        DIST[Hosting Web: GitHub Pages<br/>Versionamento: Git]:::distribuzione
    end

    %% Connessioni del Flusso Logico
    ID --> SRC & META & IMG
    SRC & META --> MAIN_REV
    
    %% main.py collega la fase 3 e la fase 5
    MAIN_REV --> |Testo normalizzato e dati| MAIN_PROD
    
    MAIN_PROD --> |Generazione diretta JSON| OUT_META
    MAIN_PROD --> |Richiama via subprocess| PANDOC
    
    CSS & TEX --> |Stili applicati| PANDOC
    PANDOC --> OUT_DOC
    
    OUT_DOC & OUT_META --> DIST

    %% Stili dei nodi per leggibilità (Colori pastello ad alto contrasto)
    classDef ideazione fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#000
    classDef acquisizione fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    classDef revisione fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000
    classDef grafica fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000
    classDef produzione fill:#ffebee,stroke:#e53935,stroke-width:2px,color:#000
    classDef distribuzione fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000