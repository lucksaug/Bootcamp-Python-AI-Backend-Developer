from os import system
from random import randint, choice
from json import *
system("clear")
# Maneiras de declarar um dicionário:
#pessoa = {"username": "rickmorty", "age": 23}
pessoa = dict(username="rickmorty", age= 23)

pessoa["Phone"] = "+5511912345678"
# print(pessoa)

contatos = {
    "lukeskywalker@outlook.com": {
        "Nome": "Luke Skywalker", 
        "Telefone": "+551178945612",
        "Planeta": "Tatooine",
    },
    "anakinskywalker@gmail.com": {
        "Nome": "Anakin Skywalker", 
        "Telefone": "+551122065987",
        "Planeta": "Tatooine",
    },
    "leiaorgana@protonmail.com": {
        "Nome": "Leia Organa", 
        "Telefone": "+551178945612",
        "Planeta": "Alderaan",
    },
     
}

# for contato in contatos:
#     print(contato, contatos[contato])
    
# for chave, valor in contatos.items():
#     print(chave, valor)

#METODOS
# .clear(): Limpa todos os elementos do dicionário
# .copy(): Copia os elementos do dicionário 

#****ATENÇÃO****
# fromkeys(): cria chaves no dicionário
jedi = {
    "1":
        {"nome": "Yoda", 
         "idade": "900",
         "mestre": "Luke Skywalker"},
    "2":    
        {"nome": "ObiWan-Kenobi", 
         "idade": "57",
         "mestre": "Qui-Gon Jinn"}

}
jedi.fromkeys(["idade"])

#.get() # Outro método de acessar o dicionário
chave_inexistente = contatos["anakinskywalker@gmail.com"].get("Nave") # Retorna: None
chave_inexistente = contatos["anakinskywalker@gmail.com"].get("Nave",{}) # Retorna: O valor que passar de parametro
nome = contatos["lukeskywalker@outlook.com"].get("Nome", {}) #Se existe, retorna o valor da chave
# print(nome)

#.items() # Retorna uma lista de tuplas
items = jedi.items()

#.keys() #Retorna somente as chaves
# print(contatos.keys()) 

#.pop() #Remove o valor de uma chave
#Se não existir e estiver sem parametros, retorna erro
jedi.pop("sabre", {})
# print(jedi)
jedi.pop("idade", {})
# print(jedi)

#.popitem() # Remove os itens na sequencia do ultimo para o primeiro. 
# jedi.popitem()

#.setdefault() #inseri uma nova chave no dicionário, se existir ele não cria e mantém a existente sem alterar o valor
jedi["1"].setdefault("Cor do Sabre","verde")
jedi["1"].setdefault("mestre","N'Kata Del Gormo")

#.update() # Atualiza alguma informação do Dicionário.
# Atualiza os dados de uma chave existente:
jedi.update({"1":{"nome":"Yoda", "idade":"900", "mestre": "N'Kata Del Gormo"}})
#Adiciona um novo item se não existir a chave
jedi.update({"3":{"nome": "Luke Skywalker", "idade":"53", "mestre": "Yoda"}})

#.values() # Retorna todos valores das chaves

todos_jedi = jedi["1"].values()
# print(todos_jedi)
 
# in 

ejedi = "Yoda" in jedi["1"]["nome"]

# print(ejedi)

#del # DELETA O OBJETO INSERIDO

# print(contatos)
del(contatos["anakinskywalker@gmail.com"])
# print(contatos)
# print("   ")
del(contatos["lukeskywalker@outlook.com"]["Telefone"])
# print(contatos)

usuarios = {
            "1" : {
                "nome": "Lucas",
                "cpf": "41955640858",
                "data_de_nascimento": "27/04/2000",
                "endereco": {
                    "rua": "Augusto Durante",
                    "nro": "600", 
                    "bairro": "Perus",
                    "cidade": "SP"     
                }
            },
            "2" : {
                "nome": "Renato",
                "cpf": "51548791508",
                "data_de_nascimento": "17/12/1976",
                "endereco": {
                    "rua": "Augusto Durante",
                    "nro": "600", 
                    "bairro": "Perus",
                    "cidade": "SP"     
                }
            }
        }

for chave in usuarios.items("cpf"):
    print(chave)






