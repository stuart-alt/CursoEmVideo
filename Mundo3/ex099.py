#numeros = [1, 5, 4, 6]
def calcMaior(* numeros):
    total = len(numeros)
    maior = 0
    print('-=' * 25)
    print('Analisando valores informados.')
    for n in numeros:
        print(f'{n} ', end='')
    print(f'Foram informados {total} valores ao todo.')
    for p, n in enumerate(numeros):
        if p == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print(f'O maior valor informado: {maior}')


calcMaior(1, 4, 7, 12)
calcMaior(-4, -9, -1, 0, 4, 7, 9)
calcMaior()