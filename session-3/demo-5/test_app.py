from app import add_price
from unittest.mock import patch


@patch("builtins.input")
def test_add_price(mock_input):
    # assemble
    mock_input.return_value = "10"
    price_list_var = [1, 2]
    expected_result = [1, 2, 10]
    
    # act
    result = add_price(price_list_var)
    
    # assert
    assert result == expected_result

    