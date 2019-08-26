cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m' }


def menu(msg):
    mini_menu(f'{cores["vermelho"]}{msg:^30}{cores["limpa"]}')
    print(f'{cores["amarelo"]}1 - Ler arquivo{cores["limpa"]}')
    print(f'{cores["amarelo"]}2 - Adicionar cliente{cores["limpa"]}')
    print(f'{cores["amarelo"]}9 - Sair{cores["limpa"]}')


def mini_menu(msg, ler=False):
    print('-' * 30)
    print(f'{cores["amarelo"]}{msg:^30}{cores["limpa"]}')
    print('-' * 30)
    if ler:
        print(f'{cores["vermelho"]}{"NOME":<25}{cores["limpa"]}', end='')
        print(f'{cores["vermelho"]}{"IDADE":>5}{cores["limpa"]}')
        print('-' * 30)


def ler_arquivo():
    mini_menu('PESSOAS CADASTRADAS', True)
    arquivo_read = open('lista.txt', 'r')
    for dados in arquivo_read.readlines():
        for pos, x in enumerate(dados.split(',')):
            if pos == 0 or pos % 2 == 0:
                print(f'{x:<27}', end='')
            else:
                print(f'{x:>1}', end='')
    arquivo_read.close()


def escrever_arq():
    mini_menu('ESCREVA OS DADOS')
    arquivo_app = open('lista.txt', 'a')
    nome = str(input('Digite o nome do cliente: ')).title()
    idade = int(input('Digite a idade do cliente: '))
    arquivo_app.write(f'{nome}, {idade}\n')
    arquivo_app.close()
