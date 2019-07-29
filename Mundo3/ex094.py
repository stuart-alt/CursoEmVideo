# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
cadastro = list()
resp = 'S'
total = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite "F - Feminino" ou "M - Masculino".')
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa["idade"]
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite "S" para continuar ou "N" para sair.')
    if resp in 'N':
        break
media = total / len(cadastro)
print('-=' * 15)
print(f'O total de pessoas cadastras, foi: {len(cadastro)}')
print(f'A média de idade, foi: {media:.2f}')
print(f'As mulheres cadastradas, foram: ')
for p in cadastro:
    if p["sexo"] == 'F':
        print(f'-> {p["nome"]} ')
print()
print(f'As pessoas acima da média de idade, são: ')
for p in cadastro:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print("<< FIM DO PROGRAMA >>")
