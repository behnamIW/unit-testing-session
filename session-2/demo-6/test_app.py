from app import random_list_generator
from unittest.mock import Mock


def test_common_case_random_list_generator():
    # assemble
    var_1 = 6
    
    mock_random_generator = Mock(return_value=5)
    
    expected_result = [5, 5, 5, 5, 5, 5]
    
    # act
    result = random_list_generator(var_1, mock_random_generator)
    
    # assert 
    assert result == expected_result
    assert mock_random_generator.call_count == 6

    
