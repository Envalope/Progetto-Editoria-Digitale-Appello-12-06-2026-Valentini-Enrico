# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

* **Repository GitHub:** [Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico](https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico)
* **Web-Book Navigabile:** [Clicca qui per visualizzare il Web-Book su GitHub Pages](https://envalope.github.io/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico/)

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle e dei File

* **`01_Sorgenti/`**: File di partenza inseriti dall'autore.
  * `input.md` (Il testo dell'opera)
  * `metadati.yaml` (Le informazioni editoriali)
  * `copertina.png` (L'immagine di copertina)
  * `bibliografia.bib` (File per la gestione delle citazioni e della bibliografia)
* **`02_Stili/`**: Regole grafiche e di impaginazione.
  * `epub.css` (Stile per e-book e sito web)
  * `latex-template.tex` (Regole tipografiche per la stampa)
* **`03_Script/`**: Il motore di automazione del progetto.
  * `main.py` (Script orchestratore principale)
* **`04_Output/`**: I documenti e i metadati generati in automatico.
  * `output.pdf` (Documento per la stampa)
  * `output.epub` (E-book)
  * `output_onix.json` (Metadati per librerie)
  * `output_schema_org.json` (Metadati per i motori di ricerca)
* **`05_webook/site/`**: La cartella dedicata al sito statico interattivo.
  * `index.html` (Web-Book)

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi dell'editoria digitale automatizzando il flusso da una singola sorgente (*Single Source Publishing*). Lo script **`main.py`** agisce come orchestratore centrale delle operazioni:

1. **Ideazione:** Scelta del tema ("One Health").
2. **Acquisizione:** I contenuti base, i dati strutturati, l'immagine e la bibliografia vengono raccolti nella cartella `01_Sorgenti/`.
3. **Revisione e Redazione (`main.py`):** Lo script preleva `input.md` e lo pulisce automaticamente, correggendo gli spazi e inserendo i riferimenti per il glossario.
4. **Progettazione Grafica:** Vengono preparati i file `epub.css` e `latex-template.tex` per istruire il compilatore su come colorare e impaginare i testi.
5. **Produzione (`main.py` + `Pandoc`):** Lo script `main.py` svolge due compiti:
   * Estrae i dati da `metadati.yaml` e genera da solo i due file JSON.
   * Chiama in aiuto il programma `Pandoc`, passandogli il testo pulito, la copertina, il file `bibliografia.bib` per la risoluzione delle citazioni e i fogli di stile. `Pandoc` crea simultaneamente `output.pdf`, `output.epub` e `index.html`.
6. **Distribuzione:** Tutti i file finiti vengono caricati su GitHub e pubblicati automaticamente online.

### Schema Visivo del Processo

Il diagramma mostra ogni singolo file del progetto e illustra in modo logico il percorso dell'informazione, dalla sua creazione fino alla pubblicazione finale sul web.

```mermaid
graph TD
    %% 1. IDEAZIONE
    ID[1. Ideazione:<br/>Tema 'One Health']
    
    %% 2. ACQUISIZIONE (Sorgenti)
    subgraph Sorgenti [2. Acquisizione: Cartella 01_Sorgenti]
        MD[Testo base:<br/>input.md]
        YAML[Dati editoriali:<br/>metadati.yaml]
        BIB[Citazioni:<br/>bibliografia.bib]
        IMG[Immagine:<br/>copertina.png]
    end
    
    ID --> MD & YAML & BIB & IMG
    
    %% 3. REVISIONE E ORCHESTRAZIONE
    MAIN((3. Revisione e Automazione:<br/>Script main.py))
    
    MD --> MAIN
    YAML --> MAIN
    BIB --> MAIN
    IMG --> MAIN
    
    %% Fogli di stile a supporto
    subgraph Stili [4. Progettazione Grafica: Cartella 02_Stili]
        CSS[Stili digitali:<br/>epub.css]
        TEX[Stili stampa:<br/>latex-template.tex]
    end
    
    %% 5. PRODUZIONE
    MAIN -->|Estrae e scrive dati| META[5. Produzione Metadati:<br/>output_onix.json<br/>output_schema_org.json]
    
    MAIN -->|Invia testo normalizzato, dati e copertina| PANDOC((5. Compilazione Automatica:<br/>Programma Pandoc))
    
    CSS --> PANDOC
    TEX --> PANDOC
    
    subgraph Output [5. File Finali Generati: 04_Output / 05_webook]
        PDF[Documento per la stampa:<br/>output.pdf]
        EPUB[Documento digitale:<br/>output.epub]
        WEB[Sito Web-Book:<br/>index.html]
    end
    
    PANDOC --> PDF & EPUB & WEB
    
    %% 6. DISTRIBUZIONE
    META --> OUT{6. Distribuzione:<br/>GitHub Pages}
    PDF --> OUT
    EPUB --> OUT
    WEB --> OUT
    
    %% STILI GRAFICI
    classDef fase fill:#f8f9fa,stroke:#adb5bd,stroke-width:2px,color:#000
    classDef script fill:#fff3cd,stroke:#ffc107,stroke-width:3px,color:#000
    classDef output fill:#e2e3e5,stroke:#6c757d,stroke-width:2px,color:#000
    
    class ID,MD,YAML,BIB,IMG,CSS,TEX fase
    class MAIN,PANDOC script
    class META,PDF,EPUB,WEB output
    class OUT fase