def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    literal_space = " "
    count = 0
    for char in text:
        if char == literal_space:
            count += 1
        else:
            break
    return(count)
