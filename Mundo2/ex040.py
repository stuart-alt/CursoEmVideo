# https://www.youtube.com/watch?v=QuWDyUeoaJs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=8
# Exercício Python 040: Crie um programa que leia duas notas de um aluno.
# Calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

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

materia = str(input('Digite o nome da materia: ')).strip().title()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
n3 = float(input('Digite a primeira nota: '))
n4 = float(input('Digite a primeira nota: '))
media = (n1 + n2 + n3+ n4) / 4

print('-' * 31)
print('Calculando a sua nota. Aguarde!')
print('-' * 31)
sleep(2)
if media >= 7:
    print('Na materia {}{}{}, sua media foi: {}{:.1f}{}'.format(cores['verde'], materia, cores['limpa'],\
                                                            cores['vermelho'], media, cores['limpa']))
    print('Voce foi APROVADO!')
elif (media <= 6.9) & (media >= 5):
    print('Na materia {}{}{}, sua media foi: {}{:.1f}{}'.format(cores['lilas'], materia, cores['limpa'],\
                                                            cores['vermelho'], media, cores['limpa']))
    print('Voce está de RECUPERAÇÃO')
else:
    print('Na materia {}{}{}, sua media foi: {}{:.1f}{}'.format(cores['lilas'], materia, cores['limpa'],\
                                                            cores['vermelho'], media, cores['limpa']))
    print('Voce foi REPROVADO!')
