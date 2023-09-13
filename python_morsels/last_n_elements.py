# last_n_elements.py
"""
A script defining `last_n_elements()`, which returns a slice of last N elements.
"""
from typing import *

def last_n_elements(mylist: list, n: int, *, reverse: bool = False) -> slice:
    """
    Return last `n` elements of `mylist`.
    Reverse the order of the slice if `reverse` is True.
    """
    if not n:
        return []
    return mylist[-n::] if not reverse else mylist[-n::][::-1]


# base problem
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
assert last_n_elements(fruits, 3) == ['peaches', 'apricots', 'bananas']
assert last_n_elements(fruits, 1) == ['bananas']
numbers = [41, 25, 54, 15, 76, 68, 32, 38]
assert last_n_elements(numbers, 4) == [76, 68, 32, 38]
assert last_n_elements(numbers, 0) == []

# bonus 1, test `reverse` argument
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
assert last_n_elements(fruits, 3, reverse=False) ==\
    ['peaches', 'apricots', 'bananas']
assert last_n_elements(fruits, 3, reverse=True) ==\
    ['bananas', 'apricots', 'peaches']