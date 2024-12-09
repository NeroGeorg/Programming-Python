menu = [
["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

print("Меню ресторана:")
for i in range(len(menu)):
    print(menu[i][0])

name = input("Найти блюдо по названию:")

for i in range(len(menu)):
    if name == menu[i][0]: 
        print("Блюдо найдено!")
        print(f"Найдено в меню: {menu[i]}")

print("Добавление нового блюда:")
title = input("Название:")
ing = input("Ингредиенты:")
cost = int(input("Цена:"))

new_bludo = [title, ing, cost]
menu.append(new_bludo)

print("Меню ресторана:")
for i in range(len(menu)):
    print(menu[i][0])

change_cost = input("Введите названия блюда и цену через ,")
name_bludo, new_cost = change_cost.split(",")

for i in range(len(menu)):
    if name_bludo == menu[i][0]: 
        menu[i][2] = new_cost
        print(f"Цена была изменена!")

print("Меню ресторана:")
for i in range(len(menu)):
    print(menu[i])
