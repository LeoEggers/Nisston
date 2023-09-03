# 6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:

    def __init__(self, nome='caneta', preco=2.5, quantidade=10):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return round(self.preco * self.quantidade, 2)


produto1 = Produto()
print(f'Foram adquiridas {produto1.quantidade} {produto1.nome}s a R${produto1.preco:.2f} cada.\n'
      f'Valor final: R${produto1.calcular_total():.2f}')
