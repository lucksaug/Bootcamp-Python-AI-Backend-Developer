class Passaro:
    def __init__(self):
        pass
    
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def __init__(self):
        pass
    
    def voar(self):
        super().voar()
        
class Avestruz(Passaro):
    def __init__(self):
        pass
    
    def voar(self):
        print("Avestruz não pode voar")

def plano_de_voo(obj):
    obj.voar()
    
if __name__ == "__main__":
    plano_de_voo(Pardal())
    plano_de_voo(Avestruz())