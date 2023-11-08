# condense_csv.py
"""
A script defining `condense_csv()` function, which groups a csv text
by the first column.

Assume that the input csv contains three columns indicating id,
an attribute name, and an attribute value.
Assume that every item has the same set of attributes and no missing values.
"""
from textwrap import dedent
import csv
from io import StringIO
from collections import Counter
from operator import itemgetter
from itertools import groupby


def condense_csv(text: str, id_name: str = None) -> str:
    """
    Group `text`, which is a CSV text with id, attribute name, and attribute
    value columns, by the first column.
    """
    reader = csv.reader(dedent(text).splitlines())
    
    if not id_name:
        id_name = next(reader)[0]
    
    groups = {}
    attributes = [id_name]
    for identifier, attribute, value in reader:
        group = groups.setdefault(identifier, {id_name: identifier})
        group[attribute] = value
        attributes.append(attribute)
    
    file = StringIO()
    writer = csv.DictWriter(file, fieldnames = list(Counter(attributes)))
    writer.writeheader()
    writer.writerows(list(groups.values()))
    return file.getvalue().replace('\r\n', '\n')
    
    

# base problem
text = """\
    ball,color,purple
    ball,size,4
    ball,notes,it's round
    cup,color,blue
    cup,size,1
    cup,notes,none"""
assert condense_csv(text, id_name='object') == """\
object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none
"""
assert condense_csv(open('songs.txt').read(), id_name='Track') == dedent(
    """\
    Track,Artist,Title,Time
    01,Otis Taylor,Ran So Hard the Sun Went Down,3:52
    02,Waylon Jennings,Honky Tonk Heroes (Like Me),3:29
    """)

# bonus 1, handle data that contain commas
text = 'A,prop1,"value, with comma"\nA,prop2,value without comma'
assert condense_csv(text, id_name='Name') ==\
    dedent("""\
        Name,prop1,prop2
        A,"value, with comma",value without comma
        """)

# bonus 2, test when `id_name` is optional
text = """\
    object,property,value
    ball,color,purple
    ball,size,4
    ball,notes,it's round
    cup,color,blue
    cup,size,1
    cup,notes,none"""
assert condense_csv(text) ==\
    """\
object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none
"""

# bonus 3, allow for missing values and out-of-order properties
text = 'A,prop1,x\nA,prop2,y\nB,prop2,z'
assert condense_csv(text, id_name='Name') == dedent(
    """\
    Name,prop1,prop2
    A,x,y
    B,,z
    """
)
