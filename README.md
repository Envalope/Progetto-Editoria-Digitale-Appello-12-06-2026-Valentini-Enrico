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

Il progetto segue le 6 fasi canoniche dell'editoria, implementate attraverso un'architettura automatizzata di *Single Source Publishing*. Dal punto di vista logico, il flusso è diviso in una fase di input (acquisizione risorse grezze), una fase di elaborazione centrale (orchestrata dallo script `main.py`) e una fase di output (generazione e distribuzione).

Ecco nel dettaglio come i singoli file interagiscono in ogni fase:

1. **Ideazione:** Si definisce il perimetro del progetto, scegliendo come tematica "One Health".
2. **Acquisizione dei contenuti:** Tutto il materiale grezzo viene depositato nella cartella `01_Sorgenti/`. Il contenuto testuale risiede in `input.md`, i dati informativi dell'opera in `metadati.yaml`, i riferimenti accademici in `bibliografia.bib` e l'estetica di facciata in `copertina.png`.
3. **Revisione e Redazione:** Inizia l'automazione. Lo script `main.py` preleva il file `input.md` ed esegue una revisione invisibile: normalizza la sintassi del testo testuale, corregge le spaziature errate e inietta automaticamente i tag necessari per collegare le parole al glossario. Il risultato è un testo "pulito" e validato.
4. **Progettazione Grafica:** Vengono predisposti i file contenuti in `02_Stili/`. Il file `epub.css` contiene le direttive visive (colori, font, spazi) per il Web-Book e l'EPUB, mentre `latex-template.tex` definisce l'impaginazione rigorosa richiesta per la stampa.
5. **Produzione:** Lo script `main.py` orchestra la fase finale sdoppiandosi in due processi logici paralleli:
   * **Elaborazione Metadati:** Lo script legge i dati da `metadati.yaml` e costruisce autonomamente i file strutturati `output_onix.json` e `output_schema_org.json`, depositandoli nella cartella `04_Output/`.
   * **Compilazione Documenti:** Lo script invoca il compilatore esterno `Pandoc`. A questo programma vengono forniti il testo pulito, i file grafici (`copertina.png`, `epub.css`, `latex-template.tex`) e il database delle citazioni (`bibliografia.bib`). `Pandoc` fonde tutti questi file per generare simultaneamente la triade editoriale: `output.pdf` e `output.epub` (nella cartella `04_Output/`) e `index.html` (nella cartella `05_webook/site/`).
6. **Distribuzione:** I metadati e i file editoriali ormai pronti vengono inviati tramite Git alla repository e ospitati pubblicamente su GitHub Pages.

### Schema Visivo del Processo

Il diagramma sottostante mappa fedelmente la spiegazione logica appena descritta. Mostra l'acquisizione dei file sorgenti, l'azione di smistamento dello script centrale, l'intervento della grafica e la produzione parallela dei formati finali.

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