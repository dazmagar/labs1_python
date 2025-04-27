"""
Task: Pattern Chaser

Have the function PatternChaser(str) take str which will be a string and 
return the longest pattern within the string. A pattern for this challenge will be defined as: 
if at least 2 or more adjacent characters within the string repeat at least twice. 

So for example "aabecaa" contains the pattern "aa". These patterns can overlap. 
For example, "aabejiabkfabed" contains a pattern "ab" which occurs twice. 
Also, if a pattern is repeated more than twice, your program should still return 
the pattern (see last example below). 

Your program should return yes/no pattern where "yes" will be the longest pattern found 
and "no" will be returned if no pattern exists. The string may either contain all characters 
(a through z only), integers, or both, but it will only be one string type at a time. 
The maximum length for the string being passed in will be 20 characters. 
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". 
You must always return the longest pattern possible.

Examples:
Input: "da2kr32a2"
Output: yes a2

Input: "sskfssbbb9bbb"
Output: yes bbb
"""

def PatternChaser(str):
    # Check if string length is less than 4
    # We need at least 4 characters because pattern must be at least 2 chars long and repeat at least once
    if len(str) < 4:
        return "no null"
    
    max_pattern = ""
    # Iterate through all possible pattern lengths from 2 to half of string length
    for length in range(2, len(str) // 2 + 1):
        # For each length, check all possible starting positions in the string
        for start in range(len(str) - 2 * length + 1):
            # Extract potential pattern
            pattern = str[start:start + length]
            # Look for this pattern in the remaining part of the string
            # If found (not -1), and it's longer than current max_pattern, update max_pattern
            if str[start + length:].find(pattern) != -1:
                if len(pattern) > len(max_pattern):
                    max_pattern = pattern
    
    # Return result in required format:
    # "yes pattern" if pattern found, "no null" if no pattern exists
    if max_pattern:
        return f"yes {max_pattern}"
    return "no null"


# Test data
test_data = [
    "da2kr3a2",      # yes a2
    "aabecaa",       # yes aa
    "nknnnnn",       # yes nn
    "123224",        # no null
    "aa2bbbaacbbb"   # yes bbb
]

# Run tests
for test in test_data:
    print(f"Input: {test}")
    print(f"Output: {PatternChaser(test)}\n")
