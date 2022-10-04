import time
import random


def api_call():
    time.sleep(3)
    return random.randint(1, 100)

def slow_function_with_DI(
    value,
    func_to_call=api_call):
    result = value * func_to_call()
    return result

# def slow_function_without_DI(value):
#     result = value * api_call()
#     return result