# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
#numeros = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
numeros = (int(input('Digite o valor: ')),
            int(input('Digite o valor: ')),
            int(input('Digite o valor: ')),
            int(input('Digite o valor: '))
           )
print(f'Os números digitados, foram: {numeros}')
print('Iniciando a análise...')
print('-=' * 20)
print(f'O Valor 9 foi digitado {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O valor 3 está na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares digitados, foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(f'{i} ', end='')
