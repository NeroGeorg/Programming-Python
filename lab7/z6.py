n = input("Введите слово(обязательно введите #):")
if "#" not in n: print("Введите специальный символ!")
else: 
    w = "".join(char for char in n if char != "#")
    print(w[::2] + w[1::2][::-1])