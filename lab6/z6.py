import random

secret = random.randint(1, 10)
cnt = 0

print("Хорошо, я загадал число. Попробуй его отгадать")

while 1:
  num = int(input(f"Попытка {cnt}: "))

  if num == secret:
    print("Поздравляю! Вы угадали!")
    n = int(input("Сыграть еще раз? Нажмите 1..."))
    if n == 1: 
      secret = random.randint(1, 10)
      cnt = 0
    else: break
  else:
    if num < secret: print("Число больше! Нее, ты не угадал. Попробуй снова")
    else: print("Число меньше! Нее, ты не угадал. Попробуй снова")
    cnt +=1