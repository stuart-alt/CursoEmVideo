from time import sleep
import os
for c in range(10, 0, -1):
    print(c)
    sleep(1)
    print('\n' * 100)
    #os.system('clear')   # Funcionaria executando pelo terminal do Linux.
print('FELIZ ANO NOVO!')