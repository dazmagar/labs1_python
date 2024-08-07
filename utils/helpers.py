import typing as t


def pretty_print_matrix(matrix: t.List[t.List[int]]) -> str:
    print("[")
    for row in matrix:
        print("    [" + ", ".join(map(str, row)) + "],")
    print("]")
