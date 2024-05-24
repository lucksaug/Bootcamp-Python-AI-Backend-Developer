from os import system
import platform as so 

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor 
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo Instancias")

    def latir(self):
        print("WOFF") 

if __name__=="__main__":
    bully = Cachorro('Bruce', 'caramelo')
    bully.latir()
    del bully
    print(f'Bruce é um American Bully')
        