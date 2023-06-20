# condense_csv.py
"""
A script defining `condense_csv()` function, which groups a csv text by the first column.

Assume that the input csv contains three columns indicating id, an attribute name, and an attribute value.
Assume that every item has the same set of attributes and no missing values.
"""
from textwrap import dedent
import csv
import io
from collections import defaultdict

from rich import print


def condense_csv(text: str, id_name: str) -> str:
    """
    `csvtext` is a string of data containing three columns: id, attribute name, and attribute value.
    Group the data so that each row is a unique id.
    Return the output as string output of csv file. This will preserve double quote characters.
    """
    grouped = defaultdict(dict)
    
    reader = csv.reader(dedent(text).strip().splitlines())
    for (row_id, attribute, value) in reader:
        grouped.setdefault(row_id, {})
        grouped[row_id][attribute] = value
    
 
    header = [id_name, *grouped[row_id].keys()]
    
    outfile = io.StringIO()
    writer = csv.writer(outfile, delimiter=',', quotechar='"')
    writer.writerow(header)
    writer.writerows(
        (row_id, *row_dict.values())
        for row_id, row_dict in grouped.items()
    )

    return outfile.getvalue()


# base problem
text = """\
    ball,color,purple
    ball,size,4
    ball,notes,it's round
    cup,color,blue
    cup,size,1
    cup,notes,none"""
print(condense_csv(text, id_name='object'))
print(condense_csv(open('songs.txt').read(), id_name='Track'))

# bonus 1
text = 'A,prop1,"value, with comma"\nA,prop2,value without comma'
print(condense_csv(text, id_name='Name'))