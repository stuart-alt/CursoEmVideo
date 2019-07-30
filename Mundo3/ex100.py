# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
numeros = []
def sorteia(lista):
    for i in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'Os valores sorteados, foram: {numeros}', end='')

def somaPar(valores):
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'\nA soma dos pares, é: {soma}')

sorteia(numeros)
somaPar(numeros)
