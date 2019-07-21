# Digite o peso de 5 pessoas e mostre ao final, qual foi o maior e o menor.

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor  = peso
print('O maior peso: {}'.format(maior))
print('O menor peso: {}'.format(menor))
