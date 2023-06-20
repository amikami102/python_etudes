# RandomLooper.py
"""
A script for RandomLooper class object. 

>>> colors = ["red", "blue", "green", "purple"]
>>> for color in RandomLooper(colors):
...     print(color)
...
green
red
purple
blue
"""
from rich import print
from typing import *
import random
import itertools

T = TypeVar('T')

class RandomLooper:
    
    def __init__(self, *iterables):
        self._iterable = list(itertools.chain(*iterables))	# makes a shallow copy
    
    def __iter__(self) -> Iterator[T]:
        random.shuffle(self._iterable)
        yield from self._iterable
    
    def __len__(self) -> int:
        return len(self._iterable)
    
    


colors = ["red", "blue", "green", "purple"]
for color in RandomLooper(colors):
    print(color)

# Return the original iterable unshuffled
numbers = [1, 2, 3, 4]
looper = RandomLooper(numbers)
list(looper)
print(numbers)
print(looper._iterable)

shapes = ["square", "circle", "triangle", "octagon"]
print(len(RandomLooper(colors, shapes)))

numbers = range(999)
one_color = ["purple"]
print(list(RandomLooper(numbers, one_color))[:10])