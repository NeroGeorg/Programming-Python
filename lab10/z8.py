n= int(input("n = "))       
m2= int(input("m = "))   

m=[]

for i in range(n):
    m.append(['.'] * m2)

for i in range(n):
    for j in range(m2):
        if i % 2 == 0: m[i][j] = '#'
        elif i % 2 != 0:
            if (i//2) % 2 == 0 and (j == m2-1): 
                m[i][j] = '#'
            elif (i//2) % 2 != 0 and (j == 0): 
                m[i][j] = '#'
                
for i in range(n):
    for j in range(m2):
        print(f"{m[i][j]}", end=' ')
    print()
