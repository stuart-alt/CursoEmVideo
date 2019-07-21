# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 1 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.

from random import randint

cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m' }


nale = randint(1, 10)
numero = int(input('Digite um número entre 1 e 10: '))
contador = 1

while nale != numero:
    if nale > numero:
        print('Voce errou! O número é {}maior{}.'.format(cores['vermelho'], cores['limpa']))
        numero = int(input('Digite um número entre 1 e 10: '))
        contador += 1
    else:
        print('Voce errou! O número é {}menor{}.'.format(cores['azul'], cores['limpa']))
        numero = int(input('Digite um número entre 1 e 10: '))
        contador += 1
print('FIM')
print('Voce acertou na {}ª tentativa!'.format(contador))
