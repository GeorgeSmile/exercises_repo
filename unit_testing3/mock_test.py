from unittest.mock import Mock
# from random import random

def add_two_numbers(a,b):
    return a+b

def test_add_two_numbers():
    #creates a new mock instance
    mock_get_random_number = Mock()
    mock_get_random_number.return_value = 5

    expected = 10
    actual = add_two_numbers(5, mock_get_random_number)
    assert expected == actual
    print("done")

