# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Tecnologie Utilizzate

Il progetto adotta un approccio di *Single Source Publishing*:
* **Contenuti:** Markdown.
* **Metadati:** YAML (Configurazione) e JSON (Output strutturato).
* **Automazione & Logica:** Python (Scripting, RegEx per la pulizia del testo).
* **Motori di Rendering:** Pandoc (Conversione universale), XeLaTeX (Tipografia avanzata per PDF), CSS (Stile Web ed E-book).
* **Versioning & Web:** Git, GitHub, GitHub Pages.

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File sorgenti (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Fogli di stile (`epub.css`, `latex-template.tex`).
* **`03_Script/`**: Logica di sistema (`main.py`).
* **`04_Output/`**: File generati (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: File per la pubblicazione Web.

## Analisi e Spiegazione del Flusso di Processo

Il processo di generazione è un flusso automatizzato che trasforma contenuti grezzi in prodotti editoriali complessi. Il flusso si divide in quattro macro-fasi:

1. **Ingestione (Input):** Il sistema acquisisce i dati grezzi. Le tecnologie chiave sono i file di testo Markdown e YAML, che garantiscono portabilità e leggibilità.
2. **Elaborazione Logica (Python/RegEx):** Lo script `main.py` normalizza il testo utilizzando le Espressioni Regolari (RegEx) per la pulizia dei caratteri e inietta i glossari automaticamente. In questa fase, vengono anche generati i metadati strutturati JSON (ONIX e Schema.org) per la distribuzione B2B e la SEO.
3. **Conversione e Rendering (Pandoc/XeLaTeX):** Il motore Pandoc funge da "ponte" universale. A seconda del formato target, il sistema richiama XeLaTeX (per la composizione tipografica del PDF ad alta qualità) o applica fogli di stile CSS customizzati (per EPUB e Web-Book).
4. **Distribuzione (GitHub Pages):** Il prodotto finito viene hostato e distribuito via web.

### Schema di Processo Dettagliato

```mermaid
graph TD
    %% Definizione Classi per Stile e Contrasto
    classDef input fill:#f9f9f9,stroke:#000,stroke-width:2px,color:#000
    classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    classDef tech fill:#fff3e0,stroke:#e65100,stroke-width:1px,color:#000
    classDef output fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000

    %% Diagramma del Flusso
    Start[Input Sorgenti<br/>Markdown & YAML]:::input
    
    Prep[Pulizia RegEx & Iniezione Glossario<br/>Tecnologia: Python]:::process
    
    Meta[Generazione Metadati<br/>Tecnologia: JSON/ONIX/Schema.org]:::tech
    
    Compiler[Compilazione Formati<br/>Tecnologia: Pandoc]:::process
    
    RenderPDF[Motore XeLaTeX<br/>Output: PDF]:::tech
    RenderWEB[Stili CSS<br/>Output: Web-Book/EPUB]:::tech
    
    Finish[Pubblicazione<br/>Tecnologia: GitHub Pages]:::output

    Start --> Prep
    Prep --> Meta
    Prep --> Compiler
    Compiler --> RenderPDF
    Compiler --> RenderWEB
    RenderPDF & RenderWEB --> Finish