c = 0
n = input("Введите 2-ое число: ")
for i in range(len(n)):
  print(i)
  print(f"ni= {int(n[i])} Len: {len(n)-i-1}")
  c += int(n[i])*2**(len(n)-i-1)
print(f"Число в десятичной: {c}") 
