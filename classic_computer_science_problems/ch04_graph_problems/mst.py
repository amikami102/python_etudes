# mst.py
"""
A script for solving minimum spanning tree problem with Jarníck's algorithm.

Jarníck's algorithm finds the minimum spanning tree in following steps.
    
    1. Pick an arbitrary vertex to include in the tree.
    2. Find the lowest-weight edge connecting the tree to the vertices not yet in the tree.
    3. Add the vertex at the end of that minimum edge to the tree.
    4. Repeat steps 2 and 3 until every vertex in the graph is in the tree.

The algorithm assumes a connected, undirected graph.
"""
from typing import *

from rich import print

from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue


V = TypeVar('V')
WeightedPath = list[WeightedEdge]


def total_weight(path: WeightedPath) -> float:
    return sum(edge.weight for edge in path)


def minimum_spanning_tree(graph: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    """
    Find the minimum spanning tree of `graph` with Jarníck's algorithm.
    """
    if start < 0 or start >= graph.vertex_count:
        return None
    
    tree: WeightedPath = []
    
    frontier: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: list[bool] = [False] * graph.vertex_count 	# if it's visited, it's in the tree
    
    def visit(i: int) -> None:
        """ Visit vertex at index `i`."""
        visited[i] = True
        for edge in graph.edges_for_index(i):
            # queue all untouched edges coming from vertex at index `i`
            if not visited[edge.v]:
                frontier.push(edge)
    
    visit(start)
    
    while not frontier.empty:
        edge = frontier.pop()	# this is the lowest cost edge
        if not visited[edge.v]: # only add the edge if the destination vertex has yet to be visited
            tree.append(edge)
            visit(edge.v)
    
    return tree


def display_weighted_path(graph: WeightedGraph, tree: WeightedPath) -> None:
    for edge in tree:
        print(f"{graph.vertex_at(edge.u)!r} > {graph.vertex_at(edge.v)!r}")
    print(f"Total weight: {total_weight(tree)}")


if __name__ == '__main__':
    
    from city_graph import city_graph_weighted
    print(city_graph_weighted)
    
    tree: Optional[WeightedPath] = minimum_spanning_tree(city_graph_weighted)
    if not tree:
        print('No solution found')
    else:
        display_weighted_path(city_graph_weighted, tree)