import PySimpleGUI as sg


from sys import exit
from lab1.zad1 import wczytaj_baze_probek_z_tekstem

def lab1(window: sg.Window) -> None:
    window["-FRAME-"].update(visible=False)
    window["home"].update(visible=True)
    if not "-INPUT_PATH-" in window.AllKeysDict:
        input_file_path = sg.Input("", key="-INPUT_PATH-")
        input_file_button = sg.FileBrowse("Wybierz", key="INPUT_FILE")
        classes_file_path = sg.Input("", key="-CLASSES_PATH-")
        classes_file_button = sg.FileBrowse("Wybierz", key="-CLASSES_FILE-")
        load_button = sg.Button("Wczytaj", key="-LOAD-")

        input_frame = sg.Frame("", [
            [input_file_path, input_file_button],
            [classes_file_path, classes_file_button],
            [sg.Push(), load_button]
        ], key="-IN_FRAME-")

        show_data_button = sg.Button("Pokaż próbki", key="-DATA-")
        show_symb_button = sg.Button("Pokaż symboliczne", key="-SYMB-")
        show_classes_button = sg.Button("Pokaż klasy", key="-CLASS-")
        output_frame = sg.Frame("", [[sg.Push(), show_data_button, show_symb_button, show_classes_button, sg.Push()]], key="-OUT_FRAME-")
        window.extend_layout(window, [[input_frame], [output_frame]])
    else:
        window["-IN_FRAME-"].update(visible=True)
        window["-OUT_FRAME-"].update(visible=True)
        window["home"].update(visible=True)
        window["-FRAME-"].update(visible=False)
        window["-LOAD-"].update(disabled=True)

    probki = [[]]
    czy_atr_symb = [[]]
    nazwy_atr = [[]]

    while True:
        event, values = window.read()
        print(event, values)

        if event == "-LOAD-":
            if len(values["-INPUT_PATH-"]) <= 0 or len(values["-CLASSES_PATH-"]) <= 0:
                continue
            try:
                probki, czy_atr_symb, nazwy_atr = wczytaj_baze_probek_z_tekstem(values["-INPUT_PATH-"], values["-CLASSES_PATH-"])
            except FileNotFoundError:
                window["-INPUT_PATH-"].update("Błąd pliku")
                window["-CLASSES_PATH-"].update("")
                continue
            continue
        if event == "-DATA-":
            table = sg.Table(probki, headings=[1, 2, 3, 4], auto_size_columns=False, num_rows=20, col_widths=[20, 20, 20, 20])
            exit_button = sg.Button("Powrót", key="exit")
            new_window = sg.Window("Próbki", layout=[[table], [exit_button]])
            event = ""
            while event not in [sg.WIN_CLOSED, "exit"]:
                event, _ = new_window.read()
            new_window.close()
            continue
        if event == "-SYMB-":
            table = sg.Table([[i] for i in czy_atr_symb], auto_size_columns=False, headings=[1], num_rows=20, col_widths=[20])
            exit_button = sg.Button("Powrót", key="exit")
            new_window = sg.Window("Czy atrybut symboliczny", layout=[[table], [exit_button]])
            event = ""
            while event not in [sg.WIN_CLOSED, "exit"]:
                event, _ = new_window.read()
            new_window.close()
            continue
        if event == "-CLASS-":
            table = sg.Table([[i] for i in nazwy_atr], auto_size_columns=False, headings=[1], num_rows=20, col_widths=[80])
            exit_button = sg.Button("Powrót", key="exit")
            new_window = sg.Window("Nazwy atrybutów", layout=[[table], [exit_button]])
            event = ""
            while event not in [sg.WIN_CLOSED, "exit"]:
                event, _ = new_window.read()
            new_window.close()
            continue
        if event == "home":
            window["-IN_FRAME-"].update(visible=False)
            window["-OUT_FRAME-"].update(visible=False)
            window["home"].update(visible=False)
            window["-FRAME-"].update(visible=True)
            break
        if event in [sg.WIN_CLOSED, "exit"]:
            exit(0)