# 9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
# método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def forma_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 \
                and self.lado1 + self.lado3 > self.lado2 \
                and self.lado2 + self.lado3 > self.lado1:
            return True
        return False

    def calcular_perimetro(self):
        if self.forma_triangulo():
            return self.lado1 + self.lado2 + self.lado3
        return 'O objeto escolhido não é um triângulo.'


triangulo1 = Triangulo(3, 3, 3)
triangulo2 = Triangulo(1, 1, 10)
print(triangulo1.calcular_perimetro())
print(triangulo2.calcular_perimetro())
