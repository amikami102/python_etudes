# OrderedSet.py
"""
A script defining `OrderedSet` class that works like a set but remembers insertion order.
"""
from typing import *


class OrderedSet(MutableSet):
    """ A set-like class that remembers insertion order. """
    
    def __init__(self, iterable: Iterable = ()):
        self.elements = dict.fromkeys(iterable)
    
    def __iter__(self) -> Iterator:
        yield from self.elements
    
    def __len__(self) -> int:
        return len(self.elements)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self.elements)})"
    
    def __contains__(self, value) -> bool:
        return value in set(self.elements)
    
    def __eq__(self, other: 'OrderedSet') -> bool:
        if not isinstance(other, (set, OrderedSet)):
            return NotImplemented
        elif isinstance(other, OrderedSet):
            return len(self) == len(other) and\
                all(x == y for x, y in zip(self, other))
        else:
            return super().__eq__(other)
    
    def add(self, element) -> None:
        self.elements.update({element: None})
    
    def discard(self, element):
        self.elements.pop(element, None)


# base problem
ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
print(*set(ordered_words))
assert ' '.join(OrderedSet(ordered_words)) == 'these are words in an order'
words = OrderedSet(['repeated', 'words', 'are', 'not', 'repeated'])
assert list(words) == ['repeated', 'words', 'are', 'not']
assert len(words) == 4
assert not 'Pie' in words

# bonus 1, keep `OrderedSet` relatively memory and time efficient
words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
assert 'hello' in words

# bonus 2, support equality
assert not OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are'])
assert OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'}
assert not OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you']

# bonus 3, make `OrderedSet` mutable by adding `add` and `discard` methods
words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
words.add('doing')
assert ' '.join(words) == 'hello how are you doing'
words.discard('are')
words.discard('are')
assert ' '.join(words) == 'hello how you doing'