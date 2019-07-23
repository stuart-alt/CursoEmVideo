# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
i = 0
for c in range(0, 3):
    valor = int(input('Digite um valor: '))
    #for i, v in enumerate(lista):
    if c == 0:
        lista.append(valor)
    else:
        if valor < v:
            lista.insert(posicao - 1, valor)
        if valor > v:
            lista.insert(posicao + 1, valor)
    print(f'Posição: {i} \nNumero: {v}')
print(lista)
