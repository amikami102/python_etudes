# fancy_iterable.py

from typing import *
from itertools import chain, dropwhile, takewhile
T = TypeVar('T')


class fancy:
    """Accepts an iterable and supports lazy chaining of operations on it."""
    
    def __init__(self, iterable: Iterable[T]):
        self.iterable = iterable

    def __iter__(self) -> Iterator:
        return iter(self.iterable)

    def filter(self, func: Callable[T, T]) -> 'fancy':
        return fancy(filter(func, self))

    def map(self, func: Callable[T, T]) -> 'fancy':
        return fancy(map(func, self))

    def every(self, predicate: Callable[T, bool]) -> bool:
        return all(predicate(item) for item in self)

    def some(self, predicate: Callable[T, bool]) -> bool:
        return any(predicate(item) for item in self)
    
    def concat(self, *iterables) -> 'fancy':
        return fancy(chain(self.iterable, *iterables))
    
    def drop_while(self, predicate: Callable[T, bool]) -> 'fancy':
        return fancy(dropwhile(predicate, self.iterable))
    
    def take_while(self, predicate: Callable[T, bool]) -> 'fancy':
        return fancy(takewhile(predicate, self.iterable))
    

# base problem
from itertools import count, islice
def square(n): return n**2
def is_odd(n): return n % 2 == 1

every_single_number = count()
numbers = fancy(every_single_number)
squared_odds = numbers.filter(is_odd).map(square)
assert list(islice(squared_odds, 4)) == [1, 9, 25, 49]
odd_squares = fancy(count()).map(square).filter(is_odd)
assert list(islice(odd_squares, 4)) == [1, 9, 25, 49]

fruits = ["lemon", "orange", "pear", "watermelon", "jujube"]
def more_than_5_letters(string): return len(string) > 5
assert not fancy(fruits).every(more_than_5_letters)
assert fancy(fruits).some(more_than_5_letters)
assert list(fancy(fruits).filter(more_than_5_letters)) ==\
    ['orange', 'watermelon', 'jujube']

# bonus 1, test `concat`, `drop_while`, and `take_while` methods
fruits = ["lemon", "orange", "pear", "watermelon", "jujube"]
vegetables = ["carrot", "kohlrabi", "onion", "arugula"]
more_fruits = ["apple"]
fruit_and_veg = fancy(fruits).concat(vegetables, more_fruits)
assert fruits.pop(1) == 'orange'
vegetables.append('broccoli')
assert list(fruit_and_veg) ==\
    ['lemon', 'pear', 'watermelon', 'jujube', 'carrot',
     'kohlrabi', 'onion', 'arugula', 'broccoli', 'apple']

letters = "aabacada"
def is_a(letter): return letter == "a"
assert "".join(fancy(letters).drop_while(is_a)) == 'bacada'

letters = "PYtHoN!"
def is_capital(letter): return letter.isupper()
assert list(fancy(letters).take_while(is_capital)) == ['P', 'Y']