class Aluno:
    def __init__(self, nome, sobrenome, endereco, media, situacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.media = media
        self.situacao = situacao


class Garrafa:
    def __init__(self, tamanho, cor, peso):
        self.tamanho = tamanho
        self.cor = cor
        self.peso = peso


aluno1 = Aluno('Rodrigo', 'Stuart', 'Rua Das Internets', 8.88, 'Aprovado')
garrafa1 = Garrafa(25, 'amarelo', 250)

print(aluno1.nome)
print(garrafa1.cor)
