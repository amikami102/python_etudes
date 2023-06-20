# loop_tracker.py
"""
A script defining `loop_tracker` class, which wraps a given iterable
and provides metadata about it à la [PEP 288](https://peps.python.org/pep-0288/).
"""
from typing import *

T = TypeVar('T')


class loop_tracker:
    """
    Attributes
    -----
        _iterator: Iterator[T]
            the iterator wrapped around a given iterable
            
        _size: int
            the number of items in `_iterable` that have been consumed
            
        empty_accesses: int
            the number of empty accesses made to the class instance
    """
    
    def __init__(self, iterable: Iterable[T]) -> None:
        self._iterator: Iterator[T] = iter(iterable)
        self._size: int = 0
        self.empty_accesses: int = 0
    
    def __next__(self) -> T:
        try:
            item = next(self._iterator)
        except StopIteration as e:
            self.empty_accesses += 1
            raise
        else:
            self._size += 1
            return item
    
    def __iter__(self) -> 'loop_tracker':
        return self
            
    
    def __len__(self) -> int:
        return self._size


# base problem
iterator = loop_tracker([11, 2, 3, -4, 5])
assert next(iterator) == 11
assert len(iterator) == 1
assert min(iterator) == -4
assert len(iterator) == 5

# bonus 1, count how many empty accesses have occurred
iterator = loop_tracker(n ** 2 for n in range(5, 10))
assert iterator.empty_accesses == 0
assert max(iterator) == 81
assert iterator.empty_accesses == 1
assert list(iterator) == []
assert iterator.empty_accesses == 2

