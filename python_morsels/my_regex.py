# my_regex.py for concat_check.py
import re

pattern = re.compile(
    r"implicit\n"
    u"line continuation"
)
m = pattern.search("""
implicit
"""
'line continuation')
print('match' if m else 'no match')