# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do livro

class Livro:

    def __init__(self, titulo='Título', autor='Autor'):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        return f'Título: {self.titulo}\n' \
               f'Autor: {self.autor}'


livro1 = Livro("Viva o Povo Brasileiro", "João Ubaldo RIbeiro")
print(livro1.exibir_detalhes())
