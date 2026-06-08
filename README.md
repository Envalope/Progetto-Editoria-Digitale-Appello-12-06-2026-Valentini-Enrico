# One Health & Futuro Digitale 🌍

Progetto realizzato nell'ambito del corso di Editoria Digitale del prof. Ceravolo Paolo.

Il Web-Book è raggiungibile e navigabile al seguente link: **[Inserisci qui il link di GitHub Pages]**

Nella repository sono presenti gli output editoriali generati automaticamente (PDF, EPUB) ottimizzati per la stampa e gli e-reader, e i file di metadati strutturati (ONIX e Schema.org) pronti per l'indicizzazione.

![Copertina One Health](./01_Sorgenti/copertina.png)

## Struttura delle Cartelle

* **`01_Sorgenti/`**: File sorgenti (`input.md`, `metadati.yaml`, `copertina.png`).
* **`02_Stili/`**: Fogli di stile (`epub.css` e asset grafici).
* **`03_Script/`**: Logica di sistema (`main.py`).
* **`04_Output/`**: File generati (PDF, EPUB, ONIX, Schema.org).
* **`05_webook/site/`**: File per la pubblicazione Web (`index.html` e asset).

## Analisi e Scopo dei File Generati

### File di Metadati (in `04_Output/`)
* **`output_onix.json`**: Mappatura standard ONIX per la comunicazione commerciale editoriale (librerie, distributori).
* **`output_schema_org.json`**: JSON-LD per l'indicizzazione semantica (Rich Snippets Google).

### File di Contenuto (in `04_Output/` e `05_webook/site/`)
* **`output.pdf`**: Formato editoriale a pagina fissa per stampa professionale.
* **`output.epub`**: Formato e-book fluido con CSS dedicato per e-reader.
* **`index.html`**: Web-Book interattivo, completo di glossario, navigazione e indice cliccabile.

## Il Flusso del Processo Editoriale

Il progetto automatizza le **6 fasi canoniche della produzione editoriale** adottando un approccio di *Single Source Publishing*. 

In questa architettura, lo script **`main.py`** (scritto in Python 3) svolge il ruolo di **Orchestratore Centrale**. Non si limita a una singola operazione, ma funge da vero e proprio motore software che unisce, elabora e smista i dati lungo tutto il ciclo di vita del progetto:

1. **Ideazione:** Definizione della tematica globale "One Health" e progettazione logica del volume.
2. **Acquisizione dei contenuti:** Raccolta dei materiali di partenza all'interno della cartella `01_Sorgenti/`. Il testo e la struttura sono scritti in `input.md`, mentre le informazioni strutturate dell'opera sono racchiuse in `metadati.yaml`.
3. **Revisione e redazione (Gestita da `main.py`):** Lo script apre il file `input.md` ed effettua una trasformazione automatica del testo. Applica filtri di pulizia tipografica e inietta dinamicamente i marcatori per i collegamenti ipertestuali del glossario, generando una sorgente pulita e validata.
4. **Progettazione grafica:** Vengono predisposti i fogli di stile esterni (come `epub.css`) e i modelli di impaginazione per la stampa, pronti per essere agganciati ai convertitori.
5. **Produzione (Orchestrata da `main.py`):** Lo script esegue ed automatizza le operazioni di compilazione finale agendo su due fronti:
    * **Generazione Metadati:** Legge il file `metadati.yaml` e scrive direttamente i file JSON di distribuzione commerciale (`output_onix.json` e `output_schema_org.json`).
    * **Generazione Documenti:** Pilota l'applicazione esterna `Pandoc` passandogli il testo d'ingresso modificato e gli stili grafici per produrre in un unico passaggio i file `output.pdf`, `output.epub` e il sito web `index.html`.
6. **Distribuzione:** I file generati vengono caricati sul server remoto e pubblicati automaticamente tramite la piattaforma di hosting `GitHub Pages`.

### Spiegazione dello Schema Logico
Il diagramma sottostante evidenzia visivamente come lo script `main.py` si posizioni al centro del flusso di lavoro. Lo schema mostra chiaramente come i file di input vengano assorbiti dall'orchestratore, il quale si fa carico sia della fase di pulizia testuale sia del coordinamento dei programmi di compilazione (`Pandoc`) e della scrittura autonoma dei metadati, fino alla messa online finale del progetto.

```mermaid
graph TD
    %% Fasi del Processo Editoriale canoniche
    subgraph F1 [1. Ideazione]
        ID[Pianificazione Opera: One Health]:::ideazione
    end

    subgraph F2 [2. Acquisizione dei contenuti]
        SRC[Testo: input.md]:::acquisizione
        META[Dati: metadati.yaml]:::acquisizione
        IMG[Risorse: copertina.png]:::acquisizione
    end

    subgraph FLUSSO_CENTRALE [Il Ruolo Centrale di main.py]
        MAIN[Orchestratore Centrale: main.py]:::orchestratore
        F3[3. Revisione e Redazione<br/>Esecuzione pulizia automatica testo]:::revisione
        F5[5. Produzione Automatica<br/>Generazione e smistamento output]:::produzione
    end

    subgraph F4 [4. Progettazione grafica]
        STILI[Fogli di Stile: epub.css & regole stampa]:::grafica
    end

    subgraph OUTPUT [Risultati della Produzione]
        PANDOC[Programma Esterno: Pandoc]:::produzione
        OUT_META[File Metadati:<br/>output_onix.json<br/>output_schema_org.json]:::produzione
        OUT_DOC[File Editoriali:<br/>output.pdf<br/>output.epub<br/>index.html]:::produzione
    end

    subgraph F6 [6. Distribuzione]
        DIST[Piattaforma Web: GitHub Pages]:::distribuzione
    end

    %% Connessioni del Flusso Logico coordinato da main.py
    ID --> SRC & META & IMG
    
    %% Ingestione dati in main.py
    SRC & META & IMG --> MAIN
    
    %% Ciclo interno di main.py (Fase 3 e Fase 5)
    MAIN -->|Esegue| F3
    F3 -->|Restituisce testo pulito| F5
    
    %% Output diretti di main.py ed evocazione Pandoc
    F5 -->|Scrittura diretta JSON| OUT_META
    F5 -->|Comanda e pilota| PANDOC
    
    %% Integrazione della grafica in Pandoc
    STILI -->|Applicazione stili visivi| PANDOC
    PANDOC --> OUT_DOC
    
    %% Rilascio sul Web
    OUT_DOC & OUT_META --> DIST

    %% Classi di stile ad alto contrasto per i nodi
    classDef ideazione fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px,color:#000
    classDef acquisizione fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#000
    classDef orchestratore fill:#fff9c4,stroke:#fbc02d,stroke-width:3px,color:#000
    classDef revisione fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#000
    classDef grafica fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#000
    classDef produzione fill:#ffebee,stroke:#e53935,stroke-width:2px,color:#000
    classDef distribuzione fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000