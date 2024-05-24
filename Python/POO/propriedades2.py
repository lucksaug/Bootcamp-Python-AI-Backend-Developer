class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
if __name__ =="__main__":
    pessoa = Pessoa("Lucas", 2000)
    print(f"{pessoa.nome} \tIdade: {pessoa.idade}")