from time import sleep

cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m'}

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
opc = '0'

while opc != 5:
    print(''' {}======== MENU DE OPÇÕES ========{} 
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa'''.format(cores['verde'], cores['limpa']))
    opc = int(input('Qual a sua opção: '))
    if opc == 1:
        total = n1 + n2
        print('O resultado da soma entre {} e {}, é: {}'.format(n1, n2, total))
        sleep(2)
    elif opc == 2:
        total = n1 * n2
        print('O produto entre {} e {}, é: {}'.format(n1, n2, total))
        sleep(2)
    elif opc == 3:
        if n1 == n2:
            print('Os números {} e {} são iuais!'.format(n1, n2))
            sleep(2)
        elif n1 > n2:
            print('O maior número, é: {}'.format(n1))
            sleep(2)
        else:
            print('O maior número, é: {}'.format(n2))
            sleep(2)
    elif opc == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
        sleep(2)
    elif opc == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-' * 30)
print('Fim do programa.')
