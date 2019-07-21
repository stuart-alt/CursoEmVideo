# https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=34
# Crie um programa que peça ao usuario o nome da cidade onde ele nasceu. Indique 'True' se o nome começar com 'Santo'.

cidade = str(input('Digite o nome da cidade onde nasceu: ')).strip()
cidade = cidade.title()
primeiro = cidade.split()

print('=' * 30)
print('O primeiro nome da cidade é: {}'.format(primeiro[0]))
print('=' * 30)
print(cidade[:5] == 'Santo')
print('=' * 30)
