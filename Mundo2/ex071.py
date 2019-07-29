# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.

print('-'*30)
print('{:-^30}'.format('BANCO DO RATAO'))
print('-'*30)
valor = int(input('Digite o valor a ser sacado: '))
total = valor
ced = 100
totalced = 0

while True:
    if total >= ced:
        total = total - ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O caixa irá lhe dar {totalced} cédulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('FIM')
