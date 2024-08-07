from collections import defaultdict
from sys import stdin
from typing import Dict, List, Tuple

# Index constants
SERIAL_NUM_INDEX = 0
HW_REVISION_INDEX = 1
FW_VERSION_INDEX = 2
LOCATION_INDEX = 3
DAYS_INDEX = 4
FAILURES_INDEX = 5

# Output constants
HW_REVISION_OUTPUT = "Hardware Revision"
FW_VERSION_OUTPUT = "Firmware Version"
LOCATION_OUTPUT = "Location"
NO_FAILURES_OUTPUT = "No failures"


def process_input_data(input_lines: List[str]) -> List[Tuple[str, str, str, str, int, int]]:
    data = []
    seen_serial_numbers = set()

    for line in input_lines:
        parts = [item.strip() for item in line.split(",")]

        serial_number = parts[SERIAL_NUM_INDEX]
        hw_revision = parts[HW_REVISION_INDEX]
        fw_version = parts[FW_VERSION_INDEX]
        location = parts[LOCATION_INDEX].lower()
        days_deployed = int(parts[DAYS_INDEX])
        number_failures = int(parts[FAILURES_INDEX]) if parts[FAILURES_INDEX] else 0

        if serial_number in seen_serial_numbers:
            continue
        seen_serial_numbers.add(serial_number)

        if days_deployed <= 0:
            continue

        data.append((serial_number, hw_revision, fw_version, location, days_deployed, number_failures))

    return data


def calculate_average_failures(data: List[Tuple[str, str, str, str, int, int]]) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float]]:
    hw_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]
    fw_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]
    loc_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]

    for entry in data:
        _, hw_revision, fw_version, location, days_deployed, number_failures = entry

        hw_failures[hw_revision][0] += number_failures
        hw_failures[hw_revision][1] += days_deployed

        fw_failures[fw_version][0] += number_failures
        fw_failures[fw_version][1] += days_deployed

        loc_failures[location][0] += number_failures
        loc_failures[location][1] += days_deployed

    avg_hw_failures = {k: v[0] / v[1] for k, v in hw_failures.items()}
    avg_fw_failures = {k: v[0] / v[1] for k, v in fw_failures.items()}
    avg_loc_failures = {k: v[0] / v[1] for k, v in loc_failures.items()}

    return avg_hw_failures, avg_fw_failures, avg_loc_failures


def find_highest_failures(avg_hw_failures: Dict[str, float], avg_fw_failures: Dict[str, float], avg_loc_failures: Dict[str, float]) -> List[Tuple[str, str]]:
    max_failures = -1
    max_properties = []

    for property_dict, name in [(avg_hw_failures, HW_REVISION_OUTPUT), (avg_fw_failures, FW_VERSION_OUTPUT), (avg_loc_failures, LOCATION_OUTPUT)]:
        for prop, avg_fail in property_dict.items():
            if avg_fail > max_failures:
                max_failures = avg_fail
                max_properties = [(name, prop)]
            elif avg_fail == max_failures:
                max_properties.append((name, prop))

    return max_properties


def main(input_lines: List[str]) -> None:
    data = process_input_data(input_lines)

    if not data or all(entry[5] == 0 for entry in data):
        print(NO_FAILURES_OUTPUT)
        return

    avg_hw_failures, avg_fw_failures, avg_loc_failures = calculate_average_failures(data)
    max_properties = find_highest_failures(avg_hw_failures, avg_fw_failures, avg_loc_failures)

    if not max_properties:
        print(NO_FAILURES_OUTPUT)
    else:
        for prop in max_properties:
            print(f"{prop[0]} {prop[1].title()}")


input_lines: List[str] = []
for line in stdin:
    input_lines.append(line.strip())


main(input_lines)

# serial_number, [hw_revision, fw_version, location], days_deployed, number_failures

input_lines = [
    "12345,Rev1,0.1,Saskatoon,50,0",
    "45678,Rev1,0.2,Regina,10,0",
    "00110,Rev2,0.2,Saskatoon,200,0",
    "11223,Rev3,1.0,Vancouver,100,0",
]
