from os import system
from random import randint, choice
system("clear")
# Remove os items repetidos
lista = [1,2,3,1,3,4]
lista_nova = set(lista)
# print(lista_nova)
# print (set("ABACAXI"))

# Só é possível acessar se o valor de set se estiver convertido 
lista_nova = list(lista_nova)
# print(lista_nova[0])

#É possivel percorrer o set
carros = ("fiat", "wolksvagem", "audi", "mercedez")
carros = set(carros)

# for carro in carros:
#     print(carro)
# ENUMERATE: numera os items
# for i, carro in enumerate(carros):
#     print(f"carro nº {i}: {carro}")

#Conjuntos Matemáricos:
numeros_pares = {i for i in range(0,10) if i%2==0}
numeros_impares = {i for i in range(0,10) if i%2!=0}
conjunto1 = {i for i in range(0,10,2)}
conjunto2 = {i for i in range(0,10)}

#União
uniao = numeros_pares.union(numeros_impares)
# print(numeros_pares)
# print(numeros_impares)
# print(uniao)

#Intersecção Tudo que tem em comun
# interseccao = conjunto1.intersection(conjunto2)

#Diferença, Tudo que não tem em comun
# diferenca = conjunto1.difference(conjunto2)

#Diferença simetrica, tudo que não é a intesecção
# diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)

#Subconjuntos
#Se o elemnto de um faz parte de outro
# subconjunto1 = conjunto1.issubset(conjunto2)
# subconjunto2 = conjunto2.issubset(conjunto1)

#Superconjuntos verifica se o elemento chamado está em qual chamou
# conjunto1 = {1,2,3}
# conjunto2 = {1,2,3,4,5,6,7,8,9}
# supconjunto1 = conjunto1.issuperset(conjunto2)
# supconjunto2 = conjunto2.issuperset(conjunto1)

#Disjunção: Verifica se um conjunto não é semelhante ao outro
# conjunto1 = {1,2,3,4,5,6}
# conjunto2 = {7,8,9,10}
conjunto_disjunto1 = conjunto1.isdisjoint(conjunto2)
conjunto_disjunto2 = conjunto2.isdisjoint(conjunto1)

# print(conjunto1)
# print(conjunto2)
# print(conjunto_disjunto1)
# print(conjunto_disjunto2)

# Add() adiciona na set se não houver
# print("ANTES")
# print(conjunto1)
conjunto1.add(3)
# print("DEPOIS")
# print(conjunto1)
conjunto1.add(3)

#.clear(): limpa
#.copy(): faz uma cópia
#.discard(numero): remove o item passado no parametro 
#.pop(): Tira o valor do COMEÇO
#remove(numero): remove o número indicado, somente se o número existir
#len(): tamanho do elemento
# in: verifica se o item esta no elemento
print(1 in conjunto1)