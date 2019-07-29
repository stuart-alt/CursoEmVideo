total = 0
media = 0
maisvelho = 0
nomevelho = ''
maisnovo = 0
nomenovo = ''
contamulher = 0

for i in range(1, 6):
    print('------ {}ª PESSOA ------'.format(i))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    total = total + idade
    if sexo == 'M':
        if i == 1:
            maisnovo = idade
            nomenovo = nome
            maisvelho = idade
            nomevelho = nome
        else:
            if idade > maisvelho:
                maisvelho = idade
                nomevelho = nome
            if idade < maisnovo:
                maisnovo = idade
                nomenovo = nome
    else:
        if idade < 20:
            contamulher += 1
media = total / i
print('-=' * 30)
print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('Homem mais novo tem {} e se chama {}.'.format(maisnovo, nomenovo))
print('Homem mais velho tem {} e se chama {}.'.format(maisvelho, nomevelho))
print('Ao todo são {} mulhers com menos de 20 anos.'.format(contamulher))
print('-=' * 30)
