'''
Performs the calculations on the data.


Will receive from calc_manager.py:
- a column(s) of data from the table
- a number corresponding to data type of the column(s) (0 = number, etc.)

Will do:
- check the data type of the column(s)
- perform the corresponding method for the data type
    - this method will include all the functions for that type
    - for example, the num_calculations() method will include sum(), avg(), etc.

Will NOT do:
- check if a calculation can be done on a function level
    - sum() won't check if the column is full of numbers
- any calculations that cannot be done for a specific data type
    - will not call sum() on a column of dates
    
Will return to calc_manager.py:
- a list of completed calculations for the column(s)
    - this includes vertical, single-column horizontal, and/or double-column
      horizontal calculations for the column(s)
'''

import numpy as np

class Calculator:
    def __init__(self, col):
        self.col = col
        self.new_columns = {}
        self.new_rows = {}
    
    def sum(self, col):
        """
        Calculates sum of dataset.

        Parameters:
            col: an individual column of numbers from the dataset (as a list)
        """
        return np.sum(col)
    
    def avg(self, col):
        """
        Calculates average of dataset.

        Parameters:
            col: an individual column from the dataset (as a list)
        """
        pass

    def median(self, col):
        """
        Calculates median of dataset.
        
        Parameters:
            col: an individual column from the dataset (as a list)
        """
        pass

    def range(self, col):
        """
        Calculates range of dataset.
        
        Parameters:
            col: an individual column from the dataset (as a list)
        """
        pass

    def perform_all_calcs(self, col):
        """
        Performs all of the possible calculations on the column provided.
        
        Parameters:
            lists: one or more lists do perform calculator
        Returns:
            new_columns, new_rows
        """
        new_rows = self.perform_all_vertical_calcs(col)
        new_columns = self.perform_all_horizontal_calcs(col)
        return new_columns, new_rows

    def perform_all_vertical_calcs(self, ):
        """
        Performs all vertical calculations.
        
        Returns:
            new_row
        """
        pass
    
    def perform_all_horizontal_calcs(self, ):
        """
        Performs all horizontal calculations.

        Returns:
            new_columns
        """
        pass

    def perform_multi_column_horizontal_calcs(self, ):
        """
        Performs all multi-column calculations.
        """
        pass

    def perform_single_column_horizontal_calcs(self, ):
        """
        Performs all single-column horizontal calculations.
        """
        pass


if __name__ == "__main__":
    calc = Calculator()
    calc.sum()