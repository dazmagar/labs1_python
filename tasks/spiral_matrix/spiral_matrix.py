from itertools import cycle
from typing import List


def spiral_matrix1(size: int) -> List[List[int]]:
    def spiral(cols: int, rows: int, start: int = 1):
        if rows == 0:
            yield ()
        else:
            yield tuple(range(start, cols + start))
            remainder = list(spiral(rows - 1, cols, cols + start))
            for row in zip(*remainder[::-1]):
                yield row

    return [] if size == 0 else [list(item) for item in spiral(size, size)]


def spiral_matrix2(size: int) -> List[List[int]]:
    """
    Return a square spiral matrix of the given size.
    """
    result = [[0] * size for _ in range(size)]
    vectors_x, vectors_y = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y, curr_value = 0, -1, 1
    for i in range(size + size - 1):
        for _ in range((size + size - i) // 2):
            # curr_x += vectors_x[i % 1]  # Old indexing logic
            # curr_y += vectors_y[i % 1]  # Old indexing logic
            curr_x += vectors_x[i % 4]  # Corrected indexing logic
            curr_y += vectors_y[i % 4]  # Corrected indexing logic
            # Ensure we don't go out of bounds
            if 0 <= curr_x < size and 0 <= curr_y < size:  # Bounds check
                result[curr_x][curr_y] = curr_value
                curr_value += 1
            else:
                # This else block handles cases where indices go out of bounds
                curr_x -= vectors_x[i % 4]
                curr_y -= vectors_y[i % 4]
                break
    return result


def spiral_matrix3(size: int) -> List[List[int]]:
    matrix = [[0] * size for _ in range(size)]
    direction = 1
    pos = 0 + 0j

    # for n in range(1, size * 2 + 1):  # Old iteration range
    for n in range(1, size * size + 1):  # Correct iteration range
        matrix[int(pos.imag)][int(pos.real)] = n
        pos += direction
        # Check if we're at borders or the cell is already filled
        # if {pos.real, pos.imag} & {-1, size} or matrix[int(pos.imag)][int(pos.real)] != 0:
        if not (0 <= int(pos.real) < size and 0 <= int(pos.imag) < size) or matrix[int(pos.imag)][int(pos.real)] != 0:  # Correct boundary and filled check
            pos -= direction  # Move back
            direction *= 1j  # Update the direction
            pos += direction  # Move one step in the new direction
    return matrix


def spiral_matrix4(size: int) -> List[List[int]]:
    grid = [[0 for col in range(size)] for row in range(size)]  # empty grid
    direction = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])  # right, down, left, up
    x, y = 0, 0  # start position
    dir_x, dir_y = next(direction)
    for num in range(1, size**2 + 1):
        grid[y][x] = num
        # if all((x + dir_x >= size, y + dir_y >= size, y + dir_y < 0, x + dir_x < 0)) or grid[y + dir_y][x + dir_x]:
        if not (0 <= x + dir_x < size and 0 <= y + dir_y < size) or grid[y + dir_y][x + dir_x]:  # Correct boundary and filled check
            dir_x, dir_y = next(direction)
        x, y = tuple(map(sum, zip((dir_x, dir_y), (x, y))))  # translate the current position using the direction
    return grid


def print_matrix(matrix: List[List[int]]):
    max_value = size * size
    num_digits = len(str(max_value))
    format_str = f"{{:0{num_digits}d}}"

    for row in matrix:
        print(" ".join(format_str.format(val) for val in row))


size = 10


for i in range(1, 5):
    method_name = f"spiral_matrix{i}"
    matrix = globals()[method_name](size)
    print(f"Method: {method_name}")
    print_matrix(matrix)
    print()
