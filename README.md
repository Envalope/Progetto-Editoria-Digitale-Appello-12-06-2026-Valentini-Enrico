# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono inoltre presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione e la distribuzione commerciale.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura e Flusso di Lavoro

L'intero progetto è gestito da un'architettura automatizzata (Single Source Publishing). 
Utilizzando lo script Python `main.py` (nella cartella `03_Script`), il sistema preleva il testo sorgente `input.md` e la configurazione da `metadati.yaml` (situati in `01_Sorgenti`). 

Il processo si articola in tre flussi principali:
1. **Normalizzazione:** Lo script esegue una pulizia delle espressioni regolari (RegEx) e inietta dinamicamente gli apici del glossario nel file Markdown.
2. **Generazione Metadati:** Vengono creati i file JSON strutturati (`output_onix.json` e `output_schema_org.json`) che fungono da carta d'identità digitale dell'opera.
3. **Compilazione:** Pandoc (con XeLaTeX o CSS personalizzati) compila i file di output (PDF, EPUB e Web-Book).


### Struttura delle Cartelle
01_Sorgenti/: Contiene il nucleo informativo primario (input.md, metadati.yaml, copertina.png).

02_Stili/: Ospita i fogli di stile (es. epub.css per l'e-book).

03_Script/: La componente logica del sistema contenente main.py.

04_Output/: Directory generata automaticamente destinata ai formati di distribuzione.

05_webook/site/: Spazio dedicato alla distribuzione del Web-Book interattivo.

Analisi e Scopo dei File Generati
File di Metadati (Generati in 04_Output/)
Questi file sono fondamentali per la reperibilità e la distribuzione del dossier:

output_onix.json:

Scopo: Mappatura degli attributi dell'opera secondo lo standard internazionale ONIX (ONline Information eXchange). Viene utilizzato per la comunicazione commerciale B2B (librerie, distributori, cataloghi editoriali).

Generazione: Creato dallo script main.py tramite la funzione convert_to_onix, che estrae le informazioni dal file metadati.yaml e le struttura nel formato richiesto.

output_schema_org.json:

Scopo: Serializzazione JSON-LD conforme al vocabolario semantico di Schema.org. Serve a "spiegare" ai motori di ricerca che il contenuto è un libro, permettendo di ottenere risultati più visibili (Rich Snippets).

Generazione: Creato dallo script main.py tramite la funzione convert_to_schema_org, che mappa i dati di metadati.yaml nelle proprietà semantiche di Book per il Web.

File di Contenuto (Generati in 04_Output/ e 05_webook/site/)
output.pdf: Formato editoriale a pagina fissa (XeLaTeX) per stampa o consultazione statica.

output.epub: Formato e-book fluido (con copertina e CSS dedicato).

index.html: Web-Book interattivo hostabile, completo di glossario e indice cliccabile.

### Schema di Generazione
```mermaid
graph TD
    Input[input.md + metadati.yaml]
    Script(main.py)
    Meta[Metadati: ONIX & Schema.org]
    Pandoc[Pandoc]
    OutPDF[Cartella 04_Output: PDF, EPUB]
    OutWeb[Cartella 05_webook/site: HTML]

    Input --> Script
    Script --> Meta
    Script --> Pandoc
    Pandoc --> OutPDF
    Pandoc --> OutWeb

    style Script fill:#f9f,stroke:#333,stroke-width:2px
    style Pandoc fill:#bbf,stroke:#333,stroke-width:2px