import random

n = int(input(">"))

b = random.randint(0,4)
k = random.randint(0,10)
sum=0
print(k)
print(b)

for i in range(n):
    sum = k*i+b
print(sum)