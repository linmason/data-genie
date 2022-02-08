from src.Calculations import Calculation
import numpy

class Sum(Calculation.Calculation):
    def __init__(self):
        super().__init__("Sum", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            result.append(numpy.sum(rc))
        return result


def get_calculation():
    return Sum
