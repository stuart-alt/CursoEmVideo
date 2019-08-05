print('-' * 30)
print('SISTEMA DE CLIENTES'.center(30))
print('-' * 30)
print('1 - Ler arquivo')
print('2 - Adicionar cliente')
print('9 - Sair')

while True:
    opc = int(input('Digite a opção: '))
    if opc == 1:
        arquivo_read = open('lista.txt', 'r')
        for nomes in arquivo_read.readlines():
            print(nomes)
        arquivo_read.close()
    if opc == 2:
        arquivo_app = open('lista.txt', 'a')
        nome = str(input('Digite o nome do cliente: ')).title()
        idade = int(input('Digite a idade do cliente: '))
        arquivo_app.write(f'{nome}, {idade}')
        arquivo_app.close()
    if opc == 9:
        break
print("FIM")
