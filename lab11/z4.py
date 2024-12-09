import PySimpleGUI as sg
import random

sg.theme('Dark Grey 13')

layout = [
    [sg.Image(filename="/home/jorik/Документы/programming-python/lab11/1.png")], 
    [sg.Text("Введите границы рандома:")],
    [sg.Text("От"), sg.InputText(key="-INPUT-"), sg.Text("до"), sg.InputText(key="-INPUT2-")],
    [sg.Button("Отправить"), sg.Button("Выход")],
    [sg.Text("Результат:", size=(80, 1), key="-OUTPUT-")]
]

window = sg.Window("Случайное число", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Выход":
        break

    if event == "Отправить":
        user_input = values["-INPUT-"]
        user_input2 = values["-INPUT2-"]
        num = random.randint(int(user_input), int(user_input2))
        if user_input.strip():
            window["-OUTPUT-"].update(f"Случайное число: {num}")
        else:
            window["-OUTPUT-"].update("Вы ничего не ввели!")

window.close()
