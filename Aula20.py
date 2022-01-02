# https://www.youtube.com/watch?v=ezfr9d7wd_k&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=30
# Aula sobre funções

def soma(a, b):
    print(f'A = {a}\nB = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


def contador(*num):
    total = len(num)
    print(f'Foram passados os valores {num}.\nSão {total} digitos no total.')


# Programa principal
soma(b=4, a=5)
contador(1, 3, 5, 2, 9)
