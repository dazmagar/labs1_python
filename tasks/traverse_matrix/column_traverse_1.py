# Here's the task:
# you've been given a 2D matrix consisting of individual cells, each holding a unique integer value.
# Your goal is to create a function that will traverse this matrix, starting at the bottom right cell.
# From there, you'll travel up to the top of the same column, then move left to the next column, and then continue downwards from the top of this new column.
# After reaching the bottom of the column, you again move left and start moving upwards. This unique traverse pattern will be performed until all the cells have been visited.

import typing as t

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def column_traverse(matrix: t.List[t.List[int]]) -> t.List[int]:
    rows, cols = len(matrix), len(matrix[0])
    direction = "up"
    row, col = rows - 1, cols - 1
    output = []

    while len(output) < rows * cols:
        output.append(matrix[row][col])

        if direction == "up":
            if row - 1 < 0:
                direction = "down"
                col -= 1
            else:
                row -= 1
        else:
            if row + 1 == rows:
                direction = "up"
                col -= 1
            else:
                row += 1

    return output


print(column_traverse(matrix))
