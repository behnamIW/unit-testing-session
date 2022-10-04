# Unit Testing 3 Exercises

1. Write a python function named `add_product` that when you call it, it will ask user to type product name in terminal (using input() function), then, if user writes a product name that already exists in the `products_list` it should return `products_list` without any change, otherwise it should add the product name that user wrote in terminal to the the end of `products_list` and then return it.

- Write at least two unit-tests to verify its functionality for both scenarios.

Hint: you need to patch `input` function in your tests.

The initial implementation of the function is like this:

```py
def add_product(products_list):
    pass
```

1. Write a unit test for the below function. You will need to patch the `input` and `print` function. Assert what the `print` function was called with, and assert how many times the `input` and `print` function were respectively called.

You will need to figure out how to supply two different values for both `input` calls. [Here's a hint](https://stackoverflow.com/a/55580216).

```py
def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f'Thank you, your name is {name} and your age is {age}')
```
