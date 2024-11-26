import PySimpleGUI as sg
import json


from lab3.zad1 import probki_str_na_liczby, ColumnsNotEvenException
from lab3.zad2 import k_means

def lab3(window: sg.Window) -> None:
    window["-FRAME-"].update(visible=False)
    window["home"].update(visible=True)
    if not "-INPUT_PATH3-" in window.AllKeysDict:
        input_file_path = sg.Input("", key="-INPUT_PATH3-")
        input_file_button = sg.FileBrowse("Wybierz", key="INPUT_FILE")

        input_frame = sg.Frame("", [
            [input_file_path, input_file_button],
        ], key="-IN_FRAME3-")

        output_button = sg.Button("Pokaz", key="-SHOW-")
        input_col = sg.Column([[input_frame], [sg.Push(), output_button]], key="-INPUT_COL-")
        output_col = sg.Column([[]], key="-OUTPUT_COL-")
        zad1_frame = sg.Frame("Zad 1", [[input_col, output_col]], key="-ZAD1-")
        n_text = sg.Text("Podaj liczbe iteracji:")
        n_input = sg.Spin([i for i in range(10000)], size=(10, 1), key="-N-")
        path_desc = sg.Text("Plik spiralka")
        zad2_path = sg.Input("", key="-ZAD2_PATH-")
        zad2_file_button = sg.FileBrowse("Wybierz", key="-ZAD2_FILE-")
        names_path_desc = sg.Text("plik spiralka-names")
        zad2_names_path = sg.Input("", key="-ZAD2_NAMES_PATH-")
        zad2_names_button = sg.FileBrowse("Wybierz", key="ZAD2_NAMES_FILE")
        zad2_execute_button = sg.Button("Wykonaj", key="-ZAD2_EXECUTE-")
        zad2_frame = sg.Frame("Zad 2", [
            [n_text, n_input], 
            [path_desc, zad2_path, zad2_file_button],
            [names_path_desc, zad2_names_path, zad2_names_button],
            [zad2_execute_button]
        ], key="-ZAD2-")
        window.extend_layout(window, [[zad1_frame], [zad2_frame]])
    else:
        window["-ZAD1-"].update(visible=True)
        window["-ZAD2-"].update(visible=True)
        window["home"].update(visible=True)
        window["-FRAME-"].update(visible=False)
        output_col = window["-OUTPUT_COL-"]
    
    event = ""
    while True:
        event, values = window.read()

        print(event, values)

        if event == "-SHOW-":
            if len(values["-INPUT_PATH3-"]) < 1:
                window["-INPUT_PATH3-"].update("")
                continue
            
            try:
                with open(values["-INPUT_PATH3-"], "r") as f:
                    zad2_data = json.load(f)
            except FileNotFoundError:
                text = sg.Text("Plik wejscia nie istnieje.")
                ok_button = sg.Button("Ok")
                new_window = sg.Window("Plik nie istnieje", [[sg.Push(), text, sg.Push()], [sg.Push(), ok_button, sg.Push()]])
                new_window.read()
                new_window.close()
                window["-INPUT_PATH3-"].update("")

            try:
                table_data = probki_str_na_liczby(zad2_data["próbki_str"], [int(e) for e in zad2_data["numery_atr"]])
            except ValueError:
                text = sg.Text("Numery atrybutow zaiweraja znaki nienumeryczne.")
                ok_button = sg.Button("Ok")
                new_window = sg.Window("Blad danych", [[sg.Push(), text, sg.Push()], [sg.Push(), ok_button, sg.Push()]])
                new_window.read()
                new_window.close()
                window["-INPUT_PATH3-"].update("")
            except ColumnsNotEvenException:
                window["-INPUT_PATH3-"].update("")
                continue
            
            table = sg.Table(       # TODO: try to make the table scrollable horizontally
                table_data, 
                headings=zad2_data["numery_atr"], 
                key="-NUM_TABLE-", 
                col_widths=[7]*len(zad2_data["numery_atr"]), 
                num_rows=10 if len(table_data) > 9 else len(table_data),
                auto_size_columns=False,
                vertical_scroll_only=False
            )
            window.extend_layout(output_col, [[table]])
        
        elif event == "-ZAD2_EXECUTE-":
            if len(values["-ZAD2_PATH-"]) < 1 or len(values["-ZAD2_NAMES_PATH-"]) < 1 or int(values["-N-"]) < 1:
                continue

            zad2_data = []
            zad2_names = []
            try:
                with open(values["-ZAD2_PATH-"], "r") as f:
                    lines = f.readlines()
                for line in lines:
                    zad2_data.append(line.split())
            except FileNotFoundError:
                text = sg.Text("Nie znaleziono podanego pliku")
                ok_button = sg.Button("-OK-")
                new_window = sg.Window("Nie znaleziono pliku", [[text], [ok_button]])
                event = ""
                while event not in [sg.WIN_CLOSED, "-OK-"]:
                    try:
                        new_window.close()
                    except:
                        ...
                    window["-ZAD2_PATH-"].update("")
                    window["-ZAD2_NAMES_PATH-"].update("")
                continue

            try:
                with open(values["-ZAD2_NAMES_PATH-"], "r") as f:
                    lines = f.readlines()
                for line in lines:
                    zad2_names.append(line.split())
            except FileNotFoundError:
                text = sg.Text("Nie znaleziono podanego pliku")
                ok_button = sg.Button("-OK-")
                new_window = sg.Window("Nie znaleziono pliku", [[text], [ok_button]])
                event = ""
                while event not in [sg.WIN_CLOSED, "-OK-"]:
                    try:
                        new_window.close()
                    except:
                        ...
                    window["-ZAD2_PATH-"].update("")
                    window["-ZAD2_NAMES_PATH-"].update("")
                continue
                      
            zad2_result = k_means(zad2_data, zad2_names, int(values["-N-"]))
            # zad2_result_table = sg.Table(zad2_result[0], headings=[], key="-ZAD2_RESULT-")
            # zad2_names_table = sg.Table(zad2_result[1], headings=[], key="-ZAD2_NAMES-")
            zad2_graph = sg.Graph((200, 200), (-2, -2), (3, 3), "white")
            exit_button = sg.Button("Wyjście", key="-ZAD2_EXIT-")

            event = ""
            new_window = sg.Window("Wynik zadania 3.2", [
                # [zad2_result_table], 
                # [zad2_names_table], 
                [zad2_graph],
                [exit_button]
            ])
            colors = ["red", "green", "blue", "orange"]
            color_iter = 0
            new_window.finalize()

            ## draw coordinates
            for i in range(-2, 3):
                zad2_graph.draw_line((i, -2), (i, 3), "lightgray")
                zad2_graph.draw_line((-2, i), (3, i), "lightgray")

            for group in zad2_result.keys():
                color = colors[color_iter]
                for x, y in zad2_result[group]:
                    zad2_graph.draw_point((x, y), 0.2, color)
                color_iter += 1
            while event not in [sg.WIN_CLOSED, "-ZAD2_EXIT-"]:
                event, values = new_window.read()
            try:
                new_window.close()
            except:
                ...

        elif event == "home":
            window["-ZAD1-"].update(visible=False)
            window["-ZAD2-"].update(visible=False)
            window["home"].update(visible=False)
            window["-FRAME-"].update(visible=True)
            break
        
        elif event in [sg.WIN_CLOSED, "exit"]:
            exit(0)