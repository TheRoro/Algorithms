from collections import defaultdict


def group_anagrams(strings):
    res = defaultdict(list)

    for s in strings:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)

    return res.values()
