import os
import subprocess
import csv
import json
import time

competition_dir = "competition"
notebooks_dir = "notebooks"


competitions = [
    {
        "name": "house-prices-advanced-regression-techniques",
        "domain": "Dados Tabulares"
    },
    {
        "name": "titanic",
        "domain": "Dados Tabulares"
    },
    {
        "name": "santander-customer-transaction-prediction",
        "domain": "Dados Tabulares"
    },
    {
        "name": "digit-recognizer",
        "domain": "Visão Computacional"
    },
    {
        "name": "cassava-leaf-disease-classification",
        "domain": "Visão Computacional"
    },
    {
        "name": "hubmap-kidney-segmentation",
        "domain": "Visão Computacional"
    },
    {
        "name": "nlp-getting-started",
        "domain": "NLP"
    },
    {
        "name": "jigsaw-unintended-bias-in-toxicity-classification",
        "domain": "NLP"
    },
    {
        "name": "commonlitreadabilityprize",
        "domain": "NLP"
    }
]

# Carregar dados do CSV
print("Carregando dados do CSV...")
all_notebooks_data = []
csv_path = "output/all_notebooks_data.csv"

try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Converter campos numéricos
            notebook_data = {
                "ref": row.get('ref', ''),
                "title": row.get('title', ''),
                "author": row.get('author', ''),
                "lastRunTime": row.get('lastRunTime', ''),
                "totalVotes": int(row.get('totalVotes', 0)),
                "competition": row.get('competition', ''),
                "domain": row.get('domain', ''),
                "dataDependency": int(row.get('dataDependency', 0)),
                "codeDependency": int(row.get('codeDependency', 0)),
                "awareness": int(row.get('awareness', 0)),
                "modularity": int(row.get('modularity', 0)),
                "configurableOptions": int(row.get('configurableOptions', 0)),
                "scalability": int(row.get('scalability', 0)),
                "readability": int(row.get('readability', 0)),
                "performance": int(row.get('performance', 0)),
                "duplicateCodeElimination": int(row.get('duplicateCodeElimination', 0))
            }
            all_notebooks_data.append(notebook_data)
    
    print(f"✓ {len(all_notebooks_data)} notebooks carregados do CSV")
except FileNotFoundError:
    print(f"✗ Erro: Arquivo {csv_path} não encontrado!")
    print("Execute primeiro o script principal (main_2.py) para gerar os dados.")
    exit(1)
except Exception as e:
    print(f"✗ Erro ao carregar CSV: {e}")
    exit(1)

print("\n" + "="*80)
print("ETAPA 3: CLONANDO NOTEBOOKS")
print("="*80)



for competition in competitions:
    competition_name = competition['name']
    domain = competition['domain']
    
    print(f"\n{'='*80}")
    print(f"Clonando notebooks de: {competition_name}")
    print(f"{'='*80}\n")
    
    # Filtrar notebooks desta competição
    competition_notebooks = [n for n in all_notebooks_data if competition_name == n['competition']]
    
    if not competition_notebooks:
        print(f"  ⚠ Nenhum notebook encontrado para clonar")
        continue
    
    # Criar diretório para clonagem
    clone_dir = os.path.join(notebooks_dir, domain.replace(" ", "_"), competition_name)
    os.makedirs(clone_dir, exist_ok=True)
    
    # Clonar cada notebook com sistema de retry
    for i, notebook in enumerate(competition_notebooks):
        ref = notebook['ref']
        if not ref:
            continue
            
        print(f"  Clonando {i+1}/{len(competition_notebooks)}: {ref}")
        clone_cmd = f"kaggle kernels pull {ref} -p {clone_dir}/{ref.split('/')[-1]}"

        while True:
            result = subprocess.run(clone_cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"    ✓ Clonado com sucesso")
                break
            else:
                print(f"    ✗ Erro: {result.stderr[:80]}")
                print(f"    ⏳ Aguardando 30 segundos antes de tentar novamente...")
                time.sleep(30)


print(f"\n{'='*80}")
print(f"Processo concluído!")
print(f"Total de notebooks coletados: {len(all_notebooks_data)}")
print(f"{'='*80}")