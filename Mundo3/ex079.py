# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
cont = 's'
while cont == 's':
    valor = int(input('Entre com um número inteiro: '))
    if valor in lista:
        print('Valor duplicado.')
    else:
        lista.append(valor)
    cont = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
lista.sort()
print(f'Voce digitou os valores: {lista}')
