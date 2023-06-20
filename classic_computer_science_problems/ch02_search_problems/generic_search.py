# generic_search.py
"""
A module containing classes and search algorithm functions.

n.b.: Need custom priority queue class defined to act like max heap (i.e. pops out the highest priority item first)
because the built-in `queue.PriorityQueue` class is min heap (i.e. pops out the lowest priority item first).
"""

from typing import *
from collections import deque
from heapq import heappush, heappop
T = TypeVar('T')


class Node(Generic[T]):
    """A wrapper around a state that keeps track of how we got from one state to another."""
    
    def __init__(self, state: T, parent: 'Node' = None, cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
    
    def __lt__(self, other: 'Node') -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        else:
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node: Node[T]) -> list[T]:
    """
    Return a list of states in descending order.
    """
    path: list[T] = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


class PriorityQueue(Generic[T]):
    """ A queue that keeps its elements in an internal order so that the first element popped out is always the highest priority element."""
    
    def __init__(self) -> None:
        self._container: list[T] = []
    
    def push(self, item: T) -> None:
        heappush(self._container, item)
    
    def pop(self) -> T:
        return heappop(self._container)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(self._container)})"
    




def depth_first_search(initial: T,
                       goal_test: Callable[T, bool],
                       successors: Callable[T, Iterator[T]]
                       ) -> Optional[Node[T]]:
    """
    Implement a depth-first search algorithm
    using Python's built-in list to stack next states to explore.
    """
    frontier: list[Node] = []
    explored: set[T] = {initial}
    
    frontier.append(Node(initial, None))
    
    while frontier:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        else:
            for child in successors(current_state):
                if child not in explored:
                    explored.add(child)
                    frontier.append(Node(child, current_node))
    return None


def breadth_first_search(initial: T,
                         goal_test: Callable[T, bool],
                         successors: Callable[T, Iterator[T]]
                         ) -> Optional[Node[T]]:
    """
    Implement a breadth-first search algorithm
    using `collections.deque` class to queue next states to explore.
    """
    frontier: deque[Node] = deque()
    explored: set[T] = {initial}
    
    frontier.append(Node(initial, None))
    
    while frontier:
        current_node: Node[T] = frontier.popleft()
        current_state: T = current_node.state
        
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child not in explored:
                explored.add(child)
                frontier.append(Node(child, current_node))
    return None
    
    

def a_star_search(initial: T, goal_test: Callable[T, bool],
                  successors: Callable[T, Iterator[T]],
                  heuristic: Callable[T, float]
                  ) -> Optional[Node[T]]:
    """
    Implement an A* starch algorithm using `queue.PriorityQueue` to
    keep Node's in order of priority, which is its total cost (cost + heuristic).
    """
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    explored: dict[T, float] = {initial: 0.0}
    
    frontier.push(
        Node(initial, None, 0.0, heuristic(initial))
    )
    
    while frontier:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1.0
            
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(
                    Node(child, current_node, new_cost, heuristic(child))
                )
    return None

    