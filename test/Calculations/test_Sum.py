from src.Calculations.Sum import Sum, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Sum

def test_sum():
    '''
    Test functionality of the Sum class
    '''
    c = Sum()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [11, 'twelve', 13],
        []
    ]
    expected_result = [
        30,
        25.14,
        24,
        0
    ]
    assert c.do(test_data) == expected_result
