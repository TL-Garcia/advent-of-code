OPERATIONS = {
    'forward': lambda x, coordinates: {'x': coordinates['x'] + x, 'y': coordinates['y']},
    'down': lambda y, coordinates: {'x': coordinates['x'], 'y': coordinates['y'] + y},
    'up': lambda y, coordinates: {'x': coordinates['x'], 'y': coordinates['y'] - y},
}

STARTING_COORDINATES = {
    'x': 0,
    'y': 0
}

def get_coordinates(movements, starting_coordinates):
    coordinates = starting_coordinates

    """
    Takes a list of movements and calculates the resulting coordinates

    >>> get_coordinates(['up 2', 'down 1', 'down 1', 'down 3', 'forward 4'])
    {'x': 4, 'y': 3}

    >>> get_coordinates(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    {'x': 15, 'y': 10}
    """

    for movement in movements:
        split_movement = movement.split(' ')
        direction = split_movement[0]
        amount = int(split_movement[1])

        calculate_movement = OPERATIONS[direction]
        coordinates = calculate_movement(amount, coordinates)

    return coordinates

def main(movements):
    """
    Takes a list of numbers and returns the product of the resulting coordinates
    >>> main(['up 2', 'down 1', 'down 1', 'down 3', 'forward 4'])
    12

    >>> main(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    150
    """

    coordinates = get_coordinates(movements, STARTING_COORDINATES)

    return coordinates['x'] * coordinates['y']
