class Fatiamento:
    def __init__(self):
        self.nome = "Lucas Augusto da Silva"
        
    def posicao_da_letra(self,numero:int):
        print(f"A letra na posição {numero} é: {self.nome[numero]}")

    def primeiras_letras(self, numero:int):
        print(self.nome[:numero])

    def exclui_primeira(self, numero:int):
        print(self.nome[numero:])

    def invert_string(self):
        print(self.nome[::-1]).lower()

if __name__ == "__main__":
    novo = Fatiamento()
    novo.invert_string()
