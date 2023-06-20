# board.py
"""
A script defining abstract classes for board games, `Piece` and `Board`.
"""
from typing import *
from abc import ABC, abstractmethod
from dataclasses import dataclass


Move = NewType('Move', int)


class Piece:
    """ A abstract base class object a boardgame piece. """
    @property
    def opposite(self) -> 'Piece':
        raise NotImplementedError('Should be implemented by subclasses')

@dataclass
class Board(ABC):
    """ An abstract base class representing the board of a board game. """
    
    @property
    @abstractmethod
    def turn(self) -> Piece:
        """ Implement a player's turn. """
    
    @abstractmethod
    def move(self, loc: Move) -> 'Board':
        """ Return a new `Board` after a move has been played on `loc` of `self`. """
    
    @property
    @abstractmethod
    def legal_moves(self) -> list[Move]:
        """ Return a list of legal moves that can be made on the current state of `Board`. """
    
    @property
    @abstractmethod
    def is_win(self) -> bool:
        """ Return True if the current state of `Board` indicates that some player has won the game? """
    
    @property
    def is_draw(self) -> bool:
        """ Return True if `self.is_win` is False and there are no more legal moves. """
        return (not self.is_win) and (not self.legal_moves)
    
    @abstractmethod
    def evaluate(self, player: Piece) -> float:
        """ Evaluate the current state of the `Board` to determine if `player` has an advantage. """