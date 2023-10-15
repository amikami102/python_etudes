# SequenceZip.py
"""A script implementing `SequenceZip` class object."""
from typing import *


class SequenceZip:
    """A class that acts like `zip` for sequences."""

    def __init__(self, *sequences):
        self.sequences = sequences

    def __len__(self) -> int:
        """Return the length of the shortest sequence."""
        return min((len(seq) for seq in self.sequences), default=0)

    def __getitem__(self, index: int|slice) -> Sequence:
        if isinstance(index, int):
            return tuple(seq[:len(self)][index] for seq in self.sequences)
        else:
            indices = range(*index.indices(len(self)))
            return SequenceZip(
                *([seq[i] for i in indices] for seq in self.sequences)
            )

    def __repr__(self) -> str:
        sequences_str = ', '.join(repr(seq) for seq in self.sequences)
        return f'{type(self).__name__}({sequences_str})'

    def __eq__(self, other: 'SequenceZip') -> bool:
        if isinstance(other, SequenceZip):
            return len(self) == len(other) and\
                all(seq1 == seq2 for seq1, seq2 in zip(self, other))
        else:
            return NotImplemented


# base problem
zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
assert list(zipped) == [('A', 'as', 1), ('B', 'easy', 2), ('C', 'as', 3)]
assert len(zipped) == 3
assert zipped[1] == ('B', 'easy', 2)

# bonus 1, test string representation
zipped = SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])
assert repr(zipped) == "SequenceZip('ABC', ['as', 'easy', 'as'], [1, 2, 3])"
assert repr(SequenceZip(range(10), "hello"))== "SequenceZip(range(0, 10), 'hello')"

# bonus 2, test equality
assert SequenceZip('hiya', [1, 2]) == SequenceZip('hi', [1, 2, 3])
assert SequenceZip('hiya', [1, 2, 3]) != SequenceZip('hi', [1, 2, 3])

# bonus 3, test slicing
zipped = SequenceZip('ABCDE', [1, 2, 3, 4, 5])
assert zipped[1:] == SequenceZip('BCDE', [2, 3, 4, 5])