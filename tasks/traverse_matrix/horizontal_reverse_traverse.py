import typing as t

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


def horizontal_reverse_traverse(matrix: t.List[t.List[int]]) -> t.List[int]:
    rows, cols = len(matrix), len(matrix[0])
    output = []

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            output.append(matrix[row][col])

    return output


print(horizontal_reverse_traverse(matrix))
