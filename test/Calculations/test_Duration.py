from src.Calculations.Duration import Duration, get_calculation, time_to_str
from datetime import datetime, timedelta

def test_get_calculation():
    '''
    Make sure the get_calculation function returns the calculation
    '''
    assert get_calculation() == Duration

def test_duration():
    '''
    Test functionality of the Duration class
    '''
    c = Duration()
    test_data = [
        ["Header1", datetime(2019, 1, 20), datetime(2018, 5, 3), datetime(2020, 2, 2)],
        ["Header2", "not a date", "not a date", "not a date"],
        ["Header3", datetime(2020, 1, 1), "", datetime(2020, 1, 2)],
        ["Header4", datetime(2019, 2, 20), datetime(2019, 5, 3), datetime(2022, 2, 10)]
    ]
    expected_result = [
        ["Duration from Header1 to Header4", time_to_str(timedelta(days=31)),
         time_to_str(timedelta(days=365)), time_to_str(timedelta(days=739))]
    ]
    assert c.do(test_data) == expected_result

def test_time_to_str():
    # days only
    assert time_to_str(timedelta(days=85)) == "85 days"
    # seconds only
    assert time_to_str(timedelta(seconds=58)) == "58 seconds"
    # seconds only (and minutes)
    assert time_to_str(timedelta(seconds=365)) == "6 minutes, 5 seconds"
    # seconds only (and hours)
    assert time_to_str(timedelta(seconds=3630)) == "1 hours, 0 minutes, 30 seconds"
    # seconds only (and minutes and hours)
    assert time_to_str(timedelta(seconds=4590)) == "1 hours, 16 minutes, 30 seconds"
    # microseconds only
    assert time_to_str(timedelta(microseconds=500)) == "0.0005 seconds"
    # microseconds and seconds
    assert time_to_str(timedelta(seconds=12, microseconds=510)) == "12.00051 seconds"
    # microseconds and days
    assert time_to_str(timedelta(days=3, microseconds=4010)) == "3 days, 0.00401 seconds"
    # seconds and days
    assert time_to_str(timedelta(days=4, seconds=26)) == "4 days, 26 seconds"
    # everything
    assert time_to_str(timedelta(days=71, seconds=4589, microseconds=217650)) == "71 days, 1 hours, 16 minutes, 29.21765 seconds"
