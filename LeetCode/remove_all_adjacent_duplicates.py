def remove_duplicates(s: str) -> str:
    stack = []

    for c in s:
        if len(stack) > 0 and c == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(c)

    return "".join(stack)
