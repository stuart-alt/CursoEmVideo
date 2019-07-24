# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# Minha versão
'''num = []
for n in range(1, 8):
    num.append(int(input(f'Digite o {n}º valor: ')))
print(f'Os valores PARES digitados, foram: ', end='')
for n in sorted(num):
    if n % 2 == 0:
        print(f'{n} ', end='')
print('\nOs valores IMPARES digitados, foram: ', end='')
for n in sorted(num):
    if n % 2 == 1:
        print(f'{n}', end=' ')
'''

# Verao do Gustavo Guanabara
num = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os valores PARES, são: {num[0]}')
print(f'Os valores IMPARES, são: {num[1]}')
