from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa mede: {:.2f}'.format(hypot(co, ca)))
