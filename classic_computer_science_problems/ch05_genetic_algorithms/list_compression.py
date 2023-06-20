# list_compression.py
"""
This script will compress a list using `zlib.compress()`.
We don't care about the order of the items, just that the items are intact.
What order of the items will maximize the compresion ratio?

n.b. I ran this once, and it took all 1000 generations to arrive at ...
```
['SungWon', 'Aenne', 'Price', 'Tarny', 'Jazzy', 'Shelby', 'Noicky', 'Ash', 
'Dunkey', 'Matt', 'Rick', 'Alex'] bytes: 132
```
Was it really worth it? Looking at the log, the best fitness of the generation
stayed at 0.007575757575757576 since the third generation.
"""
from typing import *
import random
import sys
import zlib
from copy import deepcopy
import pickle

from rich import print

from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm

T = TypeVar('T')


PEOPLE: list[str] = [
    'Tarny',
    'Noicky',
    'Shelby',
    'Matt',
    'SungWon',
    'Alex',
    'Price',
    'Ash',
    'Jazzy',
    'Rick',
    'Aenne',
    'Dunkey'
]


def compress(myobject: list[T]):
    return zlib.compress(pickle.dumps(myobject))


class ListCompression(Chromosome):
    
    def __init__(self, mylist: list[T]) -> None:
        self.mylist: list[T] = mylist
    
    @property
    def bytes_compressed(self) -> int:
        return sys.getsizeof(compress(self.mylist))
    
    def fitness(self) -> float:
        """ Lower the bytes size, the closer to 1, the more fit. """
        return 1 / self.bytes_compressed
    
    @classmethod
    def random_instance(cls) -> 'ListCompression':
        """ Randomlly shuffle `PEOPLE`. """
        my_list: list[str] = deepcopy(PEOPLE)
        random.shuffle(my_list)
        return ListCompression(my_list)

    def crossover(self, other: 'ListCompression') -> tuple['ListCompression', 'ListCompression']:
        """ Each child is a duplicate of one parent except that two elements have switched places. """
        child1, child2 = deepcopy(self), deepcopy(other)
        idx1, idx2 = random.sample(range(len(self.mylist)), 2)
        l1, l2 = child1.mylist[idx1], child2.mylist[idx2]
        
        child1.mylist[child1.mylist.index(l2)] = child1.mylist[idx2]
        child1.mylist[idx2] = l2
        
        child2.mylist[child2.mylist.index(l1)] = child2.mylist[idx1]
        child2.mylist[idx1] = l1
        
        return child1, child2
    
    def mutate(self) -> None:
        """ Swap two items. """
        idx1, idx2 = random.sample(range(len(self.mylist)), 2)
        self.mylist[idx1], self.mylist[idx2] = self.mylist[idx2], self.mylist[idx1]
    
    def __str__(self) -> str:
        return f"{repr(self.mylist)} bytes: {self.bytes_compressed}"


if __name__ == '__main__':
    
    SIZE: int = 1000
    
    initial_pop: list[ListCompression] = [
        ListCompression.random_instance() for _ in range(SIZE)
    ]
    algo: GeneticAlgorithm[ListCompression] = GeneticAlgorithm(
        initial_pop,
        threshold=1.0,
        max_gen=1000,
        mutate_prob = 0.2,
        xover_prob=0.7,
        selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT
    )
    result: ListCompression = algo.run()
    print(result)