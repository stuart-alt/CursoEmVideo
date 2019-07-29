# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {'branco'   : '\033[0;30m',
         'vermelho' : '\033[0;31m',
         'verde'    : '\033[0;32m',
         'amarelo'  : '\033[0;33m',
         'azul'     : '\033[0;34m',
         'lilas'    : '\033[0;35m',
         'azulclaro': '\033[0;36m',
         'cinza'    : '\033[0;37m',
         'limpa'    : '\033[m'}


valImovel = float(input('Digite o valor do imovel (R$): '))
salario = float(input('Digite o valor do seu salario (R$): '))
anos = float(input('Digite em quantos nos quer pagar o imovel: '))

valPrest = valImovel / (anos * 12)

print('O valor da prestação é: R$ {}{:.2f}{}'.format(cores['azul'], valPrest, cores['limpa']))

if (valPrest >= (salario * 0.30)):
    print('{}Emprestimo negado!{}'.format(cores['vermelho'], cores['limpa']))
else:
    print('{}Emprestimo aprovado!{}'.format(cores['amarelo'], cores['limpa']))
