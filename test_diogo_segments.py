import numpy as np

# Criando um array 6 por 7 (matriz)
array = np.zeros((6, 7))

# Gerando as coordenadas horizontais
horizontal_coords = []
for i in range(6):
    for j in range(4):
        horizontal_coords.append([(i, j+k) for k in range(4)])

# Gerando as coordenadas verticais
vertical_coords = []
for i in range(7):
    for j in range(3):
        vertical_coords.append([(j+k, i) for k in range(4)])

# Gerando as coordenadas diagonais
diagonal_coords = []
for i in range(6):
    for j in range(7):
        if i + 3 < 6 and j + 3 < 7:
            diagonal_coords.append([(i+k, j+k) for k in range(4)])
        if i + 3 < 6 and j - 3 >= 0:
            diagonal_coords.append([(i+k, j-k) for k in range(4)])

# Juntando todas as coordenadas em uma única lista
all_coords = horizontal_coords + vertical_coords + diagonal_coords

# Exibindo os conjuntos de coordenadas
d = {}
for coords in all_coords:
    print(coords)
    d[str(coords)] = (coords[0][0])
print("---")
for a in all_coords:
    if (5,2) in a:
        print(a)
print("------")
print(d)