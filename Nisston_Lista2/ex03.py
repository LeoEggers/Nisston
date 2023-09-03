# 3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
# chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:

    def __init__(self, base=2, altura=4):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


retangulo1 = Retangulo(4, 5)
print(retangulo1.calcular_area())
