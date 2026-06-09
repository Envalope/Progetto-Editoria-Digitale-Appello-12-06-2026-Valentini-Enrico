# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

* **Repository GitHub:** [Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico](https://github.com/Envalope/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico)
* **Web-Book Navigabile:** [Clicca qui per visualizzare il Web-Book su GitHub Pages](https://envalope.github.io/Progetto-Editoria-Digitale-Appello-12-06-2026-Valentini-Enrico/)

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle e dei File

* **`01_Sorgenti/`**: I file di partenza che ho scritto per il progetto.
  * `input.md` (Il testo dell'opera, tenuto pulito e senza codice di stile dentro)
  * `metadati.yaml` (Le informazioni editoriali e le configurazioni di Pandoc)
  * `copertina.png` (L'immagine di copertina)
  * `bibliografia.bib` (Il database con le fonti e le citazioni)
* **`02_Stili/`**: I fogli di stile separati dal testo.
  * `epub.css` (Lo stile adattivo per l'e-book)
  * `style.css` (Lo stile strutturato per il sito web)
* **`03_Script/`**: Il motore di automazione.
  * `main.py` (Lo script Python principale che fa girare tutto)
* **`04_Output/`**: I file finali e i metadati generati automaticamente.
  * `output.pdf` (Il file pronto per la stampa)
  * `output.epub` (L'e-book per gli e-reader)
  * `output_onix.json` (I metadati per i distributori e le librerie)
  * `output_schema_org.json` (I metadati per l'indicizzazione sui motori di ricerca)
* **`05_webook/site/`**: La cartella con il sito web statico.
  * `index.html` (La pagina principale del Web-Book)
  * `css/style.css` (Il foglio di stile del sito, copiato qui in automatico dallo script)

## Il Flusso del Processo Editoriale

Il progetto segue le 6 fasi classiche dell'editoria digitale. Ho usato l'approccio *Single Source Publishing*: partendo da un unico file di testo, lo script automatizza la creazione di tutti i formati finali. 

Ecco come funzionano i file e come si muovono all'interno del flusso:

1. **Ideazione:** Ho scelto l'argomento del dossier, concentrandomi sul tema di attualità "One Health".
2. **Acquisizione dei contenuti:** Ho preparato i materiali di partenza nella cartella `01_Sorgenti/`. Ho scritto il testo in `input.md`, raccolto le informazioni del libro in `metadati.yaml`, inserito i riferimenti degli articoli in `bibliografia.bib` e aggiunto l'immagine `copertina.png`.
3. **Revisione e Redazione:** Quando lancio `main.py`, lo script legge il file grezzo `input.md` e fa una pulizia automatica. Sistema la formattazione (rimuove gli spazi extra) e analizza il testo per cercare le parole chiave del glossario, inserendo in automatico i link cliccabili. In questo modo il testo diventa pulito, corretto e pronto per essere impaginato.
4. **Progettazione Grafica:** Per gestire al meglio la resa visiva, ho deciso di separare nettamente gli stili nella cartella `02_Stili/` a seconda del formato di destinazione:
   * `epub.css` serve per l'e-book. È fluido e non impone sfondi o colori fissi, così se l'utente usa la "Modalità Notte" o "Seppia" sul suo e-reader, lo sfondo e i testi cambiano colore correttamente senza creare riquadri bianchi illeggibili.
   * `style.css` serve invece per il browser web. Ha un layout più strutturato, con una palette di colori precisa (Navy Blue e toni chiari) adatta a una lettura da PC o smartphone.
5. **Produzione:** Lo script `main.py` elabora tutto in parallelo:
   * Legge `metadati.yaml` e genera da solo i file JSON dei metadati (`output_onix.json` e `output_schema_org.json`).
   * Crea la cartella `site/css/` e, usando la libreria `shutil`, ci copia dentro il file `style.css` rinominandolo correttamente. Questa automazione è fondamentale per evitare link rotti all'interno del sito web.
   * Lancia `Pandoc` passando il testo pulito, la copertina e la bibliografia per compilare insieme tutti i formati: `output.pdf`, `output.epub` (usando `epub.css`) e `index.html` (che si aggancia automaticamente al foglio di stile appena copiato).
6. **Distribuzione:** Ho caricato l'intera struttura su GitHub e, grazie a GitHub Pages, il Web-Book è navigabile online da chiunque.

### Schema Visivo del Processo

Questo diagramma mostra in modo semplice e chiaro come i file di partenza passano attraverso lo script `main.py` e il compilatore `Pandoc` fino ad arrivare alla pubblicazione sul web.

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