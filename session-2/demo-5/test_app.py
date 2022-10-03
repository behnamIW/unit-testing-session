from unittest.mock import Mock
from app import Rectangle


def test_common_case_get_price():
    # assemble
    w = 5
    l = 20
    
    mock_get_todays_price_per_unit = Mock(return_value=6)

    expected_result = 5 * 20 * 6
    
    # act
    my_rect = Rectangle(w, l)
    result = my_rect.get_price(mock_get_todays_price_per_unit)
    
    # assert
    assert result == expected_result
    assert mock_get_todays_price_per_unit.call_count == 1
