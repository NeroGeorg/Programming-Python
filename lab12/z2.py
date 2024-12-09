from random import choice

number = int(input(">"))

ans = ["Q", "A"]
a = []
cntq = 0
cnta = 0

for i in range(number):
    a.append(choice(ans))

print(a)

for i in range(len(a)):
    if "Q" in a: 
        cntq+=1
        a.remove("Q")
    if "A" in a: 
        cnta+=1
        a.remove("A")
    
if (cntq == cnta): print("+")
if (cntq != cnta): print("-")
