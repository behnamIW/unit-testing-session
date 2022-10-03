from app import random_list_generator


def test_common_case_random_list_generator():
    # assemble
    number_of_items = 5
    
    def mock_random_generator():
        return 1
    
    expected_result = [1, 1, 1, 1, 1]
    
    # act 
    result = random_list_generator(5, mock_random_generator)
    
    # assert
    assert result == expected_result
    
    
