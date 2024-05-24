from os import system
import platform as os

class ClassePai:
    def __init__(self):
        pass

class ClasseMae:
    def __init__(self):
        pass

class ClasseFilho(ClassePai, ClasseMae):
    def __init__(self):
        pass

class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_roda = numero_de_rodas
    
    def ligar_motor(self):
        print("Ligando Motor")
    
    def desligar_motor(self):
        print("Desligando Motor")
    
    
class Carro(Veiculo):
    def __init__(self):
        pass

class Moto(Veiculo):
    def __init__(self):
        pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f'{'sim, 'if self.carregado else 'Não '}está carregado')

if __name__ == "__main__":
    caminhao = Caminhao("Preto", "HDS2K45", 8, True)
    caminhao.esta_carregado()