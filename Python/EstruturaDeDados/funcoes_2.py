
#? Função como parametro
def mensagem(nome):
    print("executando mensagem")
    return f"olá {nome}!"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"
    
def executar(funcao):
    print("executando executar")
    return funcao("Lucas")

#? Função dentro de função
def principal():
    print("Função Principal")
    
    def funcao_interna1():
        print ("Função 1")

    def funcao_interna2():
        print("Função 2")

    funcao_interna2()
    funcao_interna1()

#? Função retornando função 
operadores = ["+","-","*","/"]
def calculadora(operadores):
    def soma(x,y):
        return x+y

    def sub(x,y):
        return x-y

    def mul(x,y):
        return x*y

    def div(x,y):
        return x/y

    for operador in range(len(operadores)):
        match operadores[operador]:
            case "+":
                return soma
            case "-":
                return sub
            case "*":
                return mul
            case "/":
                return div
        

if __name__ == "__main__":
    for operador in operadores:
        print(calculadora(operador)(10,10))
    # print(calculadora("-"))
    # print(calculadora("*"))
    # print(calculadora("/"))