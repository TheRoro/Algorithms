from collections import defaultdict


def shortest_alternating_paths(n: int, red_edges, blue_edges):
    graph = defaultdict(list)

    for u, v in red_edges:
        graph[u].append((v, "R"))

    for u, v, in blue_edges:
        graph[u].append((v, "B"))

    node, color = 0, "N"
    queue = [(node, color, 0)]
    ans = [-1] * n
    ans[node] = 0
    visited = set()

    while queue:
        node, color, length = queue.pop(0)
        visited.add((node, color))

        for neigh, neigh_color in graph[node]:
            if (neigh, neigh_color) not in visited and color != neigh_color:
                if ans[neigh] == -1:
                    ans[neigh] = length + 1
                queue.append((neigh, neigh_color, length + 1))

    return ans
