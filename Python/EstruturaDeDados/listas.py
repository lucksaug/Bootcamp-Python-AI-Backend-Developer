from random import randint
from os import system
# Jeitos de criar uma lista
system("clear")
frutas = ["Laranja", "Maçã", "Pêra", "Uva"]
frutas[0] # Laranja
frutas[-1] # Uva
frutas[-3] # Maçã

frutas = []

letras = list("Python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000.00, 2020, 2900, "São Paulo", True]

# Lista aninhadas, MATRIZ

matriz = [
    [1,   "a",  2],
    ["b",  3,   4],
    [6,    5,  "c"]
]
matriz[0] # [1, "a", 2]
matriz[0][0] # [1]
matriz[0][-1] # [2]
matriz[-1][-1] # ["c"]

# Fatiamento
lista = ["p","y","t","h","o","n"]

# print (lista[2:]) # ["t","h","o","n"]
# print (lista[:2]) # ["p","y"]
# print (lista[1:3]) # ["y","t"]
# print (lista[0:3:2]) # ["p","t"]
# print (lista[::]) # ["p","y","t","h","o","n"]
# print (lista[::-1]) # ["n","o","h","t","y","p"]

numeros = []

for numero in range(8):
    numeros.append(randint(0,100))
#print (numeros)

pares = [numero for numero in numeros if numero %2 == 0]
impares = [numero for numero in numeros if numero %2 != 0]

quadrados = [numero ** 2 for numero in numeros]


# print (f"Esses são os pares:\n{pares}")
# print (f"Esses são os impares:\n{impares}")
# print (f"Esses são os quadrados:\n{quadrados}")

#MÉTODOS
lista = []

#Limpa a lista
lista.clear()
# print(lista)

#Adiciona elementos na lista
for numero in range(0,10):
    lista.append(randint(0,10))
# lista.append([1,2,3])
# print(lista)


#Copia a lista
lista2 = lista.copy()
# print(lista)
# print(lista2)

contagem = lista.count(1)
# print(contagem)

# Adiciona uma nova lista numa existente
lista.extend(["eu","sou","uma","nova","lista"])
#print(lista)

# Mostra qual a primeira ocorrencia do elemento na lista
# print(lista.index("eu"))

# remove o ultimo item inserido
lista.pop()
#print(lista)
# remove o elemento selecionado
lista.pop(0)
#print(lista)

# Também remove item da lista
lista.remove("eu")
#print(lista)
lista.clear()
for numero in range(0,10):
    lista.append(randint(0,10))
    
# print(lista)

# Ordena a lista
lista.sort()
#print(lista)

# reverte a lista
#lista.reverse() # Também é possível utilizar:
lista.sort(reverse=True)
#print(lista)

lista.clear()
lista = ["JAVA", "PYTHON", "GO", "JAVASCRIPT", "CSHARP", "C++", "BASH"]
# print(lista)

# Ordenação com condição 
# Ordena conforme o tamanho da string
#lista.sort(key=lambda x: len(x))

## Ordena conforme o tamanho da string (invertida)
lista.sort(key=lambda x: len(x), reverse=True)

# exibi qual o tamanho da lista
# print(len(lista))

#Outro mei de ordenar Listas:
ordenada = sorted(lista, key = lambda x: len(x), reverse = True)
print(lista)
print(ordenada)

