class Contador:
    def __init__(self, valor):
        self.valor = valor

    def __iadd__(self, valor):
        self.valor += valor
        return self


contador = Contador(10)

print(id(contador))

contador += 5

print(id(contador))
print(contador.valor)


n = 10

print(id(n))

n += 5

print(id(n))
print(n)
