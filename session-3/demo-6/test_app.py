from app import print_name
from unittest.mock import patch


@patch("builtins.input", side_effect=['Ben'])
@patch("builtins.print")
def test_print_name(mock_print, mock_input):
    # assemble
    expected_args = "Hello, Ben!"
    
    # act
    print_name()
    
    # assert
    mock_print.assert_called_with(expected_args)
