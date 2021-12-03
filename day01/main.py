import sys

def count_increases(values):
    """
    returns the number of times that a value in a list is higher than its predecessor

    >>> count_increases([1,2,3])
    2
    >>> count_increases([1,1,1])
    0
    >>> count_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    7
    """

    i, counter = 1, 0

    while i < len(values):
        previous_value = int(values[i -1])
        current_value = int(values[i])

        if (current_value > previous_value):
            counter += 1
        i += 1

    return counter

main = count_increases
