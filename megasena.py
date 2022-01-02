import random

escolhidos = list()
sorteados = list()
for n in range(6):
    escolhidos.append(int(input(f"N{n+1}: ")))
    sorteados.append(random.randint(1, 60))

escolhidos.sort()
sorteados.sort()

print(escolhidos, '\n', sorteados)

if escolhidos == sorteados:
    print("Acertou!")
else:
    print("Ma sorte")
