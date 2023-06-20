# ChainSequence.py
"""
A script defining `ChainSequence` class which chains together sequences.
"""
from typing import *
import itertools
from SliceView import SliceView


T = TypeVar('T')


class ChainSequence(Sequence):
    """ A class that chains together sequence into one sequence. """
    
    def __init__(self, *sequences):
        self.sequences: list[Sequence[T]] = [seq for seq in sequences]
    
    def __getitem__(self, i: int|slice) -> T|Sequence[T]:
        if isinstance(i, slice):
            return SliceView(self, i.start, i.stop, i.step)
        else:
            return list(itertools.chain.from_iterable(self.sequences))[i]
    
    def __len__(self) -> int:
        return len(list(itertools.chain.from_iterable(self.sequences)))


# base problem
chained = ChainSequence('abcd', [1, 2, 3])
assert chained[1] == 'b'
assert chained[-1] == 3
assert chained[4] == 1
assert len(chained) == 7

x, y, z = [2, 1], [3, 4], [11, 18]
chained = ChainSequence(x, y, z)
assert chained.sequences == [[2, 1], [3, 4], [11, 18]]
assert (len(chained), chained[4], chained[5]) == (6, 11, 18)
y.append(7)
assert (len(chained), chained[4], chained[5]) == (7, 7, 11)

# bonus 1, test slicing
chained = ChainSequence('abcd', [1, 2, 3])
assert tuple(chained[3:]) == ('d', 1, 2, 3)
chained.sequences[-1][0] = 9
assert tuple(chained[3:6]) == ('d', 9, 2)

chain = ChainSequence('hi', [2, 1, 3, 4, 7])
view = chain[:4]
assert list(view) == ['h', 'i', 2, 1]
chain.sequences[1] = 'ya!'
assert list(view) == ['h', 'i', 'y', 'a']
