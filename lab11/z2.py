text = input(">")

numbers = {
    "1": ['A','E','I','L','N','O','R','S','T','U'],
    "2": ['D','G'],
    "3": ['B','C','M','P'],
    "4": ['F','H','V','W','Y'],
    "5": ['K'],
    "8": ['J','X'],
    "10": ['Q','Z'],
}

sum = 0

for bukva in text:
    bukva = bukva.upper()
    for key, chars in numbers.items():
        if bukva in chars:
            num = int(key)
            sum +=num
print(f"{text, sum}")
