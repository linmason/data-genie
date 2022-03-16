from src.Calculations.Calculation import Calculation, number
import numpy


class Variance(Calculation):
    def __init__(self):
        super().__init__("Variance", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.var(rc))
            else:
                result.append('')
        return result       # these are population var, not sample var


def get_calculation():
    return Variance
