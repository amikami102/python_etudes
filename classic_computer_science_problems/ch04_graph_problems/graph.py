# graph.py
"""
A script defining `Graph` class object.
"""
from typing import *
import sys
sys.path.insert(0, '..')

from rich import print

from edge import Edge


V = TypeVar('Vertex')


class Graph(Generic[V]):
    
    def __init__(self, vertices: list[V] = []) -> None:
        self._vertices: list[V] = vertices
        self._edges: list[list[Edge]] = [ [] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        """ Number of vertices """
        return len(self._vertices)
    
    @property
    def edge_count(self) -> int:
        """ Number of edges """
        return sum(len(edges) for edges in self._edges)
    
    def add_vertex(self, vertex: V) -> int:
        """ Add `vertex` to the graph and return its index. """
        self._vertices.append(vertex)
        self._edges.append([]) # edges for `vertex`
        return self.vertex_count - 1
    
    def add_edge(self, edge: Edge) -> None:
        """ Add an undirected edge to the graph. """
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
    
    def add_edge_by_indices(self, u: int, v: int) -> None:
        """ Add an edge using vertex indices. """
        edge: Edge = Edge(u, v)
        self.add_edge(edge)
    
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        """ Add an edge by looking up vertex indices. """
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)
    
    def vertex_at(self, i: int) -> V:
        """ Find the vertex at index `i`. """
        return self._vertices[i]
    
    def index_of(self, v: V) -> int:
        """ Find the index of vertex `v`. """
        return self._vertices.index(v)
    
    def neighbors_of_index(self, i: int) -> list[V]:
        """ Find the vertices that are adjacent to vertex at index `i`."""
        return [
            self.vertex_at(edge.v)
            for edge in self._edges[i]
        ]
    
    def neighbors_for_vertex(self, v: V) -> list[V]:
        """ Find the vertices that are adjacent to vertex `v`. """
        return self.neighbors_of_index(self.index_of(v))
    
    def edges_for_index(self, i) -> list[Edge]:
        """ Return all the edges associated with vertex at index `i`. """
        return self._edges[i]
    
    def edges_for_vertex(self, i) -> list[Edge]:
        """ Return all the edges associated with vertex `v`. """
        return self._edges[self.index_of(v)]
    
    def __str__(self) -> str:
        lines: Iterator[str] = (
            f"{vertex!r} -> {self.neighbors_for_vertex(vertex)!r}"
            for vertex in self._vertices
        )
        return '\n'.join(lines)
