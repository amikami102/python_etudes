# phoneAndEmail.py
"""
A program that searches the text in your clipboard for U.S. phone numbers and email addresses.
The match results are copied into clipboard.

Matches for phone numbers will not include the +1 country code.

Usage example:
    $ python phoneAndEmail.py
"""
import re

import pyperclip


PHONE_RE = re.compile(
    r"""
    (
        (?P<area>\d{3}|\(\d{3}\))	# area code, may be enclosed by parentheses
        (\s|-|\.)?			# separator
        (?P<first3>\d{3})				# first three digits
        (\s|-|\.)?			# separator
        (?P<last4>\d{4})				# last four digits
        (					
            \s*				# may or may not be separated by a whitespace
            (ext|x|ext\.)	# extension marker
            \s*				
            (?P<ext>\d{2,5})		# extension code
        )?
    )
    """,
    re.VERBOSE
)
EMAIL_RE = re.compile(
    r"""
    (
        ([a-zA-Z0-9\.\-\%\+]*)		# username
        @		# @ symbol
        ([a-zA-Z0-9\.\-]*)		# domain and dot-something
    )
    """,
    re.VERBOSE
)


if __name__ == '__main__':
    
    # wait for non-empty text string to be put on the clipboard
    text: str = pyperclip.paste()
    
    # find matches for U.S. phone numbers
    phonenums = [
        matched.group(0)
        for matched in PHONE_RE.finditer(text)
    ]
    
    # find matches for emails
    emails = [
        matched.group(0)
        for matched in EMAIL_RE.finditer(text)
    ]
    
    # concatenate the results into a string block
    result = '\n'.join(phonenums) + '\n' + '\n'.join(emails)
    
    # copy the result to the clipboard
    if result:
        pyperclip.copy(result)
        print('Copied to clipboard:')
        print(result)
    else:
        print('No phone numbers or emails found.')
