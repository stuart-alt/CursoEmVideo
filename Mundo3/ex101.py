# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
# uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(n):
    """
    Programa que ao receber o ano de nascimento, calcula a situação de votação:
    Com idade entre 16 e 17 anos, OPCIONAL.
    Acima de 18 anos, é obrigatório.
    :param n: recebe o ano de nascimento.
    :return: True
    """
    from datetime import date, datetime
    ano = date.today().year
    idade = ano - n
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos. VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos. VOTO NEGADO'


# Programa principal
nasc = int(input("Digite ano de nascimento: "))
print(voto(nasc))
