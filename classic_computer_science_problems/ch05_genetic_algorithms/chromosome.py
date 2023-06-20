# chromosome.py
"""
A script defining `Chromosome` class object for genetic algorithm.
"""
from typing import *
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Chromosome') # type of chromosome


class Chromosome(ABC):
    """All methods must be overridden."""
    
    @abstractmethod
    def fitness(self) -> float:
        """ Determine its own fitness. """
    
    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        """ Create an instance with randomly selected genes. """
    
    @abstractmethod
    def crossover(self: T, other: T) -> tuple[T, T]:
        """ Combine itself with another chromosome to create children. """
    
    @abstractmethod
    def mutate(self) -> None:
        """ Make a small change in itself. """
    
    
    

