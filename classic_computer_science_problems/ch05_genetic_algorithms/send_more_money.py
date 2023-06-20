# send_more_money.py
"""
A script solving cryptarithmetic problem using genetic algorithm.

Recall that ch.2 solved the same problem with constraint satisfaction framework.

Unlike the ch.2 version, this solution allows 'M' to equal 0.
"""
from typing import *
import random
from copy import deepcopy

from rich import print

from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm


LETTERS: list[str] = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y', '', ''] # empty spaces are fillers for two unassigned digits out of 0-9
FOURDIGITS: tuple[int] = (1000, 100, 10, 1)
FIVEDIGITS: tuple[int] = (10_000, *FOURDIGITS)


class SendMoreMoney(Chromosome):
    
    def __init__(self, letters: list[str]) -> None:
        self.letters: list[str] = letters
    
    def substitute(self) -> tuple[int, int, int]:
        send: int = sum(
            place * self.letters.index(letter)
            for place, letter in zip(FOURDIGITS, 'SEND')
        )
        more: int = sum(
            place * self.letters.index(letter)
            for place, letter in zip(FOURDIGITS, 'MORE')
        )
        money: int = sum(
            place * self.letters.index(letter)
            for place, letter in zip(FIVEDIGITS, 'MONEY')
        )
        return send, more, money
    
    def fitness(self) -> float:
        """ Closer to 1, the more fitting as solution."""
        send, more, money = self.substitute()
        diff: int = abs(money - (send + more))
        return 1 / (diff + 1)
    
    @classmethod
    def random_instance(cls) -> 'SendMoreMoney':
        letters = list(LETTERS)
        random.shuffle(letters)
        return SendMoreMoney(letters)
    
    def crossover(self, other: 'SendMoreMoney') -> tuple['SendMoreMoney', 'SendMoreMoney']:
        """
        The result of the crossover is that one child will be a replica of
        one parent except with two randomly selected letters swapped and likewise for the other child.
        """
        child1, child2 = deepcopy(self), deepcopy(other)
        idx1, idx2 = random.sample(range(len(self.letters)), 2)
        l1, l2 = child1.letters[idx1], child2.letters[idx2]
        
        child1.letters[child1.letters.index(l2)] = child1.letters[idx2]
        child1.letters[idx2] = l2
        
        child2.letters[child2.letters.index(l1)] = child2.letters[idx1]
        child2.letters[idx1] = l1
        
        return child1, child2
    
    def mutate(self) -> None:
        """ Randomly switch the values of two letters. """
        idx1, idx2 = random.sample(range(len(self.letters)), k=2)
        self.letters[idx1], self.letters[idx2] = self.letters[idx2], self.letters[idx1]
        
    def __str__(self) -> str:
        send, more, money = self.substitute()
        diff: int = abs(money - (send + more))
        return f"{money} - ({send} + {more}) = {diff}"
        
        
if __name__ == '__main__':
    
    SIZE: int = 1000
    
    initial_pop: list[SendMoreMoney] = [
        SendMoreMoney.random_instance() for _ in range(SIZE)
    ]
    algo: GeneticAlgorithm[SendMoreMoney] = GeneticAlgorithm(
        initial_pop,
        1.0,
        1000,
        0.2,
        0.7,
        GeneticAlgorithm.SelectionType.ROULETTE
    )
    
    solution: SendMoreMoney = algo.run()
    print(solution)