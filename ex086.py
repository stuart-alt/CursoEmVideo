# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um número na posição: {l} {c}: '))
print('-' * 35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}] ', end='')
    print()
