# 7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:

    def __init__(self, marca='Volkswagen', modelo='Gol', ano=2023):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f'Marca: {self.marca}\n' \
               f'Modelo: {self.modelo}\n' \
               f'Ano: {self.ano}\n'


carro1 = Carro()
print(carro1.detalhes())
