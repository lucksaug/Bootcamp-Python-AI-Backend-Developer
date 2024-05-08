class OperadoresMatematicos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def soma(self, x, y):
        print( self.x + self.y)

    def subtracao(self):
        print( self.x - self.y)

    def produto(self):
        print( self.x * self.y)

    def divisao(self):
        print( self.x / self.y)

    def divisao_inteira(self):
        print( self.x // self.y)

    def mod_da_divisao(self):
        print( self.x % self.y)

    def potencia(self):
        print( self.x**self.y)

class OperadoresComparacao:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def se_falso(self):
        if self.x != self.y:
            print("é diferente")
        else:
            print("não é diferente")

    def se_verdadeiro(self, x, y):
        if self.x == self.y:
            print("é igual")
        else:
            print("não é igual")

    def se_e_maior(self, x, y):
        if self.x > self.y:
            print("É maior")
        else:
            print("Não é maior")

    def se_e_menor(self, x, y):
        if self.x > self.y:
            print("É menor")
        else:
            print("Não é menor")

    def se_e_maior_ou_menor(self):
        if self.x >= self.y:
            print("É maior ou igual")
        else:
            print("É menor")

class OperadoresAtribuicao:
    def __init__(self, x):
        self.x = x

    def soma(self):
        self.x += self.x
        print(self.x)

    def subtracao(self):
        self.x -= self.x
        print(self.x)

    def produto(self):
        self.x *= self.x
        print(self.x)

    def divisao(self):
        self.x /= self.x
        print(self.x)

    def divisao_inteira(self):
        self.x //= self.x
        print(self.x)

    def mod_da_divisao(self):
        self.x %= self.x
        print(self.x)

    def potencia(self):
        self.x **= self.x
        print(self.x)

class OperadoresLogicos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def se_falso(self):
        if not self.x == self.y:
            print("é diferente")
        else:
            print("não é diferente")

    def se_falso_ou_maior(self):
        if self.x != self.y or self.x > self.y:
            print("é diferente ou maior")
        else:
            print("não é diferente ou maior")

    def se_verdadeiro_ou_menor(self, x, y):
        if self.x == self.y or self.x > self.y:
            print("é igual ou menor")
        else:
            print("não é igual ou menor")

    def se_e_maior_e_igual(self, x, y):
        if self.x > self.y and self.x >= self.y:
            print("É maior e maior")
        else:
            print("Não é maior e maior")

    def se_e_menor_e_igual(self, x, y):
        if self.x < self.y and self.x <= self.y:
            print("É menor e menor")
        else:
            print("Não é menor e menor")

class OperadoresIdentidade:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def se_igual(self):
        if self.x is self.y:
            print("é igual")
        else:
            print("não é igual")
    
    def se_diferente(self):
        if self.x is not self.y:
            print("é diferente")
        else:
            print("não é diferente")

class OperadoresAssociacao:
    def __init__(self, nome:list, aluno:list):
        self.nome = nome
        self.aluno = aluno

    def nome_em_aluno(self):
        if self.nome in self.aluno:
            print(f"O {self.nome} é aluno")
        elif self.nome not in self.aluno:
            print(f"O {self.nome} não é aluno")  

    
if __name__ == "__main__":
    pass
