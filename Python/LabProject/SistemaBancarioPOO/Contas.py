from Cliente import *
from Transacoes import *
from Historico import *
from abc import abstractmethod
from Main import Principal


class Conta:
    _saldo = 0.0 
    _agencia = "0001"
    
    def __init__(self, cliente=None, historico=None):
        self._cliente = cliente
        self._numero = len(cliente._contas) + 1
        self._historico = historico
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor:float) -> float:
        self._saldo = valor
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):
        self._numero = valor
    
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, valor):
        self._agencia = valor
        
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, valor):
        self._cliente = valor
    
    @property
    def historico(self):
        return self._historico
    
    @historico.setter
    def historico(self, valor):
        self._historico = valor
        
    @classmethod
    def conta_existente(cls, cliente):
        print(cliente._contas)
        # if cliente._contas.__name__ == "ContaCorrente":
            # for conta in range(len(cliente.contas)):
            #     if len(cliente._contas) > 0:
            #         limite = cliente._contas[conta]["_limite"]
            #         limite_de_saque = cliente._contas[conta]["_limite_de_saque"]
            #         saldo = cliente._contas[conta]["_saldo"]
            #         numero = cliente._contas[conta]["_numero"]
            #         agencia = cliente._contas[conta]["_agencia"]
            #         cliente = cliente              
            #         return ContaCorrente(limite, limite_de_saque, saldo, numero, agencia, cliente)
    
    @Principal.registrar_log
    def nova_conta(self, cliente):
        self.cliente = cliente
        self.historico = Historico()
        cliente.adicionar_conta(self)
    
    @Principal.registrar_log
    def depositar(self, valor:float):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return "\tNÃO FOI POSSÍVEL REALIZAR O DEPÓSITO, ACEITO SOMENTE VALORES POSITIVOS"
    
    @Principal.registrar_log
    def sacar(self, valor:float):
        if self.limite_de_saque < 3:
            if valor > 0 and valor <= self.limite:
                if valor <= self.saldo:
                    self.saldo -= valor
                    self.limite_de_saque += 1
                    print(f"\tSAQUE REALIZADO COM SUCESSO\nVALOR{valor}\nSALDO ATUAL{self.saldo}""")
                    return True
                else:
                    return "\tSALDO INSULFICIENTE"
            else:
                if valor <= 0:
                    return "\tNÃO É POSSÍVEL REALIZAR TRANSAÇÕES COM VALORES NEGATIVOS"
                elif valor >= self.limite:
                    return f"\tLIMITE MÁXIMO DE SAQUE R${self.limite}"
        else:
            return "\tLIMITE DE SAQUE DIÁRIO ALCANÇADO"
    
    def adicionar_historico(self, transacao):
        self.historico.adicionar_transacao(transacao=transacao)
    
    def exibir_historico(self):
        Principal.limpar_tela()
        print("""\t=======HISTÓRICO DE TRANSAÇÃO=======""")
        print(f"\tCONTA Nº: {self.numero}")
        if len(self.historico._transacoes) >= 1:
            for item in range(len(self.historico._transacoes)):
                tipo_de_operacao = type(self.historico._transacoes[item])
                # print(tipo_de_operacao)
                if str(tipo_de_operacao) == "<class 'Transacoes.Deposito'>":
                    print(f"""\tDEPÓSITO: +R${self.historico._transacoes[item].valor:.2f}""")
                elif str(tipo_de_operacao) == "<class 'Transacoes.Saque'>":
                    print(f"""\tSAQUE: -R${self.historico._transacoes[item].valor:.2f}""")
                    
                # {'DEPÓSITO: +'if type(self.historico._transacoes[item]) == "<class 'Transacoes.Deposito'>" } 
        else:
            print(f"""\tSEM HISTÓRICO DE TRANSAÇÕES PARA ESTA CONTA""")
        print(f"""\t\nSALDO ATUAL: {self.saldo:.2f}""")
            
class ContaCorrente(Conta):
    def __init__(self, limite=500.0, limite_de_saque=0, **kw):
        super().__init__(**kw)
        self._limite = limite
        self._limite_de_saque = limite_de_saque

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        self._limite = valor 
    
    @property
    def limite_de_saque(self):
        return self._limite_de_saque
    
    @limite_de_saque.setter
    def limite_de_saque(self, valor):
        self._limite_de_saque = valor
        
    @classmethod
    def conta_existente(cls,cliente):
        for item in range(len(cliente.contas)):
            if len(cliente.conta) > 0:
                limite = cliente._contas[item]["_limite"]
                limite_de_saque = cliente._contas[item]["_limite_de_saque"]
                saldo = cliente._contas[item]["_saldo"]
                numero = cliente._contas[item]["_numero"]
                agencia = cliente._contas[item]["_agencia"]
                cliente = cliente              
                return ContaCorrente(limite, limite_de_saque, saldo, numero, agencia, cliente)
            