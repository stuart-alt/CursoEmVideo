# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado. Se não informado, calcula fator de 1.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número 'n'.
    """
    total = 1
    for i in range(0, n):
        total *= n
        if show:  # O mesmo que: (if show  == True)
           print(f'{n} X ' if n > 1 else f'{n} = ', end='')
        n -= 1
    return total


# Programa principal
print('-=' * 15)
print(fatorial(3, show=True))
