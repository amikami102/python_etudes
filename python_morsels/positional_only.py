# positional_only.py
"""
A script defining `@positional_only` decorator that requires all function
arguments to be positional-only arguments.
"""
from typing import *
from functools import wraps


def positional_only(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Any:
        """Only pass positional arguments into `func`."""
        return func(*args)
    return wrapper


# base problem
@positional_only
def divide(x, y):
    return x / y

assert divide(437, 19) == 23.0
try:
    divide(437, y=19)
except TypeError as e:
    print('passed')
    print(e)
else:
    print('failed')

@positional_only
def my_func(a, b=2, **kwargs): return a

assert my_func(3) == 3
try:
    my_func(3, b=3)
except TypeError:
    print('passed')
try:
    my_func(3, a=3)
except TypeError:
    print('passed')
    
# bonus 1, specify number of arguments that are positional
@positional_only(1)
def product(iterable, /, start=1):
    """Return the product of start and the given iterable of numbers"""
    total = start
    for n in iterable:
        total *= n
    return total

assert product([1, 2, 3]) == 6
assert product([1, 2, 3], 2) == 12
assert product([1, 2, 3], start=2) == 12
try:
    product(iterable=[1, 2, 3], start=2)
except TypeError as e:
    print(e)
else:
    print('failed')