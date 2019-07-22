# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0
posmenor = []
posmaior = []

for i in range(0, 4):
    valores.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] >= maior:
            maior = valores[i]
        if valores[i] <= menor:
            menor = valores[i]

print(f'O menor é {menor} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end='... ')
print()
print(f'O maior é {maior} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end='... ')
print('\nFIM')
