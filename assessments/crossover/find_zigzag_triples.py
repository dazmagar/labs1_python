# Zigzag Triplets Check
# Let's say a triple (a, b, c) is a zigzag if either "a < b > c" or "a > b < c".
# Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag.
# More formally, your task is to construct an array of length 'numbers.length - 2', where the i-th element of the output array
# equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

import typing as t


def find_zigzag_triples(numbers: t.List[int]) -> t.List[int]:
    result = []
    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
        if (a < b > c) or (a > b < c):
            result.append(1)
        else:
            result.append(0)
    return result


# Example usage
numbers = [1, 3, 2, 4, 5, 3, 6]
output = find_zigzag_triples(numbers)
print(output)
