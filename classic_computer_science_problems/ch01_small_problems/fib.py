# fib1.py
"""
An element from Fibonacci sequence computed in four ways (four recursive, one iterative).
"""
from rich import print
from typing import *
from functools import lru_cache

MEMO: dict[int, int] = {0: 0, 1: 1} # base cases


def fib1(n: int) -> int:
    """Fails with RecursionError"""
    return fib1(n-1) + fib1(n-2)


def fib2(n: int) -> int:
    """Define base cases, namely when n = 0 or 1."""
    if n < 2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)
    

def fib3(n: int) -> int:
    """Employ memoization."""
    if n not in MEMO:
        MEMO[n] = fib3(n-1) + fib3(n-2)
    return MEMO[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    """Use functools.lru_cache to memoize."""
    if n < 2:
        return n
    return fib4(n-1) + fib4(n-2)


def fib5(n: int) -> int:
    if n == 0:
        return n
    fib_n_2: int = 0	# initialized to fib(0)
    fib_n_1: int = 1	# initialized to fib(1)
    
    for _ in range(1, n):
        fib_n_2, fib_n_1 = fib_n_1, fib_n_1 + fib_n_2
    
    return fib_n_1


if __name__ == '__main__':
    try:
        print(fib1(5))
    except RecursionError:
        pass
    
    print(fib2(5))
    print(fib2(10))
    
    print(fib3(50))
    print(MEMO)
    
    print(fib4(89))
    
    print(fib5(89))