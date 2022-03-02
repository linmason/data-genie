from src.Calculations import Calculation
import numpy

class Min(Calculation.Calculation):
    def __init__(self):
        super().__init__("Min", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append(0)
            else:
                result.append(numpy.min(rc))
        return result


def get_calculation():
    return Min
