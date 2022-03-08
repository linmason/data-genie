from src.parser import CsvParser
import os

# if you change this variable name, also change the identical string
# in /templates/result.html
output_file = "data_genie_output.csv"
## TODO: this should only be defined once, but is also defined in app.py
input_folder = "uploads"
output_folder = "downloads"

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

def get_twocol_calculations():
    active_calculations = []
    for calculation in get_all_calculations():
        c = calculation()
        if c.is_twocol_calculation:
            active_calculations.append(c)
    return active_calculations


def main(input_file):
    '''
    Parse input file to rows and cols
    '''
    parser = CsvParser()
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

    '''
    Perform two-column calculations
    '''
    active_calculations = get_twocol_calculations()

    # do each calculation and add it to list of rows
    for calculation in active_calculations:
        result_cols = calculation.do(cols)
        for new_col in result_cols:
            new_cols.append(new_col)


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
    parser.write_csv(os.path.join(output_folder, output_file), rows)


if __name__ == '__main__':
    print("Currently this file cannot be run on its own")
    print("Start the website using flask and use the GUI")
