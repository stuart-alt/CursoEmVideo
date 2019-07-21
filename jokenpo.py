from random import randint
from time import sleep

objetos = ('TESOURA', 'PEDRA', 'PAPEL')
opcomp = randint(0, 2)
cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m' }


print('''========= JOKENPO =========')
[ 0 ] = Tesoura
[ 1 ] = Pedra
[ 2 ] = Papel
===========================''')
opuser = int(input('Escolha o seu objeto: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
print('<=------------------=>')
print('Voce jogou: {}{}{}'.format(cores['azul'], objetos[opuser], cores['limpa']))
print('O computador jogou: {}{}{}'.format(cores['verde'], objetos[opcomp], cores['limpa']))
print('<=------------------=>')
if opuser == opcomp:
    print(cores['vermelho'], 'Empatou!', cores['limpa'])
elif opuser == 0 and opcomp == 1:  #tesoura e pedra
    print(cores['vermelho'], 'O computador ganhou!!!', cores['limpa'])
elif opuser == 0 and opcomp == 2:  #tesoura e papel
    print(cores['vermelho'], 'Voce ganhou!', cores['limpa'])
elif opuser == 1 and opcomp == 0:  #pedra e tesoura
    print(cores['vermelho'], 'Voce ganhou!', cores['limpa'])
elif opuser == 1 and opcomp == 2:  #pedra e papel
    print(cores['vermelho'], 'O computador ganhou!', cores['limpa'])
elif opuser == 2 and opcomp == 0:  #papel e tesoura
    print(cores['vermelho'], 'O computador ganhou!', cores['limpa'])
elif opuser == 2 and opcomp == 1:  #papel e pedra
    print(cores['vermelho'], 'Voce ganhou!', cores['limpa'])



