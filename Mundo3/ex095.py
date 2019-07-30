# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários cadastro,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# https://www.youtube.com/watch?v=mw1So0r317Y&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=29

cadastro = list()
gols = list()
jogador = dict()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input("Nome do jogador: ")).title()
    partidas = int(input(f'Quantas partidas jogou {jogador["nome"]}: '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols no jogo {i + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    total = 0
    cadastro.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print("Resposta inválida. Responda com 'S' para continuar ou 'N' para sair.")
    if resp == 'N':
        break
print('-=' * 30)
#print('Cod.\tNome\t\tGols\t\tTotal')
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-=' * 30)
for pos, e in enumerate(cadastro):
    print(f'{pos:>3} ', end='')
    for v in e.values():
        print(f'{str(v):<20}', end='')
    print()

while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if opc == 999:
        break
    if opc >= len(cadastro):
        print('ERRO. Opção inválida. \nTente novamente.')
    else:
        print(f'Levantamento do jogador {cadastro[opc]["nome"]}:')
        for p, g in enumerate(cadastro[opc]["gols"]):
            print(f'\tNa partida {p + 1} ele fez {g} gols.')
        print('-' * 30)
print('FIM DO PROGRAMA')
