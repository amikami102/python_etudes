# queens.py
"""
Place 8 queens on the chess board so that no two queens are threatening each other.

Variables:
    8 columns (rows) of a chess board
    
Domains:
    8 rows (columns) of a chess board
    
Constraint:
    No two queens are placed on the board such that they are threatening each other.
    (i.e. not on the same row, column, or diagonal path)
"""
from rich import print
import json
from typing import *

from csp import Constraint, ConstraintSatisfactionProblem



class QueenConstraint(Constraint[int, int]):
    
    def __init__(self, columns: list[int]) -> None:
        super().__init__(columns)
        self.columns: list[int] = columns
    
    def satisfied(self, assignment: dict[int, int]) -> bool:
        """
        The constraint is satisfied if no pair of queens are on the same column, row, or diagonal.
        They will be assigned sequentially to different columns, so there is no need to check on the columns.
        
        Check the diagonal by taking the difference between their columns and between their rows.
        If these differences are the same values, then they are on a diagonal path.
        """
        for col1, row1 in assignment.items():
            for col2 in self.columns:
                if (col1 != col2) and (col2 in assignment):
                    row2: int = assignment[col2]
                    if row1 == row2:	# check row
                        return False
                    if abs(row1 - row2) == abs(col1 - col2):	# check diagonal
                        return False
        return True


def display_board(solution: dict[int, int]) -> str:
    """Print out the queens on a chessboard layout."""
    QUEEN = 'Q'
    
    board = [['*'] * 8 for _ in range(8)]
    for col, row in solution.items():
        board[row][col] = QUEEN
    
    return '\n'.join(
        (''.join(row) for row in board)
    )
    


if __name__ == '__main__':
    columns: list[int] = list(range(8))
    rows: dict[int, list[int]] = {
        col: list(range(8))
        for col in columns
    }
    
    csp: ConstraintSatisfactionProblem[int, int] = \
         ConstraintSatisfactionProblem(columns, rows)
    csp.add_constraint(QueenConstraint(columns))
    
    solution: Optional[dict[int, int]] = csp.backtracking_search()
    if not solution:
        print('No solution found')
    else:
        print(solution)
        print(display_board(solution))