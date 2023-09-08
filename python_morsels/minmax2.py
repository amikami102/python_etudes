# minmax2.py
"""
A script defining `minmax()` function, which returns a tuple of the minimum and maximum values of an input list. 
"""
from typing import NamedTuple, Any, Iterable, Callable

SENTINEL = object()

class MinMax(NamedTuple):
    min: Any
    max: Any
    
            
def minmax(
        iterable: Iterable, *other_args,
        key: Callable = None, default: Any = SENTINEL
    ) -> tuple[int, int]:
    """
    Return a tuple of minimum and maximum values of `iterable`.
    
    Args:
    ----
        iterable: Iterable, required
            at least one iterable is required
        other_args: optional
            other iterables fed as positional arguments
        key: Callable, optional, default to None
            a function for value comparison
        default: Any, optional, default to SENTINEL
            a default value that will be used if `iterable` is empty
    """
    # check if more than one iterables are given
    if other_args:
        iterable = [iterable, *other_args]
    
    # grab the first item from the iterable
    iterator = iter(iterable)
    try:
        minimum = maximum = next(iterator)
    except StopIteration:
        minimum = maximum = default
    else:
        min_key = max_key = key(minimum) if key else minimum
    
    # find the minimum and maximum values of the iterable
    for item in iterable:
        item_key = key(item) if key else item
        if minimum is SENTINEL or item_key < min_key:
            minimum, min_key = item, item_key
        if maximum is SENTINEL or max_key < item_key:
            maximum, max_key = item, item_key
    
    if minimum is SENTINEL:
        # the iterable was empty and there was no default value given
        raise ValueError('Empty iterable with no default value is not allowed')
    return MinMax(minimum, maximum)
    
    
    
# base problem
assert minmax([0, 1, 2, 3, 4]) == (0, 4)
assert minmax([], default=0) == (0, 0)
assert minmax([10, 8, 7, 5.0, 3, 6, 2], default=0) == (2, 10)
assert minmax([], default=None) == (None, None)
try:
    minmax([])
except ValueError:
    print('passed')
else:
    print('failed')

words = ["hi", "HEY", "Hello"]
assert minmax(words) == ('HEY', 'hi')
assert minmax(words, key=lambda s: s.lower()) == ('Hello', 'hi')
assert minmax(words, key=len) == ('hi', 'Hello')

# bonus 1, test with any iterable
numbers = {8, 7, 5, 3, 9, 6, 2}
assert minmax(numbers) == (2, 9)
assert minmax(n**2 for n in numbers) == (4, 81)
try:
    minmax(iter([]))
except ValueError:
    print('passed')
else:
    print('failed')

# bonus 2, test that `minmax()` returns a tuple-like class with attributes `min` and `max`
mm = minmax([3, 2, 5, 4, -1])
assert mm.min == -1
assert mm.max == 5
smallest, largest = mm
assert smallest == -1
assert largest == 5


# bonus 3, accept any number of positional arguments
assert minmax([3, 2, 5, 4, -1]) == MinMax(min=-1, max=5)
assert minmax(3, 2, 5, 4, -1) == MinMax(min=-1, max=5)
assert minmax([3], [2, 5], [4, -1]) == MinMax(min=[2, 5], max=[4, -1])
try:
    minmax()
except TypeError:
    print('passed')
else:
    print('failed')