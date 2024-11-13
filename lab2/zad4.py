import PySimpleGUI as sg


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