import re


numeros = """
(11)95880-7903
(11)95881-7900
(11)95945-1798
(11)93915-4817
"""
#             (     1  1       )   9   1111111212 
padrao = re.compile(r"(\(*[0-9]{2}\))9([0-9]{4})\-([0-9]{4})")
numero = "(11)95881-7903"
correspondencias = padrao.finditer(numeros)

def verificar_numero(padrao, numero):
    check = re.match(padrao, numero)
    if check:
        return "Número corresponde ao padrão"
if __name__ == "__main__":
    # print(verificar_numero(padrao, numeros))
    for correspondencia in correspondencias:
        print(correspondencia)


# telefone = "55(11)951482377"
# padrao = "([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# numero_formatado = "+{}{}{}-{}".format(
#             resposta.group(1),resposta.group(2),resposta.group(3),
#             resposta.group(4)
# )
# print(numero_formatado)