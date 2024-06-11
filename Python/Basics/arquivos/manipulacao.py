
#? Caminho do arquivo
# caminho = '/home/lucas/Documentos/Code/python/Bootcamp-Python-AI-Backend-Developer/Python/Basics/arquivos/txt/lorem.txt'
caminho = '~/Documentos/Code/python/Bootcamp-Python-AI-Backend-Developer/Python/Basics/arquivos/txt/'

#? Arbetura de um arquivo
def abertura(caminho):
    #* Modo LEITURA
    # return = open(caminho, 'r')
    #* Modo ESCRITA
    return open(f"{caminho}arquivo_para_escrita.txt", 'w')
    # #* Modo INCREMENTO 
    # return = open(caminho, 'a')

#? Modo de leitura
def leitura():
    # * Lê uma linha por vez
    print(arquivo.readline())
    # * Lendo letra por letra,
    for linha in arquivo.readline():
        print(linha)
    # * Retorna uma lista, com todas as linhas
    print(arquivo.readlines())
    for linha in arquivo.readlines():
        print(linha)
    while len(linha := arquivo.readline()):
        print(linha)
    
#? Escrita de arquivo 
def escrita(arquivo):
    arquivo.write('Escrevendo dados em um novo arquivo.')
    arquivo.writelines(['\n', 'ESCREVENDO', '\n', 'UMA', '\n', 'NOVA', '\n', 'LINHA'])

#? Fechamento
def fechamento(arquivo):    
    #* Fecha o arquivo que está aberto
    arquivo.close()
    
if __name__ == '__main__':
    arquivo = abertura(caminho=caminho)
    escrita(arquivo)
    fechamento(arquivo)