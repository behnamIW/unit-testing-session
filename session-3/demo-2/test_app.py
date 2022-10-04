from app import slow_function_without_DI
from unittest.mock import patch


@patch("app.api_call")
def test_slow_function_without_DI(mock_api_call):
    # S1
    # assemble
    mock_api_call.return_value = 10
    first_var = 5
    expected_result = 5 * 10

    # act
    result = slow_function_without_DI(first_var)
    
    # assert
    assert result == expected_result
    print('mock_api_call.call_count:', mock_api_call.call_count)
    assert mock_api_call.call_count == 1
    
