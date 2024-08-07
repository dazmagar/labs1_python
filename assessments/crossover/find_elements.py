# Given an array of integers, find elements greater than their neighbors
# Given an array of integers target, return an array result consisting of all elements target[i] that are greater than both of their neighbors, i.e. that are target[i] > max(target[i - 1], target[i + 1]).
# Note that target[0] and target[target.length - 1], which are the first and the last elements, are included by default, because they do not have two neighbors.
import typing as t


def find_elements(target: t.List[int]) -> t.List[int]:
    result = [target[0]]  # Include the first element by default

    for i in range(1, len(target) - 1):
        if target[i] > max(target[i - 1], target[i + 1]):
            result.append(target[i])

    result.append(target[-1])  # Include the last element by default

    return result


# Example usage
target = [3, 5, 4, 6, 2]
print(find_elements(target))
