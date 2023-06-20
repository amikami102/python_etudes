# maze.py
"""
A script that builds a maze and finds a path through the maze.
"""
from rich import print
from collections import namedtuple
from enum import Enum
from typing import *
import random
import functools
import math

from generic_search import Node, node_to_path, depth_first_search, breadth_first_search, PriorityQueue, a_star_search


DIRECTIONS = UP, DOWN, LEFT, RIGHT = (1, 0), (-1, 0), (0, -1), (0, 1)
EMPTY, BLOCKED, START, GOAL, PATH = ' ', 'X', 'S', 'G', '*'


MazeLocation: tuple[int, int] = namedtuple('MazeLocation', ['row', 'column'])


def move(ml: MazeLocation, updown: int, leftright: int) -> MazeLocation:
    """ Move from `ml` vertically by `updown` steps and horizontally `leftright` steps."""
    return MazeLocation(ml.row + updown, ml.column + leftright)


def manhattan_distance(loc0: MazeLocation, loc1: MazeLocation) -> float:
    """
    Return the Manhattan distance between `loc0` and `loc1`.
    """
    return math.sqrt(
        (loc0.row - loc1.row) ** 2 + (loc0.column - loc1.column) ** 2
    )


class Maze:
    """
    Represent a maze as a grid (list of lists).
    
    Use sparseness to control how many empty spaces there are.
    """
    
    def __init__(self,
                 rows: int = 10,
                 columns: int = 10,
                 sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: MazeLocation = MazeLocation(9, 9)
                 )-> None:
        self.rows, self.columns = rows, columns
        self.start, self.goal = start, goal
        self.grid: list[list[str]] = [
            [
                EMPTY for c in range(columns)
            ]
            for _ in range(rows)
        ]
        
        # populate _grid with blocked cells
        self._randomly_fill(self.rows, self.columns, sparseness)
        self.grid[self.start.row][self.start.column] = START
        self.grid[self.goal.row][self.goal.column] = GOAL
    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        """
        Randomly fill self._grid with `Cell.BLOCKED`.
        """
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1) < sparseness:
                    self.grid[row][column] = BLOCKED
    
    def __str__(self) -> str:
        return '\n'.join(
            [
                ''.join([cell for cell in row])
                 for row in self.grid
            ]
        )

    def goal_test(self, ml: MazeLocation) -> bool:
        """Is`ml` is the goal of this maze?"""
        return ml == self.goal
    
    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        """ List next maze locations available to move. """
        
        successors: list[MazeLocation] = []
        
        def check_index_range(ml: MazeLocation):
            return (0 <= ml.row < self.rows) and \
                (0 <= ml.column < self.columns)
        
        for direction in DIRECTIONS:
            loc = move(ml, *direction)
            if check_index_range(loc) and self.grid[loc.row][loc.column] != BLOCKED:
                successors.append(loc)
        return successors

    def mark(self, path: list[MazeLocation]) -> None:
        """
        Mark cells listed in `path` with `Cell.PATH` by modifying `self.grid`.
        """
        for ml in path:
            if ml != self.start and ml != self.goal:
                self.grid[ml.row][ml.column] = PATH
    
    def clear_path(self, path: list[MazeLocation]) -> None:
        """
        Mark cells listed in `path` as `Cell.EMPTY` by modifying data in `self.grid`. 
        """
        for ml in path:
            if ml != self.start and ml != self.goal:
                self.grid[ml.row][ml.column] = EMPTY



if __name__ == '__main__':
    random.seed(22)
    
    maze: Maze = Maze()
    print(maze)
    
    # test moving through the maze
    print(list(maze.successors(maze.start)))
    
    # test generic_search.depth_first_search()
    print("[b]Testing depth-first search[/b]")
    solution1 = depth_first_search(
        maze.start,
        maze.goal_test,
        maze.successors
    )
    if not solution1:
        print("No solution found using depth-first search")
    else:
        path1: list[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear_path(path1)
    
    # test generic_search.breadth_first_search()
    print("[b]Testing breadth-first search[/b]")
    solution2 = breadth_first_search(
        maze.start,
        maze.goal_test,
        maze.successors
    )
    if not solution2:
        print("No solution found using breadth-first-search")
    else:
        path2: list[MazeLocation] = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear_path(path2)

    # test generic_search.a_star_search()
    print("[b]Testing A-star search [/b]")
    heuristic = functools.partial(manhattan_distance, maze.goal)
    solution3 = a_star_search(
        maze.start,
        maze.goal_test,
        maze.successors,
        heuristic
    )
    if not solution3:
        print("No solution found using A-star search")
    else:
        path3: list[MazeLocation] = node_to_path(solution3)
        maze.mark(path3)
        print(maze)
        maze.clear_path(path3)