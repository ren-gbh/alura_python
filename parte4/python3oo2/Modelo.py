class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - '
      f'Ano: {vingadores.ano} - '
      f'Duração: {vingadores.duracao} - '
      f'Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta'
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - '
      f'Ano: {atlanta.ano} - '
      f'Temporadas: {atlanta.temporadas} - '
      f'Likes: {atlanta.likes}')