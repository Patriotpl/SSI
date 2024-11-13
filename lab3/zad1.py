import PySimpleGUI as sg


class ColumnsNotEvenException(Exception):
    def __init__(self):
        super().__init__("")

        text = sg.Text("Blad danych: Kolumny nie są rowne!!!")
        ok_button = sg.Button("Ok")
        window = sg.Window("Kolumny nie są równe", [[sg.Push(), text, sg.Push()], [sg.Push(), ok_button, sg.Push()]])
        window.read()
        window.close()

def is_float(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def probki_str_na_liczby(probki_str: list[list[str]], numery_atr: list[int]) -> list[list[float]]:
    attributes = []
    for i in numery_atr:
        attributes.append([float(e[i]) for e in probki_str if is_float(e[i])])
    a_len = len(attributes[0])
    for a in attributes:
        if len(a) != a_len:
            raise ColumnsNotEvenException()
    return attributes