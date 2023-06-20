# weighted_edge.py
"""
A script defining `WeightedEdge` class inherited from `edge.Edge` class.
"""
from typing import Iterator
from dataclasses import dataclass

from edge import Edge


@dataclass
class WeightedEdge(Edge):
    weight: float
    
    def reversed(self) -> 'WeightedEdge':
        """ Reverse the source and destination vertices. """
        return WeightedEdge(self.v, self.u, self.weight)
    
    def __lt__(self, other: 'WeightedEdge') -> bool:
        """ Compare edges by their weights. """
        if not isinstance(other, WeightedEdge):
            return NotImplemented
        else:
            return self.weight < other.weight
    
    def __str__(self) -> str:
        return f"{self.u!r} {self.weight} -> {self.v!r}"
    
    def __iter__(self) -> Iterator[int|float]:
        yield self.u
        yield self.v
        yield self.weight