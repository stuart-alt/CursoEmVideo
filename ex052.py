# Primos

num = int(input('Digite um numero para verificar se é primo: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('É um numero primo.')
else:
    print('Não é um numero primo.')
