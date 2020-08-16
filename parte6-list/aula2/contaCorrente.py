class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self.codigo, self.saldo)

    def deposita(self, valor):
        self.saldo += valor
