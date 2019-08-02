# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o
# programa se encerrará. Importante: use cores.
from time import sleep

cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m' }


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'')
    print(f'{cores["amarelo"]}')
    help(comando)
    print(f'{cores["limpa"]}')
    sleep(1)


def titulo(msg):
    tam = len(msg) + 4
    print(f'{cores["azul"]}')
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)
    print(f'{cores["limpa"]}')
    sleep(1)


while True:
    titulo('PROGRAMA DE AJUDA DO PYTHON.')
    cmd = str(input(f'Função ou Biblioteca > '))
    if cmd.upper() == 'FIM':
        break
    else:
        ajuda(cmd)
titulo('ATÉ LOGO!')
