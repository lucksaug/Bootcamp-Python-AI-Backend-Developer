class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_idade(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18
    
if __name__ == "__main__":
    pessoa1 = Pessoa('Morty', 14)
    pessoa2 = Pessoa('Summer', 18)
    Pessoa.criar_de_idade(2000, 4, 27, 'Lucas')
    print(Pessoa.e_maior_de_idade(15))
    print(Pessoa.e_maior_de_idade(28))
    