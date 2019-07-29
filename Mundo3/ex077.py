# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('Arroz', 'Feijao', 'Batata', 'Cenoura', 'Cebola', 'Espinafre', 'Maracuja', 'Limao')

for palavra in lista:
    print(f'\nNa palavra {palavra.upper()}, temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
