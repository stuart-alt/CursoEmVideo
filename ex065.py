# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

op = 's'
soma = cont = media = menor = maior = 0

while op in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    op = str(input('Quer continuar [S/N]: ')).lower().strip()[0]

media = soma / cont
print('Total: {}'.format(soma))
print('Media: {:.1f}'.format(media))
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))
print('FIM')
