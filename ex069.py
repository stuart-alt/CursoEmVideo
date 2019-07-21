titulo = 'cadastre uma pessoa'
maisdezoito = homens = mulhermenosvinte = 0

while True:
    print('-' * 30)
    print(f'{titulo:^30}'.upper())
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        maisdezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulhermenosvinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastrados {maisdezoito} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulhermenosvinte} mulher(es) com menos de 20 anos.')
print('-'*30)
print('FIM')
