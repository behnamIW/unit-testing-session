import random

def random_generator():
    return random.randint(1, 10)


def random_list_generator(
    n,
    function_name=random_generator
    ):
    result = []
    for _ in range(n):
        result.append(function_name())
    return result
