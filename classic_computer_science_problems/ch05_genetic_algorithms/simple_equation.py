# simple_equation.py
"""
A script implementing genetic algorithm to find (x, y) that would maximize
f(x, y) = 6x - x^2 + 4y - y^2.

The solution is x = 3 and y = 2 where f(x, y) would be maximized at
max{f(x, y)} = 6*3 - 9 + 4(2) - 4 = 18-9+8-4 = 13.

Note that you might need a couple of tries until you get the solution,
and the number of generations it takes to reach the solution might vary.

Here is a sample output that got the solution in 42 generations:
```
Generation 0 has best fitness -19 and average fitness -5340.8.
Generation 1 has best fitness -28 and average fitness -1318.95.
Generation 2 has best fitness -4 and average fitness -101.6.
Generation 3 has best fitness 8 and average fitness 4.6.
Generation 4 has best fitness 5 and average fitness 3.1.
Generation 5 has best fitness 8 and average fitness -1.8.
Generation 6 has best fitness 9 and average fitness -4.75.
Generation 7 has best fitness 4 and average fitness -3.6.
Generation 8 has best fitness -3 and average fitness -42.
Generation 9 has best fitness -3 and average fitness -24.15.
Generation 10 has best fitness -4 and average fitness -47.2.
Generation 11 has best fitness -4 and average fitness -55.05.
Generation 12 has best fitness 5 and average fitness -32.8.
Generation 13 has best fitness 5 and average fitness -61.85.
Generation 14 has best fitness 8 and average fitness -90.15.
Generation 15 has best fitness 9 and average fitness 2.65.
Generation 16 has best fitness 9 and average fitness 8.25.
Generation 17 has best fitness -3 and average fitness -6.4.
Generation 18 has best fitness -3 and average fitness -54.7.
Generation 19 has best fitness 3 and average fitness -8.7.
Generation 20 has best fitness 4 and average fitness -16.3.
Generation 21 has best fitness 4 and average fitness -11.
Generation 22 has best fitness 4 and average fitness -9.7.
Generation 23 has best fitness 8 and average fitness -15.4.
Generation 24 has best fitness 4 and average fitness -22.25.
Generation 25 has best fitness 5 and average fitness -2.6.
Generation 26 has best fitness 4 and average fitness -84.8.
Generation 27 has best fitness 4 and average fitness -38.6.
Generation 28 has best fitness 8 and average fitness -3.
Generation 29 has best fitness 8 and average fitness 4.45.
Generation 30 has best fitness 12 and average fitness -24.9.
Generation 31 has best fitness 8 and average fitness 8.
Generation 32 has best fitness 11 and average fitness 4.7.
Generation 33 has best fitness 12 and average fitness -32.3.
Generation 34 has best fitness 12 and average fitness -29.6.
Generation 35 has best fitness 12 and average fitness -8.4.
Generation 36 has best fitness 12 and average fitness 1.1.
Generation 37 has best fitness 12 and average fitness 6.35.
Generation 38 has best fitness 12 and average fitness -4.85.
Generation 39 has best fitness 12 and average fitness 5.5.
Generation 40 has best fitness 11 and average fitness -1.45.
Generation 41 has best fitness 12 and average fitness 8.35.
X: 3 Y: 2 Fitness: 13
```
"""
from typing import *
from random import randrange, random
from copy import deepcopy

from rich import print

from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm


class SimpleEquation(Chromosome):
    
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
    
    def __iter__(self) -> Iterator[int]:
        yield self.x
        yield self.y
    
    def fitness(self) -> float:
        return (6 * self.x) - (self.x * self.x) + (4 * self.y) - (self.y * self.y)
    
    @classmethod
    def random_instance(cls) -> 'SimpleEquation':
        """ Set x and y to random number chosen between 1 and 100. """
        return SimpleEquation(randrange(100), randrange(100))
    
    def crossover(self, other: 'SimpleEquation') -> tuple['SimpleEquation', 'SimpleEquation']:
        """ Switch the (x, y) pairing between self and other. """
        child1, child2 = deepcopy(self), deepcopy(other)
        child1.y, child2.y = other.y, self.y
        return child1, child2
    
    def mutate(self) -> None:
        """
        25% chance of adding 1 to self.x, likewise for self.y.
        25% chance of subtracting 1 from self.x, likewise for self.y
        """
        if 0 <= random() < 0.25:
            self.x += 1
        elif 0.25 <= random() < 0.50:
            self.x -= 1
        elif 0.50 <= random() < 0.75:
            self.y += 1
        else:
            self.y -= 1
    
    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} Fitness: {self.fitness()}"
    

if __name__ == '__main__':
    
    
    SIZE: int = 20
    
    initial_pop: list[SimpleEquation] = [
        SimpleEquation.random_instance()
        for _ in range(SIZE)
    ]
    
    algo: GeneticAlgorithm[SimpleEquation] = GeneticAlgorithm(
        initial_pop,
        threshold = 13.0,
        max_gen = 100,
        xover_prob = 0.1,
        mutate_prob = 0.7
    )
    
    solution: SimpleEquation = algo.run()
    print(solution)
    
    
    