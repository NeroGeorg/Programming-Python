import random

n = int(input("n="))
m = int(input("m="))

matrix = []
for i in range(n):
    matrix.append([0] * m)

for i in range(n):
    for j in range(m):
        if i == 0: 
            matrix[0][j] = 1
        if j == 0:
            matrix[i][0] = 1
        else: matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]:6}", end=' ')
    print()