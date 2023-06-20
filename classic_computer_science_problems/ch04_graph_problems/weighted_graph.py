# weighted_graph.py
"""
A script defining a class representing a graph with weighted edges, `WeightedGraph`.
"""
from typing import *

from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('Vertex')


class WeightedGraph(Generic[V], Graph[V]):
    
    def __init__(self, vertices: list[V]) -> None:
        self._vertices: list[V] = vertices
        self._edges: list[list[WeightedEdge]] = [ [] for _ in self._vertices ]
    
    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)
    
    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)
    
    def neighbors_for_index_with_weights(self, i: int) -> list[tuple[V, float]]:
        """ Return the vertices adjacent to vertex with index `i` and their weights."""
        return [
            (self.vertex_at(edge.v), edge.weight)
            for edge in self.edges_for_index(i)
        ]
    
    def __str__(self) -> str:
        return '\n'.join(
            f"{v} -> {self.neighbors_for_index_with_weights(i)!r}"
            for i, v in enumerate(self._vertices)
        )
