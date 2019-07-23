# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
i = 0
while i < 2:
    valor = int(input('Digite um valor: '))
    for i, v in enumerate(lista):
        print(f'Posição: {i} \nNumero: {v}')
        if i == 0:
            lista.append(valor)
        '''else:
            if valor < numero:
                lista.insert(posicao - 1, valor)
            if valor > numero:
                lista.insert(posicao + 1, valor)'''
    i += 1
    lista.append(valor)
print(lista)
