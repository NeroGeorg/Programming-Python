text = input(">")

numbers = {
    "1": ['.',',','?','!',':'],
    "2": ['A','B','C'],
    "3": ['D','E','F'],
    "4": ['G','H','I'],
    "5": ['J','K','L'],
    "6": ['M','N','O'],
    "7": ['P','Q','R','S'],
    "8": ['T','U','V'],
    "9": ['W','X','Y','Z'],
    "0": [' ']
}

times = 0

for bukva in text:
    bukva = bukva.upper()
    for key, chars in numbers.items():
        if bukva in chars:
            times = chars.index(bukva)+1
            print(key * times, end="")
