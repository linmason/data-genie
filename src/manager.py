import csv
from src import parser

input_file = "data/test_sheet_0.csv"

def get_all_calculations():
    # dynamically fetches all calculations from Calculations dir
    import importlib.util
    import os
    calculations = []
    for filename in os.listdir("src/Calculations"):
        if filename.endswith(".py"):
            spec = importlib.util.spec_from_file_location("Calculations", os.path.join("src","Calculations",filename))
            calcfile = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(calcfile)
            if filename != "Calculation.py":
                calculations.append(calcfile.get_calculation())
    return calculations

def get_horizontal_calculations():
    active_calculations = []
    for calculation in get_all_calculations():
        c = calculation()
        if c.is_horizontal_calculation:
            active_calculations.append(c)
    return active_calculations

def get_vertical_calculations():
    active_calculations = []
    for calculation in get_all_calculations():
        c = calculation()
        if c.is_vertical_calculation:
            active_calculations.append(c)
    return active_calculations


def main(input_file):
    '''
    Parse input file to rows and cols
    '''
    rows, cols = parser.read_csv(input_file)

    '''
    Perform horizontal calculations
    '''
    active_calculations = get_horizontal_calculations()
    new_cols = [[]]

    # do each calculation and add it to list of new cols
    for calculation in active_calculations:
        result_col = calculation.do(rows[1:])
        new_cols.append([calculation.name] + result_col)

    ''' 
    Perform vertical calculations
    '''
    active_calculations = get_vertical_calculations()
    new_rows = []

    # do each calculation and add it to list of rows
    for calculation in active_calculations:
        result_row = calculation.do(cols)
        new_rows.append([calculation.name] + result_row)


    ''' Add new rows to list of rows, new cols to list of cols'''
    for new_row in new_rows:
        rows.append(new_row)

    for new_col in new_cols:
        cols.append(new_col)


    '''
    Add new column data to rows
    '''
    if len(cols) > len(rows[0]):
        for i,row in enumerate(rows):
            for j in range(len(row), len(cols) + 1):
                if i < len(cols[j-1]):
                    row.append(cols[j-1][i])


    '''
    Write data to new csv file
    '''
    out_file = input_file.split("/")
    out_file[-1] = "data_genie_"+out_file[-1]
    out_file = '/'.join(out_file)
    parser.write_csv(out_file, rows)


if __name__ == '__main__':
    # for testing
    main(input_file)
