n= int(input("n = "))       

m=[]

for i in range(n):
    m.append([0] * n)

for i in range(n):
    for j in range(n):
        m[i][j] = input(">")

for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()

print("Преобразованная матрица:")

for i in range(n):
    temp = m[i][i]
    m[i][i] = m[i][n-i-1]
    m[i][n-i-1] = temp

for i in range(n):
    for j in range(n):
        print(m[i][j], end=' ')
    print()
