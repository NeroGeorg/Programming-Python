import PySimpleGUI as sg
import random

c_image = [[sg.Image("/home/jorik/Документы/programming-python/lab12/bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    micro = value["micro"]  #здесь хранится количество бактерий изначально
    count = value["count"]  #здесь хранится количество секунд для которых требуется рассчитать
    rand_b = random.randint(0,4) #здесь хранится рандомный b
    res = 0

    for i in range(int(count)):
        rand_b = random.randint(0,4) 
        sum = int(micro)*int(count)+rand_b    
        res +=sum

    if event == "Рассчитать":
        window["res"].update(res)


window.close()

