from os import system
import platform as so

class ClassePrincipal:
    def __init__(self):
        pass
    
    def limpar_tela(self, clear=True):
        if clear == True:
            if so.system() == 'Linux':
                system("clear")
            elif so.system() == 'Windows':
                system("cls")
                
class Bicicleta(ClassePrincipal):
    def __init__(self, cor, marca, ano, valor, marcha=1):
        self.cor = cor
        self.marca = marca
        self.ano = ano 
        self.valor = valor
        self.velocidade = 0
        self.marcha = 1
        
    def __str__(self):
        # Métodos de retorno: 
        # Método 1
        # return f'Bicicleta: cor={self.cor}, marca={self.marca}, valor={self.valor}'
        # Método 2
        self.limpar_tela()
        return f'''
        {self.__class__.__name__}: 
        {', '.join([f'{chave} = {valor}'for chave,valor in self.__dict__.items()])}'''
        
    def buzinar(self):
        print("PLIM")
    
    def parar(self):
        print("Biciclera parada")
        
    def correr(self):
        print("Bicicleta em movimento")
    
    def trocar_de_marcha(self, numero_da_marcha=1):
        print(f'Trocando de marcha')
        def _trocar_de_marcha():
            if numero_da_marcha > self.marcha:
                print('Marcha trocada')
            else:
                print('Não foi possível trocar de marcha')

if __name__ == "__main__":
    b1 = Bicicleta("Amarela", "Caloi", "2012", 1000.00)
    # Bicicleta.buzinar(b1)
    # Exibição feita pelo método __str__:
    b1.trocar_de_marcha(2)