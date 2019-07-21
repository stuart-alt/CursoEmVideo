# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

if num1 == num2:
    print('Os numeros são iguais.')
elif num1 > num2:
    print('O primeiro número é maior que o segundo.')
else:
    print('O segundo numero é maior que o primeiro.')
