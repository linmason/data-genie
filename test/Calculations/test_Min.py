from src.Calculations.Min import Min, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Min

def test_min():
    '''
    Test functionality of the Sum class
    '''
    c = Min()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 9.14, 5, 7, 9],
        [11, 'twelve', 13],
        ['',''],
        [1.2, 1],
        []
    ]
    expected_result = [
        2,
        1,
        11,
        0,
        1,
        0
    ]
    assert c.do(test_data) == expected_result
