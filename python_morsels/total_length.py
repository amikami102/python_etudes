# total_length.py
"""
A script defining a function, `total_length()`, which returns the sum of the lengths of objects.
"""
from typing import *
from operator import length_hint


def ilen(iterator: Iterator) -> int:
    """ Get the length of `iterator` without `__len__` attribute."""
    return sum(1 for _ in iterator)

def total_length(*iterables, use_hints: bool = False) -> int:
    """
    Add the length of `iterables`.
    The code will use the iterable object's `__len__` attribute.
    If TypeError is raised, the object's `__length_hint__` is used if `use_hints` is True
    and the hinted length is nonzero. Otherwise, `ilen` is used to get the length of iterables
    that do not support `len`.
    """
    total = 0
    for iterable in iterables:
        try:
            total += len(iterable)
        except TypeError:
            hint = length_hint(iterable)
            if use_hints and hint:
                total += hint
            else:
                total += ilen(iterable)
    return total


# base problem
assert total_length([4, 5], (6, 7)) == 4
assert total_length('hello', {'red': 50, 'purple': 100}) == 7

# bonus 1, accepts iterables that don't have lengths
numbers = [4, 6, 8, 9]
assert total_length(enumerate(numbers), (n**2 for n in numbers))
assert total_length(n for n in numbers if n % 2 == 0) == 3

# bonus 2, work efficiently for large-sized objects that have a known length
assert total_length(range(1000), range(1000000000)) == 1000001000

# bonus 3, test `use_hints` keyword argument
assert total_length(reversed(range(1000000000)), use_hints=True) == 1000000000

class LengthHinter:
    def __init__(self, items, hinted_length):
        self.length = hinted_length
        self.items = items

    def __iter__(self):
        yield from self.items

    def __length_hint__(self):
        return self.length

things = LengthHinter([1, 2], 10)
things2 = LengthHinter([100, 50, 20, 30, 10], 0)
assert total_length(things, things, use_hints=True) == 20
assert total_length(things2, things2, use_hints=True) == 10
