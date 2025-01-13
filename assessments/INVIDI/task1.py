""" 
You are given an array of integers, which may contain duplicates.
The task is to find all pairs of integers that sum to zero.
If a number's complement appears more than once, it can pair multiple times.
Return all such pairs.
"""

import typing as t


def find_zero_sum_pairs(nums: t.List[int]) -> t.List[t.Tuple[int, int]]:
    result = []
    count_map = {}

    # Create a frequency map to track occurrences of each number
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1

    # Iterate through the array to find pairs
    for num in nums:
        complement = -num
        # Check if the complement exists in the map and can form a pair
        if count_map.get(num, 0) > 0 and count_map.get(complement, 0) > 0:
            if num == 0 and count_map[num] > 1:  # Special case for zero pairs
                result.append((0, 0))
                count_map[num] -= 2
            elif num != 0:  # General case for non-zero numbers
                result.append((num, complement))
                count_map[num] -= 1
                count_map[complement] -= 1

    return result


# Tests
def test_find_zero_sum_pairs() -> None:
    assert find_zero_sum_pairs([1, -1, 2, -2, 3, -3]) == [(1, -1), (2, -2), (3, -3)]
    assert find_zero_sum_pairs([0, 0, 1, -1]) == [(0, 0), (1, -1)]
    assert find_zero_sum_pairs([1, 2, 3]) == []
    assert find_zero_sum_pairs([]) == []
    assert find_zero_sum_pairs([1, -1, 1, -1]) == [(1, -1), (-1, 1)]
    assert find_zero_sum_pairs([0, 0, 0]) == [(0, 0)]
    print("All tests passed.")


# Run tests
test_find_zero_sum_pairs()
