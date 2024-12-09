input = input(">")
n, l = input.split()
score = 1

if (l == "ж"):
    with open('/home/jorik/Загрузки/file7.txt', 'r') as file:
        text = file.readline()
        while(text):
            name, p = text.split()
            percent = int(p)
            if (int(n) >= score):
                print(name)
                score +=1
            else: break
            text = file.readline()

if (l == "м"):
    with open('/home/jorik/Загрузки/file8.txt', 'r') as file2:
        text2 = file2.readline()
        while(text2):
            name, p = text2.split()
            percent = int(p)
            if (int(n) >= score):
                print(name)
                score +=1
            else: break
            text2 = file2.readline()