# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.

cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m'}

num = int(input('Digite um numero: '))
print('''Digite a opção desejada:
[1] - Binario
[2] - Octal
[3] - Hexadecimal''')
opc = int(input('Digite a sua escolha: '))

if opc == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O número {} em octal é: {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O número {} em hexadeciaml é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção {} inválida! Tente novamente.'.format(opc))
