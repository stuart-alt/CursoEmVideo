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
    return f'{moeda}{n:>.2f}'.replace('.', ',')
