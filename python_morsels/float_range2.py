# float_range2.py
"""
A script defining a class, `float_range`, that acts like the built-in `range` that works for floats.
"""
from typing import *
import math
from numbers import Number


class float_range(Sequence):
    """A `range`-like class that works with any numeric type."""
    
    def __init__(self, stop: Number, start: Number = None, step: Number = None, /):
        """
        Initialize by specifying 
            - the `stop` value,
            - both the `start` and `stop` values, or
            - all three `start`, `stop`, and `step` values.
        """
        match (start, stop, step):
            case Number(), Number(), Number():
                self.start, self.stop, self.step = stop, start, step
            case None, Number(), None:
                self.stop = stop
                self.start, self.step = 0, 1
            case Number(), Number(), None:
                self.start, self.stop = stop, start
                self.step = 1 if self.start < self.stop else -1
    
    def __len__(self) -> int:
        return max(
            math.ceil((self.stop - self.start) / self.step),
            0
        )
    
    def __getitem__(self, index: int|slice) -> Number|Sequence:
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return (self.start + i * self.step for i in range(start, stop, step))
        elif 0 <= index < len(self):
            return self.start + index * self.step
        elif -len(self) <= index < 0:
            return self.start + (len(self) + index) * self.step
        else:
            raise IndexError('float_range index out of range')

# Unnecessary to define `__iter__` once `__len__` and `__getitem__` are defined,
# as Python understands the object with these methods to be a sequence.
# A sequence will come with a freebie `__reversed__` method.
# You don't even need to inherit from `typing.Sequence` if you're not using `super()`.
#     def __iter__(self) -> Iterator[Number]:
#         return (
#             self.start + i * self.step
#             for i in range(0, len(self))
#         )      


# base problem
floater = float_range(1, 10, 2)
assert len(floater) == 5
assert list(floater) == [1, 3, 5, 7, 9]

try:
    next(iter(float_range(1, 6, -1)))
except StopIteration:
    print('passed')
else:
    print('failed')
    
# bonus 1, make `float_range` indexable
my_range = float_range(0.5, 7, 0.75)
assert my_range[1] == 1.25
assert my_range[-1] == 6.5
try:
    my_range[10]
except IndexError as e:
    print('passed')
else:
    print('failed')

# bonus 2, make `float_range` reversible
reverse_range = reversed(float_range(0.5, 7, 0.75))
assert list(reverse_range) == [6.5, 5.75, 5.0, 4.25, 3.5, 2.75, 2.0, 1.25, 0.5]

# bonus 3, make `float_range` sliceable
my_range = float_range(0.5, 7, 0.75)
assert list(my_range[:2]) == [0.5, 1.25]
assert list(my_range[-1:100]) == [6.5]
assert list(my_range[-3:]) == [5.0, 5.75, 6.5]
assert list(my_range[::2]) == [0.5, 2.0, 3.5, 5.0, 6.5]