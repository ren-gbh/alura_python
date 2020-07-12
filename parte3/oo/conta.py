class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    def deposita(self, valor):
        self.__saldo += valor

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.__saldo, self.__titular))

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
