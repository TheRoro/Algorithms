def backspace_compare(s, t):
    stack_s = []
    stack_t = []

    for c in s:
        if c != "#":
            stack_s.append(c)
        elif stack_s:
            stack_s.pop(-1)

    for c in t:
        if c != "#":
            stack_t.append(c)
        elif stack_t:
            stack_t.pop(-1)

    if stack_t == stack_s:
        return True

    return False
