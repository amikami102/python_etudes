# markdownify.py
"""
A script implementing `markdownify()` function that converts HTML to markdown.
"""
from rich import print
import re


SPACES_RE = re.compile(r'\s+')							# two ore more white spaces
PARAGRAPHS_RE = re.compile(r'<p>(.+?)</p>')				# <p>...</p> tag
LINEBREAKS_RE = re.compile(r'<br>')						# <br> tag


def markdownify(html_text: str) -> str:
    """
    Format `html_text` written in html to markdown by doing the following:
    
        - Handles whitespace normalization where consecutive linebreaks or spaces
        are collapsed into single space character.
        - Translates `<p>` tags so that paragraphs have two line breaks between them.
        - Convert `<br>` tags to two white spaces followed by a newline character.
    """
    html_text = SPACES_RE.sub(r' ', html_text)
    html_text = PARAGRAPHS_RE.sub(r'\1\n\n', html_text) # matches group(1) of the regex match
    html_text = LINEBREAKS_RE.sub(r'  \n', html_text)
    return html_text.strip()


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

# bonus 1
html = "Text with<br>linebreaks!"
text = "Text with  \nlinebreaks!"
assert markdownify(html) == text

html = "<p>A paragraph with a<br>linebreak</p>"
text = "A paragraph with a  \nlinebreak"
assert markdownify(html) == text