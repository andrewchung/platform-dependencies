import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    x = []
    for char in input_str:
        if char.lower() in VOWELS:
            x.append(True)
        else:
            x.append(False)
    return(all(x))


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for char in input_str:
       if char.lower() in PYTHON:
          return(True)


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for char in input_str:
        if char in string.digits:
            return(True)