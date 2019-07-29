cont = total = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    total = total + num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Voce digitou {} numeros e o total foi: {}'.format(cont, total))
