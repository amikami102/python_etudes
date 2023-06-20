# len_or_none.py
"""
A script defining `len_or_none()` function which returns the legnth of a given object
and None if the object has no length.
"""
from typing import *

from rich import print

T = TypeVar('T')


def len_or_none(my_object: T) -> Optional[int]:
    """ Return the length of `my_object` or None if there is no length. """
    try:
        return len(my_object)
    except TypeError:
        return None


assert len_or_none("hello") == 5
assert len_or_none(4) is None
assert len_or_none([]) == 0
assert len_or_none(range(10)) == 10
assert len_or_none(zip([1, 2], [3, 4])) is None
