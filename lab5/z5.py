a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a == b == c: print("Треугольник равносторонний!")
elif (a == b) or (b == c) or (a == c): print("Треугольник равнобедренный!")
else: print("Треугольник разносторонний!")