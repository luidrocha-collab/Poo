def adicionar_tarefa(tarefa, lista=None):
    if lista is None:
        lista = []

    lista.append(tarefa)
    return lista


print(adicionar_tarefa.__defaults__)

print(adicionar_tarefa("Estudar"))
print(adicionar_tarefa("Fazer exercício"))
print(adicionar_tarefa("Ler"))

print(adicionar_tarefa.__defaults__)
