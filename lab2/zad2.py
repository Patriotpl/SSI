import PySimpleGUI as sg

from lab2.globals import COLORS, COLOR_ITERATOR

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
