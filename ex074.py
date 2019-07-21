# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteio = [randint(0,99), randint(0,99), randint(0,99), randint(0,99), randint(0,99)]
print(f'Os numeros sorteados, foram: ', end='')
for i in sorteio:
    print(f'{i} ', end='')
print(f'\nO maior valor, é: {max(sorteio)}')
print(f'O menor valor, é: {min(sorteio)}')
