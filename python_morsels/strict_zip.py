# strict_zip.py
"""
A script defining `strict_zip()` function that acts like the built-in `zip` function
but looping over sequences with different lengths will raise an exception.
"""
from typing import *

from rich import print


def strict_zip(*args) -> Iterable[tuple]:
    sequences = [list(seq) for seq in args]
    if not all(len(seq)==len(args[0]) for seq in sequences):
        raise ValueError("The arguments don't have the same length")
    return zip(*sequences)
    

# base problem
for number, letter in strict_zip((1, 2, 3), 'abc'):
    print(number, letter)

for items in strict_zip([1, 2], [3, 4], [5, 6], [7, 8]):
    print(items)

assert list(strict_zip()) == []

for letters in strict_zip('here', 'are', 'four', 'sequences'):
    print(*letters) # expect ValueError to be raised