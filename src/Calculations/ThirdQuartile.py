from src.Calculations import Calculation
import numpy


class ThirdQuartile(Calculation.Calculation):
    def __init__(self):
        super().__init__("Third Quartile", vertical=True, horizontal=False)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter_out(data, str)
        result = []
        for rc in filtered_data:
            if len(rc) > 0:
                result.append(numpy.quantile(rc, 0.75))
            else:
                result.append(0)
        return result


def get_calculation():
    return ThirdQuartile
