import os
import shutil
from pathlib import Path

#* Retorna o caminho atual do arquivo,
# print(__file__)

#* Isola o diretorio pai do arquivo
ROOT_PATH = Path(__file__).parent


def criando_diretorio(caminho, nome):
    os.mkdir(caminho / nome)

def deletando_diretorio(caminho, nome):
    pass

def criando_arquivo(caminho, nome):
    return open(caminho / 'txt' / nome, 'w')

def removendo_arquivo(caminho, nome_arquivo):
    os.remove(caminho / 'txt' / nome_arquivo)
    
def fechando_arquivo(arquivo):
    arquivo.close()

def renomeando_arquivo(caminho, nome_arquivo, novo_nome):
    os.rename(caminho / 'txt' / nome_arquivo, caminho / 'txt' / novo_nome)
    
def movendo_arquivo(caminho, caminho_novo, nome_arquivo):
    shutil.move(caminho / nome_arquivo, caminho / caminho_novo / nome_arquivo)
    
if __name__ == '__main__':
    # criando_diretorio(ROOT_PATH, 'novo-diretorio')
    # print(ROOT_PATH)
    arquivo = criando_arquivo(ROOT_PATH, 'novo_teste.txt')
    # renomeando_arquivo(ROOT_PATH, arquivo.name, 'alterado.txt')
    # removendo_arquivo(ROOT_PATH, arquivo.name)  
    fechando_arquivo(arquivo)
    
    # movendo_arquivo(ROOT_PATH, 'txt', 'novo.txt')