import PySimpleGUI as sg
import random

sg.theme('DarkGrey9')#theme of game
sg.set_options(font=("Helvetica", 20))

log_file = "game_res.txt"

#layout of start menu
layout = [
    [sg.Push(), sg.Image(filename="/home/jorik/Документы/programming-python/rgz/image.png", subsample=2), sg.Push()], 
    [sg.Text("Введите количество раундов и свое имя!")],
    [sg.Text("Раунды:"), sg.InputText(key="-NUM-")],
    [sg.Text("Имя:"), sg.InputText(key="-NAME-")],
    [sg.Push(), sg.Button("Отправить"), sg.Button("Выход"), sg.Push()],
]

window = sg.Window("Камень", layout)

#vars, images
vars = ["Камень", "Ножницы", "Бумага"]
comp_b = "/home/jorik/Документы/programming-python/rgz/comp.png"
player_b = "/home/jorik/Документы/programming-python/rgz/player.png"
kamen_b = "/home/jorik/Документы/programming-python/rgz/kamen.png"
nojn_b = "/home/jorik/Документы/programming-python/rgz/noj.png"
paper_b = "/home/jorik/Документы/programming-python/rgz/list.png"
player_score = 0
comp_score = 0
rounds=0
result=""

#window
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Выход":
        break

    if event == "Отправить":
        try:
            user_round = values["-NUM-"]
            if int(user_round) <= 0 or int(user_round) >= 100:
                raise ValueError("Количество раундов должно быть больше 0 и не меньше 100!")
        except ValueError:
            sg.popup_error("Введите корректное число!")
            continue
        try:
            user_name = values["-NAME-"]
            if len(user_name) > 20:
                raise ValueError("Имя должно быть меньше 20 символов!")
            elif len(user_name) == 0:
                user_name = "Аноним"
        except ValueError:
            sg.popup_error("Введите корректное имя!")
            continue
        window.close()

    #layout of game
    layout_game = [

    [sg.Push(), sg.Text(f"Привет, {user_name}!"), sg.Text(f"Счёт: {comp_score}:{player_score}", key="Score"), sg.Push()],

    [
    sg.Column([
        [sg.Image(filename=comp_b, key = "Comp_turn", subsample=4)], 
        [sg.Push(), sg.Text("Ход компьютера!"), sg.Push()],
    ]),
    sg.Column([
        [sg.Image(filename=player_b, key = "Player_turn", subsample=4)], 
        [sg.Push(), sg.Text("Ход игрока!"), sg.Push()],
    ]),
    sg.VerticalSeparator(color='red'), 
    sg.Column([    
        [sg.Push(), sg.Button(image_filename=kamen_b, key = "kamen", image_subsample=6)],
        [sg.Push(), sg.Button(image_filename=nojn_b, key = "nojn", image_subsample=6)],
        [sg.Push(), sg.Button(image_filename=paper_b, key = "paper", image_subsample=6)],
    ])],

    [sg.Text(f"Раунд: {rounds}!", key="kolvo"), sg.Text(key="-WINNER-")],
    
    [sg.Push(), sg.Button("Выход"), sg.Push()],
    
    ]

    window_game = sg.Window("Камень", layout_game)

    #game window loop
    while True: 
        event_game, values_game = window_game.read()

        if event_game == "kamen" or "nojn" or "paper": #if player click the button
            rounds+=1
            window_game["kolvo"].update(f"Раунд: {rounds}")            
            comp_choice = random.choice(vars);
            #update computer choice
            if (comp_choice == "Камень"): window_game["Comp_turn"].update(filename=kamen_b, subsample=4)
            if (comp_choice == "Ножницы"): window_game["Comp_turn"].update(filename=nojn_b, subsample=4)
            if (comp_choice == "Бумага"): window_game["Comp_turn"].update(filename=paper_b, subsample=4)
            #update player choice
            if (event_game == "kamen"): window_game["Player_turn"].update(filename=kamen_b, subsample=4)
            if (event_game == "nojn"): window_game["Player_turn"].update(filename=nojn_b, subsample=4)
            if (event_game == "paper"): window_game["Player_turn"].update(filename=paper_b, subsample=4)          
            #comparing who is win
            if (comp_choice == event_game): sg.popup_notify("Ничья!")
            elif(comp_choice == "Камень" and event_game == "nojn") or (comp_choice == "Ножницы" and event_game == "paper") or (comp_choice == "Бумага" and event_game == "kamen"):
                comp_score+=1
                window_game["-WINNER-"].update("Победил компьютер в этом раунде!")
            elif(comp_choice == "Камень" and event_game == "kamen") or (comp_choice == "Ножницы" and event_game == "nojn") or (comp_choice == "Бумага" and event_game == "paper"):
                window_game["-WINNER-"].update("Ничья!")
            else: 
                player_score+=1
                window_game["-WINNER-"].update(f"Победил {user_name} в этом раунде!")
            #updating score
            window_game["Score"].update(f"Счёт: {comp_score}:{player_score}")

        if(int(user_round) == rounds):
            if(comp_score > player_score):
                sg.popup_annoying(f"{user_name} проиграл!😕")
                result = (f"{user_name} проиграл!")
                break
            elif(comp_score < player_score):
                sg.popup_annoying(f"{user_name} выиграл!😀")
                result = (f"{user_name} выиграл!")
                break
            else: 
                sg.popup_annoying("Ничья!")
                result = ("Ничья!")
                break
            
        if event_game == sg.WINDOW_CLOSED or event_game == "Выход":
            break
    #logging the result of game
    with open(log_file, "a") as log:
            log.write(f"Игра завершена! Итоговый счёт: {comp_score}:{player_score}. {result}\n")

    window_game.close()

window.close()