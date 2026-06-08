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
  * `epub.css` (Stile per l'e-book)
* **`03_Script/`**: Il motore di automazione del progetto.
  * `main.py` (Script principale)
* **`04_Output/`**: I documenti e i metadati generati in automatico.
  * `output.pdf` (Documento per la stampa)
  * `output.epub` (E-book)
  * `output_onix.json` (Metadati per librerie)
  * `output_schema_org.json` (Metadati per i motori di ricerca)
* **`05_webook/site/`**: La cartella dedicata al sito statico interattivo.
  * `index.html` (Web-Book)
  * `style.css` (Foglio di stile specifico per il sito web)

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi classiche dell'editoria digitale, automatizzando tutto il flusso di lavoro partendo da un unico set di file (*Single Source Publishing*). Il cuore del progetto è lo script `main.py`, che gestisce l'elaborazione dei testi e la generazione dei file finali.

Ecco nel dettaglio come i file interagiscono in ogni singola fase:

1. **Ideazione:** Scelta dell'argomento principale del progetto, in questo caso il tema "One Health".
2. **Acquisizione dei contenuti:** Tutto il materiale di partenza viene inserito nella cartella `01_Sorgenti/`. Troviamo il testo in `input.md`, i dati del libro in `metadati.yaml`, i riferimenti per le citazioni in `bibliografia.bib` e l'immagine in `copertina.png`.
3. **Revisione e Redazione:** In questa fase lo script `main.py` fa il lavoro di correzione automatica. Legge il file di testo grezzo (`input.md`) e lo prepara per i passaggi successivi. Nello specifico, si occupa di sistemare la formattazione (come rimuovere spazi extra) e cerca le parole chiave nel testo per trasformarle automaticamente in link cliccabili che rimandano al glossario. Alla fine di questo passaggio, otteniamo un testo "pulito" e perfetto per essere impaginato.
4. **Progettazione Grafica:** Prepariamo la grafica e gli stili. Il file `epub.css` definisce l'aspetto visivo che verrà applicato all'e-book, mentre vengono gestite le regole per la creazione di `style.css` che darà il layout al sito web finale.
5. **Produzione:** In questa fase lo script `main.py` fa due cose in parallelo:
   * Legge i dati da `metadati.yaml` e crea da solo i file `output_onix.json` e `output_schema_org.json` (che finiscono in `04_Output/`).
   * Lancia il programma `Pandoc`, passandogli il testo pulito, l'immagine di copertina, i fogli di stile e le citazioni (`bibliografia.bib`). Il sistema unisce tutto e genera i file finali: compila `output.pdf` e `output.epub` nella cartella di output, e crea la cartella `site` contenente il Web-Book `index.html` affiancato dal suo foglio di stile `style.css`.
6. **Distribuzione:** Tutti i file pronti vengono caricati su GitHub tramite Git e pubblicati online utilizzando GitHub Pages.

### Schema Visivo del Processo

Il diagramma riassume visivamente la spiegazione appena fatta. Mostra in modo chiaro l'acquisizione dei file di partenza, il lavoro svolto dallo script `main.py`, l'applicazione della grafica e la produzione finale dei vari formati.

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
        CSS[Stile visivo:<br/>epub.css e regole sito]
    end
    
    %% 5. PRODUZIONE
    MAIN -->|Crea automaticamente i dati| META[5. Produzione Metadati:<br/>output_onix.json<br/>output_schema_org.json]
    
    MAIN -->|Invia testo pulito, dati e copertina| PANDOC((5. Compilazione Automatica:<br/>Programma Pandoc))
    
    CSS --> PANDOC
    
    subgraph Output [5. File Finali Generati: 04_Output / 05_webook/site]
        PDF[Documento per la stampa:<br/>output.pdf]
        EPUB[Documento digitale:<br/>output.epub]
        WEB[Sito Web-Book:<br/>index.html e style.css]
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
    
    class ID,MD,YAML,BIB,IMG,CSS fase
    class MAIN,PANDOC script
    class META,PDF,EPUB,WEB output
    class OUT fase