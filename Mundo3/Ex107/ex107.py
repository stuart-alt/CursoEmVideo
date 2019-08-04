from Ex107 import moeda as m

n = float(input(f'Digite o preço: '))
print(f'A metade de R$: {n} é R$:{m.metade(n)}')
print(f'O dobro de R$: {n} é R$:{m.dobro(n)}')
print(f'Aumentando 10%, temos: R${m.aumPorc(n)}')
print(f'Subtraindo 10%, temos: R${m.dimPorc(n)}')
