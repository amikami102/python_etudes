# word_search.py
"""
Build a word search puzzle using constraint satisfaction problem framework.
No overlaps allowed.

Variables:
    words
    
Domains:
    locations on the grid for the letters of the word
    
Constraint:
    All the letters of a word must fit on the same row, column, or diagonal.
"""
from rich import print
from typing import *
import random
import string
from collections import namedtuple

from csp import Constraint, ConstraintSatisfactionProblem


ROW, COLUMN = 0, 1


Grid = list[list[str]]
GridLocation = tuple[int, int]


def generate_grid(rows: int, columns: int) -> Grid:
    """ Initialize grid with random letters"""
    return [
        [
            random.choice(string.ascii_uppercase)
            for _ in range(columns)
        ]
        for _ in range(rows)
    ]


def display_grid(grid: Grid) -> None:
    """Print out grid"""
    for row in grid:
        print(''.join(row))
        

def generate_domain(word: str, grid: Grid) -> list[list[GridLocation]]:
    """Build a list of possible GridLocations for each lettter of the word"""
    domain: list[list[GridLocation]] = []
    
    height, width = len(grid), len(grid[0])
    length: int = len(word)
    
    for row in range(height):
        for col in range(width):
            columns, rows = \
                range(col, col + length + 1),\
                range(row, row + length + 1)
            if col + length <= width:
                # place letters left to right
                domain.append(
                    [
                        (row, c) for c in columns
                    ]
                )
                if row + length <= height:
                    # place letters diagonally toward bottom right
                    domain.append(
                        [
                            (row, col + (r - row)) for r in rows
                        ]
                    )
            if row + length <= height:
                # place letters top down
                domain.append(
                    [
                        (row, col) for row in rows
                    ]
                )
                if col - length >= 0:
                    domain.append(
                        [
                            (row, col - (r - row))
                            for r in rows
                        ]
                    )
    return domain


class WordSearchConstraint(Constraint[str, list[GridLocation]]):
    """Check the locations proposed for one word does not overlap with other words'."""
    
    def __init__(self, words: list[str]) -> None:
        super().__init__(words)
        self.words: list[str] = words
    
    def satisfied(self, assignment: dict[str, list[GridLocation]]) -> bool:
        """The constraint is satisfied if there are no duplicate GridLocation between words."""
        all_locations: list[GridLocation] = [
            loc
            for list_of_locs in assignment.values()
            for loc in list_of_locs
        ]
        return len(set(all_locations)) == len(all_locations)
        
        


if __name__ == '__main__':
    
    grid: Grid = generate_grid(9, 9)
    words: list[str] = ['PHOENIX', 'MAYA', 'IRIS', 'GODOT']
    locations: dict[str, list[list[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    
    csp: ConstraintSatisfactionProblem[str, list[GridLocation]] = \
             ConstraintSatisfactionProblem(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    
    solution: Optional[dict[str, list[GridLocation]]] = csp.backtracking_search()
    if not solution:
        print('No solution found')
    else:
        for word, grid_locations in solution.items():
            for letter, (row, column) in zip(word, grid_locations):
                grid[row][column] = letter
        display_grid(grid)
                