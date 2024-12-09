n = int(input("Введите число n = "))
for i in range(1, n+1):
  print(" " * (n-i) + "#" * (2 * i-1))
print(" " * (n-1) + "#" * (2 * i-n-(n-1)))