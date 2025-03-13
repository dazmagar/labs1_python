An application requires sorting a list of students based on their marks.  

### Implement the function **sort_by_marks_descending**, which:  
- Accepts a string in JSON format.  
- Orders students by marks in **descending order**.  
- If two students have the same mark, they should be ordered **alphabetically by name**.  
- Returns a string in JSON format that is equivalent to the input format.  

### Example:  
```py
sort_by_marks_descending('[{"name":"John","mark":85}, {"name":"Alice","mark":90}, {"name":"Bob","mark":88}]')
```
### Should return:
```py
[{"name": "Alice", "mark": 90}, {"name": "Bob", "mark": 88}, {"name": "John", "mark": 85}]
```
