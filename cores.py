# Forma 1
#nome = 'Rodrigo'
#print('Seu nome é: \033[7;30m{}\033[m'.format(nome))

# Forma 2
nome = 'Rodrigo'
cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m' }

print('Seu nome é: {}{}{}'.format(cores['cinza'], nome, cores['limpa']))

