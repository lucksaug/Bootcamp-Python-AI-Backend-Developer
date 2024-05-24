class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
        
class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        super().__init__(**kw)
        self.cor_do_pelo = cor_do_pelo
    def __str__(self):
        return 'Mamifero'

class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        super().__init__(**kw)
        self.cor_do_bico = cor_do_bico
    def __str__(self):
        return 'Ave'
        

class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, numero_de_patas, cor_do_pelo, cor_do_bico):
        # Exibe a ordem em que o interpretador ira buscar no programa, no caso: Mamifero > Ave > Animal.
        # Ornitorrinco herda Mamifero e Ave, e Mamifero e Ave herda Animal
        print(Ornitorrinco.__mro__)
        # OU
        #print(Ornitorrinco.mro())
        super().__init__(numero_de_patas = numero_de_patas, cor_do_pelo=cor_do_pelo, cor_do_bico=cor_do_bico)
    def __str__(self):
        return 'Ornitorrinco'

if __name__=='__main__':
    gato = Gato(numero_de_patas=4, cor_do_pelo="Preto")
    print(gato)
    ornintorrinco = Ornitorrinco(numero_de_patas=4, cor_do_pelo="Verde", cor_do_bico="Laranja")
    print(ornintorrinco)
    