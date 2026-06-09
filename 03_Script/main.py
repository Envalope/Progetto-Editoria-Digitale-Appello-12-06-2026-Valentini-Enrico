import yaml
import json
import subprocess
import os
import re
import shutil

# ==============================================================================
# SETTAGGIO PERCORSI
# ==============================================================================
DIR_SORGENTI = "../01_Sorgenti"
DIR_STILI = "../02_Stili"
DIR_OUTPUT = "../04_Output"
DIR_WEB = "../05_webook/site"
YAML_FILE = os.path.join(DIR_SORGENTI, "metadati.yaml")
INPUT_MD = os.path.join(DIR_SORGENTI, "input.md")
# Nome del file copertina (da inserire in 01_Sorgenti)
COPERTINA_IMG = "copertina.png"

# ==============================================================================
# PREPARAZIONE TESTI (Usa il markdown nativo di Pandoc per gli apici)
# ==============================================================================
def prepara_testi_puliti():
    with open(INPUT_MD, "r", encoding="utf-8") as f:
        testo = f.read()

    # Pulisco il testo da apici HTML o Markdown creati nei test precedenti
    testo = re.sub(r'<sup><a href="#g\d+">\d+</a></sup>', '', testo)
    testo = re.sub(r'<a href="#g\d+"><sup>\d+</sup></a>', '', testo)
    testo = re.sub(r'\^\[\d+\]\(#g\d+\)\^', '', testo)
    testo = re.sub(r'\^\d+\^', '', testo)
    testo = re.sub(r'<sup>\d+</sup>', '', testo)

    glossario = {
        "Infodemia": 1, "One Health": 2, "zoonosi": 3, "Deep Learning": 4, 
        "bias algoritmico": 5, "Black Box": 6, "scienza dell'attribuzione": 7, 
        "no-till": 8, "sequestro del carbonio": 9, "prebunking": 10, 
        "Life Cycle Assessment": 11, "crisi di riproducibilità": 12, "cherry-picking": 13
    }
    
    linked_terms = set()
    righe = testo.split('\n')
    linee_pulite = []
    
    in_yaml = False
    
    for riga in righe:
        # Salto l'intestazione YAML e i titoli per evitare errori
        if riga.strip() == "---":
            in_yaml = not in_yaml
            linee_pulite.append(riga)
            continue
            
        if in_yaml or riga.startswith("#"): 
            linee_pulite.append(riga)
            continue
        
        riga_processata = riga
        
        for termine, idx in glossario.items():
            # Pattern che intercetta la parola e l'eventuale punteggiatura adiacente
            pattern = r'\b(' + re.escape(termine) + r')\b([\"\'\)\]”’]?)'
            
            if termine in riga_processata and termine not in linked_terms:
                # SINTASSI PANDOC UNIVERSALE: ^[numero](#link)^ (Apice + Link)
                riga_processata = re.sub(pattern, rf'\1\2^[{idx}](#g{idx})^', riga_processata, count=1)
                linked_terms.add(termine)
                
        linee_pulite.append(riga_processata)

    # Creo un solo file temporaneo perfetto per tutti i formati
    path_tmp = os.path.join(DIR_SORGENTI, "input_processato.md")
    with open(path_tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(linee_pulite))
        
    return path_tmp

# ==============================================================================
# 1. CODICE ORIGINALE DEL PROF (Metadati)
# ==============================================================================

def load_yaml(file_path):
    """Carica il file YAML."""
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def convert_to_onix(data):  #converte in onix
    """Converte i metadati YAML nel formato ONIX."""
    onix = {  #faccio un mapping degli attributi
        "Product": {
            "Title": data["distribuzione"]["onix"]["title"], #ho l'attributo distribuzione, all'interno di distribuzione onix e poi ho i diversi attributi
            "Contributor": { #faccio un mapping del vocabolario,se ho gia utilizzato un vocabolario compatibile con onix sto semplicemente riscrivendo questo contenuto 
                "PrimaryAuthor": data["distribuzione"]["onix"]["contributor"]["primary_author"],
                "OtherAuthors": data["distribuzione"]["onix"]["contributor"]["other_authors"],
            },
            "Publisher": data["distribuzione"]["onix"]["publisher"],
            "PublicationDate": data["distribuzione"]["onix"]["publication_date"],
            "ISBN": data["distribuzione"]["onix"]["isbn"],
            "Audience": data["distribuzione"]["onix"]["audience"],
            "Format": data["distribuzione"]["onix"]["format"],
            "Price": data["distribuzione"]["onix"]["price"],
        }
    }
    return onix

def convert_to_schema_org(data): #la conversione su schema.org
    """Converte i metadati YAML nel formato Schema.org."""
    schema_org = { #attributi necessari per lo schema.org (context,type...)
        "@context": "https://schema.org",
        "@type": "Book",
        "name": data["distribuzione"]["schema_org"]["name"],
        "author": [ #inizio a mappare i diversi attributi
            { #nel momento devo creare un elemento complesso devo dichiarare tutto
                "@type": "Person",
                "name": author["name"]
            } for author in data["distribuzione"]["schema_org"]["author"]
        ],
        "datePublished": data["distribuzione"]["schema_org"]["datePublished"],
        "publisher": {
            "@type": "Organization",
            "name": data["distribuzione"]["schema_org"]["publisher"]["name"]
        },
        "isbn": data["distribuzione"]["schema_org"]["isbn"],
        "genre": data["distribuzione"]["schema_org"]["genre"],
        "language": data["distribuzione"]["schema_org"]["language"],
        "inLanguage": data["distribuzione"]["schema_org"]["inLanguage"],
        "format": data["distribuzione"]["schema_org"]["format"],
    }
    return schema_org

def save_to_file(data, file_path, format="json"):  #funzione per salvataggio finale
    """Salva i dati in un file (ONIX o Schema.org)."""
    with open(file_path, "w", encoding="utf-8") as file:
        if format == "json":
            json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            file.write(str(data))  # Default string format
    print(f"Salvato in: {file_path}")

# ==============================================================================
# 2. CODICE ORIGINALE DEL PROF (Pandoc)
# ==============================================================================

# Funzione originale del prof (modificata solo per accettare il parametro opzionale toc)
def convert_with_pandoc(input_files, output_file, metadata, pdf_engine=None, toc=False):#alcuni parametri li prendiamo in input
    command = [ #costruiamo il nostro comando che è una lista
        'pandoc', *input_files,  # Passa tutti i file di input, l'asterisco dice di prendere i valori dalla lista
        '--metadata-file', metadata, #opzione richiesta da pandoc
        '--output', output_file,
        '--citeproc'
    ]
    
    # Gestisci la conversione in PDF con un motore specificato (opzionale)
    if pdf_engine: #nel caso della generazione del PDF,infatti c'è l'if
        command.extend(['--pdf-engine', pdf_engine]) #voglio che sia eseguito il comando con il nome pdf engine passato
    
    if toc:
        command.append('--toc')

    # Esegui il comando Pandoc con la libreria subprocess che gli passo il comando
    subprocess.run(command, check=True, cwd=DIR_SORGENTI)
    print(f"Generato: {output_file}") #stampo a video in console

# Aggiungo una funzione ad hoc per l'epub per applicare lo stile EPUB e la copertina
def convert_epub_con_stile(input_files, output_file, metadata, cover_image=None):
    command = [ 
        'pandoc', *input_files, 
        '--metadata-file', metadata,
        '--output', output_file,
        '--toc', # Indice nell'EPUB
        '--citeproc',
        '--css', '../02_Stili/epub.css' 
    ]
    
    # Se il file copertina.png esiste nella cartella 01_Sorgenti, viene aggiunto al comando
    if cover_image and os.path.exists(os.path.join(DIR_SORGENTI, cover_image)):
        command.extend(['--epub-cover-image', cover_image])
        
    subprocess.run(command, check=True, cwd=DIR_SORGENTI)
    print(f"Generato: {output_file}")

# Aggiungo la funzione per il sito HTML pescando STYLE.CSS
def generate_webbook(input_file):
    if not os.path.exists(DIR_WEB):
        os.makedirs(DIR_WEB)
    
    # Creiamo in automatico la cartella css all'interno del sito
    css_dir = os.path.join(DIR_WEB, "css")
    os.makedirs(css_dir, exist_ok=True)
    
    # Prendo il file STYLE.CSS dalla cartella stili, e lo copio nella cartella del sito web
    file_css_sorgente = os.path.join(DIR_STILI, "style.css")
    file_css_destinazione = os.path.join(css_dir, "style.css")
    
    if os.path.exists(file_css_sorgente):
        shutil.copyfile(file_css_sorgente, file_css_destinazione)
        
    output_path = os.path.join(DIR_WEB, "index.html")
    command = ['pandoc', input_file, '--metadata-file', 'metadati.yaml', '--output', output_path, '--toc', '--standalone', '--css', 'css/style.css', '--citeproc']
    subprocess.run(command, check=True, cwd=DIR_SORGENTI)
    print(f"Web-Book generato in: {output_path}")

# ==============================================================================
# MAIN 
# ==============================================================================

def main():
    if not os.path.exists(DIR_OUTPUT):
        os.makedirs(DIR_OUTPUT)

    data = load_yaml(YAML_FILE)
    
    # 1. Metadati (codice prof)
    save_to_file(convert_to_onix(data), os.path.join(DIR_OUTPUT, "output_onix.json"), format="json")
    save_to_file(convert_to_schema_org(data), os.path.join(DIR_OUTPUT, "output_schema_org.json"), format="json")

    # Creo il file temporaneo convertito nativamente in markdown per tutti gli output
    f_processato = prepara_testi_puliti()
    nome_file_processato = os.path.basename(f_processato)

    # 2. Conversione Pandoc (codice prof)
    metadata = load_yaml(YAML_FILE)
    output_formats = metadata.get('gestione_documentale', {}).get('output_formats', [])

    for format in output_formats: #con il ciclo for possiamo gestire gli output
        if format == 'pdf':
            convert_with_pandoc([nome_file_processato], os.path.join(DIR_OUTPUT, 'output.pdf'), 'metadati.yaml', pdf_engine='xelatex', toc=True)
        elif format == 'html':
            generate_webbook(nome_file_processato)
        elif format == 'epub':
            convert_epub_con_stile([nome_file_processato], os.path.join(DIR_OUTPUT, 'output.epub'), 'metadati.yaml', cover_image=COPERTINA_IMG)

    # Pulizia finale per non lasciare tracce
    if os.path.exists(f_processato): 
        os.remove(f_processato)

if __name__ == "__main__":
    main()