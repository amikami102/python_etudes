# bullet_points.py
"""
A program that parses a bullet list.
"""
from typing import *
from collections import deque
from dataclasses import dataclass, field

BULLET = '- '
INDENT_SIZE = 4

@dataclass
class Bullet:
    text: str
    children: list['Bullet'] = field(init=False, default_factory=list)
    
    @classmethod
    def create_bullet(cls, bullet_line: str) -> tuple[int, 'Bullet']:
        """ Return a tuple of the level of `bullet_line` and `Bullet` object. """
        levels, _, text = bullet_line.partition(BULLET)
        levels: int = len(levels) // INDENT_SIZE
        return levels, Bullet(text)
    
    def add_child(self, child: 'Bullet') -> None:
        self.children.append(child)
        
    
    def __str__(self) -> str:
        return f'{BULLET}{self.text}'


def parse_bullets(text: str) -> list[Bullet]:
    """ Returns a list of `Bullet` objects parsed from `text`. """
    bullets: list[Bullet] = []
    parents: dict[int, Bullet] = {}
    
    for line in text.splitlines():
        levels, bullet = Bullet.create_bullet(line)
        if not levels:
            bullets.append(bullet)
            parents.clear() # clear the dictionary to build a new tree
            parents.update({0: bullet})
        else:
            parents[levels - 1].add_child(bullet)
        
        parents.update({levels: bullet})
    return bullets


# base problem, test `parse_bullets()`
data = """\
- Email Python Morsels users
- Wish my sister happy birthday
- Call back my dad
- Do laundry
""".strip()
bullets = parse_bullets(data)
assert bullets[3].text == 'Do laundry'
assert str(bullets[1]) == '- Wish my sister happy birthday'

# bonus 1, parse nested bullets
data = """\
- Buy groceries
- Python Morsels
    - Fix bug on exercise submission page
        - Figure out how to reproduce bug
        - Write tests
        - Write and deploy fix
    - Write a new exercise
""".strip()
bullets = parse_bullets(data)
assert not len(bullets[0].children)
assert len(bullets[1].children) == 2
assert bullets[1].children[0].children[1].text == 'Write tests'