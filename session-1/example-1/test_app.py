import pytest
from app import price_updater

# common case
def test_common_case_price_updater():
    # assemble
    my_price_list = [10, 20, 30]
    my_increase_rate = 0.1
    expected_result = [11, 22, 33]
    
    # act
    result = price_updater(my_price_list, my_increase_rate)
    
    # assert
    assert result == expected_result


# corner case
def test_my_corner_case():
    # assemble
    my_price_list = ["10", 20, 30]
    my_increase_rate = 0.1
    expected_result = "Incorrect Price Detected!"
    
    # act
    result = price_updater(my_price_list, my_increase_rate)
    
    # assert
    assert expected_result == result


# edge case
def test_my_edge_case_price_updater():
    # scenario 1
    # assemble
    my_price_list = [0, 10 ** 5]
    my_increase_rate = 0
    expected_result = [0, 10 ** 5]
    
    # act 
    result = price_updater(my_price_list, my_increase_rate)

    # assert
    assert expected_result == result

    # scenario 2
    # assemble
    my_price_list = [0, 10 ** 5]
    my_increase_rate = 1
    expected_result = [0, 2 * (10 ** 5)]
    
    # act 
    result = price_updater(my_price_list, my_increase_rate)

    # assert
    assert expected_result == result


# ---------------------------------------------
# unhappy path tests
def test_type_error_for_increase_rate():
    # assemble
    my_price_list = [10, 20]
    my_increase_rate = "2"

    # act
    with pytest.raises(TypeError):
        price_updater(my_price_list, my_increase_rate)


def test_value_error_for_increase_rate():
    # assemble
    my_price_list = [10, 20]
    my_increase_rate = -2
    
    #act
    with pytest.raises(ValueError):
        price_updater(my_price_list, my_increase_rate)
