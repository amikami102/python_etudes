# bullet_points.py
"""
A program that parses a bullet list.
"""
from typing import *
from collections import UserList
from dataclasses import dataclass, field
from textwrap import indent, dedent

BULLET = '- '
INDENT_SIZE = 4


class BulletList(UserList):
    """A sequence of bullets."""
    def __str__(self) -> str:
        return '\n'.join([str(bullet) for bullet in self.data])
    
    def filter(self, pattern: str = '') -> 'BulletList':
        """
        Return bullets that contain `pattern` in their texts or children's.
        """
        filtered = BulletList()
        for bullet in self.data:
            continue
            # TODO: think of adding a new bullet with different set of children
        return filtered

@dataclass
class Bullet:
    text: str
    children: BulletList = field(init=False, default_factory=BulletList)
    parent: 'Bullet' = field(default=None)
    
    @classmethod
    def create_bullet(cls, line: str) -> tuple[int, 'Bullet']:
        """Return a tuple of the level of `line` and `Bullet` object."""
        n_tabs, _, text = line.partition(BULLET)
        return len(n_tabs) // INDENT_SIZE, Bullet(text)
    
    def add_child(self, child: 'Bullet') -> None:
        child.parent = self
        self.children.append(child)
    
    def __str__(self) -> str:
        return '\n'.join(print_bullets(self))


def parse_bullets(text: str) -> list[Bullet]:
    """Returns a list of `Bullet` objects parsed from `text`."""
    bullets: BulletList = BulletList()
    parents: dict[int, Bullet] = {}
    
    for line in text.splitlines():
        levels, bullet = Bullet.create_bullet(line)
        if levels == 0:
            bullets.append(bullet)
            parents.clear() # clear the dictionary to build a new tree
        else:
            parents[levels - 1].add_child(bullet)
        parents.update({levels: bullet})
    return bullets


def print_bullets(bullet:Bullet, level: int = 0) -> list[str]:
    """Return string representation of `bullet` including its children."""
    #TODO: simplify this code. Indenting an indented line
    # is equivalent to indenting by two tabs.
    tab: str = ' ' * INDENT_SIZE
    my_bullets = [indent(f'{BULLET}{bullet.text}', tab * level)]
    for child in bullet.children:
        if child.children:
            my_bullets.extend(print_bullets(child, level+1))
        else:
            my_bullets.append(indent(f'{BULLET}{child.text}', tab * (level+1)))
    return my_bullets
    

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

# bonus 2, test `parent` attribute
data = """
- Chapter 1
     - Section A
         - Sub-section i
     - Section B
""".strip()
my_bullets = parse_bullets(data)
chapter1 = my_bullets[0]
section_a = chapter1.children[0]
subsection1 = section_a.children[0]
assert subsection1.parent == section_a
assert section_a.parent == chapter1
assert chapter1.parent == None
assert str(my_bullets[0]) == dedent("""
- Chapter 1
    - Section A
        - Sub-section i
    - Section B
""").strip('\n')
assert str(my_bullets[0].children[0]) == dedent("""
- Section A
    - Sub-section i
""").strip('\n')
assert str(my_bullets[0].children[1]) == dedent("""
- Section B
""").strip('\n')

# bonus 3, test `parse_bullet()` output's string representation 
data = """
- Buy groceries
- Python Morsels
     - Fix bug on exercise submission page
         - Figure out how to reproduce bug
         - Write tests
         - Write and deploy fix
     - Write a new exercise
""".strip()
my_bullets = parse_bullets(data)
assert str(my_bullets) == """
- Buy groceries
- Python Morsels
    - Fix bug on exercise submission page
        - Figure out how to reproduce bug
        - Write tests
        - Write and deploy fix
    - Write a new exercise
""".strip()
assert str(my_bullets.filter("fix")) == dedent("""
- Python Morsels
    - Fix bug on exercise submission page
        - Write and deploy fix
""").strip()
results = my_bullets.filter("write")
assert str(results) == dedent("""
- Python Morsels
    - Fix bug on exercise submission page
        - Write tests
        - Write and deploy fix
    - Write a new exercise
""").strip()
assert results[0].children[0].text == 'Fix bug on exercise submission page'