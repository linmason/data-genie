from src.Calculations.Variance import Variance, get_calculation
from pytest import approx


def test_get_calculation():
    """
    Make sure the get_calculation function returns the calculation
    """
    assert get_calculation() == Variance


def test_variance():
    """
    Test functionality of the Average class
    """
    c = Variance()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [3, 3, 3, 3, 5, 100],
        [8, 2, 1, 5],
        [11, 13, 'twelve'],
        []
    ]
    expected_result = [     # these are population var, not sample var. might be wrong depending on how numpy does var
        8,
        7.891136,
        1296.5833,
        7.5,
        1,
        0
    ]
    assert c.do(test_data) == approx(expected_result)
