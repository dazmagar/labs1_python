# Calculate total running cost for servers
# You are given an array of strings 'startupTimes' representing server startup times in 24-hour format and an array of strings 'shutdownTimes' of the same length,
# representing server shutdown time in 24-hour format. For the ith server, startup time is 'startupTimes[i]' and shutdown time is 'shutdownTimes[i]', where i is a 0-based index.
# You are also given a string 'currentTime' representing the current time in 24-hour format.
# The 'shutdownTimes[i]' may be equal to "None", meaning the ith server was not shut down at the 'currentTime'.
# The cost of running each server is $1 per minute. Your task is to calculate the total amount you need to pay (in dollars) to run all servers from the start of the first-started server to the 'currentTime'.

from datetime import datetime


def time_diff_in_minutes(start: str, end: str) -> int:
    time_fmt = "%H:%M"
    tdelta = datetime.strptime(end, time_fmt) - datetime.strptime(start, time_fmt)
    return tdelta.total_seconds() / 60


def calculate_total_cost(startupTimes: str, shutdownTimes: str, currentTime: str) -> int:
    total_minutes = 0

    for i in range(len(startupTimes)):
        if shutdownTimes[i] == "None":
            total_minutes += time_diff_in_minutes(startupTimes[i], currentTime)
        else:
            total_minutes += time_diff_in_minutes(startupTimes[i], shutdownTimes[i])

    return total_minutes


# Example usage
startup_times = ["12:30", "14:00", "19:55"]
shutdown_times = ["15:00", "17:00", "None"]
current_time = "20:00"

total_cost = calculate_total_cost(startup_times, shutdown_times, current_time)
print(f"Total cost: ${total_cost:.0f}")
