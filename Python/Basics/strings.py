
class StringsPy:
    def __init__(self):
        pass

    def tornar_maiusculo(self):
       palavra = input("Entre com a palavra a ser transformada: ")
       palavra.upper()
       print(palavra),

    def tornar_minusculo(self):
        palavra = input("Entre com a palavra a ser transformada: ")
        palavra.lower()
        print(palavra)

    def tornar_primeira_maiuscula(self):
        palavra = input("Entre com a palavra a ser transformada: ")
        palavra.title()
        print(palavra)

    def retirar_espacos(self):
        nome = "******** Lucas ***********"
        print(nome)
        print(f"Esse remove os espaços da frente e de trás {nome.strip("*")}")
        print(f"Esse remove os espaços somente da esquerda {nome.lstrip("*")}")
        print(f"Esse remove os espaços somente da direita {nome.rstrip("*")}")

    def centralizar_elemento(self):
        palavra , argumento = input("Entre com uma palavra e um separador, separado por '-': ").split("-")
        print(f"A palavra digitada foi: {palavra}, e o separador: {argumento}")
        palavra = "LUCAS"
        print(palavra.center(20, argumento))
    
    def adiciona_caracter(self):
        sigla = input("Entre com uma sigla para acrescentar o caracter '.': ").upper()
        print(".".join(sigla))

if __name__=="__main__":
    texto = StringsPy()
    texto.adiciona_caracter()
