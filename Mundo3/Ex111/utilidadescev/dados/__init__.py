# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
# capaz de funcionar como a função imputa(), mas com uma validação de dados para
# aceitar apenas valores que seja monetários.

def leiaDinheiro(n):
    valido = False
    while not valido:
        entrada = input('Digite o preço: R$ ').strip().replace(',' , '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO. \"{entrada}\" não é um valor válido.\033[m')
        else:
            valido = True
            return float(entrada)
