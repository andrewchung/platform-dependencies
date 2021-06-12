def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    # [expression for item in iterable if condition is true]
    filtered_list = [x for x in numbers if x > 0 and x % 2 == 0]
    return(filtered_list)

