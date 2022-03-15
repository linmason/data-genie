from src.Calculations.Calculation import Calculation, number
import numpy

class Max(Calculation):
    def __init__(self):
        super().__init__("Max", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append(0)
            else:
                result.append(numpy.max(rc))
        return result


def get_calculation():
    return Max
