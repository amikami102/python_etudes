# minimax.py
"""
A module defining minimax algorithm that will find the best move in a two-player,
zero-sum game with perfect information (e.g. tic-tac-toe).
"""
from typing import *
from math import inf

from board import Piece, Board, Move


def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    """
    Find the best possible outcome for `original_player`.
    
    Arguments
    ----
        board: Board, the game board
        
        maximizing: bool, whether the player is maximizing their gains or minimizing the opponent's
        
        original_player: Piece, the player for whom we are trying to evaluate the position for
        
        max_depth: int, default 8, how deep the recursion should go before the loop is terminated
    
    Returns: float, the evaluation for `original_player` where
        1.0 = the best play will result in the maximizing player's win
        0.0 = draw
       -1.0 = a loss
    """
    
    # base case -- terminal position or the maximum depth has been reached
    if board.is_win or board.is_draw or not max_depth:
        return board.evaluate(original_player)
    
    # recursive case -- maximize gains or minimzie the opponent's gains
    if maximizing:
        
        best_eval: float = -inf	# initialize an arbitrary minimum
        
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        
        return best_eval
    
    else:
        worst_eval: float = inf	# initialize an arbitrary maximum
        
        for move in board.legal_moves:
            result: float = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(result, worst_eval)
        
        return worst_eval
    
    
def find_best_move(board: Board, max_depth: int = 8, algorithm: Callable) -> Move:
    """ Find the best possible move in the current position, looking up to `max_depth` ahead. """
    
    best_eval: float = -inf
    best_move: Move = Move(-1)
    
    for move in board.legal_moves:
        result: float = algorithm(board.move(move), False, board.turn, max_depth)
        
        if result > best_eval:
            best_eval, best_move = result, move
        
    return best_move


def alpha_beta_prune(
        board: Board,
        maximizing: bool,
        original_player: Piece,
        max_depth: int = 8,
        alpha: float = -inf,
        beta: float = inf
    ) -> float:
    """
    Implement alpha-beta pruning on the minimax search tree.
    The minimax algorithm is extended by keeping two values in track:
        - alpha, the value of the best maximizing move found so far;
        - beta, the value of the best minimizing move found so far.
    A branch is pruned if beta is less than or equal to alpha because there is no better move can be found
    for either minimizing or maximizing mode.
    """
    # base case
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)
    
    # recursive case -- maximize your gains or minimize the opponent's gains
    if maximizing:
        for move in board.legal_moves:
            result: float = alpha_beta_prune(
                board.move(move),
                False,
                original_player,
                max_depth - 1,
                alpha,
                beta
            )
            alpha = max(result, alpha)
            if beta <= alpha:
                break
        return alpha
    else:
        for move in board.legal_moves:
            result = alpha_beta_prune(
                board.move(move),
                True,
                original_player,
                max_depth - 1,
                alpha,
                beta
            )
            beta = min(result, beta)
            if beta <= alpha:
                break
        return beta
    