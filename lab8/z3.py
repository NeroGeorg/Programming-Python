list = []
sum = 0
for i in range(5):
    n = int(input(">"))
    list.append(n)
    sum += n
sr = sum/5
max = [x for x in list if x > sr]
print(list)
print(max)