import math as mt

class Interpolacao:
    def __init__(self):
        pass

    def porcentagem(self):
        tipo = "Porcentagem"
        print("Este é um exemplo de interpolação usando %s, %(tipo)")#Não funciona mais

    def format_variavel(self):
        tipo = "Variavel"
        print("Este é um exemplo de interpolação usando {tipo}".format(tipo=tipo))
 
    def f_format(self):
        tipo = "FString"
        ponto_flutuante = mt.pi
        #print(f"Este é um exemplo de interpolação usando {tipo}")
        # O valor antes do ponto é referente ao espaço antes do número, depois do ponto, quantas casas decimais após a virgula. 
        print(f"Esse é uma formatação com ponto flutuante:{ponto_flutuante:5.2f}")
        
if __name__ == "__main__":
    tipo = Interpolacao()
    tipo.f_format()