import PySimpleGUI as sg
import random

sg.theme('DarkGrey9')
sg.set_options(font=("Helvetica", 20))

layout = [
    [sg.Push(), sg.Image(filename="/home/jorik/Документы/programming-python/lab12/generated-image.png", subsample=2), sg.Push()], 
    [sg.Text("Введите число от -128 до 127:")],
    [sg.Text("Число: "), sg.InputText(key="-INPUT-")],
    [sg.Text("Прямой: "), sg.InputText(key="-DIR-")],
    [sg.Text("Обратный  : "), sg.InputText(key="-REV-")],
    [sg.Text("Дополнительный: "), sg.InputText(key="-EXTRA-")],
    [sg.Push(), sg.Button("Отправить"), sg.Button("Выход"), sg.Push()],
]

sum = 0

window = sg.Window("Программа!", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Выход":
        break

    if event == "Отправить":
        user_input = values["-INPUT-"]

        flag = True
        while(flag):
            try: 
                if (int(user_input) > 127) or (int(user_input) < -128): 
                    sg.popup_ok("Ошибка!")
                    break
                else: 
                    flag = False
                    if user_input.strip():
                        digit = format(int(user_input), '08b')

                        rev_digit = ''
                        for char in digit:
                            if char == '1': rev_digit += '0'
                            else: rev_digit += '1'
                                                
                        extra_digit = bin(int(rev_digit, 2) + int('1', 2))
                        
                        window["-DIR-"].update(f"{digit}")
                        window["-REV-"].update(f"{rev_digit}")
                        window["-EXTRA-"].update(f"{extra_digit}")
            except ValueError:
                sg.popup_ok("Введите число!")   
                break

window.close()