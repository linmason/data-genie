from src.Calculations import Calculation
import numpy

class Count(Calculation.Calculation):
    def __init__(self):
        super().__init__("Count", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = [[x for x in rc if x != ''] for rc in data]
        result = []
        for rc in filtered_data:
            result.append(len(rc))
        return result


def get_calculation():
    return Count
