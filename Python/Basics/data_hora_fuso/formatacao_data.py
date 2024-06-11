from datetime import datetime, timedelta, date


d = datetime.now()
hoje = date.today()

#Formatando Data e hora
# print(d.strftime("%d/%m/%Y")) # 6/6/2024 11:36

date_string = "27/04/2024 17:30"

d = datetime.strptime(date_string, "%d/%m/%Y %H:%M") # 27/04/2024 17:30
# print(d)

data_hora_atual = datetime.now()
data_hora_str = "27/04/2024 17:30"
data_hora_str_en = "04/27/2024 17:30"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%m/%d/%Y %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))
print(datetime.strptime(data_hora_str_en, mascara_en))

# dia_de_nascimento = input('Qual a data do nascimento?[dd/mm/aaaa] ')

# dia_de_nascimento_datetime = datetime.strptime(dia_de_nascimento, "%d/%m/%Y")
# # dia_de_nascimento_date = date.strptime(dia_de_nascimento, "%d/%m/%Y")

# # fdia_de_nascimento_datetime = dia_de_nascimento_datetime.strftime("%d/%m/%Y")
# fdia_de_nascimento_date = dia_de_nascimento_date.strftime("%d/%m/%Y")

# idade = hoje - timedelta(dia_de_nascimento_date.year)
# # print(idade)
# print(f'seu aniversario é {fdia_de_nascimento_datetime}, sua idade é {idade}')

