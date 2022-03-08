from src.Calculations.Calculation import Calculation, number
import numpy

class Average(Calculation):
    def __init__(self):
        super().__init__("Average", vertical=True, horizontal=True)
        self.sums = []
        self.ns = []
        self.first_row = True

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.average(rc))
            else:
                result.append(0)
        return result


def get_calculation():
    return Average
