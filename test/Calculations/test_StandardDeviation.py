from src.Calculations.StandardDeviation import StandardDeviation, get_calculation
from pytest import approx


def test_get_calculation():
    """
    Make sure the get_calculation function returns the calculation
    """
    assert get_calculation() == StandardDeviation


def test_standard_deviation():
    """
    Test functionality of the StandardDeviation class
    """
    c = StandardDeviation()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [3, 3, 3, 3, 5, 100],
        [8, 2, 1, 5],
        [11, 13, 'twelve'],
        []
    ]
    expected_result = [     # these are population std, not sample std
        2.8284271,
        2.8091166,
        36.008101,
        2.7386128,
        1,
        0
    ]
    assert c.do(test_data) == approx(expected_result)
