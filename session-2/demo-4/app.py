import random


def random_number_getter_function():
    return random.randint(1, 10)

def create_random_list(a,
                    function_name=random_number_getter_function
                    ):
    result = []
    for _ in range(5):
        result.append(a + function_name())
    return result 


print(create_random_list(2))