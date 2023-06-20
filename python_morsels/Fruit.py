# Fruit.py
"""
"""

from rich import print

class Fruit:
    def __init__(self, data = {'color': 'unknown'}) -> None:
        self._data = {}
        #self._data = data
        self._data.update(data)
    
    def set_color(self, color: str) -> None:
        self._data['color'] = color
    
    def print_data(self) -> None:
        print(f"I'm {self._data.get('color')}.")

print(Fruit()._data)
orange = Fruit()
orange.set_color('orange')

print(Fruit()._data)
apple = Fruit()
apple.print_data()
