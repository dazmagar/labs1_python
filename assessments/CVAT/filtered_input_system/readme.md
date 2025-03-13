A user interface contains two types of user input controls: **TextInput**, which accepts all characters, and **NumericInput**, which accepts only digits.  

### Implement the class **TextInput** that contains:  
- A method **add(self, character)** – adds the given character to the current value.  
- A method **get_value(self)** – returns the current value.  

## Implement the class **NumericInput** that:  
- Inherits **TextInput**.  
- Overrides the **add** method so that each non-numeric character is ignored.  

### Example:  
```py
input = NumericInput()
input.add("1")
input.add("a")
input.add("0")
print(input.get_value())
```
### Should output:
```py
"10"
```
