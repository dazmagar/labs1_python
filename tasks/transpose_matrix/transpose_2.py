import sys
import typing as t
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from utils.helpers import pretty_print_matrix


def transformMatrix(matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

pretty_print_matrix(matrix)
transposed = transformMatrix(matrix)
pretty_print_matrix(transposed)
