# https://www.youtube.com/watch?v=xz2B3bfNjEk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=48

import modulos as m

m.menu("MENU PRINCIPAL")

while True:
    opc = int(input(f'\033[0;34mDigite a opção: \033[m'))
    if opc == 1:
        m.ler_arquivo()
    if opc == 2:
        m.escrever_arq()
    if opc == 9:
        break
m.mini_menu("FIM")
