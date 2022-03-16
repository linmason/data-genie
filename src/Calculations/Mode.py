from src.Calculations.Calculation import Calculation, number
import stats

class Mode(Calculation):
    def __init__(self):
        super().__init__("Mode", vertical=True, horizontal=True)

    def do(self, data: [list]) -> list:
        filtered_data = self.filter(data, number)
        result = []
        for rc in filtered_data:
            if rc == []:
                result.append('')
            else:
                try:
                    result.append(stats.mode(rc))
                except stats.StatsError:
                    # no distinct mode
                    result.append('')
        return result


def get_calculation():
    return Mode