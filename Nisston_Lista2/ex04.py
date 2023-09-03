# 4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:

    def __init__(self, saldo=0, titular="Titular"):
        self.saldo = saldo
        self.titular = titular

    def depositar(self):
        while True:
            valor_do_deposito = input('Digite o valor do depósito: ')
            try:
                valor_do_deposito_f = float(valor_do_deposito)
                if valor_do_deposito_f <= 0:
                    print('Valor inválido. Insira um número positivo.')
                else:
                    self.saldo += round(valor_do_deposito_f, 2)
                    return f'Operação realizada com sucesso.\n' \
                           f'Seu saldo: R${self.saldo:.2f}'
            except ValueError:
                print('Valor inválido, tente novamente.')

    def sacar(self):
        while True:
            valor_do_saque = input('Digite o valor do saque: ')
            try:
                valor_do_saque_f = float(valor_do_saque)
                if valor_do_saque_f <= 0:
                    print('Valor inválido. Insira um número positivo.')
                elif self.saldo < valor_do_saque_f:
                    print('Você não possui dinheiro suficiente. Tente novamente.')
                else:
                    self.saldo -= round(valor_do_saque_f, 2)
                    return f'Operação realizada com sucesso.\n' \
                           f'Seu saldo: R${self.saldo:.2f}\n' \
                           f'Seu saque: R${valor_do_saque_f:.2f}'
            except ValueError:
                print('Valor inválido, tente novamente.')


contabancaria1 = ContaBancaria()
print(contabancaria1.depositar())
print(contabancaria1.sacar())
