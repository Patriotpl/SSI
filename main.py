import PySimpleGUI as sg
import os


if __name__ == "__main__":
    lab1_button = sg.Button("lab 1", key="1", disabled=not os.path.isfile("lab1/main.py"))
    lab2_button = sg.Button("lab 2", key="2", disabled=not os.path.isfile("lab2/main.py"))
    lab3_button = sg.Button("lab 3", key="3", disabled=not os.path.isfile("lab3/main.py"))
    lab4_button = sg.Button("lab 4", key="4", disabled=not os.path.isfile("lab4/main.py"))
    lab5_button = sg.Button("lab 5", key="5", disabled=not os.path.isfile("lab5/main.py"))
    lab6_button = sg.Button("lab 6", key="6", disabled=not os.path.isfile("lab6/main.py"))
    lab7_button = sg.Button("lab 7", key="7", disabled=not os.path.isfile("lab7/main.py"))
    lab8_button = sg.Button("lab 8", key="8", disabled=not os.path.isfile("lab8/main.py"))
    exit_button = sg.Button("wyjście", key="exit")
    layout = [
      [sg.Push(), lab1_button, sg.Push()], 
      [sg.Push(), lab2_button, sg.Push()], 
      [sg.Push(), lab3_button, sg.Push()], 
      [sg.Push(), lab4_button, sg.Push()], 
      [sg.Push(), lab5_button, sg.Push()], 
      [sg.Push(), lab6_button, sg.Push()], 
      [sg.Push(), lab7_button, sg.Push()], 
      [sg.Push(), lab8_button, sg.Push()],
      [sg.Push(), exit_button, sg.Push()]
    ]
    window = sg.Window("145019", layout)
    event = ""
    while event not in [sg.WIN_CLOSED, "exit"]:
        event, vaules = window.read()
        # if event == "1":
        #     lab1(window)
        #     continue
        # if event == "2":
        #     lab2(window)
        #     continue
        # if event == "3":
        #     lab3(window)
        #     continue
        # if event == "4":
        #     lab4(window)
        #     continue
        # if event == "5":
        #     lab5(window)
        #     continue
        # if event == "6":
        #     lab6(window)
        #     continue
        # if event == "7":
        #     lab7(window)
        #     continue
        # if event == "8":
        #     lab8(window)
        #     continue
        ...