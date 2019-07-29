# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo
# o total de gols feitos durante o campeonato.

cadastro = dict()
gols = list()
total = 0

cadastro['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input('Quantas partidas jogadas: '))
for i in range(0, partidas):
    gol = int(input(f'Quantos gols fez na {i}ª partida: '))
    total = total + gol
    gols.append(gol)
    cadastro['gols'] = gols[:]
cadastro['total'] = total
print('-=' * 15)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 15)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')

for p, i in enumerate(gols):
    print(f'\t => Na partida {p}, fez {i} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')
