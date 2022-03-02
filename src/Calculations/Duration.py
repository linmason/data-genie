from src.Calculations import Calculation
from datetime import datetime, timedelta

def time_to_str(time: timedelta) -> str:
    '''
    Converts timedelta object to readable string
    '''
    result = ""
    seconds = False
    days = False
    millis = False
    if time.days > 0:
        days = True
        result += f"{time.days} days"
    if time.seconds > 0:
        seconds = True
        if days:
            result += ", "
        if time.seconds > 3600:
            hours = time.seconds // 3600
            mins = (time.seconds - (3600 * hours)) // 60
            secs = time.seconds - (3600 * hours) - (60 * mins)
            result += f"{hours} hours, {mins} minutes, {secs}"
        elif time.seconds > 60:
            secs = time.seconds - (60 * (time.seconds // 60))
            result += f"{time.seconds // 60} minutes, {secs}"
        else:
            result += f"{time.seconds}"
    if time.microseconds > 0:
        millis = True
        ms = str(time.microseconds)
        while len(ms) < 6:
            ms = "0" + ms
        while ms.endswith("0"):
            ms = ms[:-1]
        if seconds:
            result += f".{ms} seconds"
        elif days:
            result += f", 0.{ms} seconds"
        else:
            result += f"0.{ms} seconds"
    if seconds and not millis:
        result += " seconds"
    return result


class Duration(Calculation.Calculation):
    def __init__(self):
        super().__init__("Sum", twocol=True)

    def do(self, data: [list]) -> [list]:
        filtered_data = self.filter(data, datetime)
        result = []
        done = [] # list of tuples of cols to avoid reversely repeated calculations
        # compare each pair of columns
        for i in range(len(data)):
            c1 = filtered_data[i]
            if len(c1) == 0:
                continue
            for j in range(len(data)):
                c2 = filtered_data[j]
                # don't do calculation if either rc is empty,
                #   if their lengths are different,
                #   if they are actually the same rc,
                #   or if the calculation has already been done on these 2 cols
                if len(c2) == 0 or len(c1) != len(c2) or c1 == c2 or (j,i) in done:
                    continue
                done.append((i,j))
                colname = f"Duration from {data[i][0]} to {data[j][0]}"
                result.append([colname] + [time_to_str(abs(c1[i] - c2[i])) for i in range(len(c2))])
        return result


def get_calculation():
    return Duration
