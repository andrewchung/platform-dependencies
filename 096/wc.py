from typing import Counter
import sys


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    count_lines = 0
    count_words = 0
    count_chars = 0
    with open(file_) as f:
        for line in f:
            for char in line:
                if char.isprintable():
                    count_chars += 1
            count_words += len(line.split())
            count_lines += 1
        if count_lines > 1:
            print(f"{count_lines} {count_words} {count_chars + count_lines} {sys.argv[1]}")
        else:
            print(f"{count_lines} {count_words} {count_chars} {sys.argv[1]}")

    

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))