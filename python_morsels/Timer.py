# Timer.py
"""
A script defining a context manager, `Timer`.
"""
from time import sleep, perf_counter
from typing import *

H = TypeVar('Hashable')


class Timer:
    """
    A context manager that will tracks the time it takes to finish processing the code inside the `with` context.
    
    Attributes
    ----
        start: float
            the starting time
            
        elapsed: float
            the time it elapsed since `self.start`
            
        runs: list[float]
            a list of elapsed times of the times the context manager instance was run
    
    Methods
    ----
        split() -> Timer:
            creates a sub-timer that must be run inside the parent timer
    """
    def __init__(self):
        self.runs = []
        self.subtimers: list[Timer] = []
        self.parent_exited: bool = False
    
    def __enter__(self):
        self.start = perf_counter()
        return self


    def __exit__(self, *args):
        self.elapsed = perf_counter() - self.start
        self.runs.append(self.elapsed)
        self.parent_exited: bool = True
        
    
    def split(self, name: str = None) -> 'Timer':
        """ Instantiate another `Timer` inside the current `Timer`. """
        if self.parent_exited:
            raise RuntimeError("Cannot split because parent timer is not running")
        
        if not name:
            name = len(self.subtimers) - 1
        subtimer = Timer()
        self.subtimers.append(subtimer)
        
        return subtimer
    
    def __getitem__(self, subkey: H) -> float:
        return self.subtimers[subkey]
        

# base problem
with Timer() as timer:
    sleep(0.01)
assert timer.elapsed < 0.02
with timer:
    x = sum(range(2 ** 23))

assert len(timer.runs) == 2

timer2 = Timer()
with timer2:
    x = sum(range(2 ** 22))
assert timer2.elapsed

# bonus 1, implement `Timer.split` method
with Timer() as timer:
    with timer.split():
        sleep(0.02)
    with timer.split():
        sleep(0.01)
    with timer.split():
        pass

assert timer.elapsed
#print(timer[0].elapsed)
#print(timer[1].elapsed)
#print(timer[2].elapsed)

with Timer() as timer:
    pass

try:
    with timer.split():
        pass	# expect RuntimeError
except RuntimeError:
    pass
#print(timer.subtimers)
