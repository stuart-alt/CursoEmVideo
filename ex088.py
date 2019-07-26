# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
print('-' * 30)
print(f'{"JOGO DA MEGASENA":-^30}')
print('-' * 30)
qtd = int(input('Quantos jogos voce quer que eu sorteie? '))
print()
for i in range(0, qtd):
    for n in range(0, 6):
        num = randint(1, 60)
        while num in lista:
            num = randint(1, 60)
        lista.append(num)
    sleep(1)
    print(f'O {i+1}º jogo sorteado, foi: {sorted(lista)}')
    lista.clear()
print(f'{"BOA SORTE":-^30}')
