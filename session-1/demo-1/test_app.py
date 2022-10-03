from app import add_tow_numbers


def test_my_common_case():
    # assemble
    my_first_var = 10
    my_second_var = 15
    expected_result = 25
    
    # act
    result = add_tow_numbers(my_first_var, my_second_var)
    
    # assert
    assert expected_result == result
    

test_my_common_case()
