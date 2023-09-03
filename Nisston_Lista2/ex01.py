# 1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
# “calcular_area” que retorna a área do círculo.

class Circulo:
    def __init__(self, raio=2):
        self.raio = raio

    def calcular_area(self):
        import math
        pi = math.pi
        area = pi * self.raio**2

        return area


circulo1 = Circulo(5)
print(circulo1.calcular_area())
