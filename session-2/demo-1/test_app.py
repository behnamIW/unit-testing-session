from app import Rectangle


def test_common_case_get_area():
    # assemble
    w = 5
    l = 12
    expected_result = 5 * 12
    
    # act
    my_temp_rect = Rectangle(w, l)
    result = my_temp_rect.get_area()
    
    # assert
    assert result == expected_result
