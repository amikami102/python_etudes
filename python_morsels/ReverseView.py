# ReverseView.py
"""
A script defining `ReverseView` utility class, which will work like built-in
`reversed` function except that you can loop over multiple times.
"""
from typing import *
T = TypeVar('T')


class ReverseView(MutableSequence):
    def __init__(self, sequence: Sequence[T]):
        self.sequence = sequence

    def __iter__(self) -> Iterator[T]:
        for item in reversed(self.sequence):
            yield item

    def __len__(self) -> int:
        return len(self.sequence)

    def __getitem__(self, index: int|slice) -> T|Sequence:
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if start >= 0 and stop > 0:
                return list(self)[start:stop:step]
            else:
                return list(self)[::step]
        if index < 0:
            index += len(self)
        for i, item in enumerate(self):
            if i == index:
                return item
    
    def __setitem__(self, index: int, value: T) -> None:
        self[index] = value
    
    def __delitem__(self, index: int) -> None:
        before, after = self[:index], self[index + 1:]
        self = before + after
    
    def insert(self, index: int, value: T) -> None:
        before, after = self[:index], self[index: ]
        self = before + [value] + after
                
    def __str__(self) -> str:
        return f'{list(self)}'

    def count(self, value: T) -> int:
        return sum(1 for item in self if item == value)

    def index(self, value: T) -> int:
        for i, item in enumerate(self):
            if item == value:
                return i
        raise ValueError


# base problem
numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)
assert list(reverse_numbers) == [11, 7, 4, 3, 1, 2]
assert list(reverse_numbers) == [11, 7, 4, 3, 1, 2]
numbers.append(18)
assert list(reverse_numbers) == [18, 11, 7, 4, 3, 1, 2]

# bonus 1, test that `ReverseView` has length and string representation,
# and is indexable
numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)
assert str(reverse_numbers) == '[11, 7, 4, 3, 1, 2]'
assert reverse_numbers[0] == 11
assert reverse_numbers[-1] == 2
assert len(reverse_numbers) == 6
numbers.append(18)
assert reverse_numbers[0] == 18
assert len(reverse_numbers) == 7

# bonus 2, test slicing, `ReverseView.index()`, and `ReverseView.count()` method
letters = "hi there"
view = ReverseView(letters)
assert "".join(view[-2:]) == 'ih'
assert "".join(view[:3]) == 'ere'
assert view[::-1] == list(letters)
assert view.count('h') == 2
assert view.count('z') == 0
assert view.index('e') == 0

# bonus 3, test `pop()` method
words = ["red", "green", "blue", "purple"]
view = ReverseView(words)
view.pop()
assert list(view) == ['purple', 'blue', 'green']
assert list(words) == ['green', 'blue', 'purple']
view.pop(0)
assert list(view) == ['blue', 'green']
assert list(words) == ['green', 'blue']

# test `append()` and `insert()` method
words = ["red", "green", "blue", "purple"]
reverse_view = ReverseView(words)
reverse_view.append("yellow")
assert list(words) == ['yellow', 'red', 'green', 'blue', 'purple']
assert list(reverse_view) == \
    ['purple', 'blue', 'green', 'red', 'yellow']
reverse_view.insert(0, "pink")
assert list(reverse_view) == \
    ['pink', 'purple', 'blue', 'green', 'red', 'yellow']
assert list(words) ==\
    ['yellow', 'red', 'green', 'blue', 'purple', 'pink']