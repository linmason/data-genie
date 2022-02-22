from src.Calculations import Calculation
import numpy


class Variance(Calculation.Calculation):
    def __init__(self):
        super().__init__("Variance", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.var(rc))
            else:
                result.append(0)
        return result


def get_calculation():
    return Variance
