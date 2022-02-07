def is_valid(s: str) -> bool:
    stack = []

    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        else:
            if len(stack) > 0:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            else:
                return False

    if len(stack) > 0:
        return False

    return True
