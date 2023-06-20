# dijkstra.py
"""
A script implementing Dijkstra algorithm to find the shortest paths from some vertex to other vertices in a weighted graph.

The Dijkstra algorithm procees in the following steps.

    1. Add the root (the starting vertex) to a priority queue.
    2. Pop the closest vertex. Call this the current vertex.
    3. Look at all neighboring vertices to the current vertex.
        If they have not been recorded, or if the edge offers a new shortest path to them,
        update each vertex's distance from the starting vertex,
        record the edge that produced this distance,
        add the new vertex to the priority queue.
    3. Repeat steps 2 and 3 until the priority queue is empty.
    4. Return the shortest distance to every vertex from the starting vertex
"""
from typing import *
from dataclasses import dataclass
import math

from rich import print

from mst import WeightedPath
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue
from city_graph import city_graph_weighted as city_graph2

V = TypeVar('Vertex')


@dataclass
class DijkstraNode:
    vertex: int
    distance: float
    
    def __lt__(self, other: 'DijkstraNode') -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.distance < other.distance
    
    def __eq__(self, other: 'DijkstraNode') -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.distance == other.distance


def dijkstra(graph: WeightedGraph[V], root: V) -> tuple[list[float], dict[int, WeightedEdge]]:
    """
    Returns a list of distances from `root` to each index vertex
    and a dictionary of their paths from `root`.
    """
    first: int = graph.index_of(root)
    
    # distance from root to all vertices
    distances: list[float] = [math.inf] * graph.vertex_count
    distances[first] = 0 # the root is always 0 distance from itself
    
    # dictionary of the last edge along the path from `root` to each vertex
    legs: dict[int, WeightedEdge] = {}
    
    queue: PriorityQueue[DijkstraNode] = PriorityQueue()
    queue.push(DijkstraNode(first, 0))
    
    while not queue.empty:
        u: int = queue.pop().vertex
        
        # look at every edge extending from `u` 
        for edge in graph.edges_for_index(u):
            _, v, weight = edge
            alt: float = weight + distances[u]	# distance from root to vertex `v` via `u`
            if alt < distances[v]:	# check whether the two-edge path is shorter than the edge from root to `v`
                distances[v] = alt
                legs[v] = edge
                queue.push(DijkstraNode(v, alt))

    return distances, legs


if __name__ == '__main__':
    
    # Find shortest distances from Los Angeles to cities in `city_graph2`
    distances, legs = dijkstra(city_graph2, "Los Angeles")
    
    print("[b]Distances from Los Angeles[/b]")
    for i, dist in enumerate(distances):
        print(f"{city_graph2.vertex_at(i)!r} : {dist}")









