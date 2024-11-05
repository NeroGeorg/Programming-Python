n = int(input())

words = []

for i in range(n):
    word = input();
    if len(word) > 10:
        lword = len(word) - 2
        print(word[0] + str(lword) + word[-1])
