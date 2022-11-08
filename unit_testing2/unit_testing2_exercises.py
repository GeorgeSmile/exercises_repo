# import random
# def get_random_number():
#     return random.randint(1, 10)

# def add_number_with_random_number(a):
#     return a + get_random_number()

# def mock_random():
#     return(3)

# def add_num_with_random_number(a, mock_random):
#     b = mock_random()
#     if type(a) is str:
#         a = str(a)
#         b = str(mock_random())
#     else:
#         b = mock_random
#     return(a + mock_random(a))

# def test(a, mock_Random, expected):
#     actual = add_num_with_random_number
#     assert expected == actual
#     print(f"Hooray! {expected} = {actual}")


# test(2.10, mock_random, 5.10)

import random
def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random):
    return a + get_random

def test_add_number_with_random_number():
    a = 3
    expected = 6
    def mock_get_random_number():
        return 3
    result = add_number_with_random_number(a, mock_get_random_number)