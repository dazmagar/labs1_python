# Find the optimal point on a coordinate line illuminated by lamps
# There are some lamps placed on a coordinate line. Each of these lamps illuminates some space around it within a given radius.
# You are given the coordinates of the lamps on the line, and the effective radius of each of the lamps' light.
# In other words, you are given a two-dimensional array lamps, where lamps[i] contains information about the ith lamp.
# lamps[i][0] is an integer representing the lamp's coordinate, and lamps[i][1] is a positive integer representing the effective radius of the ith lamp.
# That means that the ith lamp illuminates everything in a range from [lamps[i][0] - lamps[i][1]] to [lamps[i][0] + lamps[i][1]] inclusive.
# The task is to find the coordinate of the point that is illuminated by the highest number of lamps. In case of a tie, return the point among them with the minimal possible coordinate.

import typing as t


def solution(lamps: t.List[int]) -> int:
    events = []
    for lamp in lamps:
        coord, radius = lamp
        events.append((coord - radius, 1))  # Start of illumination
        events.append((coord + radius + 1, -1))  # End of illumination (exclusive)

    events.sort()

    max_illuminations = 0
    curr_illuminations = 0
    best_coordinate = float("inf")

    for event in events:
        coord, effect = event
        curr_illuminations += effect

        if curr_illuminations > max_illuminations:
            max_illuminations = curr_illuminations
            best_coordinate = coord
        elif curr_illuminations == max_illuminations and coord < best_coordinate:
            best_coordinate = coord

    return best_coordinate


# Example usage
lamps = [[1, 2], [3, 3], [6, 1]]
print(solution(lamps))
