#Entre com o nome de 3 alunos e o programa irá reordenar a lista de forma aleatória.
import random
aluno1 = input('Digite o nome do "aluno 1": ')
aluno2 = input('Digite o nome do "aluno 2": ')
aluno3 = input('Digite o nome do "aluno 3": ')

print('=' * 35)
lista = [aluno1, aluno2, aluno3]
random.shuffle(lista)
print('A nova lista: {}'.format(lista))
