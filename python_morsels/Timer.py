# Timer.py
"""
A script defining a context manager, `Timer`.
"""
from time import perf_counter as now
from time import sleep
from typing import Callable
import statistics


class Timer:
    """
    A context manager that track the time it takes to execute the code.
    
    Attributes
    ----
        start: float
            the starting time
            
        elapsed: float
            the time it elapsed since `self.start`
            
        runs: list[float]
            a list of elapsed times 
    """
    def __init__(self, func: Callable = None):
        self.runs = []
        self.func = func
        
    def __enter__(self):
        self.start = now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = now() - self.start
        self.runs.append(self.elapsed)

    def __call__(self, *args, **kwargs):
        with self:
            return self.func(*args, **kwargs)

    @property
    def min(self) -> float:
        return min(self.runs)

    @property
    def max(self) -> float:
        return max(self.runs)

    @property
    def mean(self) -> float:
        return statistics.mean(self.runs)

    @property
    def median(self) -> float:
        return statistics.median(self.runs)
        

# base problem
with Timer() as timer:
    sleep(0.01)
assert timer.elapsed < 0.02

# bonus 1, test `runs` attribute
timer = Timer()
with timer:
    x = sum(range(2**24))
with timer:
    x = sum(range(2 ** 23))
assert len(timer.runs) == 2

# bonus 2, test that `Timer` can be used as decorator
@Timer
def sum_of_squares(numbers):
    return sum(n**2 for n in numbers)
sum_of_squares(range(2**20))
sum_of_squares(range(2**21))
assert len(sum_of_squares.runs) == 2

# bonus 3, test `min`, `max`, `mean`, and `median` properties
wait = Timer(sleep)
wait(0.02)
wait(0.03)
wait(0.05)
wait(0.08)
wait(0.03)
times = sorted(wait.runs)
assert wait.mean == sum(times)/len(times)
assert wait.median ==  times[2]
assert wait.min == times[0]
assert wait.max == times[-1]