# CyclicList.py
"""
A script defining `CyclicList` class, looping over which will result in an infinite loop.
"""
from typing import *
from itertools import cycle
from collections import UserList

T = TypeVar('T')


class CyclicList(UserList):
    """ A list-like class except that looping over it will result in an inifinite loop."""
    def __iter__(self) -> Iterator[T]:
        yield from cycle(self.data)
    
    def __getitem__(self, index: int|slice) -> T:
        """
        Works cyclically. Assume slice only has start and stop values.
        When slicing, assume that
            - the start defaults to 0;
            - the stop defaults to
                - the length of the sequence when start >=0 and
                - 0 otherwise.
        """
        if isinstance(index, slice):
            start = index.start if index.start else 0
            stop = index.stop if index.stop else \
                len(self.data) if start >= 0 else 0
            return list(self[i] for i in range(start, stop))
        return self.data[index % len(self.data)]
    
    def __setitem__(self, key: int, value: T) -> T:
        self.data[key % len(self.data)] = value
    

# base problem
my_list = CyclicList([1, 2, 3])
for i, n in enumerate(my_list):
    print(n)
    if i > 8:
        break
from itertools import islice
assert list(islice(my_list, 5)) == [1, 2, 3, 1, 2]

# bonus 1, support `len` function and have `append` and `pop` methods like Python's list
my_list = CyclicList([1, 2, 3])
my_list.append(4)
assert my_list.pop() == 4
assert len(my_list) == 3
assert my_list.pop(0) == 1
assert len(my_list) == 2

# bonus 2, support index, which should also work in a cyclic manner
my_list = CyclicList([1, 2, 3])
assert my_list[1] == 2
assert my_list[-1] == 3
assert my_list[5] == 3
assert my_list[-4] == 3
numbers = CyclicList([1, 2, 3, 4])
numbers[5] = 0  # Should update index 1 (since the list has 4 items)
assert numbers[1] == 0

# bonus 3, support cyclic slicing
my_list = CyclicList([1, 2, 3])
assert my_list[-2:] == [2, 3]
assert my_list[:8] == [1, 2, 3, 1, 2, 3, 1, 2]
assert my_list[-2:2] == [2, 3, 1, 2]
assert my_list[:-1] == []