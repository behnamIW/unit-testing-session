from unittest.mock import Mock
from app import create_random_list


def test_common_case_add_two_numbers():
    # assemble
    var_1 = 10
    
    mock_random_number_getter_function = Mock(return_value=5)
    
    expected_result = [15, 15, 15, 15, 15]
    
    # act
    result = create_random_list(var_1, mock_random_number_getter_function)

    # assert 
    assert result == expected_result
    mock_random_number_getter_function.assert_called()
    assert mock_random_number_getter_function.call_count == 5
