import csv
from pathlib import Path 


ROOT_PATH = Path(__file__).parent

def escrita():
    try:
        with open(ROOT_PATH / 'csv' / 'usuarios.csv', 'w', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(['id','nome'])
            escritor.writerow(['1','Mariazinha'])
            escritor.writerow(['2','Joãozinho'])

    except IOError as error:
        print(f'Erro ao criar o arquivo. {error}')
        
def leitor():
    try:
        with open(ROOT_PATH / 'csv' / 'usuarios.csv', 'r', newline='', encoding='utf-8') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                print(linha)        
    except IOError as error:
        print(f'Erro ao criar o arquivo. {error}')
        
def leitor_dict():
    try:
        with open(ROOT_PATH / 'csv' / 'usuarios.csv', 'r', newline='', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            
            for linha in leitor:
                print(f'{linha['id']} | {linha['nome']}')
    except IOError as error:
        print(f'Erro ao criar o arquivo. {error}')
        
leitor_dict()