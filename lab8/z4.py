list = []

sum = 0

for i in range(5):
    n = int(input(">"))
    list.append(n)
    sum += n
sr = sum/5
b = [num for num in list if num > sr]
m = [num for num in list if num < sr]
print(list)
print(f"Среднее число:{sr}")
print(b)
print(m)


