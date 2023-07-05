# tail.py
"""
A script defining `tail()`, which returns the last `n` elements from a given sequence.
"""
from typing import *
from collections import deque

def tail(iterable: Iterable, n: int) -> Sequence:
    """ Return the last `n` elements of `sequence`. """
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
    

# base problem
assert tail([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert tail('hello', 2) == ['l', 'o']
assert tail('hello', 0) == []

# bonus 1, test that `tail()` return empty list for negative values of `n`
assert tail('hello', -2) == []

# bonus 2, test that `tail()` works with any iterable, not just sequences
squares = (n**2 for n in range(10))
assert tail(squares, 3) == [49, 64, 81]