import csv

def process_data_type(raw_value):
    '''
    Tries to parse raw strings as int, float, and returns parsed value
    '''
    # the order in which to try and covert each raw_value is important!
    process_order = [int, float, str]
    for Type in process_order:
        try:
            value = Type(raw_value)
            return value
        except ValueError:
            pass
    # we should never reach this code
    raise ValueError

def read_csv(file_name):
    # read file into lists for rows, cols
    rows = []
    cols = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        first_row = True
        for row in reader:
            new_row = ['']
            for i, col_item in enumerate(row):
                item = process_data_type(col_item)
                if first_row:
                    cols.append([item])
                else:
                    cols[i].append(item)
                new_row.append(item)
            rows.append(new_row)
            first_row = False
    return rows, cols

def write_csv(file_name, rows):
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

