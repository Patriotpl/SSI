import math
import PySimpleGUI as sg

from random import choice
from numpy import arange
from time import sleep


def y(x: float) -> float:
    return math.sin(x / 10) * math.sin(x / 200)

def zad1(variability_range: tuple[int, int], iterations: int, spread: float, growth: float, window: sg.Window, decimal_places: int) -> float:
    result = 0
    if spread < 0:
        spread = -spread

    x = choice(arange(variability_range[0], variability_range[1], 10**-decimal_places))
    sleep(1)
    for i in range(iterations):
        x_pot = round(x + choice(arange(-spread, spread, 10**-decimal_places)), decimal_places)
        if x_pot > variability_range[1]:
            x_pot = variability_range[1]
        y_pot = y(x_pot)
        if y_pot >= y(x):
            x = x_pot
            spread = round(spread * growth, 5)
        else:
            spread = round(spread / growth, 5)
        print(i, x, y(x), spread)
        # graph.draw_point((x, y(x)), 0.2)
        window.write_event_value("-DRAW_POINT-", (float(x), y(x)))
    return result