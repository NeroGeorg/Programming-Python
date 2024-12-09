rost = []
print("Введите рост: ")
while (0 not in rost):
  n = 1
  if n >= 0:rost.append(n)
if len(rost) <= 2: print("Некого сравнивать!")
rost.remove(0)
if len(rost) >= 2:
  max_number = max(rost)
  min_number = min(rost)
  print(f"Максимальный рост = {max_number}")
  print(f"Минимальный рост = {min_number}")