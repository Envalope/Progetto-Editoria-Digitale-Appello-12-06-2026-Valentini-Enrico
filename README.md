# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

* **Repository GitHub:** [Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico](https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico)
* **Web-Book Navigabile:** [Clicca qui per visualizzare il Web-Book su GitHub Pages](https://envalope.github.io/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico/)

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle e dei File

* **`01_Sorgenti/`**: File di partenza inseriti dall'autore.
  * `input.md` (Il testo dell'opera pulito dai tag di stile)
  * `metadati.yaml` (Le informazioni editoriali)
  * `copertina.png` (L'immagine di copertina)
  * `bibliografia.bib` (File per la gestione delle citazioni e della bibliografia)
* **`02_Stili/`**: Regole grafiche e di impaginazione.
  * `epub.css` (Stile fluido e adattivo per l'e-book)
  * `style.css` (Stile strutturato ed elegante per il sito web)
* **`03_Script/`**: Il motore di automazione del progetto.
  * `main.py` (Script principale orchestratore)
* **`04_Output/`**: I documenti e i metadati generati in automatico.
  * `output.pdf` (Documento per la stampa)
  * `output.epub` (E-book)
  * `output_onix.json` (Metadati per librerie)
  * `output_schema_org.json` (Metadati per i motori di ricerca)
* **`05_webook/site/`**: La cartella dedicata al sito statico interattivo.
  * `index.html` (Web-Book compilato)
  * `css/style.css` (Foglio di stile del sito, copiato in automatico dallo script)

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi classiche dell'editoria digitale, automatizzando tutto il flusso di lavoro partendo da un unico set di file (*Single Source Publishing*). Il cuore del progetto è lo script `main.py`, che gestisce l'elaborazione dei testi, la gestione logica degli stili e la generazione dei file finali.

Ecco nel dettaglio come i file interagiscono in ogni singola fase:

1. **Ideazione:** Scelta dell'argomento principale del progetto, in questo caso il tema "One Health".
2. **Acquisizione dei contenuti:** Tutto il materiale di partenza viene inserito nella cartella `01_Sorgenti/`. Troviamo il testo puro in `input.md`, i dati del libro in `metadati.yaml`, i riferimenti per le citazioni in `bibliografia.bib` e l'immagine in `copertina.png`.
3. **Revisione e Redazione:** Lo script `main.py` fa il lavoro di correzione automatica. Legge il file di testo grezzo (`input.md`), ne uniforma la formattazione e trasforma le parole chiave in link cliccabili diretti al glossario. Il risultato è un testo "pulito" ed esclusivamente semantico, pronto per ricevere la grafica in un secondo momento.
4. **Progettazione Grafica:** Per garantire la massima qualità su ogni dispositivo, abbiamo separato nettamente i fogli di stile nella cartella `02_Stili/`. 
   * Il file `epub.css` è progettato appositamente per gli e-reader: non forza sfondi o colori rigidi, permettendo al dispositivo di adattarsi perfettamente alla "Modalità Notte" o "Seppia".
   * Il file `style.css` è invece progettato per i browser web: impone un layout più strutturato a colori (Navy Blue e sfondi chiari), simile a quello di un dossier o di una rivista scientifica digitale.
5. **Produzione:** In questa fase lo script `main.py` orchestra la generazione di tutti i file finali operando su più fronti:
   * **Dati:** Legge `metadati.yaml` e crea in autonomia i file `output_onix.json` e `output_schema_org.json` nella cartella `04_Output/`.
   * **Gestione Stili Web:** Crea la cartella `site/css/` e vi copia dentro una copia esatta del file `style.css` preso da `02_Stili/`. Questa operazione automatizzata (tramite la libreria `shutil`) è essenziale per evitare link interrotti nel sito e per mantenere pulita la logica di separazione tra sorgenti e output.
   * **Compilazione Documenti:** Lancia il compilatore `Pandoc`, passandogli il testo pulito, le copertine, la bibliografia e associando a ogni output il suo stile corretto. `Pandoc` genera così `output.pdf`, `output.epub` (agganciato a `epub.css`) e l'interattivo `index.html` (agganciato al nuovo `site/css/style.css`).
6. **Distribuzione:** Tutti i file pronti vengono caricati su GitHub tramite Git e pubblicati online utilizzando GitHub Pages.

### Schema Visivo del Processo

Il diagramma mostra l'acquisizione dei file di partenza, il lavoro logico svolto dallo script `main.py` (compresa la copia strategica dei fogli di stile) e la produzione finale dei vari formati.

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
        CSS_E[Stile fluido E-book:<br/>epub.css]
        CSS_W[Stile strutturato Web:<br/>style.css]
    end
    
    %% 5. PRODUZIONE
    MAIN -->|Crea automaticamente i dati| META[5. Produzione Metadati:<br/>output_onix.json<br/>output_schema_org.json]
    
    MAIN -->|Copia file style.css da 02_Stili a site/css| WEB_CSS[Foglio di stile sito:<br/>site/css/style.css]
    
    MAIN -->|Invia testo pulito, dati e copertina| PANDOC((5. Compilazione Automatica:<br/>Programma Pandoc))
    
    CSS_E --> PANDOC
    CSS_W --> MAIN
    WEB_CSS -.->|Agganciato a| WEB
    
    subgraph Output [5. File Finali Generati: 04_Output / 05_webook/site]
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
    
    class ID,MD,YAML,BIB,IMG,CSS_E,CSS_W fase
    class MAIN,PANDOC script
    class META,PDF,EPUB,WEB,WEB_CSS output
    class OUT fase