from src import manager

def test_always_passes():
    '''
    if this test doesn't pass, something is wrong with testing framework
    '''
    assert True

def test_get_all_calculations():
    '''
    tests that the list of calculations is not empty
    '''
    assert len(manager.get_all_calculations()) > 0

def test_get_horizontal_calculations():
    '''
    tests that the list of horizontal calculations is not empty
    and is a subset of all the calculations
    '''
    assert 0 < len(manager.get_horizontal_calculations()) <= len(manager.get_all_calculations())

def test_get_vertical_calculations():
    '''
    tests that the list of horizontal calculations is not empty
    and is a subset of all the calculations
    '''
    assert 0 < len(manager.get_vertical_calculations()) <= len(manager.get_all_calculations())
