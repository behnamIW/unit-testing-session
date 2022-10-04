from app import slow_function_with_DI
from unittest.mock import Mock

def test_slow_function_with_DI():
    # assemble
    first_var = 5
    mock_func_to_call = Mock(return_value=10)
    expected_result = 5 * 10

    # act
    result = slow_function_with_DI(
        first_var,
        mock_func_to_call)
    
    # assert
    assert result == expected_result
