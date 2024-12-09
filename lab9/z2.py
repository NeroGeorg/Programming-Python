from random import choice

m = []
for i in range(3):
    m.append([0] * 3)

flag = True

while flag:

    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(3):
        for j in range(3):
            m[i][j] = choice(number)
            number.remove(m[i][j])

    sum = 0
    sum_str = 0
    sum_stl = 0
    sum_diag = 0
    sum_diag2 = 0
    cnt = 0

    sum_p = 15

    #proverka summa strok summa stolbchov summa diagonaley
    for i in range(3):
        for j in range(3):
            sum_str += m[i][j]
            sum_stl += m[j][i]
            sum_diag += m[i][i]
            sum_diag2 += m[i][2-i]
            
        if sum_str == sum_p and sum_stl == sum_p and sum_diag == sum_p and sum_diag2 == sum_p: 
            flag = False
            print(f"Строка {i}: {sum_str}")
            print(f"Столбик {i}: {sum_stl}")
            print(f"Главная диагональ {i}: {sum_diag}")
            print(f"Побочная диагональ {i}: {sum_diag2}")
        else:
            sum_str = 0
            sum_stl = 0
            sum_diag = 0
            sum_diag2 = 0
            cnt+=1

for i in range(3):
    for j in range(3):
        print(m[i][j], end=' ')
    print()