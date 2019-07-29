# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = 0
cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'O total foi: {soma}.')
print(f'Voce digitou {cont} números.')
