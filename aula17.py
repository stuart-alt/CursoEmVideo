# https://www.youtube.com/watch?v=N1hTsbW50eM&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=9
# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis
# compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

n = [0, 1, 2, 3, 4, 5]

n.insert(1, 9)
x = 5
if x in n:
    n.remove(x)
    print(f'Valor {x} removido com sucesso.')
else:
    print(f'Valor {x} não encontrado.')


for c, v in enumerate(n):
    print(f'Na posição {c}, temos o valor {v}')
print('FIM')


compras = []
for i in range(0, 2):
    compras.append(str(input('Digite um item da lista de compras: ')))

for j in compras:
    print(f'Itens adicionados: {j}')

# Se voce fizer uma lista receber a outra, isso, na verdade, cria um link. Ex.:
a = [1, 2, 3, 4]
b = a
b[2] = 8  # Como as listas estão linkadas, irá alterar tanto 'a' quanto 'b'.
# Para resolver isso, voce deve copiar o valor de uma lista para outra, assim: b = a[:]
print(a)
print(b)
