#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from Ex108 import moeda as m
n = float(input(f'Digite o preço: '))
print(f'A metade de R$: {m.moeda(n)} é R$:{m.moeda(m.metade(n))}')
print(f'O dobro de R$: {m.moeda(n)} é R$:{m.moeda(m.dobro(n))}')
print(f'Aumentando 10%, temos: R${m.moeda(m.aumPorc(n))}')
print(f'Subtraindo 10%, temos: R${m.moeda(m.dimPorc(n))}')
