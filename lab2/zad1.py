import PySimpleGUI as sg

from lab2.globals import COLOR_ITERATOR


def wykres_czysc(graph: sg.Graph) -> None:
    graph.erase()
    global COLOR_ITERATOR
    for x in range(-5, 5):
        graph.draw_line((x, -5), (x, 5), "lightgray")
        graph.draw_line((-5, x), (5, x), "lightgray")
        COLOR_ITERATOR = 0