# connectfour.py
"""
A script implementing the game of Connect Four.

The grid is indexed so that row index 0 is the top row and the column index 0 is the leftmost column.
"""
__all__ = [
    'NROWS', 'NCOLS', 'SEGMENT_LENGTH',
    'Location', 'Segment', 
    'C4Piece',
    'generate_segments',
    'C4Column',
    'C4Board'
    
]
from typing import *
from enum import Enum
from collections import deque
from dataclasses import dataclass, field

from rich import print

from board import Move, Piece, Board

NROWS, NCOLS, SEGMENT_LENGTH = 6, 7, 4

Location = tuple[int, int]
Segment = list[Location]


class C4Piece(Piece, str, Enum):
    """ A Connect Four game piece value, which is either Blue, Red, or empty. """
    
    B = 'B'
    R = 'R'
    E = ' '
    
    @property
    def opposite(self) -> 'C4Piece':
        if self == C4Piece.B:
            return C4Piece.R
        elif self == C4Piece.R:
            return C4Piece.B
        else:
            return C4Piece.E
    
    def __str__(self) -> str:
        return self.value


def generate_segments() -> Iterator[Segment]:
    """
    Generate all of the potential winning segments of size `SEGMENT_LENGTH` in a Connect Four grid of size `NROWS` by `NCOLS`.
    """
    
    # generate the vertical segments
    yield from (
        [
            (c, r + t) for t in range(SEGMENT_LENGTH)
        ]
        for c in range(NCOLS)
        for r in range(NROWS - SEGMENT_LENGTH + 1)
    )
    
    # generate the horizontal segments
    yield from (
        [
            (c + t, r) for t in range(SEGMENT_LENGTH)
        ]
        for r in range(NROWS)
        for c in range(NCOLS - SEGMENT_LENGTH + 1)
    )
    
    # generate the bottom left to the top right diagonal segments
    yield from (
        [
            (c + t, r + t) for t in range(SEGMENT_LENGTH)
        ]
        for r in range(NROWS - SEGMENT_LENGTH + 1)
        for c in range(NCOLS - SEGMENT_LENGTH + 1)
    )
    
    # generate the top left to bottom right diagonal segments
    yield from (
        [
            (c+t, r - t) for t in range(SEGMENT_LENGTH)
        ]
        for c in range(NCOLS - SEGMENT_LENGTH + 1)
        for r in range(SEGMENT_LENGTH - 1, NROWS)
    )


class C4Column:
    """ A class representing a column of connect four board. """
    
    def __init__(self, pieces: list[C4Piece]=None) -> None:
        self._column: list[C4Piece] = deque(maxlen=NROWS)
        if pieces:
            self._column = deque(pieces)
    
    def __len__(self) -> int:
        return sum(p != C4Piece.E for p in self._column)
    
    @property
    def full(self) -> bool:
        return len(self._column) == NROWS
    
    def push(self, item: C4Piece) -> None:
        if self.full:
            raise OverflowError('Trying to push piece into a full column')
        return self._column.append(item)
    
    def __getitem__(self, index: int) -> C4Piece:
        try:
            return self._column[index]
        except IndexError:
            return C4Piece.E
    
    def copy(self) -> 'C4Column':
        return C4Column(list(self._column))
    
    def __repr__(self) -> str:
        return repr(self._column)
        

@dataclass
class C4Board(Board):
    """ A class representing a Connect Four game board. """
    position: list[C4Column] = None	# represent the board as a list of columns
    _turn: C4Piece = C4Piece.B
    
    def __post_init__(self) -> None:
        """ Post-initialize `segments`, `position`, and `_turn`. """
        if not self.position:
            self.position = [
                C4Column()
                for _ in range(NCOLS)
            ]
    
    def __str__(self) -> str:
        colnumbers = '|' + '|'.join(str(i) for i in range(NCOLS)) + '|'
        return '\n'.join(
            '|' +
            '|'.join(self.position[c][r].value for c in range(NCOLS)) +
            '|'
            for r in reversed(range(NROWS))
        ) + '\n' + colnumbers
        
    @property
    def turn(self) -> C4Piece:
        return self._turn
    
    def move(self, loc: Move) -> 'C4Board':
        new_position: list[C4Column] = [col.copy() for col in self.position]
        new_position[loc].push(self._turn)
        return C4Board(new_position, self._turn.opposite)
    
    @property
    def legal_moves(self) -> list[Move]:
        """A move on a column (i.e. dropping a piece down the column) is legal if the column is not full. """
        return [
            Move(c)
            for c, column in enumerate(self.position)
            if not column.full
        ]
    
    def count_segment(self, segment: Segment) -> tuple[int, int]:
        """ Return the count of blue and red pieces in `segment`. """
        black, red = 0, 0
        for (col, row) in segment:
            black += int(self.position[col][row] == C4Piece.B)
            red += int(self.position[col][row] == C4Piece.R)
        return black, red
        
    @property
    def is_win(self) -> bool:
        """ There is a win if a segment is all red or blue. """
        def declare_win(blacks: int, reds: int) -> bool:
            return blacks == SEGMENT_LENGTH or reds == SEGMENT_LENGTH
        
        return any(
            declare_win(*self.count_segment(segment))
            for segment in generate_segments()
        )
    
    def evaluate_segment(self, segment: Segment, player: C4Piece) -> float:
        """
        Evaluate a segment depending on the number of red and black pieces:
            0 = has both red and black pieces of any number
            1 = has half of one color and half empties
            100 = has one empty and the rest of one color
            1_000_000 = has all filled with one color
        Negate the values for the opponent's segment.
        """
        black, red = self.count_segment(segment)
        if black > 0 and red > 0:
            return 0.0
        
        count: int = max(black, red)
        score: int = 0
        match count:
            case 1:
                score = 0
            case 2:
                score = 1
            case 3:
                score = 100
            case 4:
                score = 1_000_000
        color: C4Piece = C4Piece.R if red > black else C4Piece.B
        return score if player == color else -score
    
    def evaluate(self, player: C4Piece) -> float:
        return sum(
            self.evaluate_segment(segment, player)
            for segment in generate_segments()
        )
    

if __name__ == '__main__':
    
    import random
    
    board = C4Board()
    print(board)
    for _ in range(10):
        board = board.move(random.randrange(NCOLS))
    
    print(board.is_win)