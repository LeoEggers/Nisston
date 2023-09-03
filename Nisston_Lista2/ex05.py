# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
# chamado “falar” que imprime uma mensagem com o nome da pessoa

class Pessoa:

    def __init__(self, nome='João', idade=30):
        self.nome = nome
        self.idade = idade

    def falar(self, msg=None):
        if msg is None:
            msg = f'Olá, meu nome é {self.nome}, eu tenho {self.idade} anos de idade.'
        return f'{self.nome} diz:\n— {msg}'


pessoa1 = Pessoa()
pessoa2 = Pessoa('Carlos', 25)
print(pessoa1.falar())
print(pessoa2.falar(f'Bom dia, {pessoa1.nome}!'))
