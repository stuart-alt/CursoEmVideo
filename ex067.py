# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
i = 1
while True:
    print('-='*40)
    num = int(input('Digite o número para ver a tabuada dele: '))
    if num < 0:
        print('Saindo do programa...')
        break
    print('-=' * 40)
    for i in range(1, 11):
        print(f'{num} X {i} = {num * i}')
        i += 1
    print('-=' * 40)
    print('FIM DA TABUADA')
