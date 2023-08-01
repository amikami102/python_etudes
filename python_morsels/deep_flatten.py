# deep_flatten.py
"""
A script defining `deep_flatten()` function that accepts a list of nested iterables and returns it flattened.
"""
from typing import *


def deep_flatten(nested_iterable: Iterable[Iterable]) -> Iterator:
    """ Flatten `nested_iterable`. """
    for subiterable in nested_iterable:
        if isinstance(subiterable, Iterable) and not isinstance(subiterable, str):
            yield from deep_flatten(subiterable)
        else:
            yield subiterable


# base problem
assert list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])) \
    == [1, 2, 3, 4, 5, 6, 7, 8]
assert list(deep_flatten([[1, [2, 3]], 4, 5])) == [1, 2, 3, 4, 5]

# bonus 1, accept other iterables (except for strings)
assert sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})) ==\
    [1, 2, 3, 4, 5, 6, 7, 8]

# bonus 2, return an iterator
numbers_and_words = enumerate([99, 98, 97])
flattened = deep_flatten(numbers_and_words)
assert next(flattened) == 0
assert next(flattened) == 99
assert next(numbers_and_words) == (1, 98)

# bonus 3, make `deep_flatten()` work with strings
assert list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']])) ==\
    ['apple', 'pickle', 'pear', 'avocado']