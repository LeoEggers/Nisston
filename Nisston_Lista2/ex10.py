# 10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
# método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
# do funcionário

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento >= 0:
            self.salario += self.salario * (percentual_aumento / 100)
            return f"{self.nome} recebeu {percentual_aumento}% de aumento.\n" \
                   f"Salário atualizado para R${self.salario:.2f}"
        else:
            return "Percentual de aumento inválido. O aumento deve ser um número positivo."


funcionario1 = Funcionario("João", 3000, "Desenvolvedor")
print(funcionario1.aumentar_salario(10))
