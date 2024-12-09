max_score = 0
max_score2 = 0
winners = ""
prizer = ""

with open('/home/jorik/Загрузки/file4.txt', 'r') as file:
    record = file.readline()
    while record:
        human = record.split()
        if int(human[-1]) > max_score:
            winner = human[0] + " " + human[1]
            max_score = int(human[-1])
        if (abs(int(human[-1]) - max_score)) < 3: 
            prizer = human[0] + " " + human[1]
            max_score2 = int(human[-1])
        record = file.readline()
print(winner + " " + str(max_score))
print(prizer + " " + str(max_score2))