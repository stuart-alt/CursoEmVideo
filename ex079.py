lista = []
cont = 's'
while cont == 's':
    valor = int(input('Entre com um número inteiro: '))
    if valor in lista:
            print('Valor duplicado.')
    else:
        lista.append(valor)
    cont = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
print(f'Voce digitou os valores: {sorted(lista)}')
