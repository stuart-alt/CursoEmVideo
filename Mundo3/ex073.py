# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato  Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro',
         'Athletico Paranaense', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense',
         'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama', 'Fortaleza', 'CSA', 'Avaí', 'Goiás')

print(f'Os 5 primeiros: {times[0:5]}')
print(f'Os 4 últimos: {times[-4:]}')
print(f'Em ordem alfábetica: {sorted(times)}')
print(f'Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
