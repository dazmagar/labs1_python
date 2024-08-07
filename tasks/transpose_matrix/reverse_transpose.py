import sys
import typing as t
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from utils.helpers import pretty_print_matrix

matrix = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
]


def reverse_transpose(matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]


pretty_print_matrix(matrix)
transposed = reverse_transpose(matrix)
pretty_print_matrix(transposed)
