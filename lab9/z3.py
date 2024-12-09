from random import choice

n= int(input("n = "))       

m=[]

for i in range(n):
    m.append([0] * n)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(n):
    for j in range(2):
        m[i][j] = choice(number)
        number.remove(m[i][j])

for i in range(n):
    for j in range(2):
        print(m[i][j], end=' ')
    print()

k=input("Координаты Александра:")
k_num = map(int, k.split())
k=sum(k_num)

nums = 0
nums_sp= []
bl = 0

for i in range(len(m)):
    tr_k = map(int, m[i])
    nums = sum(tr_k)
    bl = abs(nums-k)
    nums_sp.append(bl)

minim = min(nums_sp)
minim_cord = nums_sp.index(min(nums_sp))
print(f"Близжайщее сокровище: {m[minim_cord]}")