# 4. Você está criando um aplicativo de lista de tarefas pendentes. As tarefas são adicionadas à fila e
# concluídas uma por uma. Use a classe de fila para implementar a lista de tarefas e concluir as tarefas
# na ordem em que foram adicionadas.

ordemTarefas = []
for c in range(5):
    tarefa = str(f'Tarefa {c + 1}')
    ordemTarefas.append(tarefa)

for tarefa in ordemTarefas:
    print(f'Concluindo {tarefa}')
