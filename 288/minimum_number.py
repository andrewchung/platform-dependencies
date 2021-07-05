from typing import List


def minimum_number(digits: List[int]) -> int:
    num_str = ""
    num_list = sorted(list(set(digits)))   

    if digits == [] or digits == [0]:
        return 0
    else:
        for num in num_list:
            num_str += str(num)
        return int(num_str.lstrip('0'))
