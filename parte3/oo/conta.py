class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.saldo, self.titular))

    def saca(self, valor):
        self.saldo -= valor
