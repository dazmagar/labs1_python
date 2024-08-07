# Transform the given matrix over its secondary diagonal
# The secondary diagonal of the matrix is the line starting from the upper-right corner and ending in the bottom-left corner of the matrix.
# 0 0 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 0

import sys
import typing as t
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from utils.helpers import pretty_print_matrix


def reflectOverSecondaryDiagonal(matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
    size = len(matrix)
    new_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_matrix[size - 1 - j][size - 1 - i] = matrix[i][j]
    return new_matrix


square_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

pretty_print_matrix(square_matrix)
transformed_matrix = reflectOverSecondaryDiagonal(square_matrix)
pretty_print_matrix(transformed_matrix)
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]
