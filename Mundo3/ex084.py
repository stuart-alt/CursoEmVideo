# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = []
dado = []
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    cadastro.append(dado[:])
    dado.clear()
    cont = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if cont in 'n':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi {maior}Kg e a(s) pessoa(a), são: ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}Kg e a(s) pessoa(s), são: ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
