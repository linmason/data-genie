from src.Calculations.Calculation import Calculation, number
import numpy

class Sum(Calculation):
    def __init__(self):
        super().__init__("Sum", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if rc != []:
                result.append(numpy.sum(rc))
            else:
                result.append('')
        return result


def get_calculation():
    return Sum
