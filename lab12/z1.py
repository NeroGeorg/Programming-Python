number = int(input("Number: "))

priority = {
    "1" : ["child", "woman"],
    "2" : ["man"],
    "3" : ["capitan"]
    }

team = []
status_team = []
evoc_pos = []
evoc_pos2 = []
evoc_pos3 = []

for i in range(number):
    text = input(">")
    people, status = text.split() 
    team.append(people)
    status_team.append(status)
    for key, chars in priority.items():
        if status_team[i] in chars: 
            if (key == "1"): evoc_pos.append(team[i])
            if (key == "2"): evoc_pos2.append(team[i])
            if (key == "3"): evoc_pos3.append(team[i])
if (len(evoc_pos2) > 0): evoc_pos.append(evoc_pos2)
if (len(evoc_pos2) > 0): evoc_pos.append(evoc_pos3)
print(evoc_pos)