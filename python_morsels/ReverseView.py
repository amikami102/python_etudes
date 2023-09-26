# ReverseView.py
"""
A script defining `ReverseView` utility class, which will work like built-in
`reversed` function except that you can loop over multiple times.
"""
from typing import *
T = TypeVar('T')


class ReverseView(Sequence):
    def __init__(self, sequence: Sequence[T]):
        self.sequence = sequence

    def __len__(self) -> int:
        return len(self.sequence)
    
    def _index(self, index) -> int:
        """Retrieve the intended index for the non-revesed sequence."""
        if 0 <= index < len(self):
            # correct index for len 5 sequence
            # 0 1 2 3 4 	<- reversed(sequence)
            # 4 3 2 1 0	<- sequence
            return len(self) - index - 1
        else:
            # -5 -4 -3 -2 -1 <- revesed(sequence)
            #  4  3  2  1  0 <- sequence
            return - index - 1 

    def __getitem__(self, index: int|slice) -> T|Sequence:
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return [self[i] for i in range(start, stop, step)]
        else:
            return self.sequence[self._index(index)]
    
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(s) for s in self) + "]"



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