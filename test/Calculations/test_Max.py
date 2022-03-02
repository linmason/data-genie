from src.Calculations.Max import Max, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Max

def test_max():
    '''
    Test functionality of the Sum class
    '''
    c = Max()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 9.14, 5, 7, 9],
        [11, 'twelve', 13],
        ['',''],
        [1.2, 1],
        []
    ]
    expected_result = [
        10,
        9.14,
        13,
        0,
        1.2,
        0
    ]
    assert c.do(test_data) == expected_result
