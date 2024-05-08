class EstruturaRepeticao:    
    def __init__ (self):
        pass
    
    def exibir_numero(self):
        numero = int(input("Entre com um valor: "))
        for num in range(6):
            print(numero + num)
    
    def conta_vogais(self):
        vogais = "AEIOU"
        numero_de_vogais = 0
        palavra = input("Entre com uma palavra: ").upper()
        for letra in palavra:
            if letra in vogais:
                numero_de_vogais +=1
        print(numero_de_vogais)

    def exibir_tabuada(self):
        for num in range (0, 51, 5):
            print(num, end=" ")

    def repeticao_while(self):
        opcao = -1
        while opcao != 0:

            opcao = int(input(""" 
>>[2] SACAR           
>>[1] DEPOSITAR
>>[0] SAIR
>>..: """))
            if opcao == 2:
                print("Sacando...")
            elif opcao == 1: 
                print("Depositando...")
            
    def exibe_exceto(self):
        num = int(input("Entre com um numero que não quer que exiba: "))
        for i in range(100):
            if i == num:
                continue
            print(i,end=" ")

if __name__ == "__main__":
    primeiro= EstruturaRepeticao()
    primeiro.exibe_exceto()
