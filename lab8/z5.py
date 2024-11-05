rost = []
cnt = 1
ra = int(input("Введите рост Андрея:"))
for i in range(5):
    n = int(input(">"))
    rost.append(n)
    if ra < rost[i]: cnt+=1
sorted_rost = sorted(rost, reverse=True)
print(cnt)
print(sorted_rost)
