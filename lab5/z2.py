n = int(input("Введите число:"))
k = int(input("Введите сколько отрезаем цифр:"))
n = n % (10**k)
print("Число " + str(n) + "!")  