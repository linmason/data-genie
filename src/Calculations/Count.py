from src.Calculations import Calculation
import numpy

class Count(Calculation.Calculation):
    def __init__(self):
        super().__init__("Count", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        result = []
        for rc in data:
            result.append(rc.size)
        return result


def get_calculation():
    return Count
