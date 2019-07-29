# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
cont = 's'

while cont == 's':
    lista.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]

for pos, val in enumerate(lista):
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)
print(f'Voce digitou os números: {lista}')
print(f'Os valores pares, são: {pares}')
print(f'Os valores impares, são: {impares}')
