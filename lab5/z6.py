name = input("Введите название месяца:")

if name == "январь" or name == "март" or name == "май" or name == "июль" or name == "август" or name == "октябрь" or name == "декабрь" :print(f"31 день в этом месяце: {name}")
elif name == "апрель" or name == "июнь" or name == "сентябрь" or name == "ноябрь":print(f"30 день в этом месяце: {name}")
else: print(f"28 или 29 день в этом месяце: {name}")