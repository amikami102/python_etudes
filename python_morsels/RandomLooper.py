# RandomLooper.py
"""A script for RandomLooper class object."""
from typing import *
import random
import itertools

T = TypeVar('T')

class RandomLooper:
    
    def __init__(self, *iterables):
        self.items = [
            item
            for iterable in iterables
            for item in iterable
        ]
    
    def __iter__(self) -> Iterator[T]:
        random.shuffle(self.items)
        yield from self.items
    
    def __len__(self) -> int:
        return len(self.items)


colors = ["red", "blue", "green", "purple"]
for color in RandomLooper(colors):
    print(color)

# Return the original iterable unshuffled
numbers = [1, 2, 3, 4]
looper = RandomLooper(numbers)
print(numbers)
print(looper.items)

shapes = ["square", "circle", "triangle", "octagon"]
print(len(RandomLooper(colors, shapes)))

numbers = range(999)
one_color = ["purple"]
print(list(RandomLooper(numbers, one_color))[:10])