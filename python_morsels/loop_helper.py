# loop_helper.py
"""
A script defining `loop_helper()` function, which gives metadata while iterating.
"""
from typing import Iterator, Iterable, TypeVar
from dataclasses import dataclass
from itertools import pairwise

T = TypeVar('T')
SENTINEL = object()

@dataclass
class LoopInfo:
    is_first: bool
    index: int
    current: T
    previous: T
    next: T
    is_last: bool


def loop_helper(
        iterable: Iterable[T],
        previous_default: T = None, next_default: T = None
    ) -> Iterator[tuple[T, LoopInfo]]:
    """
    Iteratively yield a tuple of an item from the iterable and LoopInfo object.
    """
    previous = previous_default
    it, it2 = tee(iterable)
    for i, current in enumerate(it):
        next_item = next(it2, SENTINEL)
        yield current, LoopInfo(
            i==0,
            i, current, previous, next_item, 
            next_item is SENTINEL
            )
        previous = current
        
    
# base problem
colors = ["red", "blue", "green"]
colors_helper = loop_helper(colors)
_, info = next(colors_helper)
assert info.is_first
assert info.index == 0
assert not next(colors_helper)[1].is_first
assert list(loop_helper([])) == []

# bonus 1, test that `loop_helper` returns an iterator
colors = ["red", "blue", "green"]
colors_helper = loop_helper(colors)
assert iter(colors_helper) == colors_helper

# bonus 2, test `previous` and `current` attributes
