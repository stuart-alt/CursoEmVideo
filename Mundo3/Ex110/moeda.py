def metade(n, formato=False):
    metade = n / 2
    return metade if formato is False else moeda(metade)


def dobro(n, formato=False):
    dobro = n * 2
    return dobro if formato is False else moeda(dobro)


def aumPorc(n, p=10, formato=False):
    valor = n + (n * (p / 100))
    return valor if formato is False else moeda(valor)


def dimPorc(n, p=10, formato=False):
    valor = n - (n * (p / 100))
    return valor if formato is False else moeda(valor)


def moeda(n=0, moeda='R$'):
    return f'{moeda:<} {n:>6.2f}'.replace('.', ',')


def resumo(valor=0, a=0, d=0):
    print('-' * 31)
    print(f'{"RESUMO DO VALOR":^31}')  #'RESUMO DO VALOR'.center(31) também funciona.
    print('-' * 31)
    print(f'Preço analisado..: {moeda(valor):>12}')
    print(f'Metade do valor..: {metade(valor, True):>12}')
    print(f'Dobro do valor...: {dobro(valor, True):>12}')
    print(f'Aumentando {a:2}%...: {aumPorc(valor, a, True):>12}')
    print(f'Subtraindo {d:2}%...: {dimPorc(valor, d, True):>12}')
    print('-' * 31)
