from src.Calculations import Calculation
import numpy

class Max(Calculation.Calculation):
    def __init__(self):
        super().__init__("Max", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append(0)
            else:
                result.append(numpy.max(rc))
        return result


def get_calculation():
    return Max
