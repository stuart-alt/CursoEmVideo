# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6),
             }
ranking = list()
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\n\t== RESULTADO ==\n')
for i, v in enumerate(ranking):
    print(f'\t{i+1}ª lugar: {v[0]} com {v[1]}.')
