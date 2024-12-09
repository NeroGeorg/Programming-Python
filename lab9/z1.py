def func(x):
    return ((2*x**2+3)/(x**2+3*x+5)**2)

b=int(input("Верхний предел b="))
a=int(input("Нижний предел a="))
n=int(input("N="))

h=(b-a)/n

sum = 0

for i in range(1, n):
    x = a + i * h
    sum += func(x)

sum *=h

res_sum = ((h/2)*(func(a)+func(b))) + sum

print(f"Интеграл={res_sum:.5f}")
