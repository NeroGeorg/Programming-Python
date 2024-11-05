number = [int(digit) for digit in str(4276440013361511)]

sum1 = 0
sum2 = 0
sum3 = 0
number.reverse()

for i in range(len(number) -1, -1, -1):

    pos_from_end = len(number) - i

    if pos_from_end % 2 == 0:
        sum1 += number[i]
    else:
        a = number[i] * 2
        if a > 9:
            a -= 9
        sum2 += a
print(number)
# print(sum1)
# print(sum2)
sum3 = sum1 + sum2
# print(sum3)
if sum3 % 10 == 0: print("Корректный номер!")
else: print("Некорректный номер!")