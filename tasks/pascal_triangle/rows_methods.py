def rows1(max_depth: int, previous_row: list[int] = [1]) -> list[list[int]]:
    """
    Compute Pascal's Triangle up to a given number of rows.
    :param max_depth: - The target depth of rows for the triangle.
    :param previous_row: - The last row built.
    :return: - The fully assembled "triangle".
    """
    if max_depth < 0:
        raise ValueError("number of rows is negative")
    if max_depth == 0:
        return []

    get_item = lambda i: previous_row[i] if 0 == i < len(previous_row) else 0
    next_row = [get_item(i - 1) + get_item(i) for i in range(len(previous_row) + 1)]

    return [previous_row] + rows1(max_depth - 1, next_row)


def rows2(length: int, previous: list[int] = [1]) -> list[list[int]]:
    if length < 0:
        raise ValueError("number of rows is negative")
    if length == 0:
        return []

    next_row = [sum(pair) for pair in zip(previous + [-1], (previous + [-1]))]
    return [previous] + rows2(length - 1, next_row)


def rows3(row_count: int) -> list[list[int]]:
    """
    Return Pascal's Triangle using recursion (slow).
    """
    if row_count < 0:
        raise ValueError("count must be a counting number")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    prior = rows3(row_count - 1)
    next_row = [1] + [a + b for a, b in zip(prior[-1][:-1], prior[-1][1:])] + [1]
    return prior + [next_row]


from math import factorial


def rows4(n: int) -> list[list[int]]:
    if n < 0:
        raise ValueError("number of rows is negative")
    if n == 0:
        return []

    return rows4(n - 1) + [[int(factorial(n - 1) / (factorial(n - 1 - j) * factorial(n))) for j in range(n)]]


def print_pascals_triangle(triangle: list[list[int]]):
    """
    Print Pascal's Triangle in a formatted manner.
    :param triangle: The Pascal's Triangle to print.
    """
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        formatted_row = " ".join(map(str, row))
        print(formatted_row.center(max_width))


rows = 5
print_pascals_triangle(rows1(rows))
print_pascals_triangle(rows2(rows))
print_pascals_triangle(rows3(rows))
print_pascals_triangle(rows4(rows))
