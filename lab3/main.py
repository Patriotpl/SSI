import PySimpleGUI as sg
import json


from lab3.zad1 import probki_str_na_liczby, ColumnsNotEvenException

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
        window.extend_layout(window, [[input_col, output_col]])
    else:
        window["-IN_FRAME3-"].update(visible=True)
        window["home"].update(visible=True)
        window["-FRAME-"].update(visible=False)
        window["-OUTPUT_COL-"].update(visible=True)
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
                    data = json.load(f)
            except FileNotFoundError:
                text = sg.Text("Plik wejscia nie istnieje.")
                ok_button = sg.Button("Ok")
                new_window = sg.Window("Plik nie istnieje", [[sg.Push(), text, sg.Push()], [sg.Push(), ok_button, sg.Push()]])
                new_window.read()
                new_window.close()
                window["-INPUT_PATH3-"].update("")

            try:
                table_data = probki_str_na_liczby(data["próbki_str"], [int(e) for e in data["numery_atr"]])
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
                headings=data["numery_atr"], 
                key="-NUM_TABLE-", 
                col_widths=[7]*len(data["numery_atr"]), 
                num_rows=10 if len(table_data) > 9 else len(table_data),
                auto_size_columns=False,
                vertical_scroll_only=False
            )
            window.extend_layout(output_col, [[table]])
        elif event == "home":
            window["-IN_FRAME3-"].update(visible=False)
            window["-OUTPUT_COL-"].update(visible=False)
            window["home"].update(visible=False)
            window["-FRAME-"].update(visible=True)
            break
        
        elif event in [sg.WIN_CLOSED, "exit"]:
            exit(0)