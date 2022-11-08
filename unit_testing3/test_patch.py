from unittest.mock import patch

def hello_world():
    print("hello world") # dependency

@patch("builtins.print")
def test_prints_hello_world(mock_print):
    hello_world() # act
    mock_print.assert_called_with("hello world") # passes