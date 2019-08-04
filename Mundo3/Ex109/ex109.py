#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from Ex109 import moeda as m
n = float(input(f'Digite o preço: '))
f = str(input('Deseja ver os valores formatados? [S/N] ')).upper()
if f in 'S':
    print(f'A metade de R$: {m.moeda(n)} é {(m.metade(n, True))}')
    print(f'O dobro de R$: {m.moeda(n)} é {m.dobro(n, True)}')
    print(f'Aumentando 10%, temos: {m.aumPorc(n, 10, True)}')
    print(f'Subtraindo 10%, temos: {m.dimPorc(n, 10, True)}')
else:
    print(f'A metade de {n} é {m.metade(n)}')
    print(f'O dobro de {n} é {m.dobro(n)}')
    print(f'Aumentando 10%, temos: {m.aumPorc(n)}')
    print(f'Subtraindo 10%, temos: {m.dimPorc(n)}')
