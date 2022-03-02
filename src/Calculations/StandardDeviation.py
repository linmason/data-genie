from src.Calculations import Calculation
import numpy

class StandardDeviation(Calculation.Calculation):
    def __init__(self):
        super().__init__("Standard Deviation", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.std(rc))
            else:
                result.append(0)
        return result       # these are population std, not sample std


def get_calculation():
    return StandardDeviation
