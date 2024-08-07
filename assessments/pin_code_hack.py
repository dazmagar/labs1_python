from itertools import product


def solution(pin):
    pin_map = {
        "0": ["0", "8"],
        "1": ["1", "2", "4"],
        "2": ["2", "1", "3", "5"],
        "3": ["3", "2", "6"],
        "4": ["4", "1", "5", "7"],
        "5": ["5", "2", "4", "6", "8"],
        "6": ["6", "3", "5", "9"],
        "7": ["7", "4", "8"],
        "8": ["8", "5", "7", "9", "0"],
        "9": ["9", "6", "8"],
    }

    possible_digits = [pin_map[digit] for digit in pin]
    combinations = product(*possible_digits)
    possible_pins = ["".join(combination) for combination in combinations]

    return sorted(possible_pins)


pin = "11"

out_ = solution(pin)
for i_out_ in out_:
    print(i_out_)
