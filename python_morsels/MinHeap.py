# MinHeap.py
"""
A script defining `MinHeap` class, which implements a heap data structure.
"""
from typing import *
from heapq import heapify, heappop, heappush

T = TypeVar('T')


class MinHeap:
    """ A heap data structure. """
    
    __slots__ = '_heap' # to make `MinHeap` memory-efficient
    
    def __init__(self, iterable: Iterable[T]):
        self._heap: list[T] = list(iterable)
        heapify(self._heap)
    
    def __rep__(self) -> str:
        return f'{type(self).__name__}({self._heap})'
    
    def peek(self) -> T:
        """ View the smallest item. """
        return self._heap[0]
    
    def pop(self) -> T:
        """ Remove the smallest item. """
        popped = heappop(self._heap)
        return popped
    
    def push(self, item: T) -> None:
        heappush(self._heap, item)
    
    def __len__(self) -> int:
        return len(self._heap)
    

# base problem
numbers = [4, 7, 2, 3, 1, 11]
heap = MinHeap(numbers)
assert heap.pop() == 1
assert heap.peek() == 2
assert heap.pop() == 2
assert heap.pop() == 3
assert len(heap) == len(numbers) - 3

heap = MinHeap([4, 7, 2, 11])
assert heap.pop() == 2
heap.push(5)
assert heap.pop() == 4
assert heap.peek() == 5
assert len(heap) == 3

# bonus 1, test that `MinHeap` is efficient
from random import randint
from Timer import Timer
MANY_BIG_NUMBERS = [randint(100, 1000) for n in range(10_000)]
heap = MinHeap(MANY_BIG_NUMBERS)

with Timer() as timer:
    with timer.split():
        heap.push(150)
        heap.push(950)
        heap.push(400)
        heap.push(760)
        heap.push(280)
        heap.push(870)
        heap.push(330)
        heap.push(1000)
        heap.push(50)
        heap.push(500)
        items = [heap.pop() for _ in range(10)]
    with timer.split():
        MANY_BIG_NUMBERS.sort()
    assert timer[0].elapsed < timer[1].elapsed
