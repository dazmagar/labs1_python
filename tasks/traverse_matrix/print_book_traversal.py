# In this challenge, let's adjust our book traversal method! Originally, our method involved traversing even-indexed columns upwards and odd-indexed columns downwards.
# Your task is to reverse this pattern without adding new lines of code. Make the necessary change in the condition within the loop so that even-indexed columns are traversed downwards,
# and odd-indexed ones upwards. Let's do this, Space Voyager!

import typing as t


def print_book_traversal(bookshelves: t.List[t.List[int]]) -> t.List[int]:
    """Origin: even-indexed columns upwards and odd-indexed columns downwards"""
    rows = len(bookshelves)
    cols = len(bookshelves[0])
    for col in range(cols - 1, -1, -1):
        if col % 2 == 0:
            for row in range(rows - 1, -1, -1):
                print(bookshelves[row][col], end=" ")
        else:
            for row in range(rows):
                print(bookshelves[row][col], end=" ")


def print_book_traversal_reversed(bookshelves: t.List[t.List[int]]) -> t.List[int]:
    """Reversed: even-indexed columns downwards and odd-indexed columns upwards"""
    rows = len(bookshelves)
    cols = len(bookshelves[0])
    for col in range(cols - 1, -1, -1):
        if col % 2 == 0:
            for row in range(0, rows, 1):
                print(bookshelves[row][col], end=" ")
        else:
            for row in range(rows - 1, -1, -1):
                print(bookshelves[row][col], end=" ")


if __name__ == "__main__":
    bookshelves = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print_book_traversal(bookshelves)
    print("\n")
    print_book_traversal_reversed(bookshelves)
