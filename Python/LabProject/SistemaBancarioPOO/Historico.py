from Cliente import *
from Contas import *
from Transacoes import *


class Historico:
    def __init__(self):
        self._transacoes = []
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
        