import PySimpleGUI as sg
import random

sg.theme('DarkBlue9')

layout = [
    [sg.Image(filename="/home/jorik/Документы/programming-python/lab11/2.png")], 
    [sg.Text("Введите слово:")],
    [sg.Text("Слово: "), sg.InputText(key="-INPUT-")],
    [sg.Button("Отправить"), sg.Button("Выход")],
    [sg.Text("Сумма очков:", size=(80, 1), key="-OUTPUT-")]
]

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

window = sg.Window("Программа!", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Выход":
        break

    if event == "Отправить":
        user_input = values["-INPUT-"]
        for bukva in user_input:
            bukva = bukva.upper()
            for key, chars in numbers.items():
                if bukva in chars:
                    num = int(key)
                    sum +=num
        if user_input.strip():
            window["-OUTPUT-"].update(f"Сумма очков: {sum}")
            sum = 0
        else:
            window["-OUTPUT-"].update("Вы ничего не ввели!")

window.close()