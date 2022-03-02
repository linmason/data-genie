'''
Template for all Calculation children in Calculations dir
'''
number = [int, float]

def get_calculation():
    '''
    This function is an example of what you need to do in other files in this dir.
    Return the class that is the calculation so it can be auto-detected by the manager.
    '''
    return Calculation

class Calculation:
    def __init__(self, name: str, vertical: bool = False, horizontal: bool = False, twocol: bool = False):
        '''
        Subclasses may initialize any variables that might be desired, but they
        shouldn't take any parameters in their constructor.
        `name` = string that describes the new row/col
        `vertical` = bool, is this is a vertical calculation?
        `horizontal` = bool, is this is a horizontal calculation?
        `twocol` = bool, is this a two-column calculation?
        '''
        self.name = name
        self.is_vertical_calculation = vertical
        self.is_horizontal_calculation = horizontal
        self.is_twocol_calculation = twocol

    def do(self, data: [list]) -> list:
        '''
        Takes in a list of rows or columns (rc) and does the calculation on each rc.
        Returns a list that represents the new rc with results of the calculation.
        Two-column calculations will return a list of lists.
        If the calculation cannot be done on an rc, return an empty list
        '''
        pass

    '''Below are helper functions for children classes (don't re-implement them)'''
    def filter(self, data: [list], dtype: list):
        '''
        Filters data to only include values of type dtype and returns the new result
        '''
        if type(dtype) is not list:
            dtype = [dtype]
        new_data = []
        for i in range(len(data)):
            new_data.append([cell for cell in data[i] if type(cell) in dtype])
        return new_data

    def filter_out(self, data: [list], dtype: list):
        '''
        Filters out any dtype values out of data and returns it
        '''
        if type(dtype) is not list:
            dtype = [dtype]
        new_data = []
        for i in range(len(data)):
            new_data.append([cell for cell in data[i] if type(cell) not in dtype])
        return new_data
