vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
  
n1 = input()
n2 = input()
n3 = input()

cnt1 = len([char for char in n1 if char in vowels])
cnt2 = len([char for char in n2 if char in vowels])
cnt3 = len([char for char in n3 if char in vowels])

print(f"Гласных: {cnt1} - {cnt2} - {cnt3}")

if cnt1 == 5 and cnt2 == 7 and cnt3 == 5:
    print("Хайку!")
else: print("Не хайку!")