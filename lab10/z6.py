input = input(">")
print(input)

print(input[::-1])

print("Его голос звучал спокойно, словно река, которая течёт медленно и уверенно.")

with open('/home/jorik/Загрузки/file10.txt', 'r') as file:
    text = file.read()
    print(text[::-1])
