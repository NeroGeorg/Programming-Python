
with open('/home/jorik/Загрузки/file5.txt', 'r') as file:
    text = file.readline()
    while(text):
        if "Academy" in text: 
            print("Слово в тексте!")
        text = file.readline()

with open('/home/jorik/Загрузки/file6.txt', 'r') as file2:
    text2 = file2.readline()
    while(text2):
        if "Academy" in text2: 
            print("Слово в тексте!")
        text2 = file2.readline()