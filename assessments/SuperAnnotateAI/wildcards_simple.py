"""
Task: Wildcards

Have the function Wildcards(str) read str which will contain two strings separated by a space. 
The first string will consist of the following sets of characters: +, $, and (N) which is optional. 
The plus (+) character represents a single alphabetic character, 
the ($) character represents a single numeric character, 
and the asterisk (*) represents a sequence of the same character of length 3 
unless it is followed by (N) which represents how many characters should appear in the sequence 
where N will be at least 1. 

Your goal is to determine if the second string exactly matches the pattern of the first string in the input.

For example: 
if str is "++*(5) abggggg" then the second string in this case does match the pattern 
(two any letters followed by g repeated 5 times), so your program should return the string true. 
If the second string does not match the pattern your program should return the string false.
"""

import re

def Wildcards(strParam):
    # Split input into pattern and test string
    pattern, test = strParam.split()
    
    # Convert pattern to regex pattern
    regex_pattern = ''
    i = 0
    
    while i < len(pattern):
        if pattern[i] == '+':
            regex_pattern += '[a-zA-Z]'
        elif pattern[i] == '$':
            regex_pattern += '[0-9]'
        elif pattern[i] == '*':
            # Look ahead to find what we're repeating
            repeat_count = 3  # default repeat count
            i += 1
            
            # Check for (N) pattern
            if i < len(pattern) and pattern[i] == '(':
                i += 1
                n = ''
                while i < len(pattern) and pattern[i].isdigit():
                    n += pattern[i]
                    i += 1
                repeat_count = int(n)
                i += 1  # skip closing parenthesis
            
            # Look ahead for the character to repeat
            if i < len(pattern):
                next_char = pattern[i]
                if next_char == '+':
                    regex_pattern += f'[a-zA-Z]{{{repeat_count}}}'
                elif next_char == '$':
                    regex_pattern += f'[0-9]{{{repeat_count}}}'
                else:
                    regex_pattern += f'{re.escape(next_char)}{{{repeat_count}}}'
                i += 1
        else:
            regex_pattern += re.escape(pattern[i])
        i += 1
    
    # Add start and end markers to ensure exact match
    regex_pattern = '^' + regex_pattern + '$'
    
    try:
        # Return result based on regex match
        return "true" if re.match(regex_pattern, test) else "false"
    except re.error:
        return "false"  # return false if regex pattern is invalid


# Test data
test_data = [
    "++*(5)g abggggg",     # true  (two letters + g repeated 5 times)
    "+++$(3) abc9999",     # false (three letters + one digit repeated 3 times)
    "$*(4)a 9aaaa",        # true  (one digit + a repeated 4 times)
    "+++ abc",             # true  (matches any three letters)
    "$$$*(2)+ 123aaa"      # true  (three digits followed by three same letters)
]

# Run tests
for test in test_data:
    print(f"Input: {test}")
    print(f"Output: {Wildcards(test)}\n") 