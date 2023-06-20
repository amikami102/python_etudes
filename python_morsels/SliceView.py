# SliceView.py
"""
A script implementing `SliceView` callable, which return a lazy slice of a given sequence.
"""
from typing import Sequence

class SliceView(Sequence):
    """A "view" into a sequence, like a "lazy slice"."""
    def __init__(self, sequence, start=None, stop=None, step=None):
        start, stop, step = slice(start, stop, step).indices(len(sequence))
        
        self.range = range(start, stop, step)
        self.sequence = sequence
        
    def __len__(self):
        return len(self.range)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return SliceView(self, index.start, index.stop, index.step)
        else:
            return self.sequence[self.range[index]]

# base problem
colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
assert colors[:3] == ['red', 'purple', 'pink']
assert list(SliceView(colors, stop=3)) == ['red', 'purple', 'pink']
assert colors[-2:] == list(SliceView(colors, start=-2))
assert list(SliceView(colors, start=0, step=2)) == colors[0::2]
assert list(SliceView(colors, step=-1)) == colors[::-1]

# bonus 1, return an iterable (i.e. the object can be used over and over again)
view = SliceView(colors, start=1, stop=3)
assert list(view) == ['purple', 'pink']
assert list(view) == ['purple', 'pink']

# bonus 2, support `len()` function
view = SliceView(colors, start=1, stop=3)
assert len(view) == 2
view = SliceView(colors, step=2)
assert len(view) == 3

# bonus 3, allow `SliceView` to be sliced and indexed
view = SliceView(colors)
assert list(view[:2]) == ['red', 'purple']
assert list(view[::-1]) == colors[::-1]
assert list(view[::-1][:2]) == ['black', 'green']
assert view[-3] == 'blue'