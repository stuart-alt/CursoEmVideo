#help(open)
# arq_read = open('nomes.txt', 'r')
# O segundo parametro passado é o MODE, que pode ser:
# r = read
# w = write
# a = append (escreve no final do arquivo)
'''
Somente LEITURA
arq_read = open('nomes.txt', 'r')
print(arq_read.readable())   # True or false if file is readable
for nome in arq_read.readlines():
    print(nome)
arq_read.close()   # Good practices to close the file after reading it.
'''

'''
APPEND
arq_write = open('nomes.txt', 'a')
arq_write.write('\nYukitoshi Sato, 61')
arq_write.close()
'''

'''
ESCRITA
arq_write = open('nomes_1.txt', 'w')  # Ao usar o nome que não existe, o arquivo é criado.
arq_write.write('\nStuart, 33')
arq_write.close()
'''
