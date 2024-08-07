# In this practice, you need to define how we switch directions and move left when we reach the top or bottom of our bookshelf.
# Remember, the books on these shelves are organized in a unique pattern.

import typing as t


def column_traverse(matrix: t.List[t.List[int]]) -> t.List[int]:
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, cols - 1
    direction = -1  # Start going upwards
    output = []

    for _ in range(rows * cols):
        output.append(matrix[row][col])

        if direction < 0:
            if row - 1 < 0:
                direction = 1
                col -= 1
            else:
                row -= 1
        else:
            if row + 1 == rows:
                direction = -1
                col -= 1
            else:
                row += 1

    return output


# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(column_traverse(bookshelf))
