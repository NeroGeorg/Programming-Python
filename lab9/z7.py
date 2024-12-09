import random

n = int(input("n="))
m = int(input("m="))

matrix = []
for i in range(n):
    matrix.append([0] * m)

for i in range(n):
    for j in range(m):
        matrix[i][j] = random.randint(0, 1)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

chel = int(input("Введите кол-во человек: "))

cnt = 0
flag = False

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0: 
            cnt+=1
        else:
            cnt = 0
        if cnt >= chel: 
            print("Ряд: ", i+1)
            flag = True
            break
    if flag == True: break