print('{:-^40}'.format(' Calculadora '))
total = float(input('Total da conta: '))
pes = int(input('Quantas pessoas: '))

total = total / pes

print(f'Cada pessoa irá pagar: R$ {total:.2f}')
semgarcom = total - (total * 0.10)
print(f'Sem a gorjeta: R$ {semgarcom:.2f}')
