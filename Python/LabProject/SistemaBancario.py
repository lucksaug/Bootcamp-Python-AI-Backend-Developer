import os
class Banco:
    def __init__(self):
        # Lista responsável para armazenar os depositos realizados.
        self.depositos = []
        # Lista responsável para armazenar os saques realizados.
        self.saques = []
        # Variável responsável por informar a quantidade de saques já realizados
        self.saques_realizados = 0
        #Saldo atual em conta.
        self.saldo_em_conta = 100.00
    #variável responsavél por armazenar quantos saques foram realizadas no dia 

    # Função responsável pela seleção da operação
    def menu(self):
        opcao = "-1"
        # Loop que pergunta qual a operação que o usuário deseja realizar, 
        # se for 0 ou qualquer outro número não listado o program é encerrado
        # Para cada opção uma função de cada operação é chamada.
        while opcao != "0":
            os.system("clear")
            opcao = input("""
        ENTRE COM UMA OPÇÃO:
        [1]: DEPOSITAR
        [2]: SACAR
        [3]: EXTRATO
        [0]: SAIR
        : """)
            # Opção 1 chama a função depositar()
            if opcao == "1":
                self.depositar()
                opcao = self.voltar_ao_menu()
            # Opção 2 chama a função sacar()
            elif opcao == "2":
                self.sacar()
                opcao = self.voltar_ao_menu()
            # Opção 3 chama a função extrato()
            elif opcao == "3":
                self.extrato()
                opcao = self.voltar_ao_menu()
            # Opção 0 finaliza a execução do programa
            elif opcao == "0":
                os.system("clear")
                print("OBRIGADO POR SER NOSSO CLIENTE")
            # Qualque outra entrada chama a função voltar_ao_menu
            else:
                opcao = self.voltar_ao_menu()

    # Função com lógica para voltar ao menu:
    def voltar_ao_menu(self):
        opcao = input("""    
        [1] - VOLTAR AO MENU
        [0] - SAIR
        :""")
        if opcao == "1":
            # Retorna o valor negativo para que o Loop não seja encerrado
            return "-1"
        else:
            return "0"

    # Função depositar para realizar um depósito
    def depositar(self):
        # Função do sistema(LINUX) para limpar o terminal e ter uma melhor visibilidade do programa
        # Para Windows utiliza-se
        #os.system("cls")
        os.system("clear")
        valor_deposito = float(input("QUAL É O VALOR DO DEPÓSITO: "))
        #verifica se o valor do depósito é positivo
        if valor_deposito > 0: 
            #Adiciona o valor de depósito na lista de depositos para um futuro extrato
            self.depositos.append(valor_deposito)
            self.saldo_em_conta += valor_deposito
            os.system("clear")

            print(f"""
        DEPÓSITO REALIZADO COM SUCESSO
        SALDO ATUAL: R${self.saldo_em_conta:.2f}""")

        #Se o valor for negativo, o programa retorna que não é possível realizar a operação    
        else:
            os.system("clear")
            print("""
        NÃO É POSSÍVEL FAZER O DEPÓSITO.""")

    # Função da operação de Saque
    def sacar(self):
        os.system("clear")
        #Verifica se ja foram realizadas 3 saques diários
        if self.saques_realizados < 3:
            # O usuário tem a opção de sacar o valor que deseja ou o limite de saque.
            opcao_de_saque = input(f"""
        [1] - INSIRA VALOR DE SAQUE
        [2] - SACAR LIMITE [LIMITE: R$500,00]
        : """)
            
            if opcao_de_saque == "1":
                valor_do_saque = float(input("ENTRE COM O VALOR DO SAQUE: "))
                # Verifica se o valor digitado está dentro do limite do saque
                if valor_do_saque <= 500:
                    # Verifica se há saldo em conta para efetuar o saque
                    if valor_do_saque <= self.saldo_em_conta:
                        self.saques_realizados += 1
                        self.saldo_em_conta -= valor_do_saque
                        self.saques.append(valor_do_saque)
                        os.system("clear")
                        print(f"""
        SALDO REALIZADO COM SUCESSO
        VALOR DO SAQUE R${valor_do_saque}
        SALDO ATUAL R${self.saldo_em_conta}""")
                    # Se o valor do saque for maior que o saldo em conta, retorna a mensagem de que o Saldo é inulficiente
                    elif valor_do_saque > self.saldo_em_conta:
                        os.system("clear")
                        print("""
        SALDO INSULFICIENTE""")
                # Se o valor digitado pelo usuário é maior que o limite, o sistema retorna para o menu
                elif valor_do_saque > 500:
                    os.system("clear")
                    print("""
        LIMITE DE SAQUE ATÉ R$500,00""")
            
            elif opcao_de_saque == "2":
                self.saques_realizados += 1
                self.saldo_em_conta -= 500
                self.saques.append(500.00)
                os.system("clear")
                print(f"""
        SALDO REALIZADO COM SUCESSO
        VALOR DO SAQUE R$500,00
        SALDO ATUAL R${self.saldo_em_conta}""")
        #Se o limite de saque diário é >= 3
        else:
            os.system("clear")
            print(f"""
        LIMITE DE SAQUE ATINGIDO {self.saques_realizados}/3""")
        
    # Função para verificar os extratos
    def extrato(self):
        os.system("clear")
        # O usuário pode escolher qual extrato ele vai verificar
        opcao_de_extrato = input("""
        Qual operação deseja verificar os extratos?
        [1] - DEPÓSITOS 
        [2] - SAQUES
        [3] - TODOS
        [0] - SAIR
        """)

        if opcao_de_extrato == "0":
            os.system("clear")
            print("""
        OBRIGADO POR SER NOSSO CLIENTE""") 
               
        elif opcao_de_extrato == "1":
            #Exibe somente os depósitos
            os.system("clear")
            # Variável local para impressão 
            extrato = " DEPÓSITO "
            # Verifica se há depósitos feitos durante a execução do programa
            if len(self.depositos) > 0:    
                print(f"""
        {extrato.center(20,"#")}""")
                # Loop para percorrer os valores da lista
                for deposito in self.depositos:
                    print(f"""
        R${deposito:.2f}""")
            # Caso não tiver extrato, o programa imprime "SEM NENHUM EXTRATO DE DEPÓSITO"
            else: 
                print(f"""
        SEM NENHUM EXTRATO DE {extrato.strip()}""")
            # Ao final de cada solicitação de extrato o programa exibe o saldo em conta
            print(f"""
        SALDO ATUAL: {self.saldo_em_conta}""")
        
        elif opcao_de_extrato =="2":
            #Exibe somente os saques
            extrato = " SAQUES "
            os.system("clear")
            if len(self.saques) > 0: 
                print(f"""{
        extrato.center(20,"#")}""")
                for saque in self.saques:
                    print(f"""
        R${saque:.2f}""")
            else:
                print(f"""
        SEM NENHUM EXTRATO DE {extrato.strip()}""")
            
            print(f"""
        SALDO ATUAL: {self.saldo_em_conta}""")
        
        elif opcao_de_extrato == "3":
            #Exibe saques e depósitos, 
            extrato = " DEPÓSITO "
            os.system("clear")
            print(f"""
        {extrato.center(20,"#")}""")
            if len(self.depositos) > 0:
                for deposito in self.depositos:
                    print(f"""
        R${deposito:.2f}""")
            else:
                print(f"""
        SEM NENHUM EXTRATO DE {extrato.strip()}""")
                
            extrato = " SAQUES "
            print(f"""
        {extrato.center(20,"#")}""")
            if len(self.saques) > 0:
                for saque in self.saques:
                    print(f"""
        R${saque:.2f}""")
            else:
               print(f"""
        SEM NENHUM EXTRATO DE {extrato.strip()}""") 
               
        print(f"""
        SALDO ATUAL: {self.saldo_em_conta}""")

# Condição para executar o programa.
if __name__ == "__main__":
    # Instancia da classe banco
    conta = Banco()
    # Chama a função "principal" da classe
    conta.menu()