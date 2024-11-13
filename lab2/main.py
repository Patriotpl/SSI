import PySimpleGUI as sg


from lab2.zad1 import wykres_czysc
from lab2.zad2 import wykres_linie_rysuj, wykres_linie_rysuj2, wykres_punkty_rysuj
from lab2.zad3 import wykres_usmiech_rysuj
from lab2.zad4 import wykres_iris_rysuj

def lab2(window: sg.Window) -> None:
    example_points = [1, 2, 3, 4]
    example_points2_x = [2,1, 3, 4]
    example_points2_y = [1, 2, 3, 4]
    example_points3_x = [1, 2, 3, 4]
    example_points3_y = [1, 2, 3, 4]

    window["-FRAME-"].update(visible=False)
    window["home"].update(visible=True)
    if not "-LAB2_FRAME-" in window.AllKeysDict:
        graph = sg.Graph(
            (300, 150), 
            key="-GRAPH-", 
            graph_bottom_left=(-5, -5), 
            graph_top_right=(5, 5), 
            background_color="white"
        )
        lines_1_button = sg.Button("Linie", key="-LINE1-")
        lines_2_button = sg.Button("Linie 2", key="-LINE2-")
        point_button = sg.Button("Punkty", key="-POINT-")
        smile_button = sg.Button("Usmiech", key="-SMILE-")
        iris_button = sg.Button("iris", key="-IRIS-", disabled=True)
        clear_button = sg.Button("Wyczyść", key="-CLR-")
        column = sg.Column([
            [lines_1_button], 
            [lines_2_button], 
            [point_button], 
            [smile_button],
            [iris_button],
            [clear_button]
        ])
        input_file_path = sg.Input("", key="-INPUT_PATH-")
        input_file_button = sg.FileBrowse("Wybierz", key="INPUT_FILE")
        iris_graph1 = sg.Graph(
            (150, 150), 
            key="-GRAPH1-", 
            graph_bottom_left=(-1, -1), 
            graph_top_right=(9, 9), 
            background_color="white"
        )
        iris_graph2 = sg.Graph(
            (150, 150), 
            key="-GRAPH2-", 
            graph_bottom_left=(-1, -1), 
            graph_top_right=(9, 9), 
            background_color="white"
        )
        iris_graph3 = sg.Graph(
            (150, 150), 
            key="-GRAPH3-", 
            graph_bottom_left=(-1, -1), 
            graph_top_right=(9, 9), 
            background_color="white"
        )
        iris_graph4 = sg.Graph(
            (150, 150), 
            key="-GRAPH4-", 
            graph_bottom_left=(-1, -1), 
            graph_top_right=(9, 9), 
            background_color="white"
        )
        graph_column = sg.Column([[iris_graph1, iris_graph3], [iris_graph2, iris_graph4]], visible=False, key="-IRIS_COL-")
        frame = sg.Frame("", key="-LAB2_FRAME-", layout=[[column, graph, graph_column], [input_file_path, input_file_button]])
        window.extend_layout(window, [[frame]])
    else:
        window["home"].update(visible=True)
        window["-FRAME-"].update(visible=False)
        window["-LAB2_FRAME-"].update(visible=True)
        graph = window["-GRAPH-"]
        iris_graph1 = window["-GRAPH1-"]
        iris_graph2 = window["-GRAPH2-"]
        iris_graph3 = window["-GRAPH3-"]
        iris_graph4 = window["-GRAPH4-"]
    
    event = ""
    for x in range(-5, 5):
        graph.draw_line((x, -5), (x, 5), "lightgray")
        graph.draw_line((-5, x), (5, x), "lightgray")
    while True:
        event, values = window.read()

        print(event, values)

        if len(values["-INPUT_PATH-"]) > 0:
            window["-IRIS-"].update(disabled=False)

        if event != "-IRIS-":
            window["-IRIS_COL-"].update(visible=False)
            window["-GRAPH-"].update(visible=True)
        if event == "-CLR-":
            wykres_czysc(graph)
        elif event == "-LINE1-":
            wykres_linie_rysuj(graph, example_points)
        elif event == "-LINE2-":
            wykres_linie_rysuj2(graph, example_points2_x, example_points2_y)
        elif event == "-POINT-":
            wykres_punkty_rysuj(graph, example_points3_x, example_points3_y)
        elif event == "-SMILE-":
            wykres_usmiech_rysuj(graph)
        elif event == "-IRIS-":
            window["-GRAPH-"].update(visible=False)
            window["-IRIS_COL-"].update(visible=True)
            wykres_iris_rysuj(
                [iris_graph1, iris_graph2, iris_graph3, iris_graph4], 
                values["-INPUT_PATH-"]
            )
        elif event in [sg.WIN_CLOSED, "exit"]:
            exit(0)
        elif event == "home":
            window["-LAB2_FRAME-"].update(visible=False)
            window["home"].update(visible=False)
            window["-FRAME-"].update(visible=True)
            break
