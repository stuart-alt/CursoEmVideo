Exemplos de formtação:
print(f'Seu {nome}')
print(f'Seu {nome:20}') (imprime com 20 caracteres, padrão é espaço)
print(f'Seu {nome:-20}') (imprime com 20 caracteres usando - para preencher)
print(f'Seu {nome:^20}') (imprime com 20 caracteres e centraliza)
print(f'Seu {nome:<20}') (imprime com 20 caracteres e alinha a esquerda)
print(f'Seu {nome:>20}') (imprime com 20 caracteres e alinha a direita			)

05:10 - Fatiamento de String;
13:50 - Análise:
14:15 - len(); conta os caracteres da string
14:50 - count();
16:35 - find();
18:55 - in;
19:35 - Transformação:
19:55 - replace();
20:50 - upper();
21:50 - lower();
22:25 - capitalize(); Maiuscula somente a primeira letra
23:04 - title(); Maiuscula a primeira letra de cada palavra
24:34 - strip(); remove espaços desnecessarios no inicio e no final da string
25:08 - rtrip(); remover somente espaços ao final (right)
25:50 - lstrip(); remover somente espaços no inicio (left)
26:35 - Divisão:
  26:50 - split(); por padrão, usa o espaço para dividir
28:20 - Junção:
  28:35 - join(); junta as strings // '-'.join(frase)


Cores:
\033[   style ; text ; background m

\033[0;33;44m

Style:
0 - None
1 - Bold
4 - Underline
7 - Negative

Text:
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Lilas
36 - Azul claro
37 - Cinza

Background:
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Lilas
46 - Azul claro
47 - Cinza

TUPLA = ('Arroz', 'Feijao', 'Batata')

LISTA = ['Arroz', 'Feijao', 'Batata']
lista.append('Cookie')  # Adiciona o elemento ao final da lista
lista.insert(0, 'Cookie')  # Adiciona o elemento na posição 0

del lanche[3]  # Elimina a posição 3
lanche.pop()  # Elimina a última posição.
lanche.pop(3)  # Elimina a posição 3
lanche.remove('Batata')  # Elimina o elemento através do conteúdo e não pela posição.

valores = list(range(4, 11))  # Cria uma lista com os valores de 4 até 10.

valores = [8, 4, 2, 3, 5, 0]
valores.sort()  # Ordena os valores de 'valores'.
valores.sort(reverse=True)  # Ordena os valores de maneira invertida.

len(valores)  # Mostra quantos elementos tem na lista.

enumerate(valores)