slova = ["не плохая", "Не плохая", "не плоха", "Не плоха", ]
slova2 = ["не плохой", "Не плохой"]
s = input("Введите строку:")
for i in range(4):
  if slova[i] in s:
    s = s.replace(slova[i], "хорошая")
for i in range(2):
  if slova2[i] in s:
    s = s.replace(slova2[i], "хороший")
print(s)