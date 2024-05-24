from os import system 

import platform as so


class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
    
    def limpar_tela(self, clear=True):
        if clear == True:
            if so.system()=="Linux":
                system("clear")
            elif so.system()=="Windows":
                system("cls")
    
    def mostrar_saldo(self):
        return self._saldo 
     
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self):
        self._saldo -= valor
    
    def __str__(self):
        return self._saldo
    
if __name__=="__main__":
    conta = Conta(100)
    # Jeito INCORRETO
    print(conta._saldo)
    
    conta.depositar(200)
    # Jeito CORRETO
    print(conta.mostrar_saldo())