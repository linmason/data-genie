from src.parser import process_data_type
from datetime import datetime

'''
Tests for process_data_type (one test per different type)
'''
def test_process_date():
    data = [
        "1/30/2019",
        "Jan 30, 2019",
        "1/30/19"
    ]
    expected = [
        datetime(2019, 1, 30),
        datetime(2019, 1, 30),
        datetime(2019, 1, 30)
    ]
    for i in range(len(data)):
        val = process_data_type(data[i])
        assert val == expected[i], \
            f"processed data type for cell='{data[i]}' was {val}, type {type(val)} (expected date)"

def test_process_int():
    assert process_data_type("5") == 5

def test_process_float():
    assert process_data_type("3.14") == 3.14

def test_process_str():
    assert process_data_type("string") == "string"
    assert process_data_type("") == ""
