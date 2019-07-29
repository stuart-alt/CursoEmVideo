#Entre com o nome de 3 alunos e o programa irá sortear um aluno.
import random
aluno1 = input('Digite o nome do "aluno 1": ')
aluno2 = input('Digite o nome do "aluno 2": ')
aluno3 = input('Digite o nome do "aluno 3": ')

print('=' * 35)
print('O aluno escolhido foi: {}'.format(random.choice([aluno1, aluno2, aluno3])))