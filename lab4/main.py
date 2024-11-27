import PySimpleGUI as sg
import math
import threading

from lab4.zad1 import zad1, y
from numpy import arange
from threading import Event

def lab4(window: sg.Window) -> None:
    start_drawing = Event()
    start_drawing.set()
    window["-FRAME-"].update(visible=False)
    window["home"].update(visible=True)
    if not "-VAR_MIN-" in window.AllKeysDict:
        var_text = sg.Text("Zakres zmiennosci")
        var_min = sg.Spin([i for i in arange(0, 1000000, 0.1)], key="-VAR_MIN-", size=(10, 1))
        var_max = sg.Spin([i for i in arange(0, 1000000, 0.1)], key="-VAR_MAX-", size=(10, 1))
        n_text = sg.Text("Liczba iteracji")
        n = sg.Spin([i for i in range(1000000)], key="-N4-")
        spread_text = sg.Text("Rozrzut:")
        spread = sg.Spin([i for i in arange(0, 100000, 0.1)], key="-SPREAD4-", size=(10, 1))
        growth_text = sg.Text("Przyrost")
        growth = sg.Spin([i for i in arange(0, 10000, 0.1)], key="-GROWTH4-")
        submit_button = sg.Button("Oblicz", key="-SUBMIT4-")
        result_text = sg.Text("Wynik: -", key="-RESULT4-")
        lab4_frame = sg.Frame("", [
            [var_text, var_min, var_max], 
            [n_text, n], 
            [spread_text, spread],
            [growth_text, growth],
            [submit_button, result_text]]
        , key="-LAB4_FRAME-")
        window.extend_layout(window, [[lab4_frame]])
    else:
        lab4_frame.update(visible=True)

    event = ""
    while True:
        event, values = window.read()

        if event in [sg.WIN_CLOSED, "exit"]:
            exit(0)
        
        if event == "home":
            window["-ZAD4_FRAME-"].update(visible=False)
            window["home"].update(visible=False)
            window["-FRAME-"].update(visible=True)
            break
        
        if event == "-SUBMIT4-":
            if int(values["-N4-"]) < 1 or float(values["-VAR_MAX-"]) - float(values["-VAR_MIN-"]) <= 0 or float(values["-SPREAD4-"]) <= 0 or float(values["-GROWTH4-"]) <= 0:
                continue
            graph_min = math.floor(float(values["-VAR_MIN-"]))
            graph_max = math.ceil(float(values["-VAR_MAX-"]))
            result_graph = sg.Graph((700, 300), (graph_min, -0.5), (graph_max, 0.6), "white")
            new_exit_button = sg.Button("Wyjscie", key="-NEW_EXIT-")
            new_window = sg.Window("Wynik lab4", [[result_graph], [new_exit_button]])
            new_event = ""
            new_window.finalize()
            for i in range(graph_min, graph_max):
                if i == 0:
                    result_graph.draw_line((i, -0.5), (i, 0.6), "lightgray", 5)
                else:
                    result_graph.draw_line((i, -0.5), (i, 0.6), "lightgray")
                result_graph.draw_line((graph_min, 0), (graph_max, 0), "lightgray", 5)
            decimal_places = 1
            thread = threading.Thread(target=zad1, args=(
                (float(values["-VAR_MIN-"]), float(values["-VAR_MAX-"])), 
                int(values["-N4-"]),
                float(values["-SPREAD4-"]),
                float(values["-GROWTH4-"]),
                new_window,
                decimal_places
            ))
            thread.start()
            for x in arange(graph_min, graph_max, 10**(-1 - decimal_places)):
                result_graph.draw_point((x, y(x)), 0.5)
            while new_event not in [sg.WIN_CLOSED, "-NEW_EXIT-"]:
                new_event, new_values = new_window.read()

                print("event", new_event, "values", new_values)

                if new_event == "-DRAW_POINT-":
                    result_graph.draw_point(new_values["-DRAW_POINT-"], 1)
            thread.join()
            try:
                new_window.close()
            except:
                ...
            
