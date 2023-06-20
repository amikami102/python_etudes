# test_tictactoe.py
"""
A pytest script testing the minimax algorithm defined in `minimax` module on tic-tac-toe game.
"""
import unittest
from typing import *

from rich import print

from tictactoe import TTTPiece, TTTBoard
from board import Move
from minimax import find_best_move


EASY: list[TTTPiece] = [
    TTTPiece.X, TTTPiece.O, TTTPiece.X,
    TTTPiece.X, TTTPiece.E, TTTPiece.O,
    TTTPiece.E, TTTPiece.E, TTTPiece.O
]
BLOCK: list[TTTPiece] = [
    TTTPiece.X, TTTPiece.E, TTTPiece.E,
    TTTPiece.E, TTTPiece.E, TTTPiece.O,
    TTTPiece.E, TTTPiece.X, TTTPiece.O
]
HARD: list[TTTPiece] = [
    TTTPiece.X, TTTPiece.E, TTTPiece.E,
    TTTPiece.E, TTTPiece.E, TTTPiece.O,
    TTTPiece.O, TTTPiece.X, TTTPiece.E
]


class TTTMinimaxTests(unittest.TestCase):
    
    """ Tests for `minimax` function on tic-tac-toe game defined in `tictactoe` module. """
    
    def test_easy_position(self):
        """ Win in one move. """
        board: TTTBoard = TTTBoard(EASY, TTTPiece.X)
        answer: Move = find_best_move(board)
        self.assertEqual(answer, 6)
    
    def test_block_position(self):
        """ Block O's win. """
        board: TTTBoard = TTTBoard(BLOCK, TTTPiece.X)
        answer: Move = find_best_move(board)
        self.assertEqual(answer, 2)
    
    def test_hard_position(self):
        """ Find the best move to win in two moves. """
        board: TTTBoard = TTTBoard(HARD, TTTPiece.X)
        answer: Move = find_best_move(board)
        self.assertEqual(answer, 1)
    
    
if __name__ == '__main__':
    
    # Run all three tests
    unittest.main(verbosity=2)
    
    
    
        