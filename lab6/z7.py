print("Введите номер вашего билета:")
n = input("Введите 6-ое число: ")
if len((n)) < 6: print("Ошибка!")
else:
  c = (int (n[0]) + int (n[1]) + int (n[2]))
  v = (int (n[3]) + int (n[4]) + int (n[5]))
  if (c == v): print(f"Поздравляю! Ваш билет {n} - счастливый ")
  else: print(f"Поздравляю! Ваш билет {n} - обычный ")