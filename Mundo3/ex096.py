# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calcularArea(num1, num2):
    area = num1 * num2
    print(f'A área do terreno {num1}m X {num2}m é de {area}m².')


print('CONTROLE DE TERRENOS')
print('-=' * 15)
larg = float(input('Largura (m): '))
alt = float(input('Altura (m): '))
calcularArea(larg, alt)
