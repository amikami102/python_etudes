# ReverseView.py

"""
ReverseView utility class will work like built-in `reversed` function except that
you can loop over its return value multiple times.
"""
from rich import print
from typing import *
T = TypeVar('T')


class ReverseView:
    """
    A sequence-like data structure that returns the input sequence in reverse order.
    
    This class
        - returns a reusable iterable;
        - will not take up unnecessary amount of memory;
        - is indexable;
        - has nice string representation;
        - has a length method.
    
    """
    
    def __init__(self, iterable: Sequence[T]):
        self._data = iterable
    
    def __iter__(self) -> Iterator[T]:
        return reversed(self._data)
    
    def __repr__(self) -> str:
        return f'{list(self.__iter__())!r}'
    
    def __getitem__(self, idx: int) -> T:
        return list(self.__iter__())[idx]
    
    def __len__(self) -> int:
        return len(list(self._data))


numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)
print(str(reverse_numbers))
numbers.append(18)
print(list(reverse_numbers))
print(reverse_numbers[0])
print(len(reverse_numbers))