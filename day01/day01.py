import sys

def get_list_from_file(file_path):
    with open(file_path) as file:
        return file.read().splitlines()

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
        previous_value = values[i -1]
        current_value = values[i]

        if (current_value > previous_value):
            counter += 1
        i += 1

    return counter

is_terminal_script = __name__ == '__main__' and len(sys.argv) > 1

if is_terminal_script:
    file_path = sys.argv[1]
    lines = get_list_from_file(file_path)

    print(count_increases(lines))
