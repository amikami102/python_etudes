# loop_helper.py
"""
A script defining `loop_helper()` function, which gives metadata while iterating.
"""

from rich import print
from typing import *
import collections
import itertools

T = TypeVar('T')
LoopInfo = collections.namedtuple('LoopInfo', ['is_first', 'index', 'current', 'previous'])


def loop_helper(iterable: Iterable[T], previous_default: T = None) -> Iterator[tuple[T, LoopInfo]]:
    history = (previous_default, *iterable)
    return (
        (
            item,
            LoopInfo(i == 0, i, item, prev)
        )
        for (i, item), prev in zip(enumerate(iterable), history)
    )

    

colors = ["red", "blue", "green"]
for color, info in loop_helper(colors):
    if info.is_first:
        print("This is the first color!")
    print(f"Color {info.index} is {color}")

print(loop_helper([]))

for color, info in loop_helper(colors):
    if info.is_first:
        print(f"{color.title()} is the best color!")
    else:
        print(f"No {info.current} is the best color, not {info.previous}!")