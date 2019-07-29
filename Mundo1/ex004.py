nome = input('Qual o seu nome: ')
print('Bem vindo {:^10}'.format(nome))

n1 = float(input('Digite o N1: '))
n2 = float(input('Digite o N2: '))

soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2

print('A soma é: {}'.format(soma))
print('A subtracao é: {}'.format(sub))
print('A divisao é: {:.3f}'.format(div))
print('A multiplicaoa é: {}'.format(mult))

