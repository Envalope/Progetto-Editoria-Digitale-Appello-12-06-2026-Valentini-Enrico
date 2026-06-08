# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File di partenza inseriti dall'autore (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Regole grafiche e di impaginazione (`epub.css`).
* **`03_Script/`**: Il "motore" del progetto (`main.py`).
* **`04_Output/`**: I documenti e i dati generati automaticamente (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: I file pronti per il sito web (`index.html`).

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: File che descrive il libro (titolo, autore, prezzo) secondo lo standard per le librerie e i distributori.
* **`output_schema_org.json`**: File che aiuta motori di ricerca come Google a capire di cosa parla il libro.

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato per la stampa tradizionale.
* **`output.epub`**: Formato per la lettura su e-reader (es. Kindle, Kobo).
* **`index.html`**: Il libro in formato sito web interattivo.

## Il Flusso del Processo Editoriale

Il progetto segue le **6 fasi tipiche dell'editoria**, ma le automatizza in modo digitale. Il vero protagonista di questo processo è lo script **`main.py`** (scritto in linguaggio Python), che fa da "direttore dei lavori": legge i documenti grezzi, li corregge, crea i dati aggiuntivi e comanda gli altri programmi per creare i file finali.

Ecco come si svolge il processo passo dopo passo:

1. **Ideazione:** Si decide il tema ("One Health") e si progetta la struttura del libro.
2. **Acquisizione dei contenuti:** L'autore scrive il testo nel file `input.md` e inserisce le informazioni del libro nel file `metadati.yaml`.
3. **Revisione e redazione:** Entra in gioco `main.py`. Lo script legge il testo di `input.md` e fa una pulizia automatica: corregge gli spazi, sistema la formattazione e collega automaticamente le parole chiave al glossario, preparando un testo perfetto.
4. **Progettazione grafica:** Si definisce l'aspetto visivo modificando il file `epub.css` (per i colori e i font su schermo) e impostando le regole per la pagina stampata.
5. **Produzione:** Lo script `main.py` fa il lavoro finale. Prima legge il file YAML per generare i metadati JSON (`output_onix.json` e `output_schema_org.json`). Subito dopo, "chiama" il programma di conversione **Pandoc**, passandogli il testo pulito e la grafica, per fargli generare in automatico i tre formati di lettura: `output.pdf`, `output.epub` e `index.html`.
6. **Distribuzione:** I file finiti vengono caricati sulla piattaforma GitHub Pages, che li rende visibili a tutti su internet.

### Schema Visivo del Processo

Lo schema qui sotto riassume le 6 fasi in ordine sequenziale, indicando per ogni blocco l'azione svolta, gli strumenti tecnologici utilizzati e i file esatti su cui si sta lavorando.

```mermaid
graph TD
    %% Definizione delle Fasi in sequenza logica
    F1[<b>1. Ideazione</b><br/>Definizione del tema e della struttura<br/>Progetto: One Health]
    
    F2[<b>2. Acquisizione dei contenuti</b><br/>Raccolta dei materiali di partenza<br/>File: input.md, metadati.yaml, copertina.png]
    
    F3[<b>3. Revisione e redazione</b><br/>Script: main.py<br/>Azione: Pulizia automatica del testo e inserimento glossario]
    
    F4[<b>4. Progettazione grafica</b><br/>Definizione dell'aspetto visivo<br/>File: epub.css e stili di stampa]
    
    F5[<b>5. Produzione</b><br/>Script: main.py + Programma: Pandoc<br/>File testuali generati: output.pdf, output.epub, index.html<br/>Metadati generati: output_onix.json, output_schema_org.json]
    
    F6[<b>6. Distribuzione</b><br/>Pubblicazione online<br/>Piattaforma: GitHub Pages]

    %% Flusso sequenziale
    F1 --> F2
    F2 --> F3
    F3 --> F4
    F4 --> F5
    F5 --> F6

    %% Stili dei nodi per massima chiarezza e leggibilità
    style F1 fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000
    style F2 fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    style F3 fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000
    style F4 fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000
    style F5 fill:#ffebee,stroke:#e53935,stroke-width:2px,color:#000
    style F6 fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000