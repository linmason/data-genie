from src.Calculations.Count import Count, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Count

def test_count():
    '''
    Test functionality of the Sum class
    '''
    c = Count()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 3.14, 5, 7, 9],
        [11, 'twelve', 13],
        ['',''],
        [1.0, 1],
        []
    ]
    expected_result = [
        5,
        5,
        3,
        2,
        2,
        0
    ]
    assert c.do(test_data) == expected_result
