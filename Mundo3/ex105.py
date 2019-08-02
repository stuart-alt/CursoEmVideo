# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(* num, sit=False):
    """
    -> Programa que mostra a situação de um aluno, recebendo as notas.
    :param num: Podem ser passadas quantas notas forem necessarias.
    :param sit: True/False - Mostra ou não a situação do aluno.
    :return: O dicionário completo.
    """
    alunos = dict()
    total = maior = menor = media = 0

    for pos, val in enumerate(num):
        if pos == 0:
            maior = menor = val
        if val >= maior:
            maior = val
        if val <= menor:
            menor = val
        total += val
    media = total / len(num)
    alunos["total"] = len(num)
    alunos["maior"] = maior
    alunos["menor"] = menor
    alunos["media"] = media
    #print(media)
    if media <= 4:
        alunos["situacao"] = "Reprovado"
    if 4 <= media < 7:
        alunos["situacao"] = "Recuperacao"
    if media >= 7:
        alunos["situacao"] = "Aprovado"
    if sit == False:
        alunos.pop("situacao")
    return alunos

# Programa principal
resp = notas(9, 3, 5, 7, 10, 8, 4, sit=True)
print(resp)
#help(notas)
