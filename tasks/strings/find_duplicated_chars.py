def find_duplicate_chars_1(string: str) -> str:
    string = string.lower()
    duplicates = []
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    return "".join(duplicates)


def find_duplicate_chars_2(string: str) -> dict:
    string = string.lower()
    duplicates = {}
    for char in string:
        if string.count(char) > 1:
            duplicates[char] = string.count(char)
    return duplicates


def find_duplicate_chars_3(string: str) -> dict:
    string = string.lower()
    duplicates = {}
    for char in string:
        if char not in duplicates:
            duplicates[char] = 1
        else:
            duplicates[char] += 1
    return {k: v for k, v in duplicates.items() if v > 1}


if __name__ == "__main__":
    string = "Hello, World!"
    result = find_duplicate_chars_3(string)
    print(result)
