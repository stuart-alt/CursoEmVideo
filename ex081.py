# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 's'

while cont == 's':
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
print(f'\n\nVoce digitou {len(lista)} elementos')
print(f'Os elemetos em ordem decrescente, são: {sorted(lista, reverse=True)}')
print(f'O valor 5 foi digitado.' if 5 in lista else 'O valor 5 NÃO foi digitado.')
