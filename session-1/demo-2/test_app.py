import pytest
from app import add_two_numbers


# corner case
def test_my_corner_case():
    # assemble 
    first_var = '10'
    second_var = 20
    
    with pytest.raises(Exception):
        add_two_numbers(first_var, second_var)

def test_my_corner_case_with_two_strings():
    # assemble 
    first_var = '10'
    second_var = '20'
    
    with pytest.raises(Exception):
        add_two_numbers(first_var, second_var)
    

