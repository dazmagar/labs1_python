# Your task involves writing a function that simulates a unique traversal across a library's bookshelves,
# moving through the collection in a zigzag pattern. Remember to start from the bottom right and zigzag up and down each column.

import typing as t


def bookshelfTraversal(bookshelves: t.List[t.List[int]]) -> t.List[int]:
    rows, cols = len(bookshelves), len(bookshelves[0])
    traversal_path = []

    for col in range(cols - 1, -1, -1):
        traversal_path.extend(bookshelves[row][col] for row in (range(rows) if col % 2 == 0 else range(rows - 1, -1, -1)))

    return traversal_path


bookshelves = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

# Print the traversal path of the books
print(bookshelfTraversal(bookshelves))
