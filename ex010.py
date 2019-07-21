#Carteira - https://www.youtube.com/watch?v=xM4AX3Lp2mo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=18
#Nesse exercicio, o usuario irá entrar com o valor em reais e a saída sera o valor convertido em dolares.
#Considere 1 dolar como R$ 3,85.

valor = float(input('Digite quanto tem na sua carteira: '))
dolar = valor / 3.85

print("Com R$ {:.2f} voce pode comprar USS$ {:.2f}".format(valor, dolar))
