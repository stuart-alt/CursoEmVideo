pessoas = {'nome': 'Rodrigo', 'idade': 33, 'sexo': 'M', 'peso': 61.5}
pessoas['nome'] = 'Stuart'
pessoas['estadocivil'] = 'Solteiro'

print(f'Keys: {pessoas.keys()}')
print(f'Values: {pessoas.values()}')
print(f'Itens: {pessoas.items()}')
print(f'Pessoas: {pessoas}')

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado0 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado1 = {'uf': 'São Paulo', 'sigla': 'RJ'}
brasil.append(estado0)
brasil.append(estado1)

for estado in brasil:
    for k, v in estado.items():
        print(f'{v} ', end='')
    print()

estados = dict()
pais = list()
for c in range(0, 3):
    estados['uf'] = str(input('Estado: '))
    estados['sigla'] = str(input('Sigla: '))
    pais.append(estados.copy())
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print()
