# Palindromo
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]   # Inverte todas as letras lendo de tras para frente.

#for letra in range(len(junto) - 1, -1, -1):
#    inverso = inverso + junto[letra]
if inverso == junto:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')