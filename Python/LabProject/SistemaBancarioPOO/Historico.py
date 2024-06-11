from Cliente import *
from Contas import *
from Transacoes import *


class Historico:
    _transacoes = []
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
    
    def gerar_relatorio(self, tipo_transacao=None):
        pass