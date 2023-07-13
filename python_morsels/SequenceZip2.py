# SequenceZip2.py
"""
A script defining `SequenceZip` class that acts like the built-in `zip` but for sequences and is reusable.
"""
from typing import *
from itertools import zip_longest

SENTINEL = object()


class SequenceZip(Sequence):
    """ A class that acts like `zip` but is reusable and has as its length the length of the shortest sequence. """
    
    def __init__(self, *sequences):
        self.sequences = sequences
    
    def __len__(self) -> int:
        """ Returns the length of the shortest sequence of the `sequences` attribute. """
        return len(min(self.sequences, key=len))
    
    def __getitem__(self, index: int|slice) -> Sequence:
        """ Returns the `i`-th sequence of the zipped sequence. """
        if isinstance(index, int):
            return list(zip(*self.sequences))[index]
        else:
            return SequenceZip(*(seq[:len(self)][index] for seq in self.sequences))
            
    def __eq__(self, other: 'SequenceZip') -> bool:
        """ Compare the zipped output elementwise. """
        if not isinstance(other, SequenceZip):
            return NotImplemented
        return all(
            first == second
            for first, second in zip_longest(self, other, fillvalue=SENTINEL)
        )
    
    def __setitem__(self, index: int, values: Sequence) -> None:
        for (i, seq), value in zip(enumerate(self.sequences), values):
            before, after = seq[:len(self)], seq[len(self):]
            print(before)
            before[index] = value
            seq = before + after
            self.sequences[i] = seq
            
            
    
    def __delitem__(self, index: int) -> None:
        for seq in self.sequences:
            del seq[index]



# base problem
zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
for x, y, z in zipped:
     print(x, y, z)
assert list(zipped) ==\
       [('A', 'as', 1), ('B', 'easy', 2), ('C', 'as', 3)]
assert len(zipped) == 3
assert zipped[1] == ('B', 'easy', 2)
assert SequenceZip('hi', [1, 2, 3]) == SequenceZip('hiya', [1, 2]) 
assert not SequenceZip('hi', [1, 2, 3]) == SequenceZip('hiya', [1, 2, 3])

seq1 = SequenceZip([1, 2, 3], [4, 5, 6], [7, 8, 9])
seq2 = SequenceZip([1, 2, 3], [4, 5, 6], [7, 8, 9, 0])
seq3 = SequenceZip([1, 2, 3], [4, 5, 4], [7, 8, 9, 0])
assert seq1 == seq2
assert not seq1 == seq3
assert not seq1 == list(seq2)

# bonus 1, test slicing
zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
assert zipped[1:] == SequenceZip('BCDE', [2, 3, 4, 5])
seq = SequenceZip(range(6), [1, 2, 3, 4], 'hiya!!', range(1000))
assert list(seq[-3:]) == \
[
    (1, 2, 'i', 1),
    (2, 3, 'y', 2),
    (3, 4, 'a', 3),
]

# bonus 2, test that `SequenceZip` is mutable
zipped = SequenceZip([0, 1, 2], [3, 4, 5, 6])
zipped[0] = [8, 9]
assert zipped == SequenceZip([8, 1, 2], [9, 4, 5, 6])
del zipped[-1]
assert zipped == SequenceZip([8, 1], [9, 4, 6])

# mutating `SequenceZip` object should fail if they wrap around immutable sequences
zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
try:
    del zipped[0]
except TypeError:
    print('passed')
else:
    print('failed')

x, y, z = [0, 1, 2, 3], [4, 5, 6], [7, 8, 9, 10]
seq = SequenceZip(x, y, z)
seq[0] = (-1, -2, -3)
print(x)
assert seq[0] == (-1, -2, -3)
seq[-1] = (-4, -5, -6)
print(x)
try:
    seq[-4] = (-100, -100, -100)
except IndexError:
    print('passed')
else:
    print('failed')
assert x == [-1, 1, -4, 3]