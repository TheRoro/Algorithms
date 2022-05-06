def remove_duplicates(s, k) -> str:
    stack = []
    # [d: 2], [b: 2]

    # dd
    for c in s:
        if len(stack) > 0 and stack[-1][0] == c:
            count = stack[-1][1]
            count += 1
            stack[-1] = [c, count]

            # when do we pop ?
            # when count == k
            if count == k:
                stack.pop(-1)
        else:
            stack.append([c, 1])

    # [[a, 1], [b, 1], [c, 1], [d, 1]]

    ans = []

    for tup in stack:
        char, count = tup
        for i in range(count):
            ans.append(char)

    return "".join(ans)
