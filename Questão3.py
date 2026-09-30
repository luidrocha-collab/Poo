import copy

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rasa = matriz.copy()
profunda = copy.deepcopy(matriz)

print("Original:")
print(matriz)

rasa[1][1] = 0

print("\nDepois de rasa[1][1] = 0:")
print("Original:", matriz)
print("Rasa:", rasa)

rasa[2] = [7, 7, 7]

print("\nDepois de rasa[2] = [7, 7, 7]:")
print("Original:", matriz)
print("Rasa:", rasa)

profunda[0][0] = 0

print("\nDepois de profunda[0][0] = 0:")
print("Original:", matriz)
print("Profunda:", profunda)
