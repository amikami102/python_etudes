# priority_queue.py
"""
A script defining `PriorityQueue` class object so that the item with the lowest priority is pushed out first.
"""
from typing import *
from heapq import heappush, heappop

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    
    def __init__(self) -> None:
        self._container: list[T] = []
    
    def push(self, item: T) -> None:
        """ Put `item` according to its priority. """
        heappush(self._container, item)
    
    def pop(self) -> T:
        """ Pop out by lowest priority. """
        return heappop(self._container)
    
    def __repr__(self) -> str:
        return repr(self._container)
    
    @property
    def empty(self) -> bool:
        return not self._container