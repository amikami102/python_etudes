# markdownify.py
"""
A script implementing `markdownify()` function that converts HTML to markdown.
"""
import re

SPACES_RE = re.compile(r'\s+')
PARAGRAPH_RE = re.compile(r'<p>(.+?)</p>', re.DOTALL)
LINEBREAK_RE = re.compile(r'<br>')
STRONG_RE = re.compile(r"<strong>(.*?)</strong>", re.DOTALL)


def markdownify(text: str) -> str:
    """Normalize whitespaces and trandslate paragraphs."""
    text = SPACES_RE.sub(r' ', text)
    text = PARAGRAPH_RE.sub(r'\1\n\n', text)
    text = LINEBREAK_RE.sub(r'  \n', text)
    text = STRONG_RE.sub(r'**\1**', text)
    return text.strip() 


# base problem
html: str = (
    "<p>A paragraph" +
    " of text</p>" +
    "<p>Another paragraph</p>"
)
text = "A paragraph of text\n\nAnother paragraph"
assert markdownify(html) == text

html = "This text\nhas words over\nmultiple lines"
text = "This text has words over multiple lines"
assert markdownify(html) == text

# bonus 1, test linebreak
html = "Text with<br>linebreaks!"
text = "Text with  \nlinebreaks!"
assert markdownify(html) == text

html = "<p>A paragraph with a<br>linebreak</p>"
text = "A paragraph with a  \nlinebreak"
assert markdownify(html) == text

# bonus 2, test bold
assert markdownify("There's some <strong>bold text</strong> here!") ==\
    "There's some **bold text** here!"
