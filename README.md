# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

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

Il progetto automatizza le **6 fasi canoniche della produzione editoriale**, adottando un approccio moderno in cui da una singola sorgente si ottengono formati multipli (*Single Source Publishing*). Il motore di questa automazione è lo script `main.py`.

1. **Ideazione:** Definizione della tematica "One Health" e dell'architettura dell'informazione.
2. **Acquisizione dei contenuti:** I testi vengono inseriti nel file `input.md` (usando il linguaggio Markdown), mentre le impostazioni e i dati dell'opera vanno in `metadati.yaml` (linguaggio YAML). Entrambi si trovano in `01_Sorgenti/`.
3. **Revisione e redazione:** Lo script `main.py` (scritto in Python) legge il testo originale e lo "pulisce" in automatico. Corregge eventuali errori di formattazione e inserisce da solo i collegamenti al glossario, preparando un testo perfetto per le fasi successive.
4. **Progettazione grafica:** Vengono creati i file che dettano l'aspetto estetico: `epub.css` per i formati digitali (Web ed EPUB) e le regole tipografiche per la stampa.
5. **Produzione:** Lo script `main.py` entra di nuovo in azione per la fase finale. Estrae i dati per creare i metadati (`output_onix.json` e `output_schema_org.json`) e passa il testo pulito a `Pandoc`, un programma di conversione che genera automaticamente la versione stampabile (`output.pdf`), l'e-book (`output.epub`) e il sito web (`index.html`).
6. **Distribuzione:** Tutti i file finiti vengono caricati e resi disponibili al pubblico tramite il sistema di hosting gratuito `GitHub Pages`.

### Schema Logico del Processo

```mermaid
graph TD
    %% Fasi del Processo Editoriale
    subgraph F1 [1. Ideazione]
        ID[Definizione Tema: One Health]:::ideazione
    end

    subgraph F2 [2. Acquisizione dei contenuti]
        SRC[Testo Grezzo: input.md]:::acquisizione
        META[Dati Opera: metadati.yaml]:::acquisizione
    end

    subgraph F3 [3. Revisione e redazione]
        MAIN_REV[Script Python: main.py<br/>Azione: Pulizia automatica del testo]:::revisione
    end

    subgraph F4 [4. Progettazione grafica]
        STILI[Regole Visive: epub.css e stili stampa]:::grafica
    end

    subgraph F5 [5. Produzione]
        PANDOC[Programma: Pandoc<br/>Azione: Compilazione automatica]:::produzione
        OUT_META[Metadati: output_onix.json, output_schema_org.json]:::produzione
        OUT_DOC[Documenti: output.pdf, output.epub, index.html]:::produzione
    end

    subgraph F6 [6. Distribuzione]
        DIST[Piattaforma: GitHub Pages]:::distribuzione
    end

    %% Connessioni Logiche
    ID --> SRC & META
    SRC --> MAIN_REV
    META --> OUT_META
    MAIN_REV --> PANDOC
    STILI --> PANDOC
    PANDOC --> OUT_DOC
    OUT_DOC & OUT_META --> DIST

    %% Stili dei nodi per leggibilità
    classDef ideazione fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#000
    classDef acquisizione fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    classDef revisione fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000
    classDef grafica fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000
    classDef produzione fill:#ffebee,stroke:#e53935,stroke-width:2px,color:#000
    classDef distribuzione fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000