from os import system
from random import randint
from dicionarios import jedi, contatos

#Escopo Global
notas_musicais = ["DÓ", "RÉ", "MI", "FÁ", "SOL", "LÁ","SÍ"]

aluno = {
    "1":{
        "nome": "Alberto",
        "idade": 20,
        "curso": "Engenheira Mecânica",
        "faculdade": "USP"
    },
    "2":{
        "nome": "Giovanna",
        "idade": 20,
        "curso": "Odontologia",
        "faculdade": "Unip"
    }
}

def exibir_mensagem():
    print("Seja bem vindo")

def exibir_mensagem_2(nome:str="Fulano"):
    print(f"Seja bem vindo, {nome}")

# Por padrão retorna None
def exibir_antecessor_sucessor(numero:int=1):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor
    
# * Indica que está recebendo uma tupla
def recebendo_uma_lista_voltando_tupla(*args):
    for i in range(len(args[0])):
        print (f"Nota: {args[0][i]}")
# RESULTADO ESPERADO
# Nota: DÓ
# Nota: RÉ
# Nota: MI
# Nota: FÁ
# Nota: SOL
# Nota: LÁ

def recebendo_elementos_voltando_tupla(*args):
    for i in range(len(args)):
        print (f"Nota: {args[i]}")
# RESULTADO ESPERADO
# Nota: SÍ
# Nota: DÓ
# Nota: RÉ
# Nota: MI
# Nota: FÁ
# Nota: SOL
# Nota: LÁ
# Nota: SÍ

# ** Indica que está recebendo um dicionário
def recebendo_um_dicionario(**kwargs):
    
    for x in kwargs:
        print(kwargs[x])

# Position only
# Antes do "/" é obrigatório que insira os parametros na mesma posição em que foi programado sem precisar da chave "exemplo=''"
# Depois do "/" pode ser por posição OU chave(key)
def parametros(prova:str, /, dificuldade:str, local:str):
    print(prova)
    print(dificuldade)
    print(local)
    
# Keywordonly
# Depois do "*" somente ser possível passar as chaves 
def parametros_key(*, nome, idade, curso, faculdade):
    print(nome)
    print(idade)
    print(curso)
    print(faculdade)
    
def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

# É possível chamar uma função como parametro
def imprimir_resultado(x,y, operacao):
    resultado = operacao(x,y)
    print(f"O resultado é = {resultado}")


if __name__ == "__main__":
    system("clear")
    # exibir_mensagem()
    # exibir_mensagem_2("Lucas")
    
    # antecessor, sucessor = exibir_antecessor_sucessor(2)
    # print(f"O antecessor de é {antecessor}, o sucessor é {sucessor}") 
    
    # recebendo_uma_lista_voltando_tupla(notas_musicais)
    # recebendo_elementos_voltando_tupla("DÓ", "RÉ", "MI", "FÁ", "SOL", "LÁ","SÍ")
    
    # É importante ter o "**" antes de inserir o dicionario como parametro
    # recebendo_um_dicionario(**contatos)

    #                   /
    # parametros("ENEM", dificuldade="DIFÍCIL", local="SÃO PAULO")
    
    # parametros_key(nome=aluno["1"]["nome"],idade=aluno["1"]["idade"],curso=aluno["1"]["curso"],faculdade=aluno["1"]["faculdade"])
    
    # imprimir_resultado(10, 10, somar)
    # imprimir_resultado(10, 10, subtrair)
    