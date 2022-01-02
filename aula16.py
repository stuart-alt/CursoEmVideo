# TUPLAS SÃO IMUTAVEIS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche)

# Imprimir a última posição da varável:
print(lanche[-1])

# for cont in range(0, len(lanche)):
#    print(lanche[cont])

# print('\n\n')

for pos, comida in enumerate(lanche):
    print(pos, '-', comida)

# contar os elementos de uma tupla:
a = (1, 4, 5)
b = (5, 3, 1, 9)
c = a + b
print(c.count(5))
# mostrar a posição que está o elemento
print(c.index(3))  # Está na posição 4

# Apagar uma tupla
pessoa = ('Gustavo', 22, 'Solteiro', 'M')
del pessoa  # Apaga a tupla inteira. Não tem como apagar somente um elemento.
