def add_two_numbers(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    raise Exception
