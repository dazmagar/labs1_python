# Your task is to append each book's position from our library bookshelves to the result list.
# This time, however, let's simplify the process to a vertical traverse starting from the bottom right

import typing as t


def vertical_reverse_traverse(matrix: t.List[t.List[int]]) -> t.List[int]:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    rows, cols = len(matrix), len(matrix[0])
    result = []

    for col in range(cols - 1, -1, -1):
        for row in range(rows - 1, -1, -1):
            result.append(matrix[row][col])

    return result


# Example matrix representing library bookshelves
bookshelves = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Output should be the vertical traverse of the bookshelves
print(vertical_reverse_traverse(bookshelves))  # [12, 8, 4, 11, 7, 3, 10, 6, 2, 9, 5, 1]
