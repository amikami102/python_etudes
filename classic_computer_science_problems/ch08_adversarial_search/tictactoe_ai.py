# tictactoe_ai.py
"""
A script that will play a tictactoe against an AI player defined by minimax algorithm.

The human goes first.
"""
from typing import *

from rich import print

from minimax import find_best_move
from board import Board, Move
from tictactoe import TTTBoard, TTTPiece


board: Board = TTTBoard()


def get_player_move() -> Move:
    """ Get human player's input. """
    player_move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input('Enter a legal square (0-8):'))
        player_move = Move(play)
    return player_move


if __name__ == '__main__':
    # main game loop
    
    while True:
        human_move: Move = get_player_move()
        board = board.move(human_move)
        
        if board.is_win:
            print('You win!')
            break
        
        elif board.is_draw:
            print('Draw!')
            break
        
        computer_move: Move = find_best_move(board)
        print(f'Computer move is {computer_move}.')
        
        board = board.move(computer_move)
        print(board)
        
        if board.is_win:
            print('Computer wins!')
            break
        elif board.is_draw:
            print('Draw!')
            break