from collections import Counter

def freq_digit(num: int) -> int:
    num_string = str(num)
    num_freq = dict(Counter(num_string))
    num_sorted = sorted(num_freq.items(), key=lambda x: x[1], reverse=True)
    return(int(num_sorted[0][0]))
