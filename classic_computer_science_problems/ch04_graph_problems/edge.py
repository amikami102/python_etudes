# edge.py
"""
A script defining `Edge` as a dataclass object.
"""
from typing import Iterator
from dataclasses import dataclass


@dataclass
class Edge:
    u: int 		# the "from" vertex
    v: int 		# the "to" vertex
    
    def reversed(self) -> 'Edge':
        """Flip the "from" and "to" vertices."""
        return Edge(self.v, self.u)
    
    def __str___(self) -> str:
        return f"{self.u} -> {self.v}"
    
    def __iter__(self) -> Iterator[int]:
        yield self.u
        yield self.v

