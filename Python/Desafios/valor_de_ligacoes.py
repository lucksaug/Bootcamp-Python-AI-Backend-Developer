class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        valor = self.plano.custo_chamada(int(duracao))
        saldo = self.plano.verificar_saldo()
        if valor <= saldo:
            self.plano.saldo = self.plano.deduzir_saldo(valor)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        valor = duracao * 0.1
        return valor

    def deduzir_saldo(self, valor_funcao):
        novo_saldo = self.saldo - valor_funcao
        return novo_saldo


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


"""
Rodrigo
(00) 90000-0000
10.00
(33) 93333-3333
60
"""

"""
Yule
(11) 91111-1111
30.00
(00) 90000-0000
240"""
nome = "Rodrigo"
numero = "(00) 90000-0000"
saldo_inicial = 10.00

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = "(33) 93333-3333"
duracao = "60"

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
