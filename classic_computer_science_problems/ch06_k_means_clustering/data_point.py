# data_point.py
"""
A script defining `DataPoint` class object.
"""
from typing import *
import math


class DataPoint:
    
    def __init__(self, data: Iterable[float]) -> None:
        self._data: tuple[float, ...] = tuple(data)		# read-only 
        self.dimensions: tuple[float, ...] = tuple(data)	# may later be replaced with z-scores
    
    @property
    def num_dimensions(self) -> int:
        return len(self.dimensions)
    
    def distance(self, other: 'DataPoint') -> float:
        """ Return the square root of the sum of squares of differences between `self` and `other`. """
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            sum_of_squared_diff: float = sum(
                (x - y) ** 2
                for x, y in zip(self.dimensions, other.dimensions)
            )
            return math.sqrt(sum_of_squared_diff)
        
    def __eq__(self, other: 'DataPoint') -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.dimensions == other.dimensions
    
    def __repr__(self) -> str:
        return repr(self._data)