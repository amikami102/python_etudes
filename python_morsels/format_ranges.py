# format_ranges.py
"""
A script defining `format_ranges()` function that takes a list of numbers and returns a string that groups ranges of consecutive numbers.
"""
from typing import *
from collections import Counter


def find_ranges(unique_numbers: Iterable[int]) -> Iterator[tuple[int, int]]:
    """ Groups consecutive numbers into range pairs. """
    first = last = None
    for k in unique_numbers:
        if not first:
            first = last = k
        elif k == last + 1:
            last = k
            continue
        else:
            yield first, last
            first = last = k
    yield first, last


def pair_numbers(numbers: Iterable[int]) -> Iterator[tuple[int, int]]:
    """ Pair range of consecutive numbers. Everytime a pair is found, remove the numbers in the range from `numbers`. """
    collections = Counter(numbers)
    while collections:
        pairs = list(find_ranges(sorted(collections.keys())))
        collections -= Counter({k: 1 for n, m in pairs for k in range(n, m+1) })
        yield from pairs


def format_ranges(numbers: Iterable[int]) -> str:
    """ Format `numbers` into a string that groups ranges of consecutive numbers. """
    return ','.join(
        (
            f'{n}-{m}' if n !=m else str(n)
            for n, m in sorted(pair_numbers(numbers))
        )
    )


# base problem
assert format_ranges([1, 2, 3, 4, 5, 6, 7, 8]) == '1-8'
assert format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11]) ==\
    '1-3,5-8,10-11'
numbers = [3, 4, 15, 16, 17, 19, 20]
assert format_ranges(n+1 for n in numbers) ==\
    '4-5,16-18,20-21'

# bonus 1, return singletons as singletons
assert format_ranges([4]) == '4'
assert format_ranges([1, 3, 5, 6, 8]) == '1,3,5-6,8'

# bonus 2, allow for input iterables to be unordered
assert format_ranges([9, 1, 7, 3, 2, 6, 8]) == '1-3,6-9'

# bonus 3, return duplicates as separate ranges
numbers = [1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7]
assert format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7]) ==\
    '1-2,1-4,4,7,7-9'
assert format_ranges([1, 3, 5, 6, 8]) == '1,3,5-6,8'