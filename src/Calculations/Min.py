from src.Calculations.Calculation import Calculation, number
import numpy

class Min(Calculation):
    def __init__(self):
        super().__init__("Min", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append('')
            else:
                result.append(numpy.min(rc))
        return result


def get_calculation():
    return Min
