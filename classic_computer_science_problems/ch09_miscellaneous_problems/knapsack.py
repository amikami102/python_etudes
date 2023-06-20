# knapsack.py
"""
A script defining a knapsack problem wherein you want to maximize the value of discrete items
in a knapsack within its finite capacity. 

The following table demonstrates `table` that `Knapcksack` class builds.
As you go down the column, the pool of items you can select from expands to include the items from the current and previous rows.
As you go across the row, the maximum capcity of the knapsack increases.
The first column says that none of the items can fit in a knapsack with 0 lb. capacity.
The second columns says that a knapsack of 1 lb capacity can either fit
    - one of item 1, giving the knapsack a total value of $5.00,
    - one of item 1 and zero of item 2, keeping the knapsack value at $5.00, and
    - one of item 3 and zero of others, giving the knapsack value $15.00.

                    0 lb	1 lb	2 lb	3 lb
item 1 (1 lb, $5)	0		5		5		5
item 2 (2 lb, $10)	0		5		10		15
item 3 (1 lb, $15)	0		15		20		25
"""
from typing import *
from collections import namedtuple
from dataclasses import dataclass, field


Item = namedtuple('Item', ['name', 'weight', 'value'])


@dataclass
class Knapsack:
    items: list[Item]
    max_capacity: int
    table: list[list[float]] = field(init=False)
    
    def __post_init__(self):
        self.table: list[list[float]] = [
            [0.0 for _ in range(self.max_capacity + 1)]
            for _ in range(len(self.items) + 1)
        ]
        for n, item in enumerate(self.items):
            for cap in range(1, self.max_capacity + 1):
                previous_total_value: float = self.table[n][cap]
                if cap >= item.weight:	# item fits in knapsack
                    self.table[n + 1][cap] = max(
                        self.table[n][cap - item.weight] + item.value,
                        previous_total_value
                    )
                else:	# no room for theis item
                    self.table[n + 1][cap] = previous_total_value
                    
    def solve(self) -> list[Item]:
        """
        Find the solution to the knapsack problem by working backwards from the
        highest capacity and the final explored combination of items,
        i.e. the bottom-right corner of the table and up the column unless
        an item at minus 1 of the row index is added to the knapsack, in case move leftward to the next column.
        """
        solution: list[Item] = []
        cap = self.max_capacity
        for n in range(len(items), 0, -1):
            if self.table[n][cap] != self.table[n-1][cap]:
                solution.append(self.items[n-1])
                cap -= self.items[n-1].weight
        return solution


if __name__ == '__main__':
    
    items: list[Item] = [
        Item("television", 50, 500),
        Item("candlesticks", 2, 300),
        Item("stereo", 35, 400),
        Item("laptop", 3, 1000),
        Item("food", 15, 50),
        Item("clothing", 20, 800),
        Item("jewelry", 1, 4000),
        Item("books", 100, 300),
        Item("printer", 18, 30),
        Item("refrigerator", 200, 700),
        Item("painting", 10, 1000)
    ]
    
    problem = Knapsack(items, 75)
    print(*problem.solve(), sep='\n')
