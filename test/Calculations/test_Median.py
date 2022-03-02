from src.Calculations.Median import Median, get_calculation
from pytest import approx


def test_get_calculation():
    """
    Make sure the get_calculation function returns the calculation
    """
    assert get_calculation() == Median


def test_median():
    """
    Test functionality of the Median class
    """
    c = Median()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [3, 3, 3, 3, 5, 100],
        [8, 2, 1, 5],
        [11, 13, 'twelve'],
        []
    ]
    expected_result = [
        6,
        5,
        3,
        3.5,
        12,
        0
    ]
    assert c.do(test_data) == approx(expected_result)
