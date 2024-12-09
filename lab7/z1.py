s = '''Довольно распространённая ошибка
ошибка это лишний повтор повтор
слова слова Смешно, не не правда ли?
Не нужно портить хор хоровод'''

words = s.split()

for i in range(len(words) - 1):
  if words[i] != words[i+1]:
    print(words[i])
if words[len(words) - 1] != words[len(words) - 2]:
  print(words[len(words) - 1])