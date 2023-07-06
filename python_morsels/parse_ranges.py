# parse_ranges.py
"""
A script defining `parse_ranges()`, which accepts a string containing ranges of numbers and returns an iterable of those numbers.
"""
from typing import *
import re

RANGE_SINGLETON_RE = re.compile(r'''
\b				# word boundary
\d+-\d+			# paired range of digits, e.g. '1-12'
\b				# word boundary
|				# or ...
\b				# word boundary
\d+				# singleton, e.g. '20'
\b				# word boundary
''', re.VERBOSE)


def parse_ranges(ranges: str) -> Iterator[int]:
    """ Parse the ranges of numbers in `ranges` and return an iterable of those numbers. """
    for substring in RANGE_SINGLETON_RE.findall(ranges):
        try:
            start, stop = (int(s) for s in substring.split('-'))
        except ValueError:
            stop = start = int(substring)
        finally:
            yield from range(start, stop + 1)


# base problem
assert list(parse_ranges('1-2,4-4,8-13')) == [1, 2, 4, 8, 9, 10, 11, 12, 13]
assert list(parse_ranges('0-0, 4-8, 20-20, 43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

# bonus 1, test that `parse_ranges()` returns an iterator
numbers = parse_ranges('100-10000')
assert next(numbers) == 100
assert next(numbers) == 101

# bonus 2, test that the string can include singletons
assert list(parse_ranges('0,4-8,20,43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

# bonus 3, test that `parse_ranges()` is compatible with `coverage.py` output
assert list(parse_ranges('0, 4-8, 20->exit, 43-45')) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]