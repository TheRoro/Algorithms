from collections import defaultdict


def smallest_string_with_swaps(s: str, pairs) -> str:
    p = [i for i in range(len(s))]  # [0, 1, 2, 3]

    def union(x, y):
        px = find(x)
        py = find(y)
        if px != py:
            p[py] = px

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    for x, y in pairs:
        union(x, y)

    hash_map = defaultdict(list)

    for index, elem in enumerate(p):
        hash_map[find(elem)].append(index)

    res = list(s)

    for key in hash_map.keys():
        index_list = hash_map[key]
        char_list = [s[i] for i in index_list]
        char_list.sort()

        for index, char in zip(index_list, char_list):
            res[index] = char

    return "".join(res)
