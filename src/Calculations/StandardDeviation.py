from src.Calculations.Calculation import Calculation, number
import numpy

class StandardDeviation(Calculation):
    def __init__(self):
        super().__init__("Standard Deviation", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.std(rc))
            else:
                result.append('')
        return result       # these are population std, not sample std


def get_calculation():
    return StandardDeviation
