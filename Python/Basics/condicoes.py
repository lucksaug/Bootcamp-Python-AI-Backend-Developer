class EstruturaCondicionais:   
    def __init__(self, idade, saldo, saque):
        self.idade = idade
        self.saldo = saldo
        self.saque = saque

    def e_maior(self):
        idade_especial = 12
        if self.idade >=18:
            print("Pode tirar carta")
        elif self.idade > idade_especial and self.idade < 18:
            print("Pode realizar as aulas teóricas")
        else:
            print("não pode tirar carta")
    
    def saque_conta(self):
        tipo_de_conta = "normal"
        cheque_especial = 450
        if tipo_de_conta == "normal":
            if self.saldo >= self.saque:
                print("Saque realizado com sucesso")
            elif (self.saldo + cheque_especial) < self.saque:
                print("Saldo realizado com uso do cheque especial!!")
            else:
                print("Saldo insulficiente!!")
        elif tipo_de_conta == "estudante":
            if self.saldo >= self.saque:
                print("Saque realizado com sucesso")
            elif self.saldo < self.saque:
                print("Saldo insulficiente!!")
        else:
            print("Não foi possível identificar o tipo de conta")
        
    def verifica_saldo(self):
        valor = f"Seu saldo atual é de: R${self.saldo:.2f}" if self.saldo > 0 else f"Seu saldo é de R${self.saldo:.2f} saldo insulficiente"
        print(valor)

if __name__ == "__main__":
    pessoa1 = EstruturaCondicionais(18, 200, 500)
    pessoa1.verifica_saldo()