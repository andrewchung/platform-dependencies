import string

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    output = []

    for name in names:
        if len(output) == MAX_NAMES:
            break
        if name[0] == QUIT_CHAR:
            break
        if name[0] == IGNORE_CHAR:
            continue
        for char in name:
            if char in string.digits:
                break
        else:
            output.append(name)

    return(output)