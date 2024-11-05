list = []
list2 = []
for i in range(5):
    n = input()
    try:
        n = int(n)
        list.append(n)
    except ValueError:
        list2.append(n)
print(list)
print(list2)

