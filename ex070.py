# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
nomeloja = 'SUPER RATÃO'
print('-' * 30)
print('{:-^30}'.format(' SUPER RATAO '))
#print(f'{nomeloja:^30}')
print('-' * 30)
total = maismil = maisbarato = cont = 0
prodbarato = ''

while True:

    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))
    total += preco
    cont += 1
    if preco >= 1000:
        maismil += 1

    if cont == 1 or preco < maisbarato:
        prodbarato = produto
        maisbarato = preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total da compra: R$ {total:.2f}')
print(f'{maismil} produtos custam mais de mil reais.')
print(f'O {prodbarato} é o produto mais barato e custou R$ {maisbarato:.2f}')
