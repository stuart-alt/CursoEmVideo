print('===== 10 numeros de uma PA =====')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print(termo)
for c in range(1, 11):
    termo = termo + razao
    print('{}'.format(termo), end=' > ')
print("ACABOU")
