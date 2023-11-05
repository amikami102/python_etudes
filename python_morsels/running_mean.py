# running_mean.py
"""
A script implementing `running_mean()` function, which returns
the running mean of a list of numbers.
"""
from numbers import Number
from typing import *


def running_mean(numbers: Iterable[Number]) -> Iterator[tuple[Number, Number]]:
    """
    Generate a two-item tuple of current value in `numbers` and the running mean.
    """
    running_sum = 0
    for i, n in enumerate(numbers, start=1):
        running_sum += n
        yield (n, running_sum/i)


# base problem and bonus 1 (base problem version returns a list)
assert list(running_mean([2, 4, 3, 5])) == [(2, 2.0), (4, 3.0), (3, 3.0), (5, 3.5)]
assert list(running_mean([2, -1, 2, 0])) == [(2, 2.0), (-1, 0.5), (2, 1.0), (0, 0.75)]
assert list(running_mean([10, 4, 7, 5, 2, 14])) == [(10, 10.0), (4, 7.0), (7, 7.0), (5, 6.5), (2, 5.6), (14, 7.0)]
