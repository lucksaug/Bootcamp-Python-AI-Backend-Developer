
#* timedelta, faz operações com data e hora
from datetime import datetime, timedelta, date, time


tipo_carro = 'P' #? P, M, G

tempo_p = 30
tempo_m = 45
tempo_g = 60 
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_p)
    print(f'O carro chegou as: {data_atual}\nficará pronto as: {data_estimada}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_m)
    print(f'O carro chegou as: {data_atual}\nficará pronto as: {data_estimada}')
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(days=tempo_g)
    print(f'O carro chegou as: {data_atual}\nficará pronto as: {data_estimada}')
    
print(date.today() - timedelta(days=1))

resultado = datetime(2024, 6, 3, 21, 8, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
