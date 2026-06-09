---
title: "Relazione del progetto d'esame di Editoria Digitale"
author: "Enrico Valentini"
date: "11 Giugno 2026"
institute: "Università degli Studi di Milano - CdL in Informatica Musicale"
course: "Editoria Digitale"
tags: ["Single Source Publishing", "Pandoc", "Automazione", "One Health", "Python"]
version: "1.2"
kind: "Document"
bibliography: "bibliografia.bib"
csl: "IEEE.csl"
---

<img src="./logo/minerva.jpg" alt="Logo UNIMI" width="100" height="100" />

# One Health & Futuro Digitale: Dossier Strategico
Analisi multidisciplinare su Salute, Clima, IA e Disinformazione per i professionisti dell'informazione

## Introduzione
Il presente progetto, sviluppato nell'ambito del corso di Editoria Digitale, si propone di implementare un ecosistema di pubblicazione digitale basato sul paradigma del *Single Source Publishing* (SSP). L'obiettivo è la creazione di un "Dossier Strategico" tematico, pensato per professionisti dell'informazione — giornalisti, divulgatori scientifici e curatori di contenuti — che necessitano di un flusso di lavoro efficiente per la gestione di tematiche complesse e in continua evoluzione, quali il paradigma *One Health*.

La sfida principale risiede nella trasformazione di dati scientifici grezzi (provenienti da database accademici Open Access) in prodotti editoriali pronti all'uso (HTML, EPUB, PDF). Il progetto adotta un approccio *data-centric*: l'intero contenuto è scritto in un unico file sorgente in Markdown, mentre l'automazione, orchestrata tramite script Python e il motore di conversione Pandoc, garantisce la separazione netta tra il contenuto semantico e la sua rappresentazione grafica. I risultati raggiunti testimoniano l'efficacia di questo approccio nel ridurre drasticamente i tempi di produzione e l'incidenza di errori umani, tipici dei flussi di lavoro manuali tradizionali.

## Ideazione 

### Tema
Il nucleo tematico del dossier è il paradigma "One Health". Si tratta di un approccio integrato che riconosce l'interdipendenza tra la salute umana, la salute animale e la tutela degli ecosistemi. Ho selezionato tale ambito per la sua rilevanza nell'agenda globale post-pandemica e per la criticità informativa che lo caratterizza: spesso oggetto di semplificazioni mediatiche, necessita di una mediazione che sia, al contempo, divulgativa e scientificamente rigorosa.

Gli argomenti correlati analizzati includono:
* **Zoonosi:** Analisi dei driver ambientali che favoriscono lo *spillover* virale.
* **Intelligenza Artificiale:** Studio dei bias algoritmici in ambito sanitario e del fenomeno "Black Box".
* **Crisi Climatica:** Applicazione della scienza dell'attribuzione agli eventi meteorologici estremi.
* **Agricoltura Sostenibile:** Tecniche di *no-till* e strategie di sequestro del carbonio nel suolo.
* **Disinformazione:** Strategie di *prebunking* come "vaccino cognitivo" contro l'infodemia.
* **Transizione Energetica:** Valutazione del ciclo di vita (LCA) delle tecnologie rinnovabili.

### Destinatari
Per garantire la massima efficacia comunicativa, ho definito due archetipi di destinatari (*personas*):

1. **Il Redattore Editoriale (Generalista):** Professionista che lavora in redazioni online con scadenze serrate. Necessita di sintesi tecniche verificabili per scrivere articoli su temi complessi senza avere una formazione specialistica in medicina o climatologia.
   * *Scenario d'uso:* A fronte di un'emergenza sanitaria, il redattore utilizza il Web-Book per estrarre rapidamente concetti chiave e link diretti alle fonti primarie (Nature, Science), garantendo precisione al proprio pezzo in tempi record.

2. **Il Divulgatore / Curatore di Newsletter:** Professionista che si occupa di approfondimento e *long-form*.
   * *Scenario d'uso:* Utilizza la versione EPUB su dispositivi e-ink. Sfrutta l'indice ipertestuale e il glossario dinamico per navigare tra i concetti tecnici senza interrompere l'esperienza di lettura, beneficiando di un'impaginazione ottimizzata per la fluidità del testo.

### Requisiti di accettazione
Per soddisfare gli standard del progetto, sono stati definiti i seguenti requisiti:
* **Modularità:** Separazione totale tra il file di contenuto (`input.md`) e le direttive di stile (CSS, YAML).
* **Interoperabilità:** Esportazione automatica di metadati in formati standard (ONIX per l'editoria professionale e Schema.org per il web).
* **Accessibilità:** Il formato EPUB deve essere nativamente fluido, supportando le personalizzazioni dell'utente (font, modalità notte, dimensione caratteri).
* **Integrità citazionale:** Implementazione corretta di un sistema di gestione bibliografica (`.bib`) che garantisca la tracciabilità di ogni fonte Open Access.

## Processo di produzione

### Acquisizione dei contenuti
La fase di reperimento delle fonti è stata condotta interrogando database scientifici come PubMed Central e Google Scholar, filtrando i risultati per licenze Open Access. Ho selezionato 21 articoli, focalizzandomi sulla qualità della metodologia e sulla rilevanza temporale. La sfida metodologica è stata trasformare il linguaggio accademico (spesso ostico) in una sintesi divulgativa che mantenga intatta la validità scientifica, operando una mediazione linguistica mirata al giornalismo di qualità.

### Flusso di gestione documentale
Il cuore del sistema è una *pipeline* di automazione centralizzata in `main.py`. Il flusso operativo si articola in:
1. **Analisi e Validazione:** Lettura dei metadati YAML e dell'input Markdown.
2. **Pre-processing:** Utilizzo di espressioni regolari (RegEx) per l'indicizzazione automatica dei termini del glossario: il sistema inserisce i link ipertestuali solo alla prima occorrenza, evitando saturazione di link.
3. **Generazione Metadati:** Produzione di file JSON conformi agli standard internazionali di indicizzazione editoriale.
4. **Allineamento Grafico:** Distribuzione dei file CSS nelle directory target, garantendo che lo stile Web sia distinto da quello EPUB (che richiede maggiore semplicità strutturale).
5. **Compilazione tramite Pandoc:** Invocazione del motore XeLaTeX per il PDF, ottimizzazione CSS per HTML e creazione del pacchetto EPUB.

```mermaid
graph TD
    SORGENTI[Testo: input.md + metadati.yaml] --> SCRIPT((Script Python))
    SCRIPT -->|RegEx| GLOSSARIO[Glossario Automatico]
    SCRIPT -->|Export| METADATA[JSON ONIX/Schema.org]
    SCRIPT -->|Pandoc| OUTPUT[HTML, EPUB, PDF]
    ```markdown
## Valutazione dei risultati raggiunti

### Valutazione del flusso di produzione
* **Riduzione tempi:** Il processo di pubblicazione (generazione di 3 formati) è sceso da ore di lavoro manuale a meno di 3 secondi (esecuzione dello script Python).
* **Riduzione errori:** La centralizzazione del dato in `input.md` ha eliminato l'incidenza di refusi disallineati tra le diverse versioni.
* **Qualità:** La formattazione è coerente su tutti i canali, assicurando un *look & feel* professionale.
* **Nuovi scenari:** L'automazione ha permesso di esplorare canali di distribuzione prima inaccessibili (e-book nativo).

### Confronto con lo stato dell'arte
* **Flusso ASIS (Tradizionale):** L'autore scrive su editor word-processor (es. Word), esporta manualmente in PDF, copia-incolla il contenuto in un CMS per il sito web e usa software terzi per la conversione EPUB. Ogni correzione richiede tre interventi separati, con un elevato rischio di inconsistenza dei dati.
* **Flusso TOBE (Proposto):** L'unica "fonte di verità" è il sorgente Markdown. Ogni modifica si propaga istantaneamente su tutti gli output. Il processo è robusto, tracciabile e basato su standard aperti, garantendo la longevità del prodotto digitale.

### Limiti emersi
Il sistema presenta alcune limitazioni tecniche:
1. **Dipendenza dall'ambiente locale:** Il workflow richiede l'installazione di Pandoc, Python e una distribuzione LaTeX (XeLaTeX), rendendo il sistema dipendente dalla configurazione dell'ambiente di lavoro.
2. **Discontinuità CSS-PDF:** LaTeX non supporta direttamente i file CSS. Ho dovuto creare una configurazione separata (YAML) per gestire la geometria della pagina PDF, causando una parziale duplicazione delle direttive di stile.
3. **Curva di apprendimento:** La configurazione iniziale dello script ha richiesto un tempo di setup superiore rispetto a un workflow manuale, giustificato però dai benefici di manutenzione a lungo termine.

## Conclusioni
Gli obiettivi del progetto sono stati pienamente raggiunti. Il "Dossier Strategico" si configura come un prodotto multicanale solido, che offre un concreto valore aggiunto ai professionisti dell'informazione. La separazione tra contenuto e presentazione non è stata solo una scelta tecnica, ma una necessità editoriale per garantire scalabilità e precisione. Il progetto apre la strada a futuri sviluppi, come la migrazione del workflow su *GitHub Actions* per una pubblicazione automatizzata *cloud-native* ad ogni commit, rendendo l'intero sistema indipendente dalle risorse locali.

## Bibliografia e sitografia
* Riferimenti a paper Open Access presenti nel file `bibliografia.bib` (*Nature*, *Science*, *eLife*).
* Documentazione tecnica: *Pandoc User's Guide* (MacFarlane, 2026).
* Documentazione linguaggio Python 3 e modulo `re`.
* Materiale didattico del corso di *Editoria Digitale* tenuto dal Prof. Ceravolo.