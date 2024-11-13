import PySimpleGUI as sg

from lab2.globals import COLOR_ITERATOR


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
