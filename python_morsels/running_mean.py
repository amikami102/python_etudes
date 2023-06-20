# running_mean.py
"""
A script implementing `running_mean()` function,
which returns the running mean of a list of numbers.
"""
from rich import print
from typing import *


def running_mean(numbers: list[float]) -> Iterator[tuple[float, float]]:
    """
    Return  a list of two-item tuples of each number in `numbers`
    and the current running mean.
    """
    running_sum = 0
    for i, n in enumerate(numbers, 1):
        running_sum += n
        yield (n, running_sum/i)


# bonus 1 (base problem version returns a list)
assert list(running_mean([2, 4, 3, 5])) == [(2, 2.0), (4, 3.0), (3, 3.0), (5, 3.5)]
assert list(running_mean([2, -1, 2, 0])) == [(2, 2.0), (-1, 0.5), (2, 1.0), (0, 0.75)]
assert list(running_mean([10, 4, 7, 5, 2, 14])) == [(10, 10.0), (4, 7.0), (7, 7.0), (5, 6.5), (2, 5.6), (14, 7.0)]

