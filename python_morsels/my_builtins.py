# my_builtins.py
"""
A script reimplementing built-in functions: `len`, `sum`, and `all`.
"""
from rich import print


def _len(enumerable) -> int:
    """ Return the number of elements in `enumerable`. """
    if '__len__' not in dir(enumerable):
        raise TypeError(f"object of type {type(enumerable).__name__!r} has no len()")
    else:
        length = 0
        for _ in enumerable:
            length += 1
        return length


def _sum(iterable, start: int = 0) -> int:
    """ Return the sum of the elements in `iterable`. Add `start` to the sum. """
    total = start
    for item in iterable:
        if isinstance(item, str):
            raise TypeError
        else:
            total += item
    return total


def _all(iterable) -> bool:
    """ Return True if all the items in `iterable` are true, otherwise return False."""
    return not any(bool(it) == False for it in iterable)


print(_sum({1,2,3},3))
print(_sum([]))
