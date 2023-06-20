# tictactoe.py
"""
A script that will play a Tic-Tac-Toe game against an AI player.

Note that the 3-by-3 board have squares indexed by digits 0 through 8 placed row-wise.

| 0 | 1 | 2 |
----+---+----
| 3 | 4 | 5 |
----+---+----
| 6 | 7 | 8 |

"""
from typing import *
from enum import Enum
from textwrap import dedent
from operator import itemgetter

from board import Move, Piece, Board


class TTTPiece(Piece, str, Enum):
    X = 'X'
    O = 'O'
    E = ' '		# empty space

    @property
    def opposite(self) -> 'TTTPiece':
        """ Return the other player's turn. """
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E
    
    def __str__(self) -> str:
        return self.value


class TTTBoard(Board):
    """ A class representing a tic-tac-toe board. """
    
    def __init__(self, position: list[TTTPiece] = None, turn: TTTPiece = TTTPiece.X) -> None:
        """
        A default board is an empty board.
        """
        self.position = position
        if not self.position:
            self.position: list[TTTPiece] = [TTTPiece.E] * 9
        
        self._turn: TTTPiece = turn

    @property
    def turn(self) -> TTTPiece:
        return self._turn
    
    def move(self, location: Move) -> Board:
        """ Make a move on `location` and return a new `Board`. """
        new_position = self.position.copy()
        new_position[location] = self._turn
        return TTTBoard(new_position, self._turn.opposite)

    @property
    def legal_moves(self) -> list[Move]:
        """A move is legal if the space on the board is empty. """
        return [
            Move(loc)
            for loc, space in enumerate(self.position)
            if space == TTTPiece.E
        ]
    
    @property
    def is_win(self) -> bool:
        """There is a win if a row, column, or diagonal is filled with either `TTTPiece.X` or `TTTPiece.O`."""
        rows: list[tuple[int, int, int]] = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8)
        ]
        columns: list[tuple[int, int, int]] = list(zip(*rows))
        diagonals: list[tuple[int, int, int]] = [
            (0, 4, 8),
            (2, 4, 6)
        ]
        
        def all_filled(*threes) -> bool:
            first, second, third = tuple(self.position[p] for p in threes)
            return (first == second) and\
                second == third and\
                first != TTTPiece.E
        
        return any(
            all_filled(*threes)
            for threes in rows + columns + diagonals
        )
    
    def evaluate(self, player: TTTPiece) -> float:
        """ Evaluate whether `player` has won. """
        if self.is_win and self.turn == player:
            return -1	# `player` has lost
        elif self.is_win and self.turn != player:
            return 1	# `player` has won
        else:
            return 0	# `player` has neither won nor lost
    
    def __repr__(self) -> str:
        """ Return a string representation of the board. """
        template = """\
        | {0} | {1} | {2} |
        ----+---+----
        | {3} | {4} | {5} |
        ----+---+----
        | {6} | {7} | {8} |"""
        return dedent(template).strip().format(*self.position)


if __name__ == "__main__":
    
    board: TTTBoard = TTTBoard()
    board = board.move(Move(0))
    assert board.legal_moves == list(range(1, 9))
    assert board._turn == TTTPiece.O
    assert not board.is_win
    
    