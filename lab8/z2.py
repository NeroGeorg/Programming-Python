import random

n = 1
b = []

for i in range(5):
    if i == 0: n = random.randint(1, 9)
    else: n = random.randint(1, 49)
    b.append(str(n))
    
print("Номер билета:", " ".join(b))