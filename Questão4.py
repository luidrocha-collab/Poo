import time

def concatenacao_1(repeticoes):
    texto = ""

    inicio = time.time()

    for i in range(repeticoes):
        texto += "a"

    fim = time.time()

    return fim - inicio


def concatenacao_2(repeticoes):
    textos = []

    inicio = time.time()

    for i in range(repeticoes):
        textos.append("a")

    texto = "".join(textos)

    fim = time.time()

    return fim - inicio


tempo1_500k = concatenacao_1(500000)
tempo1_2m = concatenacao_1(2000000)

tempo2_500k = concatenacao_2(500000)
tempo2_2m = concatenacao_2(2000000)

print("Concatenação 1:")
print("500 mil:", tempo1_500k)
print("2 milhões:", tempo1_2m)

print("\nConcatenação 2:")
print("500 mil:", tempo2_500k)
print("2 milhões:", tempo2_2m)

print("\nAumento da concatenação 1:",
      tempo1_2m / tempo1_500k)

print("Aumento da concatenação 2:",
      tempo2_2m / tempo2_500k)
