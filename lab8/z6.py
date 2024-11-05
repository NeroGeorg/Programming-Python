import random

list = ["O","Р"]
cnt = 0

while True:
    game = ' '.join(random.choice(list) for _ in range (5))
    cnt +=1
    print(game)

    if "O O O" in game or "Р Р Р" in game:
        print(f"Попыток: {cnt}")
        break