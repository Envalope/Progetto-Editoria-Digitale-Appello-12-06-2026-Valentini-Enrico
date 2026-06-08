# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono inoltre presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione e la distribuzione commerciale.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Tecnologie Utilizzate

Il progetto adotta un approccio di *Single Source Publishing* basato sulle seguenti tecnologie:
* **Linguaggi:** Markdown (linguaggio di marcatura per i contenuti), Python (automazione della pipeline logica), YAML (gestione dei metadati), JSON (output strutturato per l'interoperabilità), CSS (stile visivo).
* **Motori di Rendering:** Pandoc (conversione universale tra formati), XeLaTeX (motore di tipografia per il PDF).
* **Automazione:** Espressioni Regolari (RegEx) per la pulizia del testo e iniezione automatica del glossario.
* **Versionamento & Distribuzione:** Git (controllo versione), GitHub (hosting), GitHub Pages (pubblicazione web).

## Processo di Lavoro

L'intero flusso è gestito da un sistema automatizzato che trasforma le sorgenti grezze in pubblicazioni editoriali professionali. Il sistema gestisce cicli di normalizzazione, generazione di metadati e compilazione multi-formato, consentendo sia la revisione locale che il rilascio in produzione.

## Struttura delle Cartelle

* **`01_Sorgenti/`**: Contiene il nucleo informativo primario (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Ospita i fogli di stile (es. `epub.css` per l'e-book).
* **`03_Script/`**: La componente logica del sistema contenente `main.py`.
* **`04_Output/`**: Directory generata automaticamente destinata ai formati di distribuzione.
* **`05_webook/site/`**: Spazio dedicato alla distribuzione del Web-Book interattivo.

## Analisi e Scopo dei File Generati

### File di Metadati (Generati in `04_Output/`)
Questi file sono fondamentali per la reperibilità e la distribuzione del dossier:

* **`output_onix.json`**: Mappatura degli attributi dell'opera secondo lo standard internazionale ONIX. Utilizzato per la comunicazione commerciale B2B.
* **`output_schema_org.json`**: Serializzazione JSON-LD conforme al vocabolario di Schema.org per favorire l'indicizzazione semantica (Rich Snippets).

### File di Contenuto (Generati in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato editoriale a pagina fissa (XeLaTeX) per stampa professionale.
* **`output.epub`**: Formato e-book fluido con CSS dedicato per e-reader.
* **`index.html`**: Web-Book interattivo, completo di glossario, navigazione e indice cliccabile.

## Schema di Processo Dettagliato

```mermaid
graph LR
    A[Scelta Temi/Sorgenti] --> B[Estrazione Sorgenti]
    B --> C((Processamento Python))
    
    C --> D[Modifica File .md]
    C --> E[Definizione Grafica .yaml]
    C --> F[Server Locale Test]
    
    D & E & F --> G((Compilazione Pandoc))
    G --> H{Caricamento Finale<br/>GitHub Pages}

    style C fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    style H fill:#e1f5fe,stroke:#01579b