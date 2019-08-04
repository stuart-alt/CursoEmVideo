# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois
# módulos internos chamados moeda e dado. Transfira todas as funções utilizadas
# nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from Ex111.utilidadescev import moeda as m
from Ex111.utilidadescev import dados as d

n = d.leiaDinheiro(f'Digite o preço: R$ ')
m.resumo(n, 10, 6)
