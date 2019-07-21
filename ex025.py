# https://www.youtube.com/watch?v=WHWGz2Dy1ZU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=35
# Verifique se o nome tem 'Silva'

nome = str(input('Digite o seu nome completo: ')).strip()
x = nome.lower().find('silva')
print(nome[x:x+5] == 'silva')
