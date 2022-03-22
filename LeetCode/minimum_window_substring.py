import math
from collections import Counter


def min_window(s: str, t: str) -> str:
    if t == "":
        return ""

    t_count = Counter(t)
    window = {}

    min_len = math.inf
    res = [-1, -1]

    have, need = 0, len(t_count)

    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in t_count and t_count[c] == window[c]:
            have += 1

        while have == need:

            actual_len = r - l + 1

            if actual_len < min_len:
                min_len = actual_len
                res = [l, r]

            window[s[l]] -= 1

            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1

            l += 1

    l, r = res

    if min_len == math.inf:
        return ""

    return s[l:r + 1]
