from unittest import mock
from app import greeting
from unittest.mock import patch


@patch("builtins.input")
def test_greeting(mock_input):
    # assemble
    mock_input.return_value = "John"
    expected_result = "Nice to meet you, John"
    
    # act
    result = greeting()
    
    # assert
    assert result == expected_result
