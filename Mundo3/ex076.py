# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Arroz', 3.50,
         'Feijão', 4.29,
         'Batata', 1.99,
         'Couve', 0.99,
         'Café', 5.50,
         'Leite', 10.90,
         'Papel Higienico', 19.90)
print('-' * 39)
print(f'{"TABELA DE COMPRAS":-^39}')
print('-' * 39)
for pos in range(0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:_<30}', end='')
    else:
        print(f' R$ {lista[pos]:>5.2f}')
