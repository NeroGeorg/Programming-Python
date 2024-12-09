n = input()
teams, score = n.rsplit(' ', 1)
team1, team2 = teams.split("-")

score1, score2 =map(int, score.split(":"))

if score1 > score2:
    winner = team1
elif score2 > score1:
    winner = team2
else: 
    winner = ("Ничья!")

print(winner)