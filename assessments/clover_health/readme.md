You are given an integer N, followed by N lines of text. 

Each line:
 - Contains one or more words separated by single spaces.
 - Each word is composed of English alphabet letters and has a length between 1 and 10 characters, inclusive.
 - The total number of words in a line is between 1 and 100, inclusive.

Task: 
Process exactly N lines of input, and for each line:
 - Keep the first and last words in their original positions.
 - Reverse the order of all the words between the first and the last.
 - The output should have no leading or trailing spaces for each line.

# Example
Input:
```
5
Hello
Hello World
Hello My World
Hello My Beautiful World
Twinkle twinkle little star how I wonder what you are
```

Output:
```
Hello
Hello World
Hello My World
Hello Beautiful My World
Twinkle you what wonder I how star little twinkle are
```