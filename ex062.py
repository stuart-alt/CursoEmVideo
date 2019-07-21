# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro numero: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
i = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while i <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        i = i + 1
    print('Pausa')
    mais = int(input('Quantos mais: '))
print('Progressao finalizada com {} termos.'.format(total))
