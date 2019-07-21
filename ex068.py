# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
from time import sleep

cont = 0
print('=------- Vamos jogar PAR OU impar -------=')

while True:
    numpc = randint(1, 10)
    numusuario = int(input('\nDigite a quantidade de dedos: '))
    opc = ' '
    while opc not in 'PI':
        opc = str(input('Escolha [Par ou Impar]: ')).upper().strip()[0]
    print('-='*25)
    print(f'Voce digitou o número {numusuario} e o computador jogou {numpc}')
    soma = numusuario + numpc
    if soma % 2 == 0:
        print(f'O total foi: {soma}. \n{soma} é um número PAR')
        if opc == 'P':
            cont += 1
            print('Voce ganhou!')
        if opc == 'I':
            print('Voce perdeu!')
            break
    else:
        print(f'O total foi: {soma}. \n{soma} é um número IMPAR')
        if opc == 'I':
            cont += 1
            print('Voce ganhou!')
        if opc == 'P':
            print('Voce perdeu!')
            break
    print('-=' * 25)
    print('Vamos jogar novamente')
    sleep(1)
print('\n')
print(f'Voce venceu {cont} vezes')
print(('FIM DO JOGO!'))
