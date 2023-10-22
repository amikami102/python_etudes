# OrderedSet2.py
"""A script implementing `OrderedSet` class."""
from typing import *

T = TypeVar('T')


class OrderedSet(MutableSet):
    """A class that works like a set but maintains order."""
    
    def __init__(self, items: Iterable[T] = ()):
        self.items = dict.fromkeys(items)

    def __iter__(self) -> Iterator:
        yield from self.items.keys()

    def __repr__(self) -> str:
        return f'{type(self).__name__}({list(self.items)})'

    def __contains__(self, item) -> bool:
        return item in set(self)

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item) -> None:
        self.items.update({item: None})

    def discard(self, item) -> None:
        self.items.pop(item, None)

    def __getitem__(self, index) -> T:
        return list(self.items.keys())[index]

    def __eq__(self, other) -> bool:
        if isinstance(other, OrderedSet):
            return all(item1 == item2 for item1, item2 in zip(self, other))
        elif isinstance(other, set):
            return set(self) == other
        else:
            return NotImplemented


# base problem
words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
assert list(words) == ['hello', 'how', 'are', 'you']
assert words[1] == 'how'
assert words[-1] == 'you'
assert list(reversed(words)) == ['you', 'are', 'how', 'hello']
assert len(words) == 4
words.add('doing')
assert ' '.join(words) == 'hello how are you doing'
words.discard('are')
assert ' '.join(words) == 'hello how you doing'
new_set = OrderedSet()
assert len(new_set) == 0