import typing as t


def solution(s: str) -> int:
    stack: t.List[int] = []
    max_val: int = 2**20 - 1

    for op in s.split():
        if op.isdigit():
            num = int(op)
            if 0 <= num <= max_val:
                stack.append(num)
            else:
                return -1
        elif op == "POP":
            if stack:
                stack.pop()
            else:
                return -1
        elif op == "DUP":
            if stack:
                stack.append(stack[-1])
            else:
                return -1
        elif op == "+":
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if a + b <= max_val:
                    stack.append(a + b)
                else:
                    return -1
            else:
                return -1
        elif op == "-":
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if a - b >= 0:
                    stack.append(a - b)
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    return stack[-1] if stack else -1


if __name__ == "__main__":
    test_cases: t.List[str] = [
        "4 5 6 - 7 +",
        "13 DUP 4 POP 5 DUP + DUP + -",
        "5 6 +",
        "3 DUP 5 - -",
        "1048575 DUP +",
    ]

    for i, tc in enumerate(test_cases, 1):
        print(f"Test case {i}: {solution(tc)}")
