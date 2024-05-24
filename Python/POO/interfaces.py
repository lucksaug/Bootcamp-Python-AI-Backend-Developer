from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod 
    def ligar(self):
        print("ligando")
    
    @abstractmethod 
    def desligar(self):
        print("desligando")
        
    @property
    @abstractproperty
    def marca (self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
        
    def desligar(self):
        print("Desligando TV")
    
    @property   
    def marca(self):
        return 'TCL'
        
class ControleAC(ControleRemoto):
    def ligar(self):
        print("Ligando AC")

    def desligar(self):
        print("Desligando AC")
    
    @property
    def marca(self):
        return 'ac_conditionair'


if __name__ =="__main__":
    controle_tv = ControleTv()
    
    controle_tv.ligar()
    controle_tv.desligar(),
    print(controle_tv.marca)
    
    controle_ac = ControleAC()
    
    controle_ac.ligar()
    controle_ac.desligar()
    print(controle_ac.marca)
