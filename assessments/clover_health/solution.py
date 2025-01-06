def reverse_middle_words_from_text(input_text: str) -> str:
    lines = input_text.strip().split("\n")

    n = int(lines[0].strip())
    results = []

    for i in range(1, n + 1):
        line = lines[i].strip()
        words = line.split()

        if len(words) > 2:
            result = [words[0]] + words[1:-1][::-1] + [words[-1]]
        else:
            result = words

        results.append(" ".join(result))

    return "\n".join(results)


# Test the function with the given input
text = """
5
Hello
Hello World
Hello My World
Hello My Beautiful World
Twinkle twinkle little star how I wonder what you are
"""

output = reverse_middle_words_from_text(text)
print(output)
