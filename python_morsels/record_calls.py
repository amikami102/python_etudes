# record_calls.py
"""
A script defining a decorator function, `record_calls`, that records the number of times a function is called.
"""
from typing import *

T = TypeVar('T')


def record_calls(func: Callable) -> Callable:
    """ Return a version of `func` that record calls made on it."""
    def new_func(*args, **kwargs) -> T:
        return_value = func(*args, **kwargs)
        new_func.call_count += 1
        return return_value
    new_func.call_count = 0
    return new_func


# base problem
@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")

greet('Trey')
assert greet.call_count == 1
greet()
assert greet.call_count == 2