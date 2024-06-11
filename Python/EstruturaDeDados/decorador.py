
# #? Decorando uma função
# # *def meu_decorador(funcao):
# # *    def envelope():
# # *        print('fazendo algo antes da função...')
# # *        funcao()
# # *        print('fazendo algo depois da função...')  
# # *    return envelope
# # *def funcao():
# # *    print ("processando função")
    
# #? Melhor jeito para implementar decoradores em python "Açúcar sintático"

# def meu_decorador(funcao):
#     def envelope():
#         print('fazendo algo antes da função...')
#         funcao()
#         print('fazendo algo depois da função...')  
#     return envelope

# @meu_decorador
# def funcao():
#     print ("processando função")

# #? Decoradores com parametros:
# def duplicar(funcao):
#     def envelope(*args, **kwargs):
#         funcao(*args, **kwargs)

#     return envelope

# @duplicar
# def aprender(tecnologia, linguagem):
#     print(f'Estou aprendendo {tecnologia}')
    
# #? Função decoradora retorna valor
# def minuscula_para_maiuscula(funcao):
#     def envelope(*args, **kwargs):
#         maiuscula = funcao(*args, **kwargs)
#         return maiuscula
    
#     return envelope

# @minuscula_para_maiuscula
# def letras_maiusculas(palavra):
#     return f'A palavra maiuscula é {palavra.upper()}'

# def teste_decorador(funcao):
#     def funcao_dentro_da_funcao():
#         print('ESSE É A EXECUÇÃO DA FUNÇÃO DENTRO DA FUNÇÃO')
#         return funcao_dentro_da_funcao
#     print('ESSE É A EXECUÇÃO DO DECORADOR')
#     texto = funcao_dentro_da_funcao
#     funcao(texto)

# @teste_decorador
# def imprimir(texto):
#     print(f'ESSA É A EXECUÇÃO DA FUNÇÃO "PRINCIPAL"')
#     print(texto())


def calculadora(func):
    def verificar(x, y):
        if x > 0 and y > 0:     
            return func(x,y)       
        else:
            raise ValueError('Não possivél realizar conta com números negativos')   
    return verificar           

@calculadora
def som(x, y):
    # operador = "+"
    return x + y

@calculadora
def sub(x, y):
    # operador = "-"
    return x + y

@calculadora
def mul(x, y):
    # operador = "*"
    return x * y    
    
@calculadora
def div(x, y):
    # operador = "/"
    return x / y


    
if __name__ == '__main__':
    try:
        print(sub(5,4))
    except ValueError as error:
        print(error)