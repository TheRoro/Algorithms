from collections import Counter


def longest_palindrome(self, s: str) -> int:
    count = Counter(s)

    length = 0
    is_odd = False

    for key in count:
        val = count[key]

        if val % 2 != 0:
            is_odd = True
            length += (val - 1)
        else:
            length += val

    return length + 1 if is_odd else length
