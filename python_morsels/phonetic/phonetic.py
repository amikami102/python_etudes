# phonetic.py
"""
A program that spells words phonetically using NATO phonetic alphabet.
If no argument is given, the program prompts the user for input.
An optional argument can be given that contains the letter-to-word mapping to use for spelling.
Accent symbols are ignored.

Usage example:
    $ python phonetic.py Python
    Papa
    Yankee
    Tango
    Hotel
    Oscar
    November
    
    $ python phonetic.py
    Text to spell out: Python is lovely
    Papa
    Yankee
    Tango
    Hotel
    Oscar
    November

    India
    Sierra

    Lima
    Oscar
    Victor
    Echo
    Lima
    Yankee
    
    $ python phonetic.py -f words.txt PyCon
    Pudding
    Yellow
    Charlie
    Orange
    Nuts
    
    $ python phonetic.py
    Text to spell out: Hâlo
    Hotel
    Alfa
    Lima
    Oscar
"""
import argparse
import unicodedata

NATO_CODES = [
    (code[0].casefold(), code.capitalize()) for code in
    (
        'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
        'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November',
        'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
        'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu',
    )
]


def clean_words_input(words: list[str]) -> str:
    """ Join `words` into one string and remove accent symbols. """
    return ''.join(
        (
            char for char in unicodedata.normalize('NFKD', ' '.join(words))
            if char == ' ' or char.isalnum()
         )
    ).casefold()
    
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser('Spell out words phonetically using NATO phonetic alphabet or user-specified code file')
    parser.add_argument('words', nargs='*', type=str, help='Word(s) to be spelled out')
    parser.add_argument('-f', type=argparse.FileType('r'), dest='codefile', help='Optional file containing alternative codes')
    args = parser.parse_args()
    words = args.words
    
    # Ask for user input if no argument was given
    if not words:
        user_input = input('Text to spell out: ')
        args.words = user_input.split(' ')
    
    # Check if a file was passed
    if args.codefile:
        phonetics_map = dict(
            [tuple(line.split()) for line in args.codefile]
        )
    else:
        phonetics_map = dict(NATO_CODES)
    
    # Spell out the words
    for char in clean_words_input(args.words):
        if char == ' ':
            print('')
        code = phonetics_map.get(char, None)
        if not code:
            continue
        else:
            print(code)