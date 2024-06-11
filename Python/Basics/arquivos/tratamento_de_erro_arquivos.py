import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

class Erros(Exception):
    def arquivo_nao_encontrado(self):
        #? Quando o arquivo não é encontrado no diretório especificado
        raise FileNotFoundError()
    
    def permissao(self):
        #? Quando não há permissões para leitura/escrita de um arquivo
        raise PermissionError()
    
    def entrada_saida(self):
        #? Quando ocorre um erro (geral) de E/S ao trabalhar com arquivos
        #? (Permissão, falta de espaço em disco, ...)
        #? (I/O) = Input/Output
        raise IOError()
     
    def codificacao_leitura(self):
        #? Quando tenta decodificar os dados de um arquivo de txt, usando 
        #? uma codificação inadequada
        raise UnicodeDecodeError()

    def codificacao_escrita(self):
        #? Quando tenta decodificar os dados de um arquivo de txt, usando 
        #? uma codificação inadequada
        raise UnicodeEncodeError()
        
    def e_diretorio(self):
        #? Quando há a tentativa de abrir um diretorio ao invés de um arquivo
        #? de texto
        raise IsADirectoryError()

if __name__ == '__main__':
    try:
        arquivo = open('novo.txt')
        # arquivo = open(ROOT_PATH / 'novo-diretorio')
    except FileNotFoundError:
        print(f'Arquivo não encontrado')
    except IsADirectoryError as error:
        print('Isso é um diretório, não um arquivo')
        print(error)