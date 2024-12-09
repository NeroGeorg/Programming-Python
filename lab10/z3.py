e = "e"
cnt = 0
cnt_e = 0

with open('/home/jorik/Загрузки/file6.txt', 'r') as file:
    text = file.readline()
    while(text):
        words = text.split()
        for i in words:
            cnt +=1
            if e in i: 
                cnt_e +=1;
        text = file.readline()
print(cnt)
print(cnt_e)
print(cnt/cnt_e)