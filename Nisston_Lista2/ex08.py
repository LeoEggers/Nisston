# 8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
# “calcular_media” que retorna a média das notas do aluno.

class Aluno:

    def __init__(self, nome, *notas):
        self.nome = nome
        self.notas = list(notas)

    def calcular_media(self):
        if not self.notas:
            return 0
        return round(sum(self.notas) / len(self.notas), 2)

    def apresentar_media(self):
        return f'Nome: {self.nome}\n' \
               f'Média: {self.calcular_media():.2f}\n'


aluno1 = Aluno('João', 7.6, 8.5, 8.2)
aluno2 = Aluno('Carlos', 9.1, 7.0)
print(aluno1.apresentar_media())
print(aluno2.apresentar_media())
