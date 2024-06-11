from pathlib import Path


ROOT_PATH = Path(__file__).parent

#* Certifar-se de que o arquivo foi aberto corretamente
try:
    #* WITH - Otimização de memória, certificando que o arquivo irá encerrar ao concluir o bloco de código
    #* Certificar-se que o tipo de codificação corresponde ao do arquivo, (encoding='utf-8')
    with open(ROOT_PATH / 'txt' / 'lorem.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.readline())
except IOError as error:
    print(error)