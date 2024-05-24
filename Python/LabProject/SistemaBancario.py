# Biblioteca que traz o system, responsável pela execução de comandos no terminal
import os
# Biblioteca que traz o system, responsável por identificar 
import platform

# Classe principal 
class Principal:
    def __init__(self):
        # Lista de usuários
        self.usuarios = [
            [
                # CPF
                "49561237892",
                # NOME
                "Jake Harper",
                # DATA DE NASCIMENTO
                "30/02/2005",
                # ENDEREÇO
                [
                    # LOGRADOURO
                    "Av. do Estado",
                    # NÚMERO
                    12,
                    # BAIRRO
                    "Centro",
                    # CIDADE
                    "SP"
                ],
            ],
        ]
        # Lista de contas
        self.contas = [
            [
                #CPF #
                "49561237892",
                # Agência #1
                "0001",
                # Número da conta #2
                "1",
                #saldo na conta #3
                1000000.00,
                #Saques realizados no dia #4
                0
            ],
        ]
        # Variável responsável por informar a quantidade de saques já realizados
        self.saques_realizados = 0
        # Limite de valor por saque
        self.limite_de_saque = 500
        # Lista responsável para armazenar os depositos realizados.
        self.extratos = [
            [
                # Numero da Conta
                "1",
                [
                    # Depósito
                    "DEPÓSITO: + R$ 2000,00",
                    # Saque
                    "SAQUE: - R$ 300,00",
                ],
            ],
        ]
    
    # Função para limpar a tela quando necessario.
    def limpar_tela(self, clear=True):
        # Se clear for verdadeiro, limpará o terminal
        if clear == True:
            if platform.system() == "Windows":
                # Comando para Windows
                os.system("cls")
            else:
                # Comando para Linux
                os.system("clear")
        # Se for Falso, ele retorna None para que o programa continue
        else:
            return None

    # Função responsável pela seleção da operação
    def main(self, clear=True):
        self.limpar_tela(clear)
        opcao = input("""
        [1] - LOGIN
        [2] - SIGNIN
        [0] - SAIR
        : """)
        while  opcao != "0":
            if opcao == "1":
                self.login()
            elif opcao == "2":
                self.sigin()          
            else:
                self.main()
    
    # Função de menu que exibe possíveis caminhos no programa        
    def menu(self, cpf, clear=True):
        # Menu de entrada, possível criar uma conta, acessar uma conta existente e Criar um novo usuário
        self.limpar_tela(clear)
        opcao_menu = "-1"
        # Loop que pergunta qual a operação que o usuário deseja realizar, 
        # se for 0 ou qualquer outro número não listado o program é encerrado            
        while opcao_menu != "0":
            # Para cada opção uma função de cada operação é chamada.
            print("""
        ====== MENU ======""")
            opcao_menu = input("""
        ENTRE COM UMA OPÇÃO:
        [1]: LISTAR CONTAS
        [2]: CRIAR CONTAS
        [3]: DEPOSITAR
        [4]: SACAR
        [5]: EXTRATO
        [0]: SAIR
        : """)
                        
            # Opção 1 chama a função listar_conta()
            if opcao_menu == "1":
                self.listar_conta(cpf)
            
            # Opção 2 chama a função criar_conta()
            elif opcao_menu == "2":
                self.menu_conta(cpf, clear=True)
            
            # Opção 3 chama a função depositar()
            elif opcao_menu == "3":
                self.depositar(cpf)
            
            # Opção 4 chama a função sacar()
            elif opcao_menu == "4":
                self.sacar(cpf=cpf, clear=True, limite_de_saque=self.limite_de_saque)
            
            # Opção 5 chama a função extrato()
            elif opcao_menu == "5":
                self.exibir_extrato(cpf, clear=True)
            
            # Opção 0 finaliza a execução do programa
            elif opcao_menu == "0":
                self.limpar_tela(clear=True)
                print("""
        OBRIGADO POR SER NOSSO CLIENTE""")
                exit()
            
            # Qualque outra entrada chama a função voltar_ao_menu
            else:
                return None    
    
    # Função de entrar no menu se o usuário existir  
    def login(self, clear=True):
        self.limpar_tela(clear)
        # Aemazena o cpf inserido pelo usuário
        cpf = input("""
        CPF: """)
        # Verifica se o cpf inserido já está cadastrado
        usuario_existe = self.verificar_usuarios_existentes(cpf)
        # Se o usuário existe, é redirecionado para tela de menu
        if usuario_existe is True:
            self.menu(cpf)
        # Senão, pergunta se o usuário gostaria de se cadastrar.
        else:
            self.limpar_tela(clear)
            opcao = input("""
        ESTE CPF AINDA NÃO ESTÁ CADASTRADO
        DESEJA CRIAR UM NOVO USUÁRIO?
        [1] - SIM 
        [0] - NÃO
        : """)
            # Se sim, o usuário é redirecionado para a tela de cadastro(sigin)
            if opcao =="1":
                self.sigin(cpf)
            # Se não o usuário é redirecionado para a tela main para poder sair da aplicação 
            else:
                self.main(clear=True)
  
    # Função que cria uma um usuario
    def sigin(self, cpf="", clear=True):
        self.limpar_tela(clear)
        # Se o cpf não for inserido como parametro, não será necessario ao usuario entrar com o cpf novamente.
        if cpf == "":
            cpf = input(f"""
        CPF: """)
        opcao_sigin = "-1"
        # Variável armazena se o cpf está cadastrado ou não 
        usuario_existe = self.verificar_usuarios_existentes(cpf)
        
        # Se o usuário existe, ele redireciona para a tela de login
        if usuario_existe:
            self.limpar_tela(clear)
            print("""USUÁRIO JÁ CADASTRADO NO SISTEMA""") 
            #Pergunta se o usuário deseja tentar inserir o cpf novamente
            opcao_sigin = input("""
        DESEJA ENTRAR COM UM NOVO CPF?
        [1] - SIM
        [0] - VOLTAR
        : """) 
            if opcao_sigin == "1":
                self.limpar_tela()
                opcao_sigin = "0"
                return None
            elif opcao_sigin == "0":
                self.main(clear=True)
                    
                    
        # Variáveis de informação de usuário para serem armazenadas na lista global
        print(f"""
        CPF: {cpf}""")    
        # Insere os dados na lista
        self.usuarios.append([
                nome,
                cpf,
                data_de_nascimento,
                [
                    rua,
                    nro,
                    bairro,
                    cidade
                ]
            ])
        # Retorno visual positivo para o usuário
        self.limpar_tela()
        print("""
        USUARIO CRIADO COM SUCESSO
        OBRIGADO POR SER NOSSO CLIENTE""")
        # Ao final das operações, redireciona o usuário para o menu
        self.menu(cpf, clear=False)

    # Função  que verifica se um usuário está cadastrado          
    def verificar_usuarios_existentes(self, cpf):
        cpfs = []
        # Loop que adiciona o cpf à lista "cpfs" se houver um usuário na lista de cpfs global
        for usuario in range(len(self.usuarios)):
            # Condição para verificar se há um cpf na lista global.
            # Se tiver ele adiciona à lista local
            if cpf in self.usuarios[usuario][0]:
                cpfs.append(cpf)
        #Se houver o cpf na lista, é porque ja existe esse usuário no sistema, então retorno é verdadeiro
        if cpf in cpfs:
            return True
        else:
            return False

    # Função para verificar se há contas existentes com o cpf inserido no parametro                      
    def verificar_contas_existentes(self,cpf):
        contas_existentes = []
        # Loop que adiciona o cpf à lista "cpfs" se houver um usuário na lista de cpfs global
        for conta in range(len(self.contas)):
            # Condição para verificar se há um cpf na lista global.
            # Se tiver ele adiciona à lista local
            if cpf in self.contas[conta][0]:
                contas_existentes.append(cpf)
        #Se houver o cpf na lista, é porque ja existe esse usuário no sistema, então retorno é verdadeiro
        if cpf in contas_existentes:
            return True
        else:
            return False
   
    # Função para criar uma conta corrente
    def criar_conta(self, cpf, clear=True):
        # Número da agencia em string, para toda conta criada o nº será o mesmo
        agencia = "0001"
        self.limpar_tela(clear)
        opcao_criar_conta = input("""
        DESEJA CRIAR UMA NOVA CONTA?
        
        [1] - CRIAR CONTA
        [2] - LISTAR CONTAS
        [0] - VOLTAR
        : """)
        # Opção "1": cria uma conta automática
        if opcao_criar_conta == "1":
            # O calculo para o número da conta, será o tamanho da lista + 1 para não haver contas com o mesmo número.
            numero_da_conta =  str(len(self.contas) + 1)
            # Adiciona a lista de contas, uma lista contendo o CPF, Nº da agência, Nº da conta, Saldo de R$0,00, e o número de saques realizados no dia de 0(padrã).
            self.contas.append([cpf, agencia, numero_da_conta, 0, 0])
            # Adiciona à lista extrato, uma nova lista com o Nº da conta, e outra lista, que futuramente irá armazenar os valores de extrato (saque, depósito)
            self.extratos.append([numero_da_conta, []])
            self.limpar_tela(clear=True)
            # Retorna ao usuario se a operação foi realizada com sucesso e exibe ao usuário as informações de conta
            print("""
        CONTA CRIADA COM SUCESSO""")
            print(f"""
        DADOS DA CONTA: 
        AGÊNCIA: {agencia}, 
        NÚMERO DA CONTA: {numero_da_conta}""")
            # Redireciona para o Menu onde o usuário podera utilizar sua conta (sacar, depositar, verificar o extrato, etc...)
            self.menu(cpf, clear=False)
        #Opção "2": Os usuários poderão lista as contas existentes
        elif opcao_criar_conta == "2":
            self.listar_conta(cpf)
        # Volta à tela anterior
        else:
            self.limpar_tela()
            return None

    # Função de exibição quando chamar a função criar_conta() no menu()   
    def menu_conta(self, cpf, clear=True):
        self.limpar_tela(clear)
        # Verifica se há uma conta para o cpf 
        if self.verificar_contas_existentes(cpf):
            print("""
        JÁ TEM UMA CONTA COM ESSE CPF""")
            self.criar_conta(cpf, clear=False)
        else:
            self.criar_conta(cpf)
            
        # CPF DO USUARIO, AGENCIA, NUMERO DA CONTA
        # AGENCIA,[2]: CRIAR CONTAS
        # NUMERO DA CONTA,
    
    # Função que exibe contas de um determinado cpf
    def listar_conta(self, cpf, clear=True):
        self.limpar_tela(clear)
        # Lista para armazenar listas existentes para determinado cpf
        contas_existentes = []
        # Loop para percorrer a lista contas
        for conta in range(len(self.contas)):
            if cpf == self.contas[conta][0]:
                # armazena cada informação em uma variavel
                numero_agencia = self.contas[conta][1]
                numero_conta = self.contas[conta][2]
                saldo = f"{self.contas[conta][3]:.2f}"
                # Adiciona as informações na lista de contas local
                contas_existentes.append([numero_agencia,numero_conta,saldo])
        # Se existe alguma conta (se o tamanho é maior que 0)
        if len(contas_existentes) > 0:
            print("""
        ======CONTAS DISPONÍVEIS=======""")
            # Loop para imprimir os detalhes de cada conta 
            for conta in range(len(contas_existentes)):
                print(f"""
        NUMERO DA AGENCIA {contas_existentes[conta][0]}
        NUMERO DA CONTA {contas_existentes[conta][1]}
        SALDO EM CONTA {contas_existentes[conta][2]}
        """, end=f"{"="*30}".strip("%"))
        # Se não existir nenhuma conta, programa retorna ao usuário a possibilidade de criar uma nova conta
        else:
            opcao_listar_contas = input("""
        AINDA NENHUMA CONTA CRIADA
        DESEJA CRIAR UMA CONTA?
        [1] - SIM
        [0] - VOLTAR
        : """)
            if opcao_listar_contas == "1":
                self.criar_conta(cpf)
            else:
                self.menu(cpf)
    
    # Função para escolher uma conta em que será manipulada
    def selecionar_conta(self, cpf, clear=True):
        # Lista para guardar o número da conta
        contas_existentes = []
        for conta in range(len(self.contas)):
            # Somente adiciona a conta com o cpf do usuário
            if cpf == self.contas[conta][0]:
                contas_existentes.append(self.contas[conta][2])
        # Exibe as contas do usuário para que possa escolher
        self.listar_conta(cpf,clear)
        # Armazwna o número da conta que o Usuário escolher após a lista de contas no seu cpf
        opcao_selecionar_conta = input("""
        QUAL CONTA DESEJA UTILIZAR?
        Nº DA CONTA: """)
        # Verifica se a conta inserida existe no sistema
        if opcao_selecionar_conta in contas_existentes:
            return opcao_selecionar_conta
        # Se não houver, programa retorna que a conta não existe e pede para selecionar denovo chamando a mesma função
        else: 
            self.limpar_tela()
            print("""
        CONTA NÃO LISTADA NO SISTEMA""")
            self.selecionar_conta(cpf, clear = False)

    # Função depositar para realizar um depósito (POSITION ONLY)
    def depositar(self, cpf, clear=True, /):
        # Pergunta qual a conta em que o usuário deseja realizar a operação
        conta_selecionada = self.selecionar_conta(cpf, clear)
        self.limpar_tela()
        # Armazena o valor do depósito digitado pelo usuário
        valor_deposito = float(input("""
        QUAL É O VALOR DO DEPÓSITO: """))
        #verifica se o valor do depósito é positivo
        if valor_deposito > 0: 
            #Adiciona o valor de depósito na lista de depositos para um futuro extrato
            for conta in range(len(self.contas)):
                #Encontra a conta correspondente ao cpf e ao número da conta
                if cpf == self.contas[conta][0] and conta_selecionada == self.contas[conta][2]:
                    valor_extrato = f"DEPÓSITO: + {valor_deposito:.2f}"
                    # Armazena o valor do extrato na lista de extratos
                    self.inserir_extrato(conta, valor_extrato)
                    # Atualiza o saldo em conta
                    saldo = self.contas[conta][3] + valor_deposito
                    self.contas[conta][3] = saldo
                    self.limpar_tela()
                    print(f"""
        DEPÓSITO REALIZADO COM SUCESSO
        SALDO ATUAL: R${self.contas[conta][3]:.2f}""")
            self.menu(cpf, clear=False)
        #Se o valor for negativo, o programa retorna que não é possível realizar a operação    
        else:
            self.limpar_tela()
            print("""
        NÃO É POSSÍVEL FAZER O DEPÓSITO DE VALORES NEGATIVOS""")
            self.depositar(cpf, False)
            
    # Função da operação de Saque (KEYWORD ONLY)
    def sacar(self, *, cpf, clear=True, limite_de_saque):
        # Pergunta e armazen o número da conta que o usuário deseja realizar a operação
        conta_selecionada = self.selecionar_conta(cpf, clear)
        self.limpar_tela()
        # Percorre a lista contas
        for conta in range(len(self.contas)):
            # Encontra a conta correspondente a do cpf do usuário
            # E 
            # encontra a conta correspondente da variavél conta_selecionada
            if cpf == self.contas[conta][0] and conta_selecionada == self.contas[conta][2]:
                #Verifica se ja foram realizadas 3 saques diários
                if self.contas[conta][4] < 3:
                    # O usuário tem a opção de sacar o valor que deseja ou o limite de saque.
                    opcao_de_saque = input(f"""
        [1] - INSIRA VALOR DE SAQUE
        [2] - SACAR LIMITE [LIMITE: R${self.limite_de_saque:.2f}]
        : """)
                    # Opção "1" permite o usuário a inserir o valor que deseja, sendo o mesmo <= que o limite de saque
                    if opcao_de_saque == "1":
                        # Armazena o valor inserido pelo usuário
                        valor_do_saque = float(input("""
        ENTRE COM O VALOR DO SAQUE: """))
                        # Verifica se o valor digitado está dentro do limite do saque
                        if valor_do_saque <= self.limite_de_saque:
                            # Verifica se há saldo em conta para efetuar o saque
                            if valor_do_saque <= self.contas[conta][3]:
                                # Adiciona +1 no saques diários realizados
                                self.contas[conta][4] += 1
                                # Tira o valor do saque do saldo do usuário
                                self.contas[conta][3] -= valor_do_saque
                                # Armazena o valor do extrato para ser insirido na lista de extratos
                                valor_extrato = f"SAQUE: -{valor_do_saque}"
                                # Chama a função para armazenar o valor do extrato na lista de extratos
                                self.inserir_extrato(conta_selecionada,valor_extrato)
                                self.limpar_tela()
                                # Retorno de operação bem sucedida para o usuário
                                print(f"""
        SALDO REALIZADO COM SUCESSO
        VALOR DO SAQUE R${valor_do_saque}
        SALDO ATUAL R${self.contas[conta][3]:.2f}""")
                            # Se o valor do saque for maior que o saldo em conta, retorna a mensagem de que o Saldo é inulficiente
                            elif valor_do_saque > contas[conta][3]:
                                self.limpar_tela()
                                # Retorno de operação mal sucedida para o usuário
                                print(f"""
        SALDO INSULFICIENTE
        SALDO ATUAL: R$ {self.contas[conta][3]:.2f}""")
                        # Se o valor digitado pelo usuário é maior que o limite, o sistema retorna para o menu
                        elif valor_do_saque > self.limite_de_saque:
                            self.limpar_tela()
                            print(f"""
        LIMITE DE SAQUE ATÉ R${self.limite_de_saque:.2f}""")
                    # Opção "2" permite que o usuário saque o limite de saque sem precisar inserir valor.
                    elif opcao_de_saque == "2":
                        self.contas[conta][4] += 1
                        self.contas[conta][3] -= self.limite_de_saque
                        valor_extrato = f"SAQUE: -{self.limite_de_saque:.2f}"
                        self.inserir_extrato(conta_selecionada, valor_extrato)
                        self.limpar_tela()
                        print(f"""
        SALDO REALIZADO COM SUCESSO
        VALOR DO SAQUE R$ {self.limite_de_saque:.2f}
        SALDO ATUAL R${self.contas[conta][3]:.2f}""")
                    else: 
                        self.sacar(cpf=cpf, limite_de_saque=self.limite_de_saque)
                #Se o limite de saque diário é >= 3
                else:
                    self.limpar_tela()
                    print(f"""
        LIMITE DE SAQUE ATINGIDO {self.contas[conta][4]}/3""")
    
    #Função para inserir um extrato na lista de extratos
    def inserir_extrato(self, numero_da_conta,valor:str):
        # Loop que percorre a lista extratos
        for conta in range(len(self.extratos)):
            # Verifica se o numero da conta corresponde ao mesmo a conta, para inserir o valor na conta correspondente a operação
            if numero_da_conta == self.extratos[conta][0]:
                #insere o valor como uma lista para facilitar na leitura posterior na lista extratos
                self.extratos[conta].append([valor])
        
    # Função para verificar os extratos
    def exibir_extrato(self, cpf, /,*,clear=True):
        # Recebe o valor da função selecionar conta (Numero da conta)
        conta_selecionada = self.selecionar_conta(cpf, clear)
        self.limpar_tela()
        # Loop para verificar a lista de extratos 
        for extrato in range(len(self.extratos)):
            print("""
        ====== EXTRATO ======""") 
            # Verifica se a conta selecionada corresponde ao exato número da lista de extratos 
            # E
            # verfica se o tamanho da lista encontrada é maior > 0
            if conta_selecionada == self.extratos[extrato][0] and len(self.extratos[extrato][1]) > 0:
                # Loop para percorrer a lista de extratos na posição onde os valores são armazenados
                for item in range(len(self.extratos[extrato][1])):
                    print(f"""
        {self.extratos[extrato][1][item]}""")
            # Se não houver item na lista o programa imprime que não há extratos para essa conta
            else:
                print(f"""
        SEM EXTRATOS NESSA CONTA""")
            # Loop para percorrer a lista contas, para acessar o saldo em conta
            for conta in range(len(self.contas)):
                # verifica se a conta em questão pertence ao mesmo usuário que está acessando essa conta
                # E
                # verifica se os dados da conta na variavel conta_selecionada
                if cpf == self.contas[conta][0] and conta_selecionada == self.contas[conta][2]:
                    print(f"""
        SALDO EM CONTA: {self.contas[conta][3]:.2f}""")
            # Após exibir todos os dados, O loop é encerrado
            break




# Condição para executar o programa.
if __name__ == "__main__":
    # Instancia da classe banco
    conta = Banco()
    # # Chama a função "principal" da classe
    conta.main()