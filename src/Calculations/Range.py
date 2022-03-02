from src.Calculations import Calculation
import numpy

class Range(Calculation.Calculation):
    def __init__(self):
        super().__init__("Range", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append(-1)
            else:
                result.append(numpy.ptp(rc))
        return result


def get_calculation():
    return Range
