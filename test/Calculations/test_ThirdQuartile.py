from src.Calculations.ThirdQuartile import ThirdQuartile, get_calculation
from pytest import approx


def test_get_calculation():
    """
    Make sure the get_calculation function returns the calculation
    """
    assert get_calculation() == ThirdQuartile


def test_third_quartile():
    """
    Test functionality of the ThirdQuartile class
    """
    c = ThirdQuartile()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [3, 3, 3, 3, 5, 100],
        [8, 2, 1, 5],
        [11, 13, 'twelve'],
        []
    ]
    expected_result = [
        8,
        7,
        4.5,
        5.75,
        12.5,
        ''
    ]
    assert c.do(test_data) == approx(expected_result)
