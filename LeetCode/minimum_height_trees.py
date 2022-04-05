from collections import defaultdict


def find_min_height_trees(n, edges):
    if n <= 2:
        return [x for x in range(n)]

    adj_list = defaultdict(list)

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    leaves = []

    for i in range(n):
        if len(adj_list[i]) == 1:
            leaves.append(i)

    while n > 2:
        n -= len(leaves)
        temp = []

        for leaf in leaves:
            for neigh in adj_list[leaf]:
                adj_list[neigh].remove(leaf)
                if len(adj_list[neigh]) == 1:
                    temp.append(neigh)

        leaves = temp

    return leaves
