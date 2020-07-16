from filme import Filme
from playlist import Playlist
from serie import Serie

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme('Todo mundo em pânico', 1999, 100)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho do playlist: { playlist_fim_de_semana.tamanho }')
print(f'Tem o filme vingadores na lista? R: { vingadores in playlist_fim_de_semana }')
print(playlist_fim_de_semana[0])
