# Word Machine

## Problem Description

The **Word Machine** is a system that performs a sequence of simple operations on a stack of integers. Initially, the stack is empty. The sequence of operations is provided as a single string where each operation is separated by a space.

The machine supports the following operations:

- **An integer `X` (0 to \(2^{20} - 1\))**: Push `X` onto the stack.
- **`POP`**: Remove the topmost element from the stack.
- **`DUP`**: Duplicate the topmost element of the stack.
- **`+`**: Pop the top two elements from the stack, add them, and push the result back onto the stack.
- **`-`**: Pop the top two elements from the stack, subtract the second element from the first, and push the result back onto the stack.

### Error Conditions

The machine will report an error (`-1`) in the following cases:
1. **Stack underflow**: Attempting an operation that requires more elements than are present in the stack.
2. **Overflow**: The result of an addition exceeds \(2^{20} - 1\).
3. **Negative result**: The result of a subtraction is negative.
4. **Empty stack**: After all operations, the stack is empty.

The machine returns the topmost value of the stack after processing all operations. If an error occurs, the machine returns `-1`.

---

## Function Signature

Implement the following function:

```python
def solution(s: str) -> int:
    """
    Args:
        s (str): A string containing a sequence of word machine operations.
        
    Returns:
        int: The topmost value of the stack after processing operations,
             or -1 if an error occurs.
    """
```

## Examples

### Example 1:
**Input**: `"4 5 6 - 7 +"`

**Execution**:
1. Push `4`
2. Push `5`
3. Push `6`
4. Subtract `6 - 5` → Push `1`
5. Push `7`
6. Add `7 + 1` → Push `8`

**Output**: `8`
-------------------------------------------
### Example 2:
**Input**: `"13 DUP 4 POP 5 DUP + DUP + -"`

**Execution**:
1. Push `13`
2. Duplicate `13`
3. Push `4`
4. Pop `4`
5. Push `5`
6. Duplicate `5`
7. Add `5 + 5` → Push `10`
8. Duplicate `10`
9. Add `10 + 10` → Push `20`
10. Subtract `20 - 13` → Push `7`

**Output**: `7`
-------------------------------------------
### Example 3:
**Input**: `"5 6 +"`

**Execution**:
1. Push `5`
2. Push `6`
3. Add `5 + 6` → Push `11`

**Output**: `11`
-------------------------------------------
### Example 4:
**Input**: `"3 DUP 5 - -"`

**Execution**:
1. Push `3`
2. Duplicate `3`
3. Push `5`
4. Subtract `5 - 3` → Push `2`
5. Attempt to subtract `2 - 3` → Stack underflow.

**Error**: Result becomes negative.

**Output**: `-1`
-------------------------------------------
### Example 5:
**Input**: `"1048575 DUP +"`

**Execution**:
1. Push `1048575`
2. Duplicate `1048575`
3. Add `1048575 + 1048575` → Overflow.

**Error**: Addition exceeds \(2^{20} - 1\).

**Output**: `-1`
