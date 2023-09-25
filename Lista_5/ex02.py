# 2. Você está desenvolvendo um sistema de fila de atendimento para um banco. Os clientes entram na
# fila e são atendidos pelos funcionários na ordem de chegada. Use a classe de fila para simular o
# atendimento dos clientes.

ordemCliente = []
for c in range(5):
    cliente = str(f'Cliente {c + 1}')
    ordemCliente.append(cliente)

for cliente in ordemCliente:
    print(f'Atendendo {cliente}')
