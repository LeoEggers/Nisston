# 5. Em um sistema de comércio eletrônico, os pedidos online são processados em uma fila. Implemente
# uma classe de fila que gerencie os pedidos online e processe-os na ordem de chegada.

ordemPedidos = []
for c in range(5):
    pedido = str(f'Pedido {c + 1}')
    ordemPedidos.append(pedido)

for pedido in ordemPedidos:
    print(f'Gerenciando {pedido}')
