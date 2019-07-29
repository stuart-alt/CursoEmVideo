# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = dict()
alunos['nome'] = str(input('Nome: ')).title()
alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))
print('-=' * 20)
if alunos['media'] >= 7:
    alunos["situacao"] = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    alunos["situacao"] = 'Recuperação'
else:
    alunos["situacao"] = 'Reprovado'
print('-=' * 20)
for k, v in alunos.items():
    print(f'\t-{k} é igual a {v}.')
