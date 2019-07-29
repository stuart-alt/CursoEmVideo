from datetime import date
sexo = str(input('Digite o seu sexo (M) ou (F) : ')).strip().upper()
anoNas = int(input('Digite o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNas

if sexo == 'F':
    print('Voce nao precisa se alistar.')
else:
    if idade == 18:
        print('Voce deve se apresentar a junta militar imediatamentte!')
    elif idade <= 17:
        anosRest = 18 - idade
        print('Voce ainda tem {} ano(s). Ainda falta(m) {} ano(s) para você se apresentar.'.format(idade, anosRest))
    else:
        anoPas = idade - 18
        print('Voce já tem {} ano(s). Voce deveria ter se apresentado há {} ano(s)'.format(idade, anoPas))
