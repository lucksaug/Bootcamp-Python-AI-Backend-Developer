
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":

itens = []

# Insere items na lista
for x in range(3):
    item = input("Nome do Equipamento: ")
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
    