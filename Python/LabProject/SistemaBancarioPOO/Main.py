from os import system
import platform as so
from datetime import datetime
from patlib import Path
import csv
from Cliente import *
from Contas import *
from Transacoes import *
from Historico import *



class Principal:  
    ROOT_PATH = Path(__file__).parent
        
    def registrar_log(self, funcao):
        try:
            with open(ROOT_PATH / "log" / "log.txt","a") as arquivo:
                nome_da_funcao = funcao().__name__
                arquivo.write(f"\n{datetime.utcnow()} {nome_da_funcao}")
        except IOError as error:
            print(f"\t{error}") 
        funcao()  
    
    @classmethod    
    def limpar_tela(cls, clear=True):
        if clear == True:
            if so.system() == "Windows":
                system("cls")
            else:
                system("clear")
        else:
            return None
    
    def main(self, clear=True):
        self.limpar_tela(clear)
        opcao = input("""
        [1] - LOGIN
        [2] - CADASTRO
        [0] - SAIR
        : """)
        while  opcao != "0":
            if opcao == "1":
                self.login()
            elif opcao == "2":
                self.cadastro_usuario()          
            elif opcao == "0":
                break
            else:
                self.main()

    @classmethod
    def menu(cls, cliente, conta=None, opcao_menu="-1", clear=True):
        cls.limpar_tela(clear)
        while True:
            if opcao_menu == "-1":
                print("""
        ======== MENU ========""")
                opcao_menu = input("""
        ENTRE COM UMA OPÇÃO:
        [1]: EXIBIR CONTAS
        [2]: CRIAR CONTAS
        [3]: TRANSAÇÕES
        [4]: EXTRATO
        [0]: SAIR
        : """) 
            
            # LISTAR CONTAS  
            elif opcao_menu == "1":
                cliente.listar_conta()
                cls.menu(cliente, conta, opcao_menu="-1", clear=False)
            # CRIAR CONTAS
            elif opcao_menu == "2":
                cls.limpar_tela()
                opcao_conta = input(f"""
        TIPO DE CONTA
        [1]: CONTA CORRENTE
        [2]: CONTA POUPANÇA
        [0]: VOLTAR
        : """)
                if opcao_conta == "1":
                    cls.limpar_tela()
                    conta = ContaCorrente(cliente=cliente)                    
                    conta.nova_conta(cliente=cliente)
                    cls.menu(cliente, conta, opcao_menu="-1", clear=False)
                elif opcao_conta == "2":
                    # conta = ContaPoupanca(cliente=cliente)                    
                    # conta.nova_conta(cliente=cliente,,tipo_de_conta=tipo_de_conta)
                    # cls.menu(cliente, conta, opcao_menu="-1", clear=False)
                    pass
                else: 
                    cls.menu(cliente, conta, opcao_menu="-1")
            
            # TRANSAÇÕES
            elif opcao_menu =="3":
                cls.limpar_tela()
                opcao_transacao = input("""
        QUAL OPERAÇÃO DESEJA REALIZAR?
        [1]: DEPÓSITO
        [2]: SAQUE
        [0]: VOTAR
        : """)
                cls.limpar_tela()
                # DEPÓSITO
                if opcao_transacao == "1":
                    isconta, conta_selecionada = cliente.selecionar_conta()
                    if isconta:
                        valor_da_transacao = float(input("""\tVALOR DA TRANSAÇÃO: """))
                        print(f"""\tOPERAÇÃO SELECIONADA: DEPÓSITO""")
                        cliente.realizar_transacao(conta_selecionada, Deposito(valor=valor_da_transacao))
                        cls.menu(cliente, conta, opcao_menu="-1", clear=False)
                    else:
                        print(conta_selecionada)
                        cls.menu(cliente, conta, opcao_menu="3", clear=False)
                # SAQUE
                elif opcao_transacao == "2":
                    isconta, conta_selecionada = cliente.selecionar_conta()
                    if isconta:
                        valor_da_transacao = float(input("""\tVALOR DA TRANSAÇÃO: """))
                        print(f"""\tOPERAÇÃO SELECIONADA: SAQUE""")
                        cliente.realizar_transacao(conta_selecionada, Saque(valor=valor_da_transacao))
                        cls.menu(cliente, conta, opcao_menu="-1")
                    else: 
                        print(conta_selecionada)
                        cls.menu(cliente, conta, opcao_menu="3") 
                # VOLTAR
                else:
                    cls.menu(cliente, conta, opcao_menu="-1")
            # EXTRATO                
            elif opcao_menu == "4":
                isconta, conta = cliente.selecionar_conta()
                if isconta:
                    conta.exibir_historico()
                    cls.menu(cliente, conta, clear=False)
                else:
                    print("\tNÃO EXISTE CONTA COM O NÚMERO DIGITADO")
                    cls.menu(cliente, conta, clear=False)
            # SAIR
            elif opcao_menu == "0":
                cls.limpar_tela(clear=True)
                print(f"""\tOBRIGADO POR SER NOSSO CLIENTE""")
                exit()
            else:
                cls.menu(cliente,conta)

    @registrar_log
    def login(self, clear=True):
        self.limpar_tela(clear)
        cliente_id = input("""
        CPF/CNPJ: """)
        tipo_de_cliente = self.validar_identificacao(cliente_id)
        if len(cliente_id) < 11 or len(cliente_id) >= 12:
            self.limpar_tela()
            print("""\tNÚMERO INCORRETO""")
            self.login(clear=False)
        usuario_existe = PessoaFisica.e_cliente(identificacao=cliente_id)
        if usuario_existe:
            cliente = self.info_user_login(cliente_id)
            conta = conta_existente(cls,cliente)
            self.menu(cliente=cliente,conta=conta)
        else:
            self.limpar_tela()
            opcao = input(f"""
        ID: {cliente_id}       
        ESTE {tipo_de_cliente} AINDA NÃO ESTÁ CADASTRADO
        DESEJA CRIAR UM NOVO USUÁRIO?
        [1] - SIM 
        [0] - NÃO
        : """)
            if opcao =="1":
                self.cadastro_usuario(tipo_de_cliente, cliente_id)
            else:
                self.main()
    
    @registrar_log
    def cadastro_usuario(self, tipo_de_cliente=None, cliente_id=None, clear=True):
        self.limpar_tela(clear)
        if tipo_de_cliente == "CPF":
            self.limpar_tela()
            try:
                cliente = self.info_user_cadastro(tipo_de_cliente="CPF", cliente_id=cliente_id)            
            except ValueError as error:
                print(f"\t{error}")
            else:
                self.limpar_tela()
                print("\tUSUARIO CRIADO COM SUCESSO\n\tOBRIGADO POR SER NOSSO CLIENTE")
                self.menu(cliente, clear=False)
        elif tipo_de_cliente =="CNPJ":
            try:
                cliente = self.info_user_cadastro(tipo_de_cliente="CNPJ", cliente_id=cliente_id)
            except ValueError as error:
                print(f"{error}")
            else:
                self.limpar_tela()
                print("\tUSUARIO CRIADO COM SUCESSO\n\tOBRIGADO POR SER NOSSO CLIENTE")
                self.menu(cliente, clear=False)
        elif tipo_de_cliente == None:
            cadastro = input("""
        CADASTRO DE
        [1] - PESSOA FISICA
        [2] - PESSOA JURÍDICA
        [0] - VOLTAR
        : """)     
            if cadastro == "1":
                self.limpar_tela()
                tipo_de_cliente = "CPF"
                try:
                    cliente = self.info_user_cadastro(tipo_de_cliente)
                    try: 
                        with open(ROOT_PATH / "data" / "usuario.csv", "w") as arquivo:
                            escritor = csv.writer(arquivo)
                            escritor.writerow(["cpf",{cliente.cpf}])
                    except IOError as error:
                        print(f"\t{error}")
                except ValueError as error:
                    print(f"{error}")
                else:
                    self.limpar_tela()
                    print("\tUSUARIO CRIADO COM SUCESSO\n\tOBRIGADO POR SER NOSSO CLIENTE")
                    self.menu(cliente, clear=False)
            
            elif cadastro == "2":
                self.limpar_tela()
                tipo_de_cliente = "CNPJ"
                try:
                    cliente = self.info_user_cadastro(tipo_de_cliente, cliente_id=cliente_id)
                except ValueError as error:
                    print(f"{error}")
                else:
                    self.limpar_tela()
                    print("\tUSUARIO CRIADO COM SUCESSO\n\tOBRIGADO POR SER NOSSO CLIENTE")
                    self.menu(cliente, clear=False)
                # cliente = PessoaJuridica()
                # self.menu(cliente, clear=False)
            else:
                self.main()
    
    @abstractmethod
    def info_user_cadastro(cls, tipo_de_cliente=None, cliente_id=None):
        if tipo_de_cliente == "CPF":   
            if cliente_id != None:
                cpf = cliente_id
            else:
                cpf = input(f"""\n\tCPF: """)
                tipo_de_cliente = cls.validar_identificacao(cpf)
                if len(cpf) < 11 or len(cpf) >= 12:
                    cls.limpar_tela()
                    print("""\tNÚMERO INCORRETO""")
                    cls.cadastro_usuario(tipo_de_cliente=tipo_de_cliente,clear=False)
            usuario_existe = PessoaFisica.e_cliente(cpf)
            if usuario_existe:
                raise ValueError("\tUSUARIO JA CADASTRADO NO SISTEMA")
            else:
                nome =  input("""\n\tNOME: """)
                data_de_nascimento = input("""\n\tDATA DE NASCIMENTO[DD/MM/AAAA]: """)
                rua = input(f"""\n\tLOGRADOURO: """)
                numero = input(f"""\n\tNº: """)
                bairro = input(f"""\n\tBAIRRO: """)
                cidade = input(f"""\n\tCIDADE: """)
                endereco = f"{rua}, {numero}, {bairro}, {cidade}"
                return PessoaFisica(cpf=cpf, nome=nome, data_de_nascimento=data_de_nascimento, endereco=endereco)
        elif tipo_de_cliente == "CNPJ":
            if cliente_id != None:
                cpnj = input(f"""\tCNPJ: """)
                if len(cpf) < 14 or len(cpf) >= 15:
                    cls.limpar_tela()
                    print("""\tNÚMERO INCORRETO""")
                    cls.cadastro_usuario(tipo_de_cliente=tipo_de_cliente,clear=False)
            else:
                cnpj = cliente_id
            # return PessoaJuridica()
    
    @classmethod
    def info_user_login(cls,cliente_id):
        for item in range(len(Cliente.clientes)):
            if cliente_id == Cliente.clientes[item]["_cpf"]:
                nome = cliente.clientes[item]["_nome"]
                data_de_nascimento = cliente.clientes[item]["_data_de_nascimento"]
                endereco = cliente.clientes[item]["_endereco"]
                contas = cliente.clientes[item]["_contas"]
                return PessoaFisica(cliente_id,nome,data_de_nascimento,endereco,contas)
            if len(cliente._contas) > 0:
                limite = cliente._contas[item]["_limite"]
                limite_de_saque = cliente._contas[item]["_limite_de_saque"]
                saldo = cliente._contas[item]["_saldo"]
                numero = cliente._contas[item]["_numero"]
                agencia = cliente._contas[item]["_agencia"]
                cliente = cliente              
                return ContaCorrente(limite, limite_de_saque, saldo, numero, agencia, cliente)
    
    # Função para identificar o tipo de identificação 
    @classmethod
    def validar_identificacao(self, identificacao):
        if len(identificacao) == 11:
            return "CPF"
        elif len(identificacao) == 14:
            return "CNPJ"
        else:
            return None

if __name__ == "__main__":
    principal = Principal()
    principal.main()