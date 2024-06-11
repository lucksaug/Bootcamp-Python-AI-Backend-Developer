from abc import ABC, abstractmethod, abstractproperty
from Cliente import *
from Contas import *
from Historico import *
from Main import Principal


class Transacao(ABC):
    @abstractmethod
    def registrar(conta):
        self


class Deposito(Transacao):
    def __init__(self, valor: float = 0.00):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @Principal.registrar_log
    def registrar(self, conta):
        depositar = conta.depositar(self.valor)
        if depositar == True:
            return (
                True,
                f"""
    DEPÓSITO REALIZADO COM SUCESSO
    CONTA Nº: {conta.numero}
    SALDO ATUAL R${conta.saldo:.2f}""",
            )
        else:
            return False, depositar


class Saque(Transacao):
    def __init__(self, valor: float = 0.0, **kw):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @Principal.registrar_log
    def registrar(self, conta):
        sacar = conta.sacar(self.valor)
        if sacar == True:
            Principal.limpar_tela()
            return (
                True,
                f"""
    SAQUE REALIZADO COM SUCESSO
    CONTA Nº: {conta.numero}
    SALDO ATUAL R${conta.saldo:.2f}""",
            )
        else:
            return False, sacar
