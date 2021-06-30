import string
import secrets


chars = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    key = ''
    for i in range(parts):
        key += ''.join(secrets.choice(chars) for i in range(chars_per_part)) + '-'
    return(key[0:-1])
