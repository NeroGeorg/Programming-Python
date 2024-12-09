input = input(">")
print(input)

with open('/home/jorik/Загрузки/file9.txt', 'r') as file:
    text = file.read()
    words = text.split()
    length = len(words)
    mid = length//2
    words.insert(mid, input)
    print(words)
