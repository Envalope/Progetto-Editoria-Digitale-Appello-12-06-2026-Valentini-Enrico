# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File sorgenti (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Fogli di stile (`epub.css`, `latex-template.tex`).
* **`03_Script/`**: Logica di sistema (`main.py`).
* **`04_Output/`**: File generati (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: File per la pubblicazione Web.

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: Mappatura standard ONIX per la comunicazione commerciale editoriale (librerie, distributori).
* **`output_schema_org.json`**: JSON-LD per l'indicizzazione semantica (Rich Snippets Google).

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato editoriale a pagina fissa per stampa professionale.
* **`output.epub`**: Formato e-book fluido con CSS dedicato per e-reader.
* **`index.html`**: Web-Book interattivo, completo di glossario, navigazione e indice cliccabile.

## Il Flusso del Processo Editoriale

Il progetto segue rigorosamente le **6 fasi del processo di produzione editoriale**, implementate in un'ottica di automazione digitale (*Single Source Publishing*):

1. **Ideazione:** Scelta del tema ("One Health"), definizione dell'architettura dell'informazione e delle necessità del progetto.
2. **Acquisizione dei contenuti:** Raccolta dei materiali di partenza. Per garantire la massima separazione tra contenuto e presentazione, si utilizzano file puri: `Markdown` per il testo e `YAML` per i parametri di base e i metadati.
3. **Revisione e redazione:** Il nucleo logico del sistema interviene sul testo. Uno script `Python` utilizza le Espressioni Regolari (RegEx) per normalizzare la sintassi, correggere le anomalie e iniettare automaticamente gli apici per il collegamento al glossario.
4. **Progettazione grafica:** Definizione delle regole di impaginazione e stile per i diversi output tramite tecnologie standard: `CSS3` per il web e l'e-book, e `LaTeX` per l'output destinato alla stampa.
5. **Produzione:** È la fase di compilazione vera e propria. Il programma `Pandoc` prende in carico il testo revisionato e i file di stile, delegando a `XeLaTeX` la generazione del PDF e producendo in parallelo il Web-Book HTML e l'EPUB. Contemporaneamente, vengono generati i file `JSON` (ONIX e Schema.org).
6. **Distribuzione:** I prodotti editoriali finali (testo, grafica, metadati) vengono inviati al server tramite `Git` e resi disponibili al pubblico globale tramite la piattaforma di hosting `GitHub Pages`.

### Schema di Processo Dettagliato

```mermaid
graph TD
    %% Fasi del Processo Editoriale
    subgraph F1 [1. Ideazione]
        ID[Definizione Tema e Architettura]:::ideazione
    end

    subgraph F2 [2. Acquisizione dei contenuti]
        SRC[Testo Sorgente<br/>Linguaggio: Markdown]:::acquisizione
        META[Parametri e Configurazione<br/>Linguaggio: YAML]:::acquisizione
    end

    subgraph F3 [3. Revisione e redazione]
        REV[Normalizzazione RegEx e Glossario<br/>Tecnologia: Python 3]:::revisione
    end

    subgraph F4 [4. Progettazione grafica]
        GRAF[Definizione Stili e Layout<br/>Linguaggi: CSS3, LaTeX]:::grafica
    end

    subgraph F5 [5. Produzione]
        PROD_DOC[Compilazione Output: PDF, HTML, EPUB<br/>Tecnologie: Pandoc, XeLaTeX]:::produzione
        PROD_META[Generazione Metadati Strutturati<br/>Linguaggio: JSON / ONIX, Schema.org]:::produzione
    end

    subgraph F6 [6. Distribuzione]
        DIST[Versioning e Hosting Pubblico<br/>Tecnologie: Git, GitHub Pages]:::distribuzione
    end

    %% Connessioni del Flusso Logico
    ID --> SRC & META
    SRC & META --> REV
    REV --> GRAF
    GRAF --> PROD_DOC & PROD_META
    PROD_DOC & PROD_META --> DIST

    %% Stili dei nodi per leggibilità (Colori pastello ad alto contrasto)
    classDef ideazione fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#000
    classDef acquisizione fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    classDef revisione fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000
    classDef grafica fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000
    classDef produzione fill:#ffebee,stroke:#e53935,stroke-width:2px,color:#000
    classDef distribuzione fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000