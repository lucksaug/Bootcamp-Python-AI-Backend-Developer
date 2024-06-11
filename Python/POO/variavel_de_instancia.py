class Estudante:
    escola = 'DIO'
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'        

def mostrar_valores(*objs):
    for obj in objs:
        print (obj)

if __name__ == "__main__":
    aluno1 = Estudante('Summer', 1)
    aluno2 = Estudante('Morty', 2)
    
    Estudante.escola = 'Harry Herpson High School'
    aluno3 = Estudante('Jessica', 3)    

    
    mostrar_valores(aluno1, aluno2, aluno3)
