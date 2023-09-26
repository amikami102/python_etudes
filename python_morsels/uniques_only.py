# uniques_only.py
"""
A script defining `uniques_only()` function which returns a new iterable with all the duplicates removes from the original.
"""
from typing import *


def uniques_only(iterable: Iterable) -> Iterator:
    """Remove duplicates from `iterable`."""
    hash_seen = set()	# hashable items we've seen in the iterable
    unhash_seen = []		# hashable items we've seen in the iterable
    for item in iterable:
        if isinstance(item, Hashable):
            if item not in hash_seen:
                yield item
                hash_seen.add(item)
        else:
            if item not in unhash_seen:
                yield item
                unhash_seen.append(item)


# base problem
assert list(uniques_only([1, 2, 2, 1, 1, 3, 2, 1])) == [1, 2, 3]
nums = [1, -3, 2, 3, -1]
squares = (n**2 for n in nums)
assert list(uniques_only(squares)) == [1, 9, 4]

# bonus 1, return an iterator without consuming the original input wholly
nums = iter([1, 2, 3])
output = uniques_only(nums)
assert iter(output) == iter(output)
assert next(output) == 1
# The below line tests that the incoming generator isn't exhausted.
# It may look odd to test the nums input, but this is correct
# because after 1 item has been consumed from the uniques_only
# iterator, nums should only have 1 item consumed as well
try:
    next(nums) == 2
except StopIteration:
    print("Failed. The incoming nums iterator was fully consumed!")
    
# bonus 2, work with unhashable objects like lists
assert list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']]))\
    == [['a', 'b'], ['a', 'c']]

# bonus 3, make sure that iterable of hashable objects work efficiently
