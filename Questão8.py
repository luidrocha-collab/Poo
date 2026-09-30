import copy

# b e a apontam para a mesma lista
a = [1, 2, 3]
b = a

b.append(4)

print("a:", a)
print("b:", b)


# Cópia rasa
a = [[1, 2], [3, 4]]
b = a.copy()

b[0][0] = 99

print("\nCópia rasa:")
print("a:", a)
print("b:", b)


# Cópia profunda
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99

print("\nCópia profunda:")
print("a:", a)
print("b:", b)


# += com lista
lista = [1, 2]

lista += [3, 4]

print("\nLista com +=:", lista)


# += com string
texto = "Olá"

texto += " mundo"

print("String com +=:", texto)
