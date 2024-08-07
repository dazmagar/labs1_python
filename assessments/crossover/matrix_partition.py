# Partition a matrix into 4 sub-matrices minimizing the difference of averages
# Given a two-dimensional integer array named matrix, your task is to partition the matrix into 4 rectangular sub-matrices (each with at least one non-negative valued cell),
# while minimizing the difference between the maximal and minimal average values of the partitions.
# The average value of a partition is the sum of all the non-negative values divided by the count of the non-negative values, rounded down.
# Return the row 'res_row' and column 'res_col' with the minimal difference between the maximal and minimal average value of the partitions.

import typing as t


def calculate_average(matrix: t.List[t.List[int]], startRow: int, endRow: int, startCol: int, endCol: int) -> int:
    total_sum = 0
    count = 0
    for r in range(startRow, endRow + 1):
        for c in range(startCol, endCol + 1):
            if matrix[r][c] >= 0:
                total_sum += matrix[r][c]
                count += 1
    return total_sum // count if count > 0 else float("inf")


def solution(matrix: t.List[t.List[int]]) -> t.List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    min_diff = float("inf")
    res_row = -1
    res_col = -1

    for r in range(rows - 1):
        for c in range(cols - 1):
            top_left = calculate_average(matrix, 0, r, 0, c)
            top_right = calculate_average(matrix, 0, r, c + 1, cols - 1)
            bottom_left = calculate_average(matrix, r + 1, rows - 1, 0, c)
            bottom_right = calculate_average(matrix, r + 1, rows - 1, c + 1, cols - 1)

            max_avg = max(top_left, top_right, bottom_left, bottom_right)
            min_avg = min(top_left, top_right, bottom_left, bottom_right)
            diff = max_avg - min_avg

            if diff < min_diff:
                min_diff = diff
                res_row = r
                res_col = c

    return [res_row, res_col]


# Example usage
matrix = [
    [7, 9, -1, -1],
    [3, 8, -1, -1],
    [5, 5, 7, -1],
]

result = solution(matrix)
print(solution(matrix))
