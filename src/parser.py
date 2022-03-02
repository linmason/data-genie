import csv
from dateutil import parser
from datetime import datetime

def _date(s):
    date = parser.parse(s)
    return date

def process_data_type(raw_value):
    '''
    Tries to parse raw strings as int, float, and returns parsed value
    '''
    # the order in which to try and covert each raw_value is important!
    process_order = [int, float, _date, str]
    for Type in process_order:
        try:
            value = Type(raw_value)
            return value
        except ValueError:
            pass
    # we should never reach this code
    raise ValueError

class CsvParser:
    def __init__(self):
        # dates will record row index as key,
        # tuple (j, s) where j in index in row of date and s is raw string of date
        self.dates = {}

    def read_csv(self, file_name):
        # read file into lists for rows, cols
        rows = []
        cols = []
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            first_row = True
            for r, row in enumerate(reader):
                new_row = ['']
                for i, col_item in enumerate(row):
                    item = process_data_type(col_item)
                    # if item is date, store raw info
                    if type(item) is datetime:
                        if r not in self.dates:
                            self.dates[r] = []
                        self.dates[r].append((i, col_item))
                    if first_row:
                        cols.append([item])
                    else:
                        cols[i].append(item)
                    new_row.append(item)
                rows.append(new_row)
                first_row = False
        return rows, cols

    def write_csv(self, file_name, rows):
        # fix dates
        for i_row in self.dates:
            for (i, raw_str) in self.dates[i_row]:
                i += 1   # offset to account for added "row header" column
                rows[i_row][i] = raw_str
        # write to output file
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
