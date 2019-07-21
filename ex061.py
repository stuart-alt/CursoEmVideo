# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

razao = int(input('Digite a razão: '))
pa = int(input('Digite a PA: '))

i = 1
print('{}'.format(razao), end=' -> ')
while i < 10:
    razao += pa
    i += 1
    if i == 10:
        print('{}'.format(razao), end=' -> FIM')
    else:
        print('{}'.format(razao), end=' -> ')
