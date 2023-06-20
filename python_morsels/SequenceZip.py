# SequenceZip.py
"""
A script implementing `SequenceZip` class object.
"""
from rich import print
from typing import *
import itertools


class SequenceZip(Sequence):
    """A special-purposed class that acts like built-in `zip` class."""
    
    def __init__(self, *iterables):
        self.iterables = iterables
    
    def __getitem__(self, index) -> Sequence:
        return tuple(iterable[index] for iterable in self.iterables)
    
    def __len__(self) -> int:
        """
        Lenth of SequenceZip is defined as the shortest of the sequences,
        not the number of sequences.
        """
        return min(
            (len(s) for s in self.iterables),
            default=0
        )
    
    def __repr__(self) -> str:
        body = ', '.join(repr(iterable) for iterable in self.iterables)
        return f'{type(self).__name__}' + '(' + body + ')'
    
    def __eq__(self, other: 'SequenceZip') -> bool:
        """
        Since `self` and `other` could have different number of sequences,
        only compare as many as the shorter of the two.
        e.g. `SequenceZip('hiya', [1, 2, 3]) has length 3,
        so it will only be compared up to ('y', 3).
        """
        if not isinstance(other, SequenceZip):
            return NotImplemented
        
        my_seq = tuple(
            tuple(s[:len(self)]) for s in self.iterables
        )
        other_seq = tuple(
            tuple(s[:len(other)]) for s in other.iterables
        )
        return tuple(my_seq) == tuple(other_seq)
    

# base problem
zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
for x, y, z in zipped:
    print(x, y, z)
print(list(zipped))
print(len(zipped))
print(zipped[1])
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
seq1 = SequenceZip(x, y, z)
print(seq1[-1])
assert seq1[-1] == (3, 6, 9)
x[-1], z[-1] = z[-1], x[-1]
print(seq1[-1])
assert seq1[-1] == (9, 6, 3)

# bonus 1
print(zipped)

# bonus 2
assert SequenceZip('hiya', [1, 2]) == SequenceZip('hi', [1, 2, 3])
print(list(SequenceZip('hiya', [1, 2, 3])))
print(list(SequenceZip('hi', [1, 2, 3])))
my_iterables = 'hiya', [1, 2, 3]
other_iterables = 'hi', [1, 2, 3]
print(
    tuple(
       tuple(s[:len(my_iterables)]) for s in my_iterables
    )
)
print(
    tuple(
       tuple(s[:len(other_iterables)]) for s in other_iterables
    )
)