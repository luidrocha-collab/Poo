def remover_negativos(numeros):
    nova_lista = []

    for numero in numeros:
        if numero >= 0:
            nova_lista.append(numero)

    return nova_lista


leituras = [12, -3, 7, -1, 5]

positivas = remover_negativos(leituras)

print("Positivas:", positivas)
print("Leituras:", leituras)
