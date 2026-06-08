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

## Analisi e Spiegazione del Flusso di Processo

Il processo di generazione è un flusso automatizzato (*Single Source Publishing*) che trasforma i contenuti grezzi in prodotti editoriali complessi. Il ciclo di vita del progetto si articola nelle seguenti fasi tecnologiche:

1. **Acquisizione Dati (Input):** Il flusso inizia prelevando i dati grezzi. Si utilizzano file leggeri e facilmente leggibili: il linguaggio di marcatura `Markdown` per il testo e il formato `YAML` per i parametri di configurazione.
2. **Elaborazione e Normalizzazione:** Il cuore logico è gestito da `Python 3` tramite lo script `main.py`. Lo script utilizza la libreria nativa `re` per applicare le Espressioni Regolari (RegEx), ripulendo il testo e automatizzando l'inserimento degli apici per il glossario.
3. **Generazione Metadati:** Parallelamente alla pulizia del testo, `Python` struttura le informazioni editoriali esportandole nel formato universale `JSON`, mappandole secondo gli standard richiesti dal mercato (`ONIX` per i cataloghi B2B, `Schema.org` per i motori di ricerca).
4. **Compilazione Core:** Il testo normalizzato viene passato a `Pandoc`, un programma da riga di comando che funge da convertitore universale (Universal Document Converter). Pandoc orchestra la creazione dei vari formati di output.
5. **Rendering Multi-Formato:**
   * Per l'output destinato alla stampa (`PDF`), Pandoc richiama il programma `XeLaTeX`, un motore tipografico avanzato capace di gestire impaginazioni complesse.
   * Per gli output destinati agli schermi (`EPUB` e `HTML`), vengono applicate le tecnologie web standard `HTML5` e `CSS3` per garantire fluidità e adattabilità del layout.
6. **Distribuzione:** I prodotti finiti vengono tracciati dal sistema di versionamento `Git` e infine pubblicati e hostati gratuitamente tramite i server di `GitHub Pages`.

### Schema di Processo Dettagliato

```mermaid
graph TD
    %% Definizione Classi di Stile
    classDef fase fill:#ffffff,stroke:#000,stroke-width:2px,color:#000
    classDef tech fill:#f4f4f4,stroke:#333,stroke-width:1px,color:#333,stroke-dasharray: 5 5

    %% Nodi del Diagramma
    F1["Fase 1: Input Dati<br/>(Contenuti e Configurazioni)"]:::fase
    T1["Linguaggi: Markdown (.md), YAML (.yaml)"]:::tech
    
    F2["Fase 2: Elaborazione e Pulizia Testuale<br/>(Esecuzione script main.py)"]:::fase
    T2["Linguaggio: Python 3<br/>Tecnologia: RegEx (modulo 're')"]:::tech
    
    F3["Fase 3: Generazione Metadati Strutturati<br/>(output_onix, output_schema_org)"]:::fase
    T3["Formato: JSON<br/>Standard: ONIX, Schema.org"]:::tech
    
    F4["Fase 4: Compilazione e Smistamento<br/>(Conversione formati)"]:::fase
    T4["Programma: Pandoc<br/>(Universal Document Converter)"]:::tech
    
    F5A["Fase 5A: Rendering Stampa<br/>(Creazione output.pdf)"]:::fase
    T5A["Programma: XeLaTeX<br/>(Motore di composizione tipografica)"]:::tech
    
    F5B["Fase 5B: Rendering Digitale<br/>(Creazione index.html, output.epub)"]:::fase
    T5B["Linguaggi: HTML5, CSS3<br/>(Fogli di stile personalizzati)"]:::tech
    
    F6["Fase 6: Hosting e Distribuzione<br/>(Messa online)"]:::fase
    T6["Tecnologie: Git, GitHub Pages"]:::tech

    %% Collegamenti tra Nodi
    F1 --- T1
    T1 --> F2
    
    F2 --- T2
    T2 --> F3
    T2 --> F4
    
    F3 --- T3
    
    F4 --- T4
    T4 --> F5A
    T4 --> F5B
    
    F5A --- T5A
    F5B --- T5B
    
    T5A --> F6
    T5B --> F6