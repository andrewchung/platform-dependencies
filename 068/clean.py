import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    output = ""
    for char in input_string:
        if char not in string.punctuation:
            output = output + char
    return(output)

