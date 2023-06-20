# min_n.py
"""
A script defining `min_n()` function.
"""
from heapq import nsmallest 
from typing import *


def min_n(iterable: Iterable, n: int = 0, key: Callable = None) -> Iterable:
    """ Return the `n` smallest items in `iterable`."""
    if not n:
        n = len(iterable)
    return nsmallest(n, iterable, key=key)