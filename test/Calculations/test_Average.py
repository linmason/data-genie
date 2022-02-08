from src.Calculations.Average import Average, get_calculation
from pytest import approx

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Average

def test_average():
    '''
    Test functionality of the Average class
    '''
    c = Average()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [11, 'twelve', 13],
        []
    ]
    expected_result = [
        6,
        5.028,
        12,
        0
    ]
    assert c.do(test_data) == approx(expected_result)
