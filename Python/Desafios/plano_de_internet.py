
# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
    # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
    # TODO: Retorne o plano de internet adequado: 
      
#     - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

# Entrada 	Saída

# 10 - Plano Essencial Fibra - 50Mbps

# 19 - Plano Prata Fibra - 100Mbps

# 21 - Plano Premium Fibra - 300Mbps

def recomendar_plano(consumo:float):
  if consumo <= 10:
    return "Plano Essencial Fibra - 50Mbps"
  elif consumo > 10 and consumo <= 19:
    return "Plano Prata Fibra - 100Mbps"
  elif consumo > 19:
    return "Plano Premium Fibra - 300Mbps"
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
