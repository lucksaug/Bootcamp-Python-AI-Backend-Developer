from os import system 

caminho = '~/Documentos/Code/python/Bootcamp-Python-AI-Backend-Developer/Python/Basics/arquivos/txt/'
def criar_arquivo(caminho):
    nome = input('NOME DO ARQUIVO: ')
    extensao = input('EXTENSÃO[txt/py]: ').lower()
    comando = f'touch {caminho}{nome}.{extensao}'
    system(comando)
    texto = input('ESCREVA ALGUMA COISA NO DOCUMENTO: ')
    system(f'echo {texto} >> {caminho}{nome}.{extensao}')
    system(f'cat {caminho}{nome}.{extensao}')

def deletar_arquivo(caminho, nome):
    comando = f'rm {caminho}{nome}'
    system(command=comando)
    
def deletar_todos_arquivos_no_caminho(caminho):
    comando = f'rm {caminho}*'
    system(command=comando)

# criar_arquivo(caminho)
# deletar_arquivo(caminho, 'teste.txt')
deletar_todos_arquivos_no_caminho(caminho)