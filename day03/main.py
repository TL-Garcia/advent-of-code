from functools import reduce

def generate_rate_value(accumulated_values, discrimination_fn):
    result_binary = []

    for value in accumulated_values:
        if (discrimination_fn(value)):
            result_binary.append('1')
        else:
            result_binary.append('0')
    return int(''.join(result_binary), 2)

def main(entries):
    number_of_positions_per_entry = len(entries[0])
    accumulated_values = [0] * number_of_positions_per_entry

    for entry in entries:
        for index in range(0, number_of_positions_per_entry):
            digit_value = int(entry[index])
            accumulated_values[index] += digit_value




    gamma_rate = generate_rate_value(accumulated_values, lambda value: value > len(entries) // 2)
    epsilon_rate = generate_rate_value(accumulated_values, lambda value: value < len(entries) // 2)

    return gamma_rate * epsilon_rate
