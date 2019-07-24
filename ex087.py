# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = menor = 0

for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um número na posição: {l} {c}: '))
        if num[l][c] % 2 == 0:
            somapar = somapar + num[l][c]
        if c == 2:
            somacol = somacol + num[l][c]
        if l == 1 and c == 0:
            maior = menor = num[l][c]
        if l == 1 and num[l][c] > maior:
                maior = num[l][c]
        if l == 1 and num[l][c] < menor:
                menor = num[l][c]

print('-' * 35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}] ', end='')
    print()
print(f'A soma de todos os valores pares, é: {somapar}')
print(f'A soma de todos os valores da terceira coluna, é: {somacol}')
print(f'O menor e o maior número, respectivamente, é: {menor} | {maior}')
