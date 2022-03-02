from src.Calculations.Range import Range, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Range

def test_range():
    '''
    Test functionality of the Sum class
    '''
    c = Range()
    test_data = [
        [2, 4, 6, 8, 10],
        [1, 9.14, 5, 7, 9],
        [11, 'twelve', 13],
        ['',''],
        [1.0, 1],
        []
    ]
    expected_result = [
        8,
        8.14,
        2,
        -1,
        0,
        -1
    ]
    assert c.do(test_data) == expected_result
