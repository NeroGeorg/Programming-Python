n = int(input())

cnt = 0

for i in range(n):
    chel = int(input("Человек в комнате:"))
    maxchel = int(input("Максимальное кол-во человек:"))
    if (chel < maxchel): cnt +=1
print(cnt)