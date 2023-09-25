# 3. Imagine um sistema de gerenciamento de pedidos para um restaurante. Os pedidos dos clientes são
# colocados em uma fila e processados na ordem em que foram feitos. Use a classe de fila para
# gerenciar os pedidos e processá-los na ordem correta.

ordemPedidos = []
for c in range(5):
    pedido = str(f'Pedido {c + 1}')
    ordemPedidos.append(pedido)

for pedido in ordemPedidos:
    print(f'Entregando {pedido}')
