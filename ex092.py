# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com
# quantos anos a pessoa vai se aposentar.
#Ex: {'nome': 'Creuza', 'nasc': '1990', 'ctps': '44321', 'anocontra': '2015', 'salario': '3000'}

from datetime import date
ano = date.today().year
cadastro = dict()
while True:
    cadastro['nome'] = str(input('Nome: ')).title()
    anonasc = int(input('Ano de Nascimento: '))
    cadastro['idade'] = (ano - anonasc)
    cadastro['ctps'] = int(input('CTPS: '))
    if cadastro['ctps'] == 0:
        print('Saindo do programa.')
        break
    else:
        cadastro['anocontra'] = int(input('Ano de contratação: '))
        cadastro['aposentadoria'] = (65 - cadastro['idade'])
        cadastro['salario'] = float(input('Salário: '))
        break
print('-=' * 15)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
