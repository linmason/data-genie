from src.Calculations.FirstQuartile import FirstQuartile, get_calculation
from pytest import approx


def test_get_calculation():
    """
    Make sure the get_calculation function returns the calculation
    """
    assert get_calculation() == FirstQuartile


def test_first_quartile():
    """
    Test functionality of the FirstQuartile class
    """
    c = FirstQuartile()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [3, 3, 3, 3, 5, 100],
        [8, 2, 1, 5],
        [11, 13, 'twelve'],
        []
    ]
    expected_result = [
        4,
        3.14,
        3,
        1.75,
        11.5,
        ''
    ]
    assert c.do(test_data) == approx(expected_result)
