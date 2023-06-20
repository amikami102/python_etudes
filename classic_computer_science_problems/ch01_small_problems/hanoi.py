# hanoi.py
"""
A script for solving Tower of Hanoi puzzle.
"""
from rich import print
from typing import *

T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self._container: list[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    """
    Base case: there's only `n`=1 disc on `begin`.
        Move the single disc from `begin` to `end`.
        
    Recursive case: there are more than 1 disc on `begin`.
        Move the upper n-1 discs from `begin` to `temp` tower using `end` as in-between.
        Move the last disc from `begin` to `end`, i.e. the base case.
        Move the n-1 discs from `temp` to `end`, using `begin` as in-between.
    """
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == '__main__':
    
    num_discs: int = 3
    tower_a, tower_b, tower_c = Stack(), Stack(), Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    print(tower_a, tower_b, tower_c)