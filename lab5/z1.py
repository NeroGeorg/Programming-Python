f = int(input("Выбор: дни(1)/часы(2)/минуты(3)/секунды(4):"));

# days
if(f==1): 
  n = int(input("Введите количество дней:"));
  c = (n*24*60*60)
  print(c)

# hours
elif(f==2): 
  n = int(input("Введите количество часов:"));
  c = (n*60*60)
  print(c)

# minutes
elif(f==3): 
  n = int(input("Введите минуты:"));
  c = (n*60)
  print(c)

#sec
elif(f==4): 
  n = int(input("Введите секунды:"));
  c = (n)
  print(c)

else: print("Eror x_x")
