# 1. Você está desenvolvendo um sistema de fila de impressão para uma empresa. Os documentos são
# adicionados à fila e impressos na ordem em que foram recebidos. Implemente um programa Python
# que use a classe de fila para simular esse processo.

ordemImpressao = []
for c in range(5):
    documento = str(f'Documento {c + 1}')
    ordemImpressao.append(documento)

for documento in ordemImpressao:
    print(f'Imprimindo {documento}')
    