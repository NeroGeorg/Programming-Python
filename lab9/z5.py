import random

n = int(input("n="))
m = int(input("m="))

matrix = []
for i in range(n):
    matrix.append([0] * m)

for i in range(n):
    for j in range(m):
        matrix[i][j] = random.randint(10, 99)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print("Транспонированная матрица:")

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()