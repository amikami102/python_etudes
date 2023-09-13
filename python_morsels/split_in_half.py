# split_in_half.py
"""
A script defining `split_in_half()`, which splits a list in half.
"""
from typing import *


def split_in_half(mylist: Sequence) -> tuple[Sequence, Sequence]:
    """Return both halves of `mylist`."""
    n = len(mylist)//2
    return mylist[:n], mylist[n:]


# base problem
assert split_in_half([1, 2, 3, 4]) == ([1, 2], [3, 4])
assert split_in_half([1, 2, 3, 4, 5]) == ([1, 2], [3, 4, 5])
assert split_in_half([1, 2]) == ([1], [2])
assert split_in_half([]) == ([], [])
assert split_in_half([1]) == ([], [1])

# bonus 1, test any sequence
assert split_in_half("This is a string") == ('This is ', 'a string')
assert split_in_half((1, 2, 3, 4, 5, 6)) == ((1, 2, 3), (4, 5, 6))
assert split_in_half(b"bytestring") == (b'bytes', b'tring')
