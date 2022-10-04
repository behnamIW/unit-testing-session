from unittest.mock import patch
from app import hello_to_you


@patch('builtins.print')
def test_hello_to_you(mock_print):
    # assemble
    name_var = "Jessica"
    expected_terminal_output = "Hello, Jessica!"
    
    # act
    hello_to_you(name_var)
    
    # assert
    mock_print.assert_called_with(expected_terminal_output)
    