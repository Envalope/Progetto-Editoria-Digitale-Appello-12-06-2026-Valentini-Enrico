# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Tecnologie Utilizzate

Il progetto segue un workflow di *Single Source Publishing*:
* **Linguaggi:** Markdown (Contenuti), YAML (Metadati), JSON (Interoperabilità).
* **Automazione & Logica:** Python (Scripting, RegEx per pulizia testo, Serializzazione metadati).
* **Motori di Rendering:** Pandoc (Conversione formati), XeLaTeX (Tipografia avanzata per PDF), CSS (Stile Web/E-book).
* **Versioning & Web:** Git, GitHub, GitHub Pages.

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File sorgenti (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Fogli di stile (`epub.css`, `latex-template.tex`).
* **`03_Script/`**: Logica di sistema (`main.py`).
* **`04_Output/`**: File generati (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: File per la pubblicazione Web.

## Analisi e Scopo dei File Generati

### Metadati (Generati in `04_Output/`)
* **`output_onix.json`**: Mappatura secondo standard internazionale ONIX per librerie e distributori.
* **`output_schema_org.json`**: Dati strutturati JSON-LD per l'indicizzazione semantica (Rich Snippets).

### Contenuti (Generati in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato a pagina fissa (via XeLaTeX) per stampa professionale.
* **`output.epub`**: Formato fluido con CSS dedicato per e-reader.
* **`index.html`**: Web-Book interattivo, completo di glossario, navigazione e indice.

## Flusso di Processo Dettagliato

```mermaid
graph TD
    %% Definizione Stili ad alto contrasto
    classDef process fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    classDef tech fill:#f4f4f4,stroke:#666,stroke-width:1px,color:#333
    classDef output fill:#e0e0e0,stroke:#000,stroke-width:2px,color:#000

    %% Passaggi
    Start[Input Sorgenti] --> Prep[Preparazione Metadati & Testo]
    Prep --> Python((Python Logic))
    
    Python --> RegEx[Normalizzazione & RegEx]
    Python --> MetaGen[Generazione JSON: ONIX & Schema.org]
    
    RegEx --> Pandoc((Pandoc Engine))
    
    Pandoc --> XeLaTeX[Motore XeLaTeX]
    Pandoc --> CSS[Stili CSS]
    
    XeLaTeX --> PDF[Generazione PDF]
    CSS --> HTML[Generazione Web-Book]
    CSS --> EPUB[Generazione EPUB]
    
    PDF & HTML & EPUB --> Deploy[Pubblicazione GitHub Pages]

    %% Assegnazione Stili
    class Start,Prep,Deploy output
    class Python,Pandoc process
    class RegEx,MetaGen,XeLaTeX,CSS tech
    class PDF,HTML,EPUB output