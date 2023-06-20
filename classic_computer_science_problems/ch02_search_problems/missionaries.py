# missionaries.py
"""
A script for solving the Missionaries and Cannibals problem.
"""
from rich import print
from typing import *

from generic_search import Node, node_to_path, breadth_first_search


MAX_NUM: int = 3
BOAT_CAPACITY: tuple[int, int] = (1, 2)

class Riverbank:
    WEST: int = 0
    EAST: int = 1
    


class MCState:
    """
    A class representing the number of missionaries and cannibals on the west bank and which bank the boat is docked.
    """
    
    def __init__(self,
                 missionaries: int = MAX_NUM,
                 cannibals: int = MAX_NUM,
                 boat: Riverbank = Riverbank.WEST) -> None:
        """
        Input
        ---
        missionaries (int, default MAX_NUM):
            number of Missionaries on the west bank
        cannibals (int, default MAX_NUM):
            number of Cannibals on the west bank
        boat (Riverbank, default Riverbank.WEST):
            `Riverbank.WEST` if the boat in on the west bank, `Riverbank.EAST` otherwise
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat: Riverbank = boat
    
    def __str__(self) -> str:
        missionary = ":woman:"
        cannibal = ":zombie:"
        boat = ":canoe:"
        water = "~~~~~~~~~~~~~~"
        westbank = (
            missionary * self.missionaries
            + ' ' +
            cannibal * self.cannibals
        )
        eastbank = (
            missionary * (MAX_NUM - self.missionaries)
            + ' ' + 
            cannibal * (MAX_NUM - self.cannibals)
        )
        if self.boat == Riverbank.WEST:
            state = (westbank, boat, water, eastbank)
        else:
            state = (westbank, water, boat, eastbank)
        return ' '.join(('West', *state, 'East'))
    
    def goal_test(self) -> bool:
        """ Check whether all the missionaries and cannibals have moved to the east bank."""
        return self.missionaries == 0 and self.cannibals == 0 and self.is_legal
    
    @property
    def is_legal(self) -> bool:
        """ A legal state is when the cannibals do not outnumber the missionaries on either bank."""
        if (0 > self.missionaries) or (0 > self.cannibals) or (MAX_NUM < self.missionaries) or (MAX_NUM < self.cannibals):
            return False
        elif 0 < self.missionaries < self.cannibals:
            return False
        elif 0 < (MAX_NUM - self.missionaries) < (MAX_NUM - self.cannibals):
            return False
        else:
            return True

    def legal_carry_loads(self, boat_capacity: tuple[int, int] = BOAT_CAPACITY) -> Iterator[tuple[int, int]]:
        """
        Return the list of legal loads that the boat can carry so that the load is within the boat capacity range.
        """
        min_capacity, max_capacity = min(boat_capacity), max(boat_capacity)
        return (
            (missionaries, cannibals)
            for missionaries in range(MAX_NUM)
            for cannibals in range(MAX_NUM)
            if min_capacity <= (missionaries + cannibals) <= max_capacity
        )
        
    
    def carry(self, missionaries: int, cannibals: int) -> 'MCState':
        """
        Carry `missionaries` and `cannibals` on the boat to the other side of the river.
        """
        return MCState(
            self.missionaries - missionaries if not self.boat else self.missionaries + missionaries,
            self.cannibals - cannibals if not self.boat else self.cannibals + cannibals,
            Riverbank.EAST if not self.boat else Riverbank.WEST
        )
    
    def successors(self) -> Iterator['MCState']:
        """
        Return an iterator of possible next states
        """        
        return (
            new_state
            for load in self.legal_carry_loads()
            if (new_state := self.carry(*load)).is_legal
        )
    

def display_solution(path: list[MCState]) -> None:
    """
    Print out the solution path
    """
    if not path:
        return None
    for state in path:
        print(f'{state}')
    
    

if __name__ == '__main__':
    
    print(f'[b]Solving Missionaries and Cannibals problem with {MAX_NUM} each[/b]')
    problem = MCState()
    
    solution: Optional[Node[MCState]] = breadth_first_search(
        problem,
        MCState.goal_test,
        MCState.successors
    )
    if not solution:
        print("No solution found")
    else:
        path: list[MCState] = node_to_path(solution)
        display_solution(path)
    
    
    
                                                                                