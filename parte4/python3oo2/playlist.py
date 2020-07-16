class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    def __getitem__(self, item):
        return self.__programas[item]

    @property
    def tamanho(self):
        return len(self.__programas)
