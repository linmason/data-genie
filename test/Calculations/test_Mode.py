from src.Calculations.Mode import Mode, get_calculation

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Mode

def test_mode():
    '''
    Test functionality of the Sum class
    '''
    c = Mode()
    test_data = [
        [2, 4, 8, 8, 10],
        [1, 9.14, 5, 7, 9.14],
        ['twelve', 'twelve', 13, 13],
        ['',''],
        [1.0, 1],
        []
    ]
    expected_result = [
        8,
        9.14,
        13,
        -1,
        1,
        -1
    ]
    assert c.do(test_data) == expected_result
