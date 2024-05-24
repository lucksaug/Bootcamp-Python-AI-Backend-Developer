from Contas import * 
from Transacoes import Deposito, Saque
from Main import Principal


class Cliente:
    def __init__(self, endereco=None):
        self._endereco = endereco
        self._contas:list = []
        
    @property
    def endereco(self):
        return self._endereco
        
    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor
                  
    def realizar_transacao(self, conta, transacao):
        isregistro, registro = transacao.registrar(conta=conta)
        if isregistro:
            conta.adicionar_historico(transacao)
            print(f"""{registro}""")
        else:
            Principal.limpar_tela()
            print(f"""{registro}""")
            
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        Principal.limpar_tela()
        print(f"""
        CONTA CRIADA COM SUCESSO:
        NUMERO: {conta.numero}
        AGENCIA: {conta.agencia}
        SALDO: R${conta.saldo:.2f}""")

    def listar_conta(self):
        Principal.limpar_tela()
        print(""" CONTAS """.center(35,"="))
        if len(self._contas) > 0:
            for item in range(len(self._contas)):
                print(f"""
        NÚMERO: {self._contas[item].numero}
        AGÊNCIA: {self._contas[item].agencia}
        SALDO: R${self._contas[item].saldo:.2f}
        """)
                print(f"{'=' * 35}")         
        else:
            tipo_de_conta = Principal.validar_identificacao(identificacao=self.cpf)
            opcao_listar_conta = input(f"""
        AINDA NÃO EXISTE UMA CONTA PARA ESSE {str(tipo_de_conta).upper()}
        DESEJA CRIAR UMA NOVA?
        [1] - SIM
        [0] - VOLTAR
        : """)
            if opcao_listar_conta == "1":
                conta = ContaCorrente(cliente=self)
                conta.nova_conta(cliente=self)
            else:
                Principal.menu(self)
            
    def selecionar_conta(self, clear=True):
        Principal.limpar_tela(clear)
        self.listar_conta()
        conta_selecionada = int(input("""
        QUAL CONTA DESEJA UTILIZAR
        Nº DA CONTA: """))
        self.listar_conta()
        for item in range(len(self._contas)):
            if self._contas[item].numero == conta_selecionada:
                Principal.limpar_tela()
                print(f"""\tCONTA SELECIONADA: {conta_selecionada}""")
                return True, self._contas[item]
            elif conta_selecionada > len(self._contas) or self._contas[item].numero <= 0:
                Principal.limpar_tela()
                return False, """\tCONTA SELECIONADA NÃO EXISTE"""
   
    
class PessoaFisica(Cliente):
    def __init__(self, cpf=None, nome=None, data_de_nascimento=None,**kw):
        self._cpf = cpf
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento
        super().__init__(**kw)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,valor):
        self._cpf = valor
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self,valor):
        self._data_de_nascimento = valor

    @abstractmethod
    def e_cliente(cls, identificacao):
        if cls.cpf == identificacao:
            return True
        else:
            return False
        