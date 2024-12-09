from random import choice

password = ""

with open('/home/jorik/Загрузки/file11.txt', 'r') as file:
    text = file.read()
    words = text.split()
    for word in words:
        password = choice(words) + choice(words)
        if (len(password) <= 10):
                print("Password:", password)
        password = ""
