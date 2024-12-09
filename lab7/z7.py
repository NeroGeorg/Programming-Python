import string
import random

alphabetlowwer = string.ascii_lowercase
alphabetupper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

characters = ""

l = int(input("Длина пароля:"))
al = input("Использовать строчные буквы?(Если нет ничего не вводите)")
if len(al) > 0: characters +=alphabetlowwer
au = input("Использовать заглавные буквы?(Если нет ничего не вводите)")
if len(au) > 0: characters +=alphabetupper
d = input("Использовать цифры?(Если нет ничего не вводите)")
if len(d) > 0: characters +=digits
sp = input("Использовать специальные символы?(Если нет ничего не вводите)")
if len(sp) > 0: characters +=special

password = ''.join(random.choice(characters) for _ in range (l))
print(password)