# Fibonacci
print('-'*60)
qtd = int(input('Quantos numeros da sequencia voce quer imprimir: '))
print('~'* (6 * qtd))
i = 3
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
while i <= qtd:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print('FIM')
print('-'* (6 * qtd))
