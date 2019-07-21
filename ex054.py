# Analise se 7 pessoas, atraves do ano de nascimento, são maiores de idade ou nao.
from datetime import date
atual = date.today().year
totalmaior: int = 0
totalmenor: int = 0

for pess in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('Total maior: {}'.format(totalmaior))
print('Total menor: {}'.format(totalmenor))
