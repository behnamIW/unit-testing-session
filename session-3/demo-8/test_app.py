from app import add_multiple_products
from unittest.mock import patch


@patch("builtins.input", side_effect=["pepsi", "coke", "fanta"])
def test_add_multiple_products(mock_input):
    # assemble
    init_products = ["P1", "p2"]
    n = 3
    expected_result = ["P1", "p2", "pepsi", "coke", "fanta"]
    
    # act
    result = add_multiple_products(init_products, n)

    # assert
    assert expected_result == result
    assert mock_input.call_count == 3
