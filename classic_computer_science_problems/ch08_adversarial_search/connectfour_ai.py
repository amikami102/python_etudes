# connectfour_ai.py
"""
A script that plays Connect Four against an AI player programmed by minimax algorithm.
"""
from minimax import find_best_move, minimax, alpha_beta_prune
from connectfour import C4Board, C4Column
from board import Move

board: C4Board = C4Board()


def get_player_move() -> Move:
    """ Get human player's input, which is the column to drop the piece."""
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("Enter a legal column (0-6):"))
        player_move = Move(play)
    return player_move


if __name__ == '__main__':
    
    while True:
        print('Human plays the (B)lack piece. The computer plays the (R)ed piece.')
        human_move: Move = get_player_move()
        board = board.move(human_move)
        
        if board.is_win:
            print('Human wins!')
            break
        elif board.is_draw:
            print('Draw!')
            break

        computer_move: Move = find_best_move(board, 3)
        print(f'Computer move is {computer_move}')
        
        board = board.move(computer_move)
        print(board)
        
        if board.is_win:
            print('Computer wins!')
            break
        elif board.is_draw:
            print('Draw!')
            break
        
