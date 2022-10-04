from app import full_name_creator
from unittest.mock import patch


@patch("builtins.input", side_effect=['Ben', 'Vakili'])
def test_full_name_creator(mock_input):
    # assemble
    expected_result = "Ben Vakili"
    
    # act
    result = full_name_creator()
    
    # assert
    assert result == expected_result