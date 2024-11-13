import PySimpleGUI as sg


COLORS = ["black", "red", "pink", "blue", "cyan", "purple", "darkgreen", "lightgreen", "orange", "yellow"]
COLOR_ITERATOR = 0

def wykres_czysc(graph: sg.Graph) -> None:
    graph.erase()
    global COLOR_ITERATOR
    for x in range(-5, 5):
        graph.draw_line((x, -5), (x, 5), "lightgray")
        graph.draw_line((-5, x), (5, x), "lightgray")
        COLOR_ITERATOR = 0

def wykres_linie_rysuj(graph: sg.Graph, wartosci_y: list[int]) -> None:
    global COLOR_ITERATOR
    for i in range(len(wartosci_y) - 1):
        graph.draw_line((i, wartosci_y[i]), (i + 1, wartosci_y[i + 1]), color=COLORS[COLOR_ITERATOR])
    COLOR_ITERATOR += 1
    if COLOR_ITERATOR >= len(COLORS):
        COLOR_ITERATOR = 0

def wykres_linie_rysuj2(graph: sg.Graph, wartosci_x: list[int], wartosci_y: list[int]) -> None:
    global COLOR_ITERATOR
    sorted_points = []
    for x, y in sorted(zip(wartosci_x, wartosci_y), key=lambda x: x[0]):
        sorted_points.append((x, y))
    for i in range(len(sorted_points) - 1):
        graph.draw_line((sorted_points[i][0], sorted_points[i][1]), (sorted_points[i + 1][0], sorted_points[i + 1][1]), color=COLORS[COLOR_ITERATOR])
    
    COLOR_ITERATOR += 1
    if COLOR_ITERATOR >= len(COLORS):
        COLOR_ITERATOR = 0

def wykres_punkty_rysuj(graph: sg.Graph, wartosci_x: list[int], wartosci_y: list[int]) -> None:
    global COLOR_ITERATOR
    for x, y in zip(wartosci_x, wartosci_y):
        graph.draw_point((x, y), 0.5, color=COLORS[COLOR_ITERATOR])

    COLOR_ITERATOR += 1
    if COLOR_ITERATOR >= len(COLORS):
        COLOR_ITERATOR = 0


def wykres_usmiech_rysuj(graph: sg.Graph) -> None:
    graph.erase()
    global COLOR_ITERATOR
    COLOR_ITERATOR = 0
    for i in range(-2, 3):
        graph.draw_line((i, -3), (i, 3), "lightgray")
        graph.draw_text(i, (i, -3.5))
    for i in range(-3, 4):
        graph.draw_line((-2, i), (2, i), "lightgray")
        graph.draw_text(i, (-2.5, i))
    
    ## oczy
    graph.draw_point((-1, 1), 0.2, "blue")
    graph.draw_point((0, 0), 0.2, "blue")
    graph.draw_point((1, 1), 0.2, "blue")
    ## usmiech
    graph.draw_arc((-1, 1), (1, -1), -90, -90, "arc", "green")
    graph.draw_arc((-1, 1), (1, -1), 90, -90, "arc", "green")
    ## twarz
    graph.draw_arc((-2, 2), (2, -2), -90, 180, "arc", "red")
    graph.draw_arc((-2, 2), (2, -2), 90, 180, "arc", "red")
    graph.draw_arc((-2, 2), (2, -2), -180, 180, "arc", "red")
    graph.draw_arc((-2, 2), (2, -2), 180, 180, "arc", "red")
    # legenda
    graph.draw_text("okrag", (4, 3))
    graph.draw_line((3, 3), (3.5, 3), "red")
    graph.draw_line((3, 2), (3.5, 2), "green")
    graph.draw_text("sinus", (4, 2))
    graph.draw_point((3, 1), 0.2, "blue")
    graph.draw_text("punkty", (4, 1))


def wykres_iris_rysuj(graphs: list[sg.Graph], file_path: str) -> None:
    for graph in graphs:
        for i in range(-1, 10):
            graph.draw_line((i, -1), (i, 9), "lightgray")
            graph.draw_line((-1, i), (9, i), "lightgray")
    
    with open(file_path, "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split())
    iris1 = [e for e in data if e[-1] == "1"]
    iris2 = [e for e in data if e[-1] == "2"]
    iris3 = [e for e in data if e[-1] == "3"]

    for entry in iris1:
        graphs[0].draw_point((float(entry[2]), float(entry[3])), 0.2)
        graphs[1].draw_point((float(entry[1]), float(entry[3])), 0.2)
        graphs[2].draw_point((float(entry[0]), float(entry[3])), 0.2)
        graphs[3].draw_point((float(entry[1]), float(entry[2])), 0.2)
    for entry in iris2:
        graphs[0].draw_point((float(entry[2]), float(entry[3])), 0.2, "blue")
        graphs[1].draw_point((float(entry[1]), float(entry[3])), 0.2, "blue")
        graphs[2].draw_point((float(entry[0]), float(entry[3])), 0.2, "blue")
        graphs[3].draw_point((float(entry[1]), float(entry[2])), 0.2, "blue")
    for entry in iris3:
        graphs[0].draw_point((float(entry[2]), float(entry[3])), 0.2, "red")
        graphs[1].draw_point((float(entry[1]), float(entry[3])), 0.2, "red")
        graphs[2].draw_point((float(entry[0]), float(entry[3])), 0.2, "red")
        graphs[3].draw_point((float(entry[1]), float(entry[2])), 0.2, "red")


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
