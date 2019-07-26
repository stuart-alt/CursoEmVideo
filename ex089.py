# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

cadastro = list()
aux = list()
i = 0
aluno = 0

while True:
    nome = str(input('Nome: ')).title().strip()
    aux.append(nome)
    nota1 = float(input('Nota 1: '))
    aux.append(nota1)
    nota2 = float(input('Nota 2: '))
    aux.append(nota2)
    cadastro.append(aux[:])
    aux.clear()
    resp = str(input('Quer adicionar outro aluno [S/N]: ')).lower().strip()[0]
    if resp in 'n':
        break
    i += 1
print('-=' * 15)
print('Nº\tNome\tMedia')
print('-' * 30)

for pos, val in enumerate(cadastro):
    media = (val[1] + val[2]) / 2
    print(f'{pos}\t{val[0]}\t{media:>.1f}')

while True:
    aluno = int(input('Deseja mostrar a nota de qual aluno: '))
    if aluno == 999:
        break
    print(f'As notas do aluno {cadastro[aluno][0]}, foram: {cadastro[aluno][1]} e {cadastro[aluno][2]}')
print('Fim do programa.')
