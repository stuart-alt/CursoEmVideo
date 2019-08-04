def metade(n):
    metade = n / 2
    return metade


def dobro(n):
    dobro = n * 2
    return dobro


def aumPorc(n, p=10):
    valor = n + (n * (p / 100))
    return valor


def dimPorc(n, p=10):
    valor = n - (n * (p / 100))
    return valor


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
